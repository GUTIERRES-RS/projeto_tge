# RECONCILIAÇÃO DA DIMENSÃO ESPECTRAL — SPECTRAL_DIMENSION_RECONCILIATION.md
**Teoria Geométrico-Espectral da Emergência (TGE)**  
**Data:** 2026-08-14

---

## 1. O Problema da Inconsistência nos Resultados de $d_{\text{spec}}$

Ao longo das iterações do repositório TGE, foram reportados valores discrepantes para a dimensão espectral:
1. $d_{\text{spec}} \approx 3.728 \pm 0.498$ (Manifesto e Baseline TGE-2);
2. $d_{\text{spec}} \approx 1.15$ (Núcleo TGE-CORE-01 / TGE-CORE-02 em $N=128$);
3. $d_{\text{spec}} \approx 0.98 - 1.05$ (Regime assintótico de matrizes aleatórias GUE puras).

Este documento reconcilia analítica e computacionalmente a origem exata de cada número.

---

## 2. Origem e Comparação Metodológica

| Parâmetro | Baseline TGE-2 | TGE-CORE-01 / 02 | Matriz GUE Pura (Teórico) |
|---|---|---|---|
| **Valor $d_{\text{spec}}$** | $3.72835380 \pm 0.49844691$ | $1.15 \pm 0.05$ | $1.00 \pm 0.05$ |
| **Dimensão $N$** | $N = 48$ | $N = 64, 128, 256$ | $N \to \infty$ |
| **Operador Utilizado** | $L = D^2$ sob discretização TGE-2 | $L = D_{\text{base}}^2$ (GUE) | $L = M^2$ (Wigner GUE) |
| **Faixa de Tempos $t$** | $t \in [10^{-2}, 10^0]$ (Janela restrita) | $t \in [10^{-4}, 10^1]$ (Janela deslizante) | $t \to 0$ |
| **Seleção de Janela** | Janela fixa pré-selecionada | Busca de $\max(R^2)$ | Limite analítico assintótico |
| **Interpretação Física** | **BASELINE NEGATIVO** | **RESULTADO REAL ATUAL** | **COMPORTAMENTO ASSINTÓTICO** |

---

## 3. Explicação Matemática da Diferença

### A. Regime de Matriz Aleatória Pura ($d_{\text{spec}} \approx 1.0 - 1.15$)
Para uma matriz hermitiana Gaussiana (GUE) de dimensão $N$, a densidade de estados obedece à Lei do Semicírculo de Wigner $\rho(\lambda) = \frac{1}{2\pi} \sqrt{4 - \lambda^2}$.
O Heat Trace $P(t) = \text{Tr}(e^{-t L}) = \int \rho(\lambda) e^{-t \lambda^2} d\lambda$.
No regime de difusão de baixa energia ($\lambda \to 0$), $\rho(\lambda) \approx \text{constante}$.
Logo:
$$P(t) \sim \int_0^\infty e^{-t \lambda^2} d\lambda \propto t^{-1/2}$$
Comparando com a definição $P(t) \propto t^{-d_{\text{spec}}/2}$, obtém-se exatamente:
$$-\frac{d_{\text{spec}}}{2} = -\frac{1}{2} \implies d_{\text{spec}} = 1.0$$
Com correções numéricas de borda e tamanho finito de matriz ($N=64, 128$), o ajuste por mínimos quadrados na faixa $t \in [10^{-4}, 10^1]$ resulta em $d_{\text{spec}} \approx 1.10 - 1.15$.

### B. Regime de $N$ Pequeno e Janela Restrita na TGE-2 ($d_{\text{spec}} \approx 3.728$)
Na TGE-2, utilizou-se uma matriz de dimensão muito pequena ($N=48$) e uma janela de tempo restrita onde o efeito de transição de discretização (crossover entre ruído UV e saturação IR) gerou transitoriamente uma inclinação mais acentuada com desvio padrão expressivo ($\pm 0.498$). Quando a dimensão $N$ é aumentada ($N=128, 256, 512$), essa inclinação espúria colapsa no valor assintótico fundamental $d_{\text{spec}} \approx 1.15$.

---

## 4. Conclusão Oficial
1. O valor $d_{\text{spec}} \approx 1.15$ é a dimensão espectral genuína do operador de Dirac hermitiano aleatório discreto.
2. O valor histórico $3.728$ foi um artefato de discretização de $N=48$ com janela restrita, preservado permanentemente como **Baseline Negativo Histórico**.
3. **Falsificação Consolidada:** O operador de Dirac desprovido de ação não-comutativa com potencial de quebra de calibre $V(\phi)$ **não produz $d_{\text{spec}} = 4$**.
