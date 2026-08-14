"""
optimizer_tge.py - Otimizador Variacional Espectral Global da TGE (ToE)
Mapeia a condição variacional de ação mínima delta S(D) = 0 e encontra os parâmetros
ótimos da Ação Espectral de Connes-Chamseddine minimizando o desvio orbital global.
"""

import numpy as np
from scipy.optimize import minimize
from typing import Dict, Any, List, Tuple
from core_dirac import DiracSpectralOperator
from orbits_solar import SolarSystemOrbitalEngine


class SpectralGlobalOptimizer:
    """
    Otimizador Variacional para os Acoplamentos Não-Comutativos da TGE.
    """

    def __init__(self, n_resolution: int = 512, seed: int = 2026):
        self.dirac = DiracSpectralOperator(matrix_dim=n_resolution, random_seed=seed)
        self.dirac.initialize_operator()
        self.eigenvalues = self.dirac.compute_laplacian_spectrum()
        self.engine = SolarSystemOrbitalEngine()

    def loss_function_v13(self, params: np.ndarray) -> float:
        """
        Função de perda variacional TGE-13.0 ToE (Maré de 3 Corpos + Ressonâncias de Laplace).
        """
        alpha1, alpha2, beta, gamma_a6, delta_kuiper, xi_resonance, zeta_tidal, escala_base, kappa_sm = params

        if (alpha1 <= 0 or alpha2 <= 0 or beta < 0 or gamma_a6 < 0 or
            delta_kuiper < 0 or xi_resonance < 0 or zeta_tidal < 0 or escala_base <= 0 or kappa_sm < 0):
            return 1e6

        res = self.engine.predict_orbits_v13(self.eigenvalues, params.tolist())
        erro_medio = res["erro_medio_global"]

        fator_weyl = self.engine.compute_weyl_correction_v13(
            alpha1, alpha2, beta, gamma_a6, delta_kuiper, xi_resonance, zeta_tidal
        )
        monotonicidade_loss = np.sum(np.maximum(0, -np.diff(fator_weyl))) * 25.0

        return erro_medio + monotonicidade_loss

    def run_optimization_v13(self) -> Dict[str, Any]:
        """
        Executa a busca global multivariada para o modelo TGE-13.0 ToE.
        """
        p0 = np.array([0.985, 1.095, 0.148, 0.022, 0.865, 0.115, 0.082, 0.388, 0.00014])

        bounds = [
            (0.8, 1.3),    # alpha1
            (0.8, 1.6),    # alpha2
            (0.0, 0.5),    # beta
            (0.0, 0.10),   # gamma_a6
            (0.0, 2.0),    # delta_kuiper
            (0.0, 0.4),    # xi_resonance
            (0.0, 0.3),    # zeta_tidal
            (0.2, 0.8),    # escala_base
            (0.0, 0.001)   # kappa_sm
        ]

        print("[Otimizador Espectral] Minimizando Ação Espectral TGE-13.0 (ToE Alta Precisão)...")
        opt_res = minimize(
            self.loss_function_v13,
            p0,
            method="L-BFGS-B",
            bounds=bounds,
            options={"maxiter": 5000, "ftol": 1e-11}
        )

        params_otimos = opt_res.x.tolist()
        res_final = self.engine.predict_orbits_v13(self.eigenvalues, params_otimos)

        return {
            "sucesso": opt_res.success,
            "mensagem": opt_res.message,
            "iteracoes": opt_res.nit,
            "parametros_otimos": {
                "alpha1": params_otimos[0],
                "alpha2": params_otimos[1],
                "beta": params_otimos[2],
                "gamma_a6 (Seeley-DeWitt)": params_otimos[3],
                "delta_kuiper (Campo Distante)": params_otimos[4],
                "xi_resonance (Laplace)": params_otimos[5],
                "zeta_tidal (Maré 3 Corpos)": params_otimos[6],
                "escala_base": params_otimos[7],
                "kappa_sm (Eletrofraco)": params_otimos[8]
            },
            "erro_medio_otimizado": res_final["erro_medio_global"],
            "resultados_orbitais": res_final
        }


if __name__ == "__main__":
    opt = SpectralGlobalOptimizer(512, 2026)
    resultado = opt.run_optimization_v13()

    print("=" * 72)
    print("RESULTADO DA OTIMIZAÇÃO VARIACIONAL TGE-13.0 (ToE)")
    print(f"Status: {resultado['mensagem']} (Iterações: {resultado['iteracoes']})")
    print(f"Erro Médio Global Otimizado: {resultado['erro_medio_otimizado']:.2f}%")
    print("\nParâmetros Fundamentais da Ação Espectral:")
    for k, v in resultado["parametros_otimos"].items():
        print(f"  • {k}: {v:.6f}")

    print("\nTabela Orbital Otimizada:")
    print(f"{'Planeta':<10} | {'Real (UA)':<12} | {'TGE-13 (UA)':<12} | {'Erro (%)':<10}")
    print("-" * 52)
    for p in resultado["resultados_orbitais"]["tabela"]:
        print(f"{p['planeta']:<10} | {p['real_ua']:<12.4f} | {p['tge_ua']:<12.4f} | {p['erro_rel_pct']:<10.2f}%")
    print("=" * 72)
