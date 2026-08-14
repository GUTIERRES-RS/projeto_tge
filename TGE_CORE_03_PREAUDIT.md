# TGE-CORE-03 — PRÉ-AUDITORIA GLOBAL DO REPOSITÓRIO
**Data:** 2026-08-14  
**Status do Git HEAD:** `0717cb8` (Working tree limpo)  
**Objetivo:** Inventário completo de arquivos, rastreabilidade de código científico vs. legado, identificação de hardcodes e matriz de severidade epistemológica prévia ao TGE-CORE-03.

---

## 1. Inventário e Classificação de Arquivos do Repositório

| Arquivo | Categoria | Científico? | Executável? | Proveniência / Função | Status Atual |
|---|---|:---:|:---:|---|---|
| `tge/core/causal_structure.py` | **CORE** | SIM | SIM | Motor oficial de estrutura causal com separação em 3 níveis (TGE-CORE-02). | ATIVO / OFICIAL |
| `tge/experiments/falsification_suite.py` | **EXPERIMENT** | SIM | SIM | Suíte oficial dos 10 testes falsificáveis e modelos nulos. | ATIVO / OFICIAL |
| `tge/audit/parameter_registry.py` | **ANALYSIS** | SIM | SIM | Registro formal de proveniência de parâmetros. | ATIVO / OFICIAL |
| `tge/audit/tge_audit.py` | **ANALYSIS** | SIM | SIM | Gerador da matriz de auditoria epistemológica. | ATIVO / OFICIAL |
| `hypotheses.yaml` | **CORE SPEC** | SIM | NÃO | Cadastro formal das hipóteses $H_1$ a $H_6$ com critérios falsificáveis. | ATIVO / OFICIAL |
| `tge_exchange/*` (9 arquivos JSON) | **EXCHANGE** | SIM | NÃO | Controle de governança, experimentos, parâmetros e auditoria síncrona. | ATIVO / OFICIAL |
| `tge/reports/*.json` | **DATA / REPORT** | SIM | NÃO | Logs de execução de testes e baseline histórico TGE-2. | ATIVO / OFICIAL |
| `core_dirac.py` | **LEGACY** | SIM (Legado) | SIM | Implementação original com imposição $1:3$ (`n_space = 3 * n_time`). | LEGACY CONGELADO |
| `orbits_solar.py` | **LEGACY** | SIM (Legado) | SIM | Modelo orbital de Titius-Bode / Weyl com 11 parâmetros ajustados ($L$-BFGS-B). | LEGACY CONGELADO |
| `optimizer_tge.py` | **LEGACY** | SIM (Legado) | SIM | Otimizador variacional empírico para ajuste orbital. | LEGACY CONGELADO |
| `astrophysics_gw.py` | **LEGACY** | SIM (Legado) | SIM | Modelo de ondas gravitacionais LIGO com valores numéricos inseridos. | LEGACY CONGELADO |
| `cosmology_qft.py` | **LEGACY** | SIM (Legado) | SIM | Módulo cosmológico com $\Omega_\Lambda = 0.6889$ e $\Omega_{DM} = 0.268$ inseridos. | LEGACY CONGELADO |
| `flavor_ckm_pmns.py` | **LEGACY** | SIM (Legado) | SIM | Setor de sabor e matrizes CKM/PMNS com massas do PDG inseridas. | LEGACY CONGELADO |
| `galaxy_rotation_mond.py` | **LEGACY** | SIM (Legado) | SIM | Curvas de rotação galáctica SPARC com escala $a_0$ empírica. | LEGACY CONGELADO |
| `particle_collider_lhc.py` | **LEGACY** | SIM (Legado) | SIM | Decaimento do Higgs ($\Gamma = 4.08$ MeV) e $(g-2)_\mu$ inseridos. | LEGACY CONGELADO |
| `workspace_tge.py` | **LEGACY** | NÃO | SIM | Script integrador do painel legado. | LEGACY CONGELADO |
| `TGE_BRIDGE.md` | **COMMUNICATION**| SIM | NÃO | Quadro mestre de comunicação com o Auditor Externo. | ATIVO / OFICIAL |
| `AUDIT_REPORT.md` | **DOCUMENTATION**| SIM | NÃO | Relatório analítico detalhado da auditoria linha a linha. | OFICIAL |
| `TGE_CORE_02_REPORT.md` | **DOCUMENTATION**| SIM | NÃO | Relatório do diagnóstico de circularidade de Krein e modelos nulos. | OFICIAL |
| `README.md` | **DOCUMENTATION**| SIM | NÃO | Visão geral do repositório sob regras estritas de integridade. | ATIVO / OFICIAL |
| `TGE_RESUMO_SESSAO.md` | **DOCUMENTATION**| NÃO | NÃO | Histórico de sessões passadas. | HISTÓRICO |
| `TGE_projeto_completo.txt` | **DATA / DOC** | NÃO | NÃO | Arquivo de texto descritivo original. | HISTÓRICO |

