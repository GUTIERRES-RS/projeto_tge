# TGE — Teoria Geométrico-Espectral da Emergência (Arquitetura Falsificável & Auditável)

Este repositório contém a implementação computacional da **Teoria Geométrico-Espectral da Emergência (TGE)** sob um arcabouço estritamente **auditável, falsificável e reprodutível**.

---

## ⚠️ Princípio Fundamental de Integridade Científica

Nenhum resultado é considerado "previsto pela TGE" apenas porque o código o reproduz. Todo resultado computacional do projeto é obrigatoriamente classificado em uma das seguintes categorias nos relatórios e documentação:

- **DERIVADO**: Resultado obtido matematicamente/computacionalmente a partir das estruturas fundamentais, sem inserir o resultado esperado no código.
- **CALIBRADO**: Resultado obtido por ajuste de parâmetros contra dados observacionais, experimentais ou valores conhecidos.
- **INSERIDO**: Resultado, constante ou estrutura-alvo colocada explicitamente no código.
- **NÃO DEMONSTRADO**: O código calcula alguma quantidade relacionada, mas não demonstra a interpretação física alegada.

---

## 📋 Matriz de Auditoria do Repositório (Fase TGE-CORE-02)

+-----------------------------------------+-------------------------------------------------------------+
| Resultado                               | Classificação                                               |
+-----------------------------------------+-------------------------------------------------------------+
| d_spec (Heat Kernel / Plateau R^2)      | DERIVADO (Falha da Hipótese 4D: d_spec ~ 1.15 no Dirac puro)|
| assinatura (G_eff sob Krein eta)        | DERIVADO CONDICIONAL / ESTRUTURA INSERIDA (eta)             |
| emergência causal 1+3 (H2)              | NÃO DEMONSTRADO / FALHA NO MODELO ATUAL                     |
| Seeley-DeWitt (a_0 a a_6)               | CALIBRADO / INSERIDO                                        |
| Yukawa (Setor de Massa)                 | INSERIDO / CALIBRADO                                        |
| CKM (Mistura de Quarks)                 | INSERIDO / CALIBRADO                                        |
| PMNS (Oscilação de Neutrinos)           | INSERIDO                                                    |
| Seesaw (Escala Sub-eV)                  | DERIVADO (Fórmula) / INSERIDO (Valores)                     |
| ΩΛ (Energia Escura)                     | INSERIDO                                                    |
| ΩDM (Matéria Escura)                    | INSERIDO                                                    |
| Higgs (Largura e Branching LHC)         | INSERIDO                                                    |
| g-2 (Anomalia do Múon)                  | INSERIDO                                                    |
| LIGO (Ringdown GW150914)                | INSERIDO / CALIBRADO                                        |
| SPARC (Curvas de Rotação)               | CALIBRADO / HIPÓTESE INSERIDA                               |
| Órbitas Planetárias                     | CALIBRADO / INSERIDO                                        |
+-----------------------------------------+-------------------------------------------------------------+

*Relatório analítico completo com citações de linha em [`AUDIT_REPORT.md`](file:///d:/GOOGLE/projeto_tge/AUDIT_REPORT.md) e [`TGE_CORE_02_REPORT.md`](file:///d:/GOOGLE/projeto_tge/TGE_CORE_02_REPORT.md).*

---

## 🚫 Proibições e Regras Estritas de Falsificabilidade

1. **Assinatura Lorentziana $(1,3,0)$:** Proibida qualquer regra multiplicativa forçada (`3 * n_time`) ou hardcoded.
2. **Estrutura de Krein ($\eta$):** A matriz $\eta$ é reconhecida e classificada como **HIPÓTESE INSERIDA**. A assinatura obtida em $G_{\text{eff}}$ é **condicional** à partição de $\eta$. No teste de controle negativo com $\eta = I$, a métrica colapsa exatamente em geometria euclidiana $(N, 0, 0)$.
3. **Proibição de Alvo $d=4$:** O número $4$ não pode ser utilizado como alvo de otimização (`minimize(|d - 4|)` é proibido).
4. **Preservação de Falhas Históricas:** O resultado **TGE-2** ($\text{média } d_{\text{spec}} = 3.728$, assinatura $(0,48,0)$, falha da hipótese 4D) é mantido intacto como baseline negativo em `tge/reports/baseline_tge2.json`.

---

## 🎯 Hipóteses Formalizadas (`hypotheses.yaml`)

- **H1:** A dinâmica do Heat Kernel produz dimensão espectral $d_{\text{spec}} \approx 4$ (*FAILED no Dirac puro*).
- **H2:** A estrutura causal Lorentziana 1+3 emerge sem inserção prévia (*FAILED / NOT DEMONSTRATED no modelo atual; condicionada a $\eta$*).
- **H3:** A geometria interna quebra a degenerescência espectral dos autovalores (*UNTESTED*).
- **H4:** O setor leptônico gera a hierarquia de massas de neutrinos via Seesaw (*TESTING*).
- **H5:** A expansão de Seeley-DeWitt gera termos de gravidade efetiva (*TESTING*).
- **H6:** A teoria possui capacidade preditiva fora da amostra (Out-of-sample) (*TESTING*).

---

## 🛠️ Estrutura do Projeto

```text
projeto_tge/
├── AUDIT_REPORT.md                # Relatório oficial de auditoria detalhada por linha
├── TGE_CORE_02_REPORT.md          # Relatório de auditoria de Krein e circularidade causal
├── TGE_BRIDGE.md                  # Protocolo de comunicação síncrona com o Auditor Externo
├── hypotheses.yaml                # Hipóteses formalizadas (H1 a H6) com critérios de falha
├── tge_exchange/                  # Diretório de controle e intercâmbio de dados JSON
├── tge/
│   ├── core/
│   │   └── causal_structure.py   # TGE-CORE-02: Assinatura espectral calculada condicionalmente a eta
│   ├── audit/
│   │   ├── tge_audit.py          # Gerador automatizado da matriz de auditoria
│   │   └── parameter_registry.py # Rastreamento de proveniência de parâmetros
│   ├── experiments/
│   │   └── falsification_suite.py# TGE-FALSIFICATION-SUITE (10 testes falsificáveis)
│   └── reports/
│       ├── baseline_tge2.json    # Registro inviolável do baseline histórico negativo TGE-2
│       ├── audit_report.json     # Exportação JSON do relatório de auditoria
│       └── falsification_suite_report.json # Relatório de execução dos 10 testes
└── core_dirac.py ...              # Módulos legados mantidos congelados para histórico
```

---

## 🔬 Execução da Suíte de Falsificação

Para executar os 10 testes falsificáveis da TGE:

```bash
python tge/experiments/falsification_suite.py
```

Para executar o motor de estrutura causal e testes de Krein:

```bash
python tge/core/causal_structure.py
```
