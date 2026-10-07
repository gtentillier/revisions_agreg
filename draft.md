# Fonctions vectorielles

## Inégalité de la norme

Soit $f : [a, b] \to \mathbb{R}^n$ une fonction continue par morceaux. Alors :
$$\left\|\int_a^b f(t) dt\right\| \leq \int_a^b \|f(t)\| dt$$

<details>
<summary>Idée de preuve</summary>
Toute fonction continue sur un segment est limite uniforme de fonctions en escaliers.
</details>

## Approximation uniforme de fonctions continues par des fonctions en escaliers

Soit $E$ un $\mathbb{R}$-espace vectoriel normé. Soit $f : [a, b] \to E$ une fonction continue. Alors, $f$ peut être approchée uniformément par des fonctions en escaliers.

Autrement dit, pour tout $\epsilon > 0$, il existe une fonction en escaliers $g : [a, b] \to E$ telle que :
$$\sup_{t \in [a, b]} \|f(t) - g(t)\| < \epsilon$$

<details>
<summary>Idée de preuve</summary>

---

Théorème de Heine : toute fonction continue sur un segment est uniformément continue.

</details>

## Inégalité des accroissements finis

Soit $f : [a, b] \to \mathbb{R}^n$, $g : [a, b] \to \mathbb{R}$ deux fonctions $C^1$, telles que $\|f'(t)\| \le g'(t)$ pour tout $t \in [a, b]$. Alors :
$$\|f(b) - f(a)\| \le g(b) - g(a)$$

## Formule de changement de variable

Soit $f : [a, b] \to \mathbb{R}^n$ une fonction continue, et soit $\varphi : [\alpha, \beta] \to [a, b]$ une fonction $C^1$. Alors :
$$\int_{\alpha}^{\beta} f(\varphi(t)) \varphi'(t) dt = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(u) du$$