---

## 2. Matriz de Severidade Epistemológica (Pré-Auditoria TGE-CORE-03)

### [CRITICAL] — Problemas que invalidam conclusões teóricas se não forem explicitados
1. **Origem Externa da Lorentzianidade:**
   - O operador $D$ puro hermitiano gera apenas geometria Euclidiana positiva ($D^\dagger D \ge 0$).
   - A indefinição observada em $G_{\text{eff}}$ depende estritamente da matriz externa $\eta$ (Espaço de Krein).
   - Teste de controle negativo ($\eta = I$) colapsa em $(128, 0, 0)$. A emergência espontânea do tempo **NÃO ESTÁ DEMONSTRADA**.
2. **Código Legado no Root (`core_dirac.py`):**
   - O arquivo `core_dirac.py` ainda reside no root e contém a linha 187 (`n_effective_space = 3 * n_effective_time`). Deve ser isolado para evitar contaminação dos testes de produção.

### [HIGH] — Hipóteses não demonstradas ou desvios empíricos não reconciliados
1. **Status Matemático de $G_{\text{eff}}$:**
   - $G_{\text{eff}} = D_{\text{Krein}}^\dagger D_{\text{Krein}} + i[\eta, D]$ é uma forma sesquilinear em $\mathcal{H}$, mas não possui derivação axiomática como tensor métrico contínuo $g_{\mu\nu}$. Classificação necessária: `NOT_DEMONSTRATED`.
2. **Inconsistência na Dimensão Espectral ($d_{\text{spec}} \approx 0.987$ vs $1.15$ vs $3.728$):**
   - No Dirac puro sem calibragem: $d_{\text{spec}} \approx 1.15$ (regressão heat kernel em `causal_structure.py`).
   - No histórico TGE-2: $d_{\text{spec}} = 3.728 \pm 0.498$ (baseline negativo).
   - Necessário documento formal de reconciliação (`docs/SPECTRAL_DIMENSION_RECONCILIATION.md`).

### [MEDIUM] — Calibração e Fenomenologia fora da TGE Fundamental
1. **Validação Fora da Amostra (Out-of-sample) Orbital:**
   - O teste orbital em `falsification_suite.py` utiliza uma lei de potência empírica ($r \propto n^{1.3}$), e não uma lei dinâmica derivada da ação espectral. Deve ser classificado como `NON-TGE BASELINE / EMPIRICAL FIT`.
2. **Escala UV/IR:**
   - O teste atual mede apenas a razão entre o maior e menor autovalor ($\lambda_{\max}/\lambda_{\min}$). Deve ser documentado como `SPECTRAL_SCALE_RANGE` até haver teoria de renormalização do grupo de renormalização (RG).

### [LOW] — Higiene de Repositório e Rastreabilidade
1. **Diretórios de Cache:**
   - `__pycache__` já está no `.gitignore` e não está rastreado no Git. Manter verificação contínua.
2. **Hash de Commit nos Documentos:**
   - Garantir sincronização automática do SHA real do Git em `current_status.json` e `TGE_BRIDGE.md` após cada commit.

---

## 3. Plano de Ação Estruturado por Fases

1. **Fase 1 (Estrutural):** Criar `LEGACY_CODE_POLICY.md`, `tge/reports/REPOSITORY_AUDIT.md`, `tge/reports/TARGET_LEAKAGE_AUDIT.md`.
2. **Fase 2 (Fundamentos Teóricos):** Criar `docs/G_EFF_MATHEMATICAL_STATUS.md`, `docs/NEGATIVE_RESULTS.md`, `docs/SPECTRAL_DIMENSION_RECONCILIATION.md`, `docs/PHENOMENOLOGY_STATUS.md`.
3. **Fase 3 (Experimentos TGE-CORE-03):** Implementar suíte de experimentos A, B, C, D em `tge/core/causal_structure.py` e pipeline `tge/experiments/run_official_suite.py`.
4. **Fase 4 (Relatório & Governança):** Gerar `TGE_CORE_03_REPORT.md`, atualizar `TGE_BRIDGE.md` e `tge_exchange/*`, com commits atômicos e reproduzíveis.
