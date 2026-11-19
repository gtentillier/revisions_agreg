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

