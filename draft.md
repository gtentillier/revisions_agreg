# Probabilités

## Variable aléatoire

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité, et $(E, \mathcal{E})$ un espace mesurable. Une variable aléatoire est une fonction mesurable $X : \Omega \to E$.

## Tribu engendrée par une famille de variables aléatoires

Soit $(X_i)_{i \in I}$ une famille de variables aléatoires définies sur $(\Omega, \mathcal{F}, \mathbb{P})$ et à valeurs dans des espaces mesurables $(E_i, \mathcal{E}_i)$. 

La tribu engendrée par cette famille est la plus petite tribu $\sigma(X_i, i \in I)$ sur $\Omega$ telle que chaque $X_i$ soit mesurable. Elle est donnée par :
$$
\sigma(X_i, i \in I) = \sigma(\{X_i^{-1}(A) : A \in \mathcal{E}_i, i \in I\})
$$

## Théorème de représentation de Doob

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité, $(E, \mathcal{E})$ un espace mesurable, et $X : \Omega \to E$ une variable aléatoire. Soit $Y : \Omega \to \mathbb{R}$ $\sigma(X)$-mesurable.

Alors il existe une fonction mesurable $\varphi : E \to \mathbb{R}$ telle que :
$$
Y = \varphi(X)
$$

Cas général : Soit $(X_i)_{1 \leq i \leq n}$ une famille de variables aléatoires définies sur $(\Omega, \mathcal{F}, \mathbb{P})$ et à valeurs dans des espaces mesurables $(E_i, \mathcal{E}_i)$. Soit $Y : \Omega \to \mathbb{R}$ $\sigma(X_i, 1 \leq i \leq n)$-mesurable.

Alors il existe une fonction mesurable $\varphi : E_1 \times \cdots \times E_n \to \mathbb{R}$ telle que :
$$
Y = \varphi(X_1, \ldots, X_n)
$$

## Espérance et variable aléatoire intégrable

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité, et $X : \Omega \to [0, +\infty]$ une variable aléatoire.

$$
\mathbb{E}[X] = \int_\Omega X \, d\mathbb{P} = \int_\Omega X(\omega) \, d\mathbb{P}(\omega)
$$

Si $X : \Omega \to \mathbb{C}$ variable aléatoire, on dit que $X$ est $\mathbb{P}$-intégrable si $\mathbb{E}[|X|] < +\infty$. Dans ce cas, on définit l'espérance de $X$ par :

$$
\mathbb{E}[X] = \int_\Omega X \, d\mathbb{P} = \int_\Omega X(\omega) \, d\mathbb{P}(\omega)
$$

Propriétés de l'espérance :

1. Linéarité : Pour toutes variables aléatoires intégrables $X$ et $Y$, et pour tous scalaires $a, b \in \mathbb{C}$, on a :
   $$
   \mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]
   $$

2. Positivité : Si $X \geq Y$ presque sûrement, alors $\mathbb{E}[X] \geq \mathbb{E}[Y]$ où X et Y sont réelles.
3. Inégalité triangulaire : Pour toute variable aléatoire intégrable $X$, on a :
   $$
   |\mathbb{E}[X]| \leq \mathbb{E}[|X|]
   $$
4. Définie : Si $X$ : $\Omega \to [0, +\infty]$, alors $\mathbb{E}[X] = 0$ si et seulement si $X = 0$ presque sûrement.
5. Si $X$ : $\Omega \to [0, +\infty]$, $\mathbb{E}[X] < +\infty$ alors $X < +\infty$ presque sûrement.
6. Si $X$ : $\Omega \to \mathbb{C}$ $\mathbb{P}$-intégrable, $\mathbb{E}[|X|] = |\mathbb{E}[X]|$ alors $X = e^{i\theta} |X|$ presque sûrement pour un certain $\theta \in \mathbb{R}$.
7. Si $X$ : $\Omega \to [0, +\infty]$ bornée par $M > 0$ presque sûrement, alors $\mathbb{E}[X] \leq M$.

## Théorème de convergence monotone pour l'espérance

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires réelles positives croissantes presque sûrement, et soit $X = \lim_{n \to +\infty} X_n$.

Alors $X$ est une variable aléatoire réelle positive, et on a :
$$
\mathbb{E}[X] = \lim_{n \to +\infty} \mathbb{E}[X_n]
$$

## Théorème d'interversion somme et espérance

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires réelles positives, et soit $X = \sum_{n=1}^{+\infty} X_n$.
Alors $X$ est une variable aléatoire réelle positive, et on a :
$$
\mathbb{E}[X] = \sum_{n=1}^{+\infty} \mathbb{E}[X_n]
$$

<details>
<summary>Idée de preuve</summary>

---

Vérifier que $X$ est bien une variable aléatoire, puis appliquer le théorème de convergence monotone à la suite $(S_n)_{n \geq 1}$ définie par $S_n = \sum_{k=1}^{n} X_k$.

</details>

## Lemme de Fatou

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires réelles à valeurs dans $[0, +\infty]$, et soit $X = \liminf_{n \to +\infty} X_n$.

Alors $X$ est une variable aléatoire réelle positive, et on a :
$$
\mathbb{E}[X] \leq \liminf_{n \to +\infty} \mathbb{E}[X_n]
$$
C'est-à-dire :
$$
\mathbb{E}[\liminf_{n \to +\infty} X_n] \leq \liminf_{n \to +\infty} \mathbb{E}[X_n]
$$

## Liminf et Limsup d'une suite d'événements

Soit $(A_n)_{n \geq 1}$ une suite d'événements.

