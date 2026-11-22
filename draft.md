# Probabilités

## Variable aléatoire

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité, et $(E, \mathcal{E})$ un espace mesurable. Une variable aléatoire est une fonction mesurable $X : \Omega \to E$.

## tribu engendrée par une famille de variables aléatoires

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

