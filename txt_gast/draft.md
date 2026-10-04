# Algèbre linéaire

## Décomposition de Dunford

Soit $E$ un espace vectoriel de dimension finie sur $\mathbb{K}$. Soit $u \in \mathcal{L}(E)$ un endomorphisme dont le polynôme caractéristique est scindé sur $\mathbb{K}$.
Alors il existe un unique couple $(d, n) \in \mathcal{L}(E)^2$ tel que :

1. $u = d + n$
2. $d$ est diagonalisable et $n$ est nilpotent
3. $d$ et $n$ commutent ($d \circ n = n \circ d$)

De plus, $d$ et $n$ sont des polynômes en $u$.

## Théorème de Cayley-Hamilton

Soit $E$ un espace vectoriel de dimension finie $n$. Pour tout endomorphisme $u \in \mathcal{L}(E)$, son polynôme caractéristique $\chi_u$ est un polynôme annulateur de $u$ :
$$\chi_u(u) = 0_{\mathcal{L}(E)}$$

## Théorème spectral

Soit $E$ un espace euclidien (espace vectoriel réel muni d'un produit scalaire). Soit $u \in \mathcal{L}(E)$ un endomorphisme symétrique.

Alors il existe une base orthonormée de $E$ composée de vecteurs propres de $u$. En particulier, $u$ est diagonalisable.

## Caractérisation des matrices trigonalisables

Une matrice $A \in \mathcal{M}_n(\mathbb{K})$ est trigonalisable sur $\mathbb{K}$ si et seulement si son polynôme caractéristique $\chi_A$ est scindé sur $\mathbb{K}$.

## Caractérisation des matrices diagonalisables

Une matrice $A \in \mathcal{M}_n(\mathbb{K})$ est diagonalisable sur $\mathbb{K}$ si et seulement si l'une des conditions suivantes est vérifiée :

1. Son polynôme caractéristique $\chi_A$ est scindé sur $\mathbb{K}$ et la dimension de chaque sous-espace propre est égale à la multiplicité de la valeur propre correspondante.
2. Son polynôme minimal $m_A$ est scindé à racines simples sur $\mathbb{K}$.

## Commutant d'un endomorphisme

Soit $u \in \mathcal{L}(E)$. Le commutant de $u$ est l'ensemble $C(u) = \{v \in \mathcal{L}(E) : u \circ v = v \circ u\}$. C'est une sous-algèbre de $\mathcal{L}(E)$.
Si $u$ est diagonalisable à valeurs propres simples, alors $\dim(C(u)) = n$ et $C(u) = \mathbb{K}[u]$.

# Groupes

## Action de groupe

Soit $G$ un groupe et $E$ un ensemble. Une action de $G$ sur $E$ est un morphisme de groupes
$$\rho : G \to \operatorname{Bij}(E)$$

L'action est dite **fidèle** si $\rho$ est injectif, c'est-à-dire si :
$$\operatorname{Ker}(\rho) = \{e_G\}$$

## Théorème de Lagrange

Soit $G$ un groupe fini et $H$ un sous-groupe de $G$.
Alors l'ordre de $H$ divise l'ordre de $G$ :
$$|G| = |H| \times [G:H]$$
où $[G:H]$ est l'indice de $H$ dans $G$ (le nombre de classes à gauche).

## Théorème de Cauchy

Soit $G$ un groupe fini et $p$ un nombre premier divisant l'ordre de $G$.
Alors il existe un élément de $G$ d'ordre $p$.

## Théorème de décomposition des groupes abéliens finis

Tout groupe abélien fini $G$ est isomorphe à un produit direct de groupes cycliques :
$$G \cong \mathbb{Z}/n_1\mathbb{Z} \times \mathbb{Z}/n_2\mathbb{Z} \times \dots \times \mathbb{Z}/n_k\mathbb{Z}$$
où $n_1 | n_2 | \dots | n_k$. La suite d'entiers $(n_1, \dots, n_k)$ est unique et ses éléments sont appelés les facteurs invariants de $G$.

## Générateurs de $\mathfrak{S}_n$ et $\mathfrak{A}_n$

1. Le groupe symétrique $\mathfrak{S}_n$ est engendré par les transpositions $(i, j)$. Il est aussi engendré par les transpositions élémentaires $(i, i+1)$.
2. Le groupe alterné $\mathfrak{A}_n$ est engendré par les 3-cycles $(i, j, k)$.

## Simplicité de $\mathfrak{A}_n$

$\forall n \ge 5$, le groupe alterné $\mathfrak{A}_n$ est un groupe simple (il n'admet aucun sous-groupe distingué propre non trivial).

## Produit semi-direct

Soient $N$ et $H$ deux groupes et $\phi : H \to \text{Aut}(N)$ un morphisme de groupes. Le produit semi-direct $N \rtimes_\phi H$ est le groupe dont l'ensemble sous-jacent est $N \times H$ muni de la loi :
$$(n, h) \cdot (n', h') = (n \phi(h)(n'), hh')$$

## Produit semi-direct par conjugaison

Si $N$ est un sous-groupe distingué de $G$ et $H$ un sous-groupe de $G$ tels que $N \cap H = \{e\}$ et $G = NH$, alors $G$ est isomorphe au produit semi-direct de $N$ par $H$ pour l'action de conjugaison de $H$ sur $N$ : $\phi(h)(n) = hnh^{-1}$.