$$
\liminf_{n \to +\infty} A_n = \bigcup_{n=1}^{\infty} \bigcap_{k=n}^{\infty} A_k
$$
$$
\limsup_{n \to +\infty} A_n = \bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} A_k
$$

On peut retrouver ces formules à l'aide des fonctions indicatrices. En effet, on a :
$$
\mathbf{1}_{\liminf_{n \to +\infty} A_n} = \liminf_{n \to +\infty} \mathbf{1}_{A_n}
$$
$$
\mathbf{1}_{\limsup_{n \to +\infty} A_n} = \limsup_{n \to +\infty} \mathbf{1}_{A_n}
$$

$\limsup_{n \to +\infty} A_n$ correspond à l'événement "Une infinité de $A_n$ sont réalisés"

$\liminf_{n \to +\infty} A_n$ correspond à l'événement "Tous les $A_n$ sont réalisés à partir d'un certain rang".

## Théorème de convergence dominée

Soit $X$ et $(X_n)_{n \geq 1}$ des variables aléatoires complexes. On suppose :
1. $X_n \to X$ presque sûrement.
2. Il existe une variable aléatoire positive intégrable $Z$ telle que pour tout $n \geq 1$, $|X_n| \leq Z$ presque sûrement.

Alors les $X_n$ et $X$ sont intégrables, et on a :
1. $\mathbb{E}[X_n] \to \mathbb{E}[X]$
2. $\mathbb{E}[|X_n - X|] \to 0$.

## Théorème d'interversion somme et espérance $l^1$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires complexes telles que $\sum_{n=1}^{+\infty} \mathbb{E}[|X_n|] < +\infty$.

Alors :
1. presque sûrement, la série $\sum_{n=1}^{+\infty} |X_n|$ converge
2. Il existe une variable aléatoire complexe $Y$ telle que $Y = \sum_{n=1}^{+\infty} X_n$ presque sûrement
3. $\mathbb{E}[Y] = \sum_{n=1}^{+\infty} \mathbb{E}[X_n]$
4. $\mathbb{E}[|Y - \sum_{k=1}^{n} X_k|] \to 0$ lorsque $n \to +\infty$.

On écrira malgré un léger abus de notation : 
$$
\mathbb{E}\left[\sum_{n=1}^{+\infty} X_n\right] = \sum_{n=1}^{+\infty} \mathbb{E}[X_n]
$$

## Inégalité de Jensen pour l'espérance

Soit $X$ une variable aléatoire réelle intégrable, et $\varphi : \mathbb{R} \to \mathbb{R}$ une fonction convexe.

Si $\mathbb{E}[|\varphi(X)|] < +\infty$, alors :
$$    
\varphi(\mathbb{E}[X]) \leq \mathbb{E}[\varphi(X)]
$$

## Moment absolu d'ordre $p$ d'une variable aléatoire

Soit $X$ une variable aléatoire complexe, et $p > 0$. On définit le moment absolu d'ordre $p$ de $X$ par :
$$
\mathbb{E}[|X|^p] = \int_\Omega |X(\omega)|^p \, d\mathbb{P}(\omega)
$$

Si $\mathbb{E}[|X|^p] < +\infty$, on dit que $X$ est $p$-intégrable. et on définit son moment d'ordre $p$ par :
$$
\mathbb{E}[X^p] = \int_\Omega X(\omega)^p \, d\mathbb{P}(\omega)
$$

Pour $0<p<q$, si $X$ est $q$-intégrable, alors $X$ est $p$-intégrable et on a :
$$
\mathbb{E}[|X|^p]^{1/p} \leq \mathbb{E}[|X|^q]^{1/q}
$$

## Inégalité de Hölder pour l'espérance

Soit $X$ et $Y$ deux variables aléatoires à valeurs dans $[0, +\infty)$, et $p, q > 1$ tels que $\frac{1}{p} + \frac{1}{q} = 1$. Alors :
$$
\mathbb{E}[|XY|] \leq \mathbb{E}[|X|^p]^{1/p} \mathbb{E}[|Y|^q]^{1/q}
$$

Ainsi, si $X$ et $Y$ sont complexes, que $X$ est $p$-intégrable et $Y$ est $q$-intégrable, alors $XY$ est intégrable et on a :
$$
\mathbb{E}[XY] \leq \mathbb{E}[|X|^p]^{1/p} \mathbb{E}[|Y|^q]^{1/q}
$$

## Inégalité de Markov

Soit $X$ une variable aléatoire réelle positive, $a > 0$, et $\varphi$ une fonction croissante de $\mathbb{R}_+$ dans $\mathbb{R}_+$ éventuellement nulle en 0 mais nulle part ailleurs. Alors :
$$
\mathbb{P}(X \geq a) \leq \frac{\mathbb{E}[\varphi(X)]}{\varphi(a)}
$$

## Variance, lemme de König-Huygens et écart-type

Soit $X$ une variable aléatoire réelle qui admet un moment d'ordre 2. On définit la variance de $X$ par :
$$
\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]
$$

Le lemme de König-Huygens permet d'exprimer la variance en fonction du moment d'ordre 2 et de l'espérance :
$$
\text{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2
$$

L'écart-type de $X$ est défini par :
$$
\sigma(X) = \sqrt{\text{Var}(X)}
$$

## Inégalité de Bienaymé-Tchebychev

Soit $X$ une variable aléatoire réelle qui admet un moment d'ordre 2, et $a > 0$. Alors :
$$
\mathbb{P}(|X - \mathbb{E}[X]| \geq a) \leq \frac{\text{Var}(X)}{a^2}
$$