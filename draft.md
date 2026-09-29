# Analyse réelle

## Suite de Cauchy

Soit $(E, d)$ un espace métrique. Une suite $(u_n)_{n \in \mathbb{N}}$ d'éléments de $E$ est dite de Cauchy si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, d(u_p, u_q) < \varepsilon$$

## Composition de fonctions convexes

Soient $I$ et $J$ deux intervalles de $\mathbb{R}$. Soit $f : I \to J$ et $g : J \to \mathbb{R}$ deux fonctions.
Si $f$ est convexe, $g$ est convexe et $g$ est croissante, alors $g \circ f$ est convexe sur $I$.

## Inégalité des pentes

Soit $I$ un intervalle de $\mathbb{R}$ et $f : I \to \mathbb{R}$ une fonction convexe. Soient $a, b, c \in I$ tels que $a < b < c$.
Alors :
$$\frac{f(b)-f(a)}{b-a} \le \frac{f(c)-f(a)}{c-a} \le \frac{f(c)-f(b)}{c-b}$$
Autrement dit, la fonction taux d'accroissement $T_f : (x, y) \mapsto \frac{f(y)-f(x)}{y-x}$ définie sur $\{(x, y) \in I^2, x \neq y\}$ est croissante par rapport à chacune de ses variables.

## Théorème de Bolzano-Weierstrass

Toute suite bornée de réels (ou d'éléments de $\mathbb{R}^n$) admet au moins une valeur d'adhérence. Autrement dit, on peut en extraire une sous-suite convergente.

## Théorème de la limite monotone

Soit $f : ]a, b[ \to \mathbb{R}$ une fonction croissante.

1. Si $f$ est majorée, alors $f$ admet une limite finie en $b^-$.
2. Sinon, $\lim_{x \to b^-} f(x) = +\infty$.

De même pour la limite en $a^+$.

## Théorème du point fixe de Banach

Soit $(E, d)$ un espace métrique complet non vide. Soit $f : E \to E$ une application contractante, c'est-à-dire qu'il existe $k \in [0, 1[$ tel que :
$$\forall x, y \in E, d(f(x), f(y)) \le k d(x, y)$$
Alors :

1. $f$ admet un unique point fixe $x^* \in E$ (tel que $f(x^*) = x^*$).
2. Pour tout point de départ $u_0 \in E$, la suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_{n+1} = f(u_n)$ converge vers $x^*$.
3. On a l'estimation de la vitesse de convergence suivante : $d(u_n, x^*) \le \frac{k^n}{1-k} d(u_1, u_0)$.

## Dérivée de la fonction réciproque

Soit $f : A \to B$ une bijection dérivable sur $A$. Soit $a \in A$.
Si $f'(a) \neq 0$ et si $f^{-1}$ est continue en $b = f(a)$, alors $f^{-1}$ est dérivable en $b$ et :
$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

## Formule de Taylor-Young

Soit $f \in \mathcal{C}^n(I, E)$ où $E$ est un espace vectoriel normé de dimension finie. Soit $a \in I$.
Alors, au voisinage de $h=0$ tel que $a+h \in I$ :
$$f(a+h) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} h^k + o(h^n)$$

## Inégalité de Taylor-Lagrange

Soit $f \in \mathcal{C}^n([a, b], E)$ telle que $f^{(n)}$ soit dérivable sur $]a, b[$.
Alors :
$$\left\| f(b) - \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (b-a)^k \right\| \le \frac{(b-a)^{n+1}}{(n+1)!} \sup_{t \in ]a, b[} \|f^{(n+1)}(t)\|$$

## Formule de Taylor avec reste intégral

Soit $f \in \mathcal{C}^{n+1}(I, E)$. Soient $a, b \in I$.
Alors :
$$f(b) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (b-a)^k + \int_a^b \frac{(b-t)^n}{n!} f^{(n+1)}(t) dt$$

# Analyse complexe

## Sinus de la somme

Soient $a, b \in \mathbb{C}$. On a :
$$\sin(a+b) = \sin(a)\cos(b) + \cos(a)\sin(b)$$

## Cosinus de la somme

Soient $a, b \in \mathbb{C}$. On a :
$$\cos(a+b) = \cos(a)\cos(b) - \sin(a)\sin(b)$$

## Règle de D'Alembert

Soit $\sum a_n z^n$ une série entière avec $a_n \neq 0$ pour $n$ assez grand.
Si $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = \ell \in [0, +\infty]$, alors le rayon de convergence $R$ de la série est :
$$R = \frac{1}{\ell}$$
(avec la convention $1/0 = +\infty$ et $1/\infty = 0$).

## Règle de Cauchy

Soit $\sum a_n z^n$ une série entière.
Si $\lim_{n \to \infty} |a_n|^{1/n} = \ell \in [0, +\infty]$, alors le rayon de convergence $R$ de la série est :
$$R = \frac{1}{\ell}$$
(avec la convention $1/0 = +\infty$ et $1/\infty = 0$).

## Théorème de Cauchy

Soit $U$ un ouvert simplement connexe de $\mathbb{C}$ et $f : U \to \mathbb{C}$ une fonction holomorphe. Soit $\gamma$ un lacet (chemin fermé) rectifiable dans $U$.
Alors :
$$\int_{\gamma} f(z) dz = 0$$

## Théorème de Liouville

Toute fonction entière (holomorphe sur $\mathbb{C}$) et bornée est constante.

## Théorème des résidus

Soit $U$ un ouvert simplement connexe de $\mathbb{C}$ et $S$ un ensemble de points isolés dans $U$. Soit $f : U \setminus S \to \mathbb{C}$ une fonction holomorphe. Soit $\gamma$ un lacet rectifiable dans $U \setminus S$.
Alors :
$$\int_{\gamma} f(z) dz = 2i\pi \sum_{a \in S} \text{Ind}_{\gamma}(a) \text{Res}(f, a)$$
où $\text{Ind}_{\gamma}(a)$ est l'indice du lacet $\gamma$ par rapport au point $a$ et $\text{Res}(f, a)$ est le résidu de $f$ en $a$.

# Fonctions vectorielles

## Convergence simple

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions d'un ensemble $X$ vers un espace vectoriel normé $F$. La suite $(f_n)$ converge simplement vers $f : X \to F$ si :
$$\forall x \in X, \lim_{n \to \infty} f_n(x) = f(x)$$

## Convergence uniforme d'une suite de fonctions

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $(F, \|\cdot\|)$. La suite $(f_n)$ converge uniformément vers $f : X \to F$ si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in X, \|f_n(x) - f(x)\| < \varepsilon$$
ou encore $\lim_{n \to \infty} \sup_{x \in X} \|f_n(x) - f(x)\| = 0$.

## Convergence uniforme d'une série de fonctions

Soit $\sum u_n$ une série de fonctions de $X$ vers $F$. On dit qu'elle converge uniformément si la suite de ses sommes partielles $S_n = \sum_{k=0}^n u_k$ converge uniformément sur $X$.

## Convergence absolue d'une série de fonctions

Soit $\sum u_n$ une série de fonctions de $X$ vers $F$. On dit qu'elle converge absolument en $x \in X$ si la série numérique $\sum \|u_n(x)\|$ converge.

## Convergence normale d'une série de fonctions

Soit $\sum u_n$ une série de fonctions de $X$ vers $(F, \|\cdot\|)$. On dit qu'elle converge normalement sur $X$ si la série numérique $\sum \sup_{x \in X} \|u_n(x)\|$ converge.

## Limite uniforme de fonctions bornées

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions bornées de $X$ vers $F$. Si $(f_n)$ converge uniformément vers $f$, alors $f$ est bornée sur $X$.

## Limite uniforme de fonctions continues

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions d'un espace topologique $X$ vers un espace vectoriel normé $F$. Si les $f_n$ sont continues et si $(f_n)$ converge uniformément vers $f$, alors $f$ est continue sur $X$.

## Théorème de la double limite

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers un espace de Banach $F$. Soit $a$ un point adhérent à $X$.
Supposons que :

1. Pour tout $n$, $\lim_{x \to a} f_n(x) = L_n$ existe.
2. $(f_n)$ converge uniformément vers $f$ sur $X$.
   Alors la suite $(L_n)$ converge vers une limite $L$, et $\lim_{x \to a} f(x) = L$.
   On a ainsi : $\lim_{n \to \infty} \lim_{x \to a} f_n(x) = \lim_{x \to a} \lim_{n \to \infty} f_n(x)$.

## Théorème d'intégration d'une suite de fonctions

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions continues de $[a, b]$ vers $F$. Si $(f_n)$ converge uniformément vers $f$ sur $[a, b]$, alors :
$$\lim_{n \to \infty} \int_a^b f_n(t) dt = \int_a^b \left( \lim_{n \to \infty} f_n(t) \right) dt = \int_a^b f(t) dt$$

## Théorème de dérivation d'une suite de fonctions

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de classe $\mathcal{C}^1$ de $[a, b]$ vers $F$. Supposons que :

1. Il existe $x_0 \in [a, b]$ tel que $(f_n(x_0))$ converge.
2. La suite des dérivées $(f_n')$ converge uniformément vers une fonction $g$ sur $[a, b]$.
   Alors $(f_n)$ converge uniformément vers une fonction $f$ de classe $\mathcal{C}^1$ et $f' = g$.

## Théorème de dérivation terme à terme

C'est l'application du théorème précédent aux sommes partielles d'une série de fonctions $\sum u_n$. Si chaque $u_n$ est $\mathcal{C}^1$, si $\sum u_n(x_0)$ converge et $\sum u_n'$ converge uniformément, alors $S = \sum u_n$ est $\mathcal{C}^1$ et $S' = \sum u_n'$.

## Théorème d'intégration terme à terme

Application du théorème d'intégration des suites aux séries de fonctions : si $\sum u_n$ converge uniformément et que les $u_n$ sont continues, alors $\int \sum u_n = \sum \int u_n$.

## Théorème de la double limite terme à terme

Application du théorème de la double limite aux séries de fonctions $\sum u_n$.

## Critère de cauchy uniforme

Une suite de fonctions $(f_n)$ de $X$ vers un espace de Banach $F$ converge uniformément sur $X$ si et seulement si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, \forall x \in X, \|f_p(x) - f_q(x)\| < \varepsilon$$

# Topologie

## Distance

Soit $E$ un ensemble. Une distance sur $E$ est une application $d : E \times E \to \mathbb{R}_+$ vérifiant :

1. Séparation : $d(x, y) = 0 \iff x = y$
2. Symétrie : $d(x, y) = d(y, x)$
3. Inégalité triangulaire : $d(x, z) \le d(x, y) + d(y, z)$

## Norme

Soit $E$ un espace vectoriel sur $\mathbb{K}$. Une norme sur $E$ est une application $\|\cdot\| : E \to \mathbb{R}_+$ vérifiant :

1. Séparation : $\|x\| = 0 \iff x = 0$
2. Homogénéité : $\|\lambda x\| = |\lambda| \|x\|$
3. Inégalité triangulaire : $\|x+y\| \le \|x\| + \|y\|$

## Image continue d'un compact

Soit $f : E \to F$ une application continue d'un espace topologique $E$ dans un espace topologique $F$.
Si $K$ est un sous-ensemble compact de $E$, alors son image $f(K)$ est un sous-ensemble compact de $F$.

## Théorème de Heine

Soit $f : E \to F$ une application continue d'un espace métrique compact $E$ dans un espace métrique $F$.
Alors $f$ est uniformément continue sur $E$, c'est-à-dire :
$$\forall \varepsilon > 0, \exists \delta > 0, \forall x, y \in E, d_E(x, y) < \delta \implies d_F(f(x), f(y)) < \varepsilon$$

## Connexité

Un espace topologique $E$ est connexe s'il n'est pas la réunion de deux ouverts non vides et disjoints.
De manière équivalente, les seules parties de $E$ à la fois ouvertes et fermées sont $\emptyset$ et $E$.

## Homéomorphisme

Une application $f : E \to F$ entre deux espaces topologiques est un homéomorphisme si $f$ est bijective, continue, et si sa réciproque $f^{-1}$ est continue.

## Théorème de Heine-Borel

Dans un espace vectoriel normé de dimension finie, les parties compactes sont exactement les parties fermées et bornées.

## Adhérence d'un connexe

Soit $E$ un espace topologique et $A$ une partie connexe de $E$.
Si $B$ est une partie telle que $A \subseteq B \subseteq \bar{A}$, alors $B$ est connexe. En particulier, l'adhérence $\bar{A}$ d'un connexe est connexe.

## Théorème de Baire

Dans un espace métrique complet (ou un espace localement compact), toute intersection dénombrable d'ouverts denses est dense.
Équivalemment, un tel espace n'est pas la réunion dénombrable de fermés d'intérieur vide.

# Algèbre linéaire

## Endomorphismes qui commutent, sous-espaces stables

Soient $u, v \in \mathcal{L}(E)$ deux endomorphismes d'un espace vectoriel $E$ tels que $u \circ v = v \circ u$.
Alors les sous-espaces propres de $u$ (respectivement $\ker(u)$ and $\text{im}(u)$) sont stables par $v$.

## Décomposition de Dunford

Soit $E$ un espace vectoriel de dimension finie sur $\mathbb{K}$. Soit $u \in \mathcal{L}(E)$ un endomorphisme dont le polynôme caractéristique est scindé sur $\mathbb{K}$.
Alors il existe un unique couple $(d, n) \in \mathcal{L}(E)^2$ tel que :

1. $u = d + n$
2. $d$ est diagonalisable et $n$ est nilpotent
3. $d$ and $n$ commutent ($d \circ n = n \circ d$)
   De plus, $d$ and $n$ sont des polynômes en $u$.

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

1. Son polynôme caractéristique $\chi_A$ est scindé sur $\mathbb{K}$ and la dimension de chaque sous-espace propre est égale à la multiplicité de la valeur propre correspondante.
2. Elle admet un polynôme annulateur scindé à racines simples sur $\mathbb{K}$.
3. Son polynôme minimal $m_A$ est scindé à racines simples sur $\mathbb{K}$.

## Commutant d'un endomorphisme

Soit $u \in \mathcal{L}(E)$. Le commutant de $u$ est l'ensemble $C(u) = \{v \in \mathcal{L}(E) : u \circ v = v \circ u\}$. C'est une sous-algèbre de $\mathcal{L}(E)$.
Si $u$ est diagonalisable à valeurs propres simples, alors $\dim(C(u)) = n$ and $C(u) = \mathbb{K}[u]$.

# Groupes

## Action de groupe

Une action d'un groupe $G$ sur un ensemble $X$ est une application $\cdot : G \times X \to X$ telle que :

1. $\forall x \in X, e_G \cdot x = x$
2. $\forall g, g' \in G, \forall x \in X, (gg') \cdot x = g \cdot (g' \cdot x)$

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
où $n_1 | n_2 | \dots | n_k$ sont les facteurs invariants de $G$.

## Générateurs de Sn et An

1. Le groupe symétrique $\mathfrak{S}_n$ est engendré par les transpositions $(i, j)$. Il est aussi engendré par les transpositions élémentaires $(i, i+1)$.
2. Le groupe alterné $\mathfrak{A}_n$ est engendré par les 3-cycles $(i, j, k)$.

## Simplicité de An (pour n >= 5)

Le groupe alterné $\mathfrak{A}_n$ est un groupe simple (il n'admet aucun sous-groupe distingué propre non trivial) si et seulement si $n \ge 5$.

## Produit semi-direct

Soient $N$ and $H$ deux groupes and $\phi : H \to \text{Aut}(N)$ un morphisme de groupes. Le produit semi-direct $N \rtimes_\phi H$ est le groupe dont l'ensemble sous-jacent est $N \times H$ muni de la loi :
$$(n, h) \cdot (n', h') = (n \phi(h)(n'), hh')$$

## Produit semi-direct par conjugaison

Si $N$ est un sous-groupe distingué de $G$ and $H$ un sous-groupe de $G$ tels que $N \cap H = \{e\}$ and $G = NH$, alors $G$ est isomorphe au produit semi-direct de $N$ par $H$ pour l'action de conjugaison de $H$ sur $N$ : $\phi(h)(n) = hnh^{-1}$.

# Aucun

## Factorisation de a^n - b^n

Soient $a, b \in \mathbb{C}$ and $n \in \mathbb{N}^*$. On a :
$$a^n - b^n = (a-b) \sum_{k=0}^{n-1} a^{n-1-k} b^k$$
