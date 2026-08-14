# POLÍTICA DE CÓDIGO LEGADO (LEGACY CODE POLICY)
**Teoria Geométrico-Espectral da Emergência (TGE)**  
**Data:** 2026-08-14

---

## 1. Princípio Fundamental: Código Legado $\neq$ Evidência Atual

O repositório contém arquivos criados em fases anteriores da pesquisa que utilizavam métodos não-falsificáveis, calibração manual, parâmetros inseridos diretamente ou imposições forçadas (como a regra $1:3$).

**REGRA ESTRITA:**
1. Nenhum arquivo legado é considerado evidência científica válida para as hipóteses fundamentais da TGE ($H_1$ a $H_6$).
2. Nenhum resultado ou número presente nos arquivos legados pode alimentar o pipeline oficial (`tge/experiments/run_official_suite.py`) nem o intercâmbio de dados com o auditor externo (`tge_exchange/`).
3. Somente o código contido no pacote oficial `tge/` (`tge/core/`, `tge/experiments/`, `tge/audit/`) constitui a base executável oficial e auditável da teoria.

---

## 2. Inventário de Módulos Legados Congelados

| Arquivo Legado | Função Original | Motivo do Congelamento / Problema Identificado |
|---|---|---|
| `core_dirac.py` | Núcleo de Dirac original | Imposição $1:3$ forçada (`L187: n_space = 3 * n_time`) e divisores ad-hoc ($10^2, 10^5, 10^8$). |
| `orbits_solar.py` | Modelo orbital de Titius-Bode | 11 parâmetros variacionais ajustados numericamente via $L$-BFGS-B contra dados reais do Sistema Solar. |
| `optimizer_tge.py` | Otimizador de parâmetros | Minimização de resíduos contra dados empíricos observacionais. |
| `astrophysics_gw.py` | Ondas gravitacionais | Frequência de pico de 250 Hz e ringdown inseridos explicitamente. |
| `cosmology_qft.py` | Cosmologia espectral | Valores de $\Omega_\Lambda = 0.6889$ e $\Omega_{DM} = 0.268$ inseridos diretamente do satélite Planck. |
| `flavor_ckm_pmns.py` | Setor de sabor e neutrinos | Massas de quarks e ângulos de mistura empíricos do PDG inseridos nas matrizes. |
| `galaxy_rotation_mond.py` | Curvas de rotação galáctica | Aceleração crítica MOND ($a_0 = 1.2 \times 10^{-10} \text{ m/s}^2$) inserida como hipótese fenonemológica. |
| `particle_collider_lhc.py` | Colisões e física de partículas | Largura do Higgs ($\Gamma = 4.08$ MeV) e $(g-2)_\mu$ inseridos diretamente. |
| `workspace_tge.py` | Painel integrador legado | Orquestrador dos módulos acima. |

---

## 3. Preservação Histórica

Estes arquivos são mantidos congelados exclusivamente para:
- Rastreabilidade histórica e reprodutibilidade de auditorias passadas;
- Comparação crítica e demonstração de integridade no relatório de auditoria (`AUDIT_REPORT.md`).
