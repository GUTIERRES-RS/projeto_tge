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

## 📋 Matriz de Auditoria do Repositório (Fase 1)

+-----------------------------------------+-----------------------------------------+
| Resultado                               | Classificação                           |
+-----------------------------------------+-----------------------------------------+
| d_spec (Heat Kernel / Plateau R^2)      | DERIVADO                                |
| assinatura (Krein Real TGE-CORE-01)     | DERIVADO (Real) / INSERIDO (Hist. (1,3))|
| Seeley-DeWitt (a_0 a a_6)               | CALIBRADO / INSERIDO                    |
| Yukawa (Setor de Massa)                 | INSERIDO / CALIBRADO                    |
| CKM (Mistura de Quarks)                 | INSERIDO / CALIBRADO                    |
| PMNS (Oscilação de Neutrinos)           | INSERIDO                                |
| Seesaw (Escala Sub-eV)                  | DERIVADO (Fórmula) / INSERIDO (Valores) |
| ΩΛ (Energia Escura)                     | INSERIDO                                |
| ΩDM (Matéria Escura)                    | INSERIDO                                |
| Higgs (Largura e Branching LHC)         | INSERIDO                                |
| g-2 (Anomalia do Múon)                  | INSERIDO                                |
| LIGO (Ringdown GW150914)                | INSERIDO / CALIBRADO                    |
| SPARC (Curvas de Rotação)               | CALIBRADO / HIPÓTESE INSERIDA           |
| Órbitas Planetárias                     | CALIBRADO / INSERIDO                    |
+-----------------------------------------+-----------------------------------------+

*Relatório analítico completo com citações de linha em [`AUDIT_REPORT.md`](file:///d:/GOOGLE/projeto_tge/AUDIT_REPORT.md).*

---

## 🚫 Proibições e Regras Estritas de Falsificabilidade

1. **Assinatura Lorentziana $(1,3,0)$:** Removida a regra artificial `3 * n_effective_time`. A assinatura é computada puramente dos sinais dos autovalores da métrica efetiva $G_{\text{eff}}$.
2. **Proibição de Alvo $d=4$:** O número $4$ não pode ser utilizado como alvo de otimização (`minimize(|d - 4|)` é proibido).
3. **Preservação de Falhas Historicas:** O resultado **TGE-2** ($\text{média } d_{\text{spec}} = 3.728$, assinatura $(0,48,0)$, falha da hipótese 4D) é mantido intacto como baseline negativo em `tge/reports/baseline_tge2.json`.

---

## 🎯 Hipóteses Formalizadas (`hypotheses.yaml`)

- **H1:** A dinâmica do Heat Kernel produz dimensão espectral $d_{\text{spec}} \approx 4$.
- **H2:** A estrutura causal do Espaço de Krein produz assinatura Lorentziana indefinida.
- **H3:** A geometria interna quebra a degenerescência espectral dos autovalores.
- **H4:** O setor leptônico gera a hierarquia de massas de neutrinos via Seesaw.
- **H5:** A expansão de Seeley-DeWitt gera termos de gravidade efetiva.
- **H6:** A teoria possui capacidade preditiva fora da amostra (Out-of-sample).

---

## 🛠️ Estrutura do Projeto

```text
projeto_tge/
├── AUDIT_REPORT.md                # Relatório oficial de auditoria detalhada por linha
├── hypotheses.yaml                # Hipóteses formalizadas (H1 a H6) com critérios de falha
├── tge/
│   ├── core/
│   │   ├── dirac.py              # Núcleo espectral de Dirac
│   │   └── causal_structure.py   # TGE-CORE-01: Assinatura causal independente (sem circularidade)
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

Para gerar a matriz de auditoria de proveniência:

```bash
python tge/audit/tge_audit.py
```
