# AUDITORIA EXAUSTIVA DO REPOSITÓRIO — REPOSITORY_AUDIT.md
**Teoria Geométrico-Espectral da Emergência (TGE)**  
**Data:** 2026-08-14

---

## 1. Classificação de Arquivos

| Arquivo | Função | Científico? | Executável? | Proveniência | Status |
|---|---|:---:|:---:|---|---|
| `tge/core/causal_structure.py` | Motor de Estrutura Causal e Krein | SIM | SIM | DERIVADO_CONDITIONAL | CORE |
| `tge/experiments/falsification_suite.py` | Suíte dos 10 Testes Falsificáveis | SIM | SIM | DERIVADO | EXPERIMENT |
| `tge/audit/parameter_registry.py` | Rastreamento de Parâmetros | SIM | SIM | META | ANALYSIS |
| `tge/audit/tge_audit.py` | Gerador da Matriz de Auditoria | SIM | SIM | META | ANALYSIS |
| `hypotheses.yaml` | Cadastro Formal de Hipóteses | SIM | NÃO | META | CORE SPEC |
| `tge_exchange/current_status.json` | Status do Projeto e SHA do Commit | SIM | NÃO | META | EXCHANGE |
| `tge_exchange/hypotheses.json` | Hipóteses H1 a H6 em JSON | SIM | NÃO | META | EXCHANGE |
| `tge_exchange/parameters.json` | Proveniência de Parâmetros | SIM | NÃO | META | EXCHANGE |
| `tge_exchange/experiments.json` | Histórico de Experimentos | SIM | NÃO | META | EXCHANGE |
| `tge_exchange/audit_requests.json` | Pedidos de Auditoria Externa | SIM | NÃO | META | EXCHANGE |
| `tge_exchange/audit_results.json` | Pareceres do Auditor Externo | SIM | NÃO | META | EXCHANGE |
| `tge_exchange/decisions.json` | Registro de Decisões Pactuadas | SIM | NÃO | META | EXCHANGE |
| `tge_exchange/changelog.json` | Histórico de Mudanças | SIM | NÃO | META | EXCHANGE |
| `tge/reports/baseline_tge2.json` | Baseline Histórico TGE-2 | SIM | NÃO | EXPERIMENTAL | DATA |
| `tge/reports/falsification_suite_report.json` | Relatório de Testes Falsificáveis | SIM | NÃO | GENERATED | DATA |
| `tge/reports/audit_report.json` | Relatório de Auditoria JSON | SIM | NÃO | GENERATED | DATA |
| `core_dirac.py` | Operador de Dirac Original | SIM (Legado)| SIM | INSERIDO / CALIBRADO | LEGACY |
| `orbits_solar.py` | Modelo Orbital Solar | SIM (Legado)| SIM | CALIBRADO / INSERIDO | LEGACY |
| `optimizer_tge.py` | Otimizador Variacional | SIM (Legado)| SIM | CALIBRADO | LEGACY |
| `astrophysics_gw.py` | Modelo Ondas Gravitacionais | SIM (Legado)| SIM | INSERIDO / CALIBRADO | LEGACY |
| `cosmology_qft.py` | Modelo Cosmológico | SIM (Legado)| SIM | INSERIDO / OBSERVATIONAL | LEGACY |
| `flavor_ckm_pmns.py` | Setor de Sabor e Neutrinos | SIM (Legado)| SIM | INSERIDO / EXPERIMENTAL | LEGACY |
| `galaxy_rotation_mond.py` | Curvas de Rotação Galáctica | SIM (Legado)| SIM | CALIBRADO / HYPOTHESIS | LEGACY |
| `particle_collider_lhc.py` | Setor de Partículas e Higgs | SIM (Legado)| SIM | INSERIDO / EXPERIMENTAL | LEGACY |
| `workspace_tge.py` | Painel Integrador Legado | NÃO | SIM | N/A | LEGACY |
| `TGE_BRIDGE.md` | Quadro Síncrono de Comunicação | SIM | NÃO | META | DOCUMENTATION |
| `TGE_CORE_03_PREAUDIT.md` | Pré-Auditoria Global TGE-CORE-03 | SIM | NÃO | META | DOCUMENTATION |
| `TGE_CORE_02_REPORT.md` | Relatório de Diagnóstico Krein | SIM | NÃO | META | DOCUMENTATION |
| `AUDIT_REPORT.md` | Relatório Geral Linha a Linha | SIM | NÃO | META | DOCUMENTATION |
| `LEGACY_CODE_POLICY.md` | Política de Isolamento Legado | SIM | NÃO | META | DOCUMENTATION |
| `README.md` | Documentação Geral do Projeto | SIM | NÃO | META | DOCUMENTATION |
| `TGE_RESUMO_SESSAO.md` | Resumo de Sessão Histórico | NÃO | NÃO | HISTORICAL | DOCUMENTATION |
| `TGE_projeto_completo.txt` | Manifesto Original | NÃO | NÃO | HISTORICAL | DATA |

---

## 2. Resumo Quantitativo
- **Total de Arquivos:** 33
- **Arquivos Oficiais Ativos no Núcleo `tge/` e Raiz:** 18
- **Módulos Legados Congelados:** 9
- **Documentos de Governança e Relatórios:** 6
