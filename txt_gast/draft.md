# Topologie

## Continuité et caractérisations

Soit $(E, d_E)$ et $(F, d_F)$ deux espaces métriques. Soit $f : E \to F$ une application, $x \in E$. Alors les assertions suivantes sont équivalentes :

1. $f$ est continue en $x$.
2. Pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que
   $$f(B^f(x, \delta)) \subseteq B^f(f(x), \varepsilon)$$
3. Pour toute suite $(x_n)_{n \in \mathbb{N}}$ de $E$ convergeant vers $x$, la suite $(f(x_n))_{n \in \mathbb{N}}$ converge vers $f(x)$.

On dit que $f$ est continue sur $E$ ssi

1. $f$ est continue en tout point de $E$
2. Pour tout ouvert $O$ de $F$,
   $$f^{-1}(O) = \{x \in E : f(x) \in O\} \text{ est un ouvert de } E.$$
3. Pour tout fermé $C$ de $F$,
   $$f^{-1}(C) = \{x \in E : f(x) \in C\} \text{ est un fermé de } E.$$

## Valeurs d'adhérence et caractérisations

Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments d'un espace métrique $(E, d)$. Un point $l \in E$ est une **valeur d'adhérence** de la suite $(x_n)$ si :
$$\forall \varepsilon > 0, \quad \{n \in \mathbb{N} : x_n \in B(l, \varepsilon)\} \text{ est infini}$$

**Caractérisation par les ensembles de restes** :
$$Adh(x_n) = \bigcap\limits_{n \in \mathbb{N}} \overline{\{x_m : m \ge n\}} \text{ est donc fermé}$$

**Caractérisation séquentielle** :
$$l \in Adh(x_n) \iff \exists \varphi \text{ extractrice} \text{ telle que } x_{\varphi(n)} \to l$$

# Algèbre linéaire

## Formule de Grassmann

Soient $E$ un espace vectoriel et $F, G$ deux sous-espaces vectoriels de $E$. Alors :
$$\dim(F + G) = \dim(F) + \dim(G) - \dim(F \cap G)$$

## Endomorphismes qui commutent, sous-espaces stables

Soient $u, v \in \mathcal{L}(E)$ deux endomorphismes d'un espace vectoriel $E$ tels que $u \circ v = v \circ u$.

Alors les sous-espaces propres de $u$, $\text{Ker}(u)$ et $\text{Im}(u)$ sont stables par $v$.

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

# à suppr après avoir révisé et vérifié :

# Fonctions vectorielles à suppr après les avoir faites et validées

## Théorème de limite de la dérivée

Soit $(E, \|\cdot\|)$ un $\mathbb{K}$-espace vectoriel de dimension finie. Soit $I$ un intervalle de $\mathbb{R}$ et $a \in I$. Soit $f : I \to E$ une fonction continue sur $I$ et dérivable sur $I \setminus \{a\}$.
Si $f'(x) \xrightarrow[x \to a]{} l$ existe (avec $l \in E$), alors $f$ est dérivable en $a$ et $f'(a) = l$.
La fonction $f'$ est alors continue en $a$.

## Convergence simple d'une suite de fonctions

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$. On dit que la suite $(f_n)$ converge simplement vers une fonction $f : X \to E$ si :
$$\forall x \in X, f_n(x) \xrightarrow[n \to \infty]{} f(x)$$

## Convergence uniforme d'une suite de fonctions

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$. On dit que la suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$ si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in X, \|f_n(x) - f(x)\| < \varepsilon$$
Ceci est équivalent à dire que $\sup_{x \in X} \|f_n(x) - f(x)\| \xrightarrow[n \to \infty]{} 0$.

## Convergence uniforme d'une série de fonctions

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions de $X$ vers $E$. On dit que la série $\sum f_n$ converge uniformément sur $X$ si la suite de ses sommes partielles $(S_n)_{n \in \mathbb{N}}$ converge uniformément sur $X$ vers une fonction $S : X \to E$.

## Convergence absolue d'une série de fonctions

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions de $X$ vers $E$. On dit que la série $\sum f_n$ converge absolument si pour tout $x \in X$, la série numérique $\sum\limits_{n=0}^{\infty} \|f_n(x)\|$ converge.

## Convergence normale d'une série de fonctions

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions de $X$ vers $E$. On dit que la série $\sum f_n$ converge normalement sur $X$ si chaque fonction $f_n$ est bornée sur $X$ et si la série numérique $\sum\limits_{n=0}^{\infty} \sup_{x \in X} \|f_n(x)\|$ converge.

## Limite uniforme de fonctions bornées

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions bornées de $X$ vers $E$. Si la suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$, alors $f$ est bornée sur $X$.

## Limite uniforme de fonctions continues

Soit $X$ un espace topologique et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$. Si chaque fonction $f_n$ est continue sur $X$ et si la suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$, alors $f$ est continue sur $X$.

## Théorème de la double limite

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $a \in \overline{X}$ (avec $a \in \overline{\mathbb{R}}$ si $E = \mathbb{R}$). Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$.
Supposons que :

1. Pour tout $n \in \mathbb{N}$, $\lim_{x \to a} f_n(x) = \lambda_n$ existe dans $E$.
2. La suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$.

Alors :

- La suite $(\lambda_n)_{n \in \mathbb{N}}$ converge vers une limite $\lambda \in E$.
- La fonction $f$ admet une limite en $a$ qui est égale à $\lambda$.

On a alors l'égalité : $\lim_{n \to \infty} \lim_{x \to a} f_n(x) = \lim_{x \to a} \lim_{n \to \infty} f_n(x)$.

## Théorème d'intégration d'une suite de fonctions

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions continues de $I$ vers $E$. Si la suite $(f_n)$ converge uniformément sur tout segment de $I$ vers une fonction $f$ :

Alors :

1. $f$ est continue
2. $\forall x_0 \in I$, la suite des primitives $(F_n)$ définies par $F_n(x) = \int_{x_0}^x f_n(t) dt$ converge simplement et uniformément sur tout segment de $I$ vers la fonction $F : x \mapsto \int_{x_0}^x f(t) dt$.

On a notamment pour tout $[a, b] \subseteq I$ :
$$\int_a^b f_n(t) dt \xrightarrow[n \to \infty]{} \int_a^b f(t) dt$$

## Théorème de dérivation d'une suite de fonctions

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de classe $\mathcal{C}^1$ de $I$ vers $E$. Supposons que :

1. Il existe un point $x_0 \in I$ tel que la suite $(f_n(x_0))_{n \in \mathbb{N}}$ converge dans $E$.
2. La suite des dérivées $(f_n')_{n \in \mathbb{N}}$ converge uniformément sur tout segment de $I$ vers une fonction $g : I \to E$.

Alors :

- La suite $(f_n)_{n \in \mathbb{N}}$ converge uniformément sur tout segment de $I$ vers une fonction $f : I \to E$.
- La fonction $f$ est de classe $\mathcal{C}^1$ sur $I$ et sa dérivée est $f' = g$.

## Théorème de dérivation terme à terme d'une série de fonctions

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $\sum f_n$ une série de fonctions de classe $\mathcal{C}^1$ de $I$ vers $E$. Supposons que :

1. Il existe un point $x_0 \in I$ tel que la série numérique $\sum\limits_{n=0}^{\infty} f_n(x_0)$ converge dans $E$.
2. La série des dérivées $\sum f_n'$ converge uniformément sur tout segment de $I$ vers une fonction $g : I \to E$.

Alors :

- La série $\sum f_n$ converge uniformément sur tout segment de $I$ vers une fonction $S : I \to E$.
- La fonction $S$ est de classe $\mathcal{C}^1$ sur $I$ et sa dérivée est $S' = \sum\limits_{n=0}^\infty f_n' = g$.

## Théorème d'intégration terme à terme d'une série de fonctions

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions continues de $I$ vers $E$. Si la série $\sum f_n$ converge uniformément sur tout segment de $I$ vers une fonction $S : I \to E$, alors pour tout $x_0 \in I$, la suite des sommes partielles des primitives $(\sum\limits_{k=0}^n \int_{x_0}^x f_k(t) dt)_{n \in \mathbb{N}}$ converge simplement et uniformément sur tout segment de $I$ vers la fonction $x \mapsto \int_{x_0}^x S(t) dt$.

On a notamment pour tout $[a, b] \subseteq I$ :
$$\int_a^b \left( \sum\limits_{n=0}^\infty f_n(t) \right) dt = \sum\limits_{n=0}^\infty \int_a^b f_n(t) dt$$

## Théorème de la double limite pour les séries de fonctions

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $a$ un point adhérent à $X$ (avec $a \in \overline{\mathbb{R}}$ si $E = \mathbb{R}$). Soit $\sum f_n$ une série de fonctions de $X$ vers $E$.
Supposons que :

1. Pour tout $n \in \mathbb{N}$, $f_n(x) \xrightarrow[x \to a]{} \lambda_n$ existe dans $E$.
2. La série de fonctions $\sum f_n$ converge uniformément sur $X$ vers une fonction $S : X \to E$.

Alors :

- La série numérique $\sum\limits_{n \in \mathbb{N}} \lambda_n$ converge vers une limite $\lambda \in E$.
- La fonction $S$ admet une limite en $a$ qui est égale à $\lambda$.

On a alors l'égalité : $\sum\limits_{n=0}^\infty f_n(x) \xrightarrow[x \to a]{} \sum\limits_{n=0}^\infty \lambda_n$.

## Critère de Cauchy uniforme

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). On dit qu'une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ de $X$ vers $E$ vérifie le critère de Cauchy uniforme sur $X$ si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, \forall x \in X, \|f_p(x) - f_q(x)\| < \varepsilon$$
Une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ converge uniformément sur $X$ vers une fonction $f : X \to E$ si et seulement si elle vérifie le critère de Cauchy uniforme sur $X$.

# Topologie à suppr quand je les aurai révisé et vérifié

## Distance

Soit $E$ un ensemble. Une distance sur $E$ est une application $d : E \times E \to \mathbb{R}_+$ vérifiant :

1. Séparation : $d(x, y) = 0 \iff x = y$
2. Symétrie : $d(x, y) = d(y, x)$
3. Inégalité triangulaire : $d(x, z) \le d(x, y) + d(y, z)$

<details>
<summary>quatre exemples usuels</summary>

---

- Si $(E, \|\cdot\|)$ est un espace vectoriel normé, alors $d(x, y) = \|x-y\|$ est une distance sur $E$.
- Sur $\overline{\mathbb{R}} = \mathbb{R} \cup \{-\infty, +\infty\}$, on pose $\arctan(-\infty) = -\frac{\pi}{2}$ et $\arctan(+\infty) = \frac{\pi}{2}$. Alors
  $$d(x, y) = |\arctan(x) - \arctan(y)|$$
  est une distance sur $\overline{\mathbb{R}}$.
- La distance discrète sur un ensemble $E$ est définie par
  $$d(x, y) = \mathbf{1}_{x \neq y}.$$
- Soit $E^{\mathbb{N}}$ l'ensemble des suites à valeurs dans un ensemble $E$. La formule
  $$d(U, V) = 2^{-\inf\{k \in \mathbb{N} : U_k \neq V_k\}}$$
  (avec la convention que l'infimum vaut $+\infty$ si $U = V$)
  définit une distance ultra-métrique sur $E^{\mathbb{N}}$, c'est-à-dire qu'elle vérifie
  $$d(U, W) \le \max(d(U, V), d(V, W)).$$

</details>

## Applications lipschitziennes et isométries

Soient $(E, d_E)$ et $(F, d_F)$ deux espaces métriques. Une application $f : E \to F$ est dite $L$-lipschitzienne, où $L \ge 0$, si
$$\forall x, y \in E, \quad d_F(f(x), f(y)) \le L d_E(x, y).$$

Une application $f : E \to F$ est une isométrie si elle préserve les distances, c'est-à-dire si
$$\forall x, y \in E, \quad d_F(f(x), f(y)) = d_E(x, y).$$
Toute isométrie est injective et $1$-lipschitzienne. Si elle est bijective, on parle d'une isométrie de $E$ sur $F$.

## Boules ouvertes, fermées, intérieur et adhérence

Soit $(E, d)$ un espace métrique, $x \in E$ et $r > 0$. La boule ouverte de centre $x$ et de rayon $r$ est
$$B(x,r) = \{y \in E : d(x,y) < r\},$$
et la boule fermée est notée
$$B^f(x,r) = \{y \in E : d(x,y) \le r\}.$$
On a
$$B(x,r) \subseteq B^f(x,r), \qquad \overline{B(x,r)} \subseteq B^f(x,r), \qquad B(x,r) \subseteq \mathring{B^f(x,r)}.$$
Dans un espace métrique quelconque, ces inclusions peuvent être strictes. Par exemple, soit $E = \{a,b\}$ muni de la distance discrète $d(a,b)=1$, et prenons $r=1$. Alors
$$B(a,1)=\{a\}, \qquad B^f(a,1)=E.$$
Comme toute partie d'un espace métrique fini est ouverte et fermée, on obtient
$$\overline{B(a,1)}=\{a\} \subsetneq E=B^f(a,1),$$
et
$$B(a,1)=\{a\} \subsetneq E=\mathring{B^f(a,1)}.$$
Dans un espace vectoriel normé, les deux dernières inclusions sont des égalités : l'adhérence de la boule ouverte est la boule fermée et l'intérieur de la boule fermée est la boule ouverte.

## Diamètre

Soit $(E, d)$ un espace métrique et $A \subseteq E$. Le diamètre de $A$ est défini par :
$$\text{diam}(A) = \sup\{d(x, y) : x, y \in A\}$$

A est borné ssi $\text{diam}(A) < +\infty$
$$\iff \exists x_0 \in E, r > 0, \text{ tel que } A \subseteq B(x_0, r)$$
$$\iff \forall x_0 \in E, \exists r > 0, \text{ tel que } A \subseteq B(x_0, r)$$

## Points intérieurs, adhérents, isolés et d'accumulation

Soit $(E, d)$ un espace métrique et $A \subseteq E$.

Un point $x \in E$ est **intérieur** à $A$ s'il existe $r > 0$ tel que
$B(x, r) \subseteq A.$

Un point $x \in E$ est **adhérent** à $A$ si
$\forall r > 0, \quad B(x, r) \cap A \neq \emptyset.$

Un point $x \in A$ est **isolé** dans $A$ s'il existe $r > 0$ tel que
$B(x, r) \cap A = \{x\}.$
A est dit **discret** si tous ses points sont isolés.

Un point $x \in E$ est un **point d'accumulation** de $A$ si
$\forall r > 0, \quad B(x, r) \cap (A \setminus \{x\}) \neq \emptyset.$

$$\overline{A} = \text{Acc}(A) \sqcup \text{Isol}(A)$$

## Intérieur et adhérence des opérations ensemblistes

Pour toutes parties $A, B \subseteq E$ :
$$\mathring{E \setminus A} = E \setminus \overline{A}, \qquad \overline{E \setminus A} = E \setminus \mathring{A}.$$
$$\mathring{A} \cup \mathring{B} \subseteq \mathring{A \cup B}, \qquad \overline{A \cup B} = \overline{A} \cup \overline{B}.$$
$$\mathring{A \cap B} = \mathring{A} \cap \mathring{B}, \qquad \overline{A \cap B} \subseteq \overline{A} \cap \overline{B}.$$

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

## Ensemble connexe

Un espace topologique $E$ est connexe si
$$\nexists U, V \in \mathcal{P}(E), \quad U \text{ et } V \text{ ouverts non-vides}, \quad E = U \sqcup V.$$
De manière équivalente :
$$\forall A \subseteq E, \quad \left(A \text{ ouvert et fermé}\right) \implies A \in \{\emptyset, E\}.$$

## Homéomorphisme

Une application $f : E \to F$ entre deux espaces topologiques est un homéomorphisme si :

$(i)$ $f$ est bijective

$(ii)$ $f$ est continue

$(iii)$ $f^{-1}$ est continue

## Théorème de Borel-Lebesgue / Heine-Borel

Dans un espace vectoriel normé de dimension finie, les fermés bornés sont compacts.

## Adhérence d'un connexe

Soit $E$ un espace topologique et $A$ une partie connexe de $E$.
Si $B$ est une partie telle que $A \subseteq B \subseteq \bar{A}$, alors $B$ est connexe. En particulier, l'adhérence $\bar{A}$ d'un connexe est connexe.

# Théorie des ensembles à suppr après avoir révisé et vérifié

## Bon ordre

Un ordre sur un ensemble $E$ est dit **bon** si toute partie non vide de $E$ possède un minimum.

# Topologie à suppr après avoir révisé et vérifié

## Espace métrique séparable

Un espace métrique $(E, d)$ est dit **séparable** s'il existe une partie de $E$ dénombrable dense.

# Anneaux à suppr après avoir révisé et vérifié

## Polynôme

Soit $A$ un anneau commutatif. L'anneau des polynômes à une indéterminée $X$ à coefficients dans $A$ est l'ensemble :
$$A[X] = \left\{ \sum_{i=0}^n a_i X^i : n \in \mathbb{N}, a_i \in A \right\}$$

## Caractérisation racine d'un polynôme, lien nombre de racines / degré, degré d'un produit de polynômes

Soit $A$ un anneau commutatif et $P \in A[X]$. Alors $a \in A$ est racine de $P$ si et seulement si $(X - a) \mid P$ dans $A[X]$.

Si de plus $A$ est intègre, alors le nombre de racines distinctes de $P$ dans $A$ est inférieur ou égal au degré de $P$.

## Lemme d'Euclide

Soit $A$ un anneau principal. Soit $p \in A$ un élément irréductible. Soient $a, b \in A$.
Si $p | ab$, alors $p | a$ ou $p | b$.

## Anneau euclidien

Un anneau commutatif intègre $A$ est dit **euclidien** s'il existe une application $\varphi : A \setminus \{0\} \to \mathbb{N}$, appelée stathme, telle que :
$$\forall (a, b) \in A \times A \setminus \{0\}, \exists (q, r) \in A^2, \quad a = bq + r \quad \text{avec} \quad r = 0 \text{ ou } \varphi(r) < \varphi(b)$$

De plus, tout anneau **euclidien** est **principal**.

<details>
<summary>Exemples</summary>

---

- L'anneau $\mathbb{Z}$ avec le stathme $\varphi(n) = |n|$.
- L'anneau des entiers de Gauss $\mathbb{Z}[i]$ avec le stathme $\varphi(a+ib) = a^2 + b^2$.
- L'anneau des polynômes $k[X]$ sur un corps $k$ avec le stathme $\varphi(P) = \deg(P)$.

L'algorithme de la division euclidienne fonctionne dans $A[X]$ pour tout anneau commutatif $A$, à condition que le diviseur possède un coefficient dominant inversible dans $A$.

</details>

## Caractérisation d'un élément irréductible dans un anneau principal

Soit $A$ un anneau principal. Soit $p \in A \setminus \{0\}$.
Les assertions suivantes sont équivalentes :

1. $p$ est irréductible.
2. L'idéal $(p)$ est premier.
3. L'idéal $(p)$ est maximal.

## Idéaux et Anneaux principaux

Un idéal $I$ d'un anneau $A$ est dit **principal** s'il existe un élément $a \in A$ tel que $I = (a) = \{ax : x \in A\}$.

Un anneau $A$ est dit **principal** si tout idéal de $A$ est principal.

## $1^{\text{er}}$ théorème d'isomorphisme pour les anneaux

Soient $A, B$ deux anneaux et $\varphi : A \to B$ un morphisme d'anneaux.
Alors $\text{Ker}(\varphi)$ est un idéal de $A$, $\text{Im}(\varphi)$ est un sous-anneau de $B$, et $\varphi$ induit un isomorphisme d'anneaux :
$$\bar{\varphi} : A/\text{Ker}(\varphi) \xrightarrow{\sim} \text{Im}(\varphi)$$

## Théorème chinois, version générale

Soit $A$ un anneau. Soient $I, J$ deux idéaux de $A$. Si $I + J = A$, alors $I \cap J = IJ$ et l'on a l'isomorphisme d'anneaux :
$$A/(I \cap J) \cong A/I \times A/J$$

Plus généralement, soit $A$ un anneau. Soient $I_1, \dots, I_n$ des idéaux de $A$.
On considère le morphisme d'anneaux :
$$\phi : A \to A/I_1 \times \dots \times A/I_n$$
$$x \mapsto (x \pmod{I_1}, \dots, x \pmod{I_n})$$

1. Le noyau de $\phi$ est $\text{Ker}(\phi) = \bigcap\limits_{i=1}^n I_i$.
2. Si les idéaux sont deux à deux comaximaux (i.e. $I_i + I_j = A$ pour $i \neq j$), alors :
   - $\prod\limits_{i=1}^n I_i = \bigcap\limits_{i=1}^n I_i$
   - Le morphisme $\phi$ est surjectif.
     En particulier, on a l'isomorphisme d'anneaux :
     $$A / \left( \bigcap\limits_{i=1}^n I_i \right) \cong \prod\limits_{i=1}^n A/I_i$$

## Caractérisation d'un corps avec les idéaux

Soit $A$ un anneau commutatif. Alors $A$ est un corps ssi les seuls idéaux de $A$ sont $\{0\}$ et $A$.
