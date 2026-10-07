# Chapitre : Groupes

## Groupe

Un **groupe** est un ensemble $G$ muni d'une loi de composition interne $\cdot : G \times G \to G$ vérifiant les axiomes suivants :

1. **Associativité** : $\forall x, y, z \in G$, $(x \cdot y) \cdot z = x \cdot (y \cdot z)$.
2. **Élément neutre** : Il existe un élément $e \in G$ tel que $\forall x \in G$, $e \cdot x = x \cdot e = x$.
3. **Inverse** : $\forall x \in G$, il existe un élément $x^{-1} \in G$ tel que $x \cdot x^{-1} = x^{-1} \cdot x = e$.

## p-groupe, p-sous-groupe, p-Sylow

Un **p-groupe** est un groupe fini tel que : $|G| = p^n$ avec $n \ge 1$ et $p$ premier.

Un **p-sous-groupe** d'un groupe $G$ est un sous-groupe $H$ de $G$ tel que $|H| = p^m$ avec $m \ge 1$ et $p$ premier.

Un **p-sous-groupe de Sylow**, ou **p-Sylow** d'un groupe fini $G$ est un p-sous-groupe maximal de $G$, c'est-à-dire un p-sous-groupe $P$ tel que $|P| = p^n$ avec $p^n$ le plus grand facteur premier de l'ordre de $G$.

## Morphisme de groupes

Un **morphisme de groupes** est une application $f : G \to H$ entre deux groupes $(G, \cdot)$ et $(H, *)$ telle que :
$$\forall x, y \in G, \quad f(x \cdot y) = f(x) * f(y)$$

De plus, on peut montrer que :
$$f(e_G) = e_H \quad \text{et} \quad f(x^{-1}) = f(x)^{-1} \quad \text{pour tout } x \in G.$$

On parle d'**isomorphisme**, d'**endomorphisme** ou d'**automorphisme** selon que $f$ est bijective, de $G$ dans lui-même, ou bijective de $G$ dans lui-même.

## Action de groupe, fidèle, transitive

Soit $G$ un groupe et $E$ un ensemble. Une action de $G$ sur $E$ est un morphisme de groupes
$$\rho : G \to \operatorname{Bij}(E)$$

L'action est dite **fidèle** si $\rho$ est injectif, c'est-à-dire si :
$$\operatorname{Ker}(\rho) = \{e_G\}$$

L'action est dite **transitive** si pour tout $x, y \in E$, il existe $g \in G$ tel que $\rho(g)(x) = y$.

## Orbites, Stabilisateurs, Points fixes et propriétés

Soit $G$ un groupe agissant sur un ensemble $E$. Pour tout $x \in E$, on définit :

- L'**orbite** de $x$ sous l'action de $G$ :
  $$O_x = \{\rho(g)(x) \mid g \in G\}$$
- Le **stabilisateur** de $x$ dans $G$ :
  $$\operatorname{Stab}_x = \{g \in G \mid \rho(g)(x) = x\}$$
- L'ensemble des **points fixes** :
  $$E^G = \{x \in E \mid \forall g \in G, \rho(g)(x) = x\}$$

L'application suivante est une bijection :
$$\begin{aligned} f : G / \operatorname{Stab}_x &\to O_x \\ g \operatorname{Stab}_x &\mapsto \rho(g)(x) \end{aligned}$$
En particulier, si $G$ est un groupe fini, on a la relation :
$$|O_x| = [G : \operatorname{Stab}_x] = \frac{|G|}{|\operatorname{Stab}_x|}$$

Si $G$ est un p-groupe, alors $|E^G| \equiv |E| \mod p$.

## Formule des classes

Soit $G$ un groupe agissant sur un ensemble $E$. Alors l'ensemble des orbites de $E$ sous l'action de $G$ forme une partition de $E$, et on a la formule suivante :
$$|E| = \sum_{x \in \mathcal{R}} |O_x|$$
où $\mathcal{R}$ est l'espace quotient, c'est-à-dire un ensemble de représentants des orbites de $E$ sous l'action de $G$.

## Groupe de type fini, monogène, cyclique, simple

Un groupe $G$ est dit **de type fini** s'il existe un ensemble fini $X \subset G$ tel que $G = \langle X \rangle$.

Un groupe $G$ est dit **monogène** s'il existe un élément $g \in G$ tel que $G = \langle g \rangle$.

Un groupe monogène fini est dit **cyclique**.

Un groupe $G$ est dit **simple** s'il est non trivial et n'admet aucun sous-groupe distingué propre non trivial.<br>
En particulier, tout groupe abélien simple est isomorphe à $\mathbb{Z}/p\mathbb{Z}$ avec $p$ premier.

## Sous-groupe distingué/normal

Un sous-groupe $N$ d'un groupe $G$ est dit **distingué** (ou **normal**) ie. $N \triangleleft G$ ssi l'une des conditions équivalentes suivantes est vérifiée :

1. $gNg^{-1} = N$ pour tout $g \in G$.
2. $gN = Ng$ pour tout $g \in G$.
3. Il existe un morphisme de groupes $f : G \to H$ tel que $N = \operatorname{Ker}(f)$.
4. Il existe une structure de groupe sur l'ensemble quotient $G/N$ compatible avec la loi de G, ie. la projection canonique $\pi : G \to G/N$ est un morphisme de groupes.

## 1er théorème d'isomorphisme pour les groupes

Soient $G, H$ deux groupes et $\varphi : G \to H$ un morphisme de groupes.
Alors $\text{Ker}(\varphi) \triangleleft G$, $\text{Im}(\varphi)$ est un sous-groupe de $H$, et $\varphi$ induit un isomorphisme de groupes :
$$\bar{\varphi} : G/\text{Ker}(\varphi) \xrightarrow{\sim} \text{Im}(\varphi)$$

## Théorème de Lagrange

Soit $G$ un groupe fini et $H$ un sous-groupe de $G$.
Alors l'ordre de $H$ divise l'ordre de $G$ :
$$|G| = |H| \times [G:H]$$
où $[G:H]$ est l'indice de $H$ dans $G$ (le nombre de classes à gauche).

## Théorème de Cauchy

Soit $G$ un groupe fini et $p$ un nombre premier divisant l'ordre de $G$.
Alors il existe un élément de $G$ d'ordre $p$.

## Théorème de structure des groupes abéliens finis

Tout groupe abélien fini $G$ est isomorphe à un produit direct de groupes cycliques :
$$G \cong \mathbb{Z}/n_1\mathbb{Z} \times \mathbb{Z}/n_2\mathbb{Z} \times \dots \times \mathbb{Z}/n_k\mathbb{Z}$$
où $n_1 | n_2 | \dots | n_k$. La suite d'entiers $(n_1, \dots, n_k)$ est unique et ses éléments sont appelés les facteurs invariants de $G$.

## Générateurs de $\mathfrak{S}_n$ et $\mathfrak{A}_n$

1. Le groupe symétrique $\mathfrak{S}_n$ est engendré par les transpositions $(i, j)$. Il est aussi engendré par les transpositions élémentaires $(i, i+1)$.
2. Le groupe alterné $\mathfrak{A}_n$ est engendré par les 3-cycles $(i, j, k)$.

## Décomposition d'une permutation

Toute permutation $\sigma \in \mathfrak{S}_n$ peut s'écrire de manière unique (à l'ordre des cycles près) comme un produit de cycles disjoints :
$$\sigma = c_1 c_2 \dots c_k$$

## Simplicité de $\mathfrak{A}_n$

$\forall n \ge 5$, le groupe alterné $\mathfrak{A}_n$ est un groupe simple (il n'admet aucun sous-groupe distingué propre non trivial).

Ainsi, pour $n \ge 5$, le groupe symétrique $\mathfrak{S}_n$ n'admet aucun sous-groupe distingué propre non trivial autre que $\mathfrak{A}_n$.

## Conjugaison d'un cycle par un élément de $\mathfrak{S}_n$

Soit $\sigma \in \mathfrak{S}_n$ et $(i_1, i_2, \dots, i_k)$ un cycle de $\mathfrak{S}_n$. Alors :
$$\sigma (i_1, i_2, \dots, i_k) \sigma^{-1} = (\sigma(i_1), \sigma(i_2), \dots, \sigma(i_k))$$

## Produit semi-direct

Soient $N$ et $H$ deux groupes et $\rho : H \to \text{Aut}(N)$ un morphisme de groupes. Le produit semi-direct $N \rtimes_\rho H$ est le groupe dont l'ensemble sous-jacent est $N \times H$ muni de la loi :
$$ (n, h) \cdot (n', h') = (n \rho(h)(n'), hh') $$

## Produit semi-direct par conjugaison

Si $N$ est un sous-groupe distingué de $G$ et $H$ un sous-groupe de $G$ tels que $N \cap H = \{e\}$ et $G = NH$, alors $G$ est isomorphe au produit semi-direct de $N$ par $H$ pour l'action de conjugaison de $H$ sur $N$ : $\rho(h)(n) = hnh^{-1}$.

## Quatre exemples de produits semi-directs

1. **Le groupe symétrique $\mathfrak{S}_n$**
<details>
<summary>Voir plus</summary>

---

Soit $n \ge 2$. Le groupe alterné $\mathfrak{A}_n$ est un sous-groupe distingué de $\mathfrak{S}_n$ car il est le noyau du morphisme signature $\varepsilon : \mathfrak{S}_n \to \{-1, 1\}$. Soit $\tau \in \mathfrak{S}_n$ une transposition (par exemple $\tau = (1, 2)$). On considère le sous-groupe $H = \{id, \tau\} \cong \mathbb{Z}/2\mathbb{Z}$. Comme $\mathfrak{A}_n \cap H = \{id\}$ et $|\mathfrak{A}_n| \cdot |H| = \frac{n!}{2} \cdot 2 = n! = |\mathfrak{S}_n|$, on a :
$$\mathfrak{S}_n \cong \mathfrak{A}_n \rtimes_\rho \mathbb{Z}/2\mathbb{Z}$$
où l'action $\rho$ de l'élément non nul de $\mathbb{Z}/2\mathbb{Z}$ sur $\mathfrak{A}_n$ est la conjugaison par $\tau$.

---

</details>
<br>

2. **Le groupe linéaire $GL_n(\mathbb{K})$**
<details>
<summary>Voir plus</summary>

---

Soit $n \ge 1$ et $\mathbb{K}$ un corps. Le groupe spécial linéaire $SL_n(\mathbb{K})$ est le noyau du morphisme déterminant $\det : GL_n(\mathbb{K}) \to \mathbb{K}^*$, c'est donc un sous-groupe distingué. Soit $H$ le sous-groupe des matrices de la forme $\operatorname{diag}(\lambda, 1, \dots, 1)$ pour $\lambda \in \mathbb{K}^*$. On a $H \cong \mathbb{K}^*$, $SL_n(\mathbb{K}) \cap H = \{I_n\}$ et $GL_n(\mathbb{K}) = SL_n(\mathbb{K})H$. Ainsi :
$$GL_n(\mathbb{K}) \cong SL_n(\mathbb{K}) \rtimes_\rho \mathbb{K}^*$$
où l'action est donnée par $\rho(\lambda)(M) = \operatorname{diag}(\lambda, 1, \dots, 1) M \operatorname{diag}(\lambda, 1, \dots, 1)^{-1}$.

---

</details>
<br>

3. **Le groupe diédral $D_n$**
<details>
<summary>Voir plus</summary>

---

Soit $n \ge 3$. Le groupe diédral $D_n$ est le groupe des isométries d'un polygone régulier à $n$ sommets. Il est engendré par une rotation $r$ d'ordre $n$ et une réflexion $s$ d'ordre $2$. En voyant $D_n$ comme un sous-groupe de $O_2(\mathbb{R})$, le sous-groupe des rotations $N = \langle r \rangle \cong \mathbb{Z}/n\mathbb{Z}$ est le noyau du déterminant (restreint à $D_n$) $\det : D_n \to \{-1, 1\}$, il est donc distingué. Le sous-groupe $H = \langle s \rangle \cong \mathbb{Z}/2\mathbb{Z}$ vérifie $N \cap H = \{id\}$ et $D_n = NH$. On a :
$$D_n \cong \mathbb{Z}/n\mathbb{Z} \rtimes_\rho \mathbb{Z}/2\mathbb{Z}$$
où l'action $\rho$ de l'élément non nul de $\mathbb{Z}/2\mathbb{Z}$ sur $\mathbb{Z}/n\mathbb{Z}$ est l'inversion $x \mapsto -x$ (en notation additive). On retrouve ici la relation de conjugaison interne dans $D_n$ : $srs^{-1} = r^{-1}$.

---

</details>
<br>

4. **Le groupe affine $\operatorname{GA}(E)$**
<details>
<summary>Voir plus</summary>

---

Soit $E$ un espace vectoriel sur un corps $\mathbb{K}$. On peut définir le produit semi-direct du groupe additif $(E, +)$ par le groupe linéaire $GL(E)$ en utilisant l'action naturelle de $GL(E)$ sur $E$ :
$$\rho : GL(E) \to \operatorname{Aut}(E)$$
$$u \mapsto (x \mapsto u(x))$$
Le groupe obtenu $E \rtimes_\rho GL(E)$ est le **groupe affine** de $E$, noté $\operatorname{GA}(E)$. On peut identifier $E$ au sous-groupe des translations $t_x$. Ce sous-groupe est distingué car il est le noyau du morphisme "partie linéaire" $L : \operatorname{GA}(E) \to GL(E)$ qui à une application affine $f$ associe son application linéaire associée $\vec{f}$. On peut aussi voir cette action comme une conjugaison au sein de $\operatorname{GA}(E)$ : pour tout $u \in GL(E)$ et $x \in E$, on a $u \circ t_x \circ u^{-1} = t_{u(x)}$.

---

</details>
<br>

## Éléments de torsion et sous-groupe de torsion

Soit $G$ un groupe. Un élément $g \in G$ est un **élément de torsion** si son ordre est fini, i.e. si $g^n = e$ pour un certain entier $n \ge 1$.

Si $G$ est abélien, l'ensemble des éléments de torsion de $G$ forme un sous-groupe de $G$, appelé le **sous-groupe de torsion** de $G$.

## Théorème de structure des groupes abéliens de type fini

Soit $G$ un groupe abélien de type fini. Alors il existe un entier $r \ge 0$ et des entiers $n_1, \dots, n_k \ge 2$ tels que :
$$G \cong \mathbb{Z}^r \times \mathbb{Z}/n_1\mathbb{Z} \times \dots \times \mathbb{/Z}/n_k\mathbb{Z}$$
où $n_1 | n_2 | \dots | n_k$. La suite d'entiers $(n_1, \dots, n_k)$ est unique et ses éléments sont appelés les facteurs invariants de $G$.

# Chapitre : Algèbre linéaire

## Topologie de $GL_n(\mathbb{K})$

### $GL_n(\mathbb{K})$ est ouvert

<details>
<summary>Voir plus</summary>

---

Soit $n \in \mathbb{N}^*$. L'ensemble $GL_n(\mathbb{K})$ est un ouvert de l'espace vectoriel normé $(\mathcal{M}_n(\mathbb{K}), \|\cdot\|)$.

En effet, l'application $\det : \mathcal{M}_n(\mathbb{K}) \to \mathbb{K}$ est continue et $GL_n(\mathbb{K}) = \det^{-1}(\mathbb{K}^*)$. Comme $\mathbb{K}^*$ est un ouvert de $\mathbb{K}$, son image réciproque par une application continue est un ouvert de $\mathcal{M}_n(\mathbb{K})$.

---

</details>

### $GL_n(\mathbb{K})$ est dense dans $\mathcal{M}_n(\mathbb{K})$

<details>
<summary>Voir plus</summary>

---

Soit $n \in \mathbb{N}^*$. Le groupe $GL_n(\mathbb{K})$ est dense dans $(\mathcal{M}_n(\mathbb{K}), \|\cdot\|)$.

Pour toute matrice $A \in \mathcal{M}_n(\mathbb{K})$, le polynôme $P(\lambda) = \det(A - \lambda I_n)$ n'est pas identiquement nul (le coefficient de $\lambda^n$ est $(-1)^n$), il admet donc un nombre fini de racines.

Ainsi, il existe $\varepsilon_0 > 0$ tel que pour tout $\varepsilon \in ]0, \varepsilon_0[$, $\det(A - \varepsilon I_n) \neq 0$, donc $A - \varepsilon I_n \in GL_n(\mathbb{K})$. On a alors $A - \varepsilon I_n \xrightarrow{\varepsilon \to 0} A$.

---

</details>

### $GL_n(\mathbb{K})$ est connexe par arcs ?

<details>
<summary>Voir plus</summary>

---

Soit $n \in \mathbb{N}^*$.

1. Le groupe $GL_n(\mathbb{C})$ est connexe par arcs.
2. Le groupe $GL_n(\mathbb{R})$ possède exactement deux composantes connexes par arcs :
   - $GL_n^+(\mathbb{R}) = \{M \in GL_n(\mathbb{R}) \mid \det(M) > 0\}$, qui contient la matrice identité $I_n$.
   - $GL_n^-(\mathbb{R}) = \{M \in GL_n(\mathbb{R}) \mid \det(M) < 0\}$.
     En particulier, $GL_n(\mathbb{R})$ n'est pas connexe.

---

</details>

## Groupe orthogonal $O_n(\mathbb{R})$ et unitaire $U_n(\mathbb{C})$

Version matricielle : <br>$O_n(\mathbb{R}) = \{M \in GL_n(\mathbb{R}) \mid M^T M = I_n\}$
<br>$SO_n(\mathbb{R}) = \{M \in O_n(\mathbb{R}) \mid \det(M) = 1\}$
<br>$U_n(\mathbb{C}) = \{M \in GL_n(\mathbb{C}) \mid M^* M = I_n\}$
<br>$SU_n(\mathbb{C}) = \{M \in U_n(\mathbb{C}) \mid \det(M) = 1\}$

Version fonctionnelle : <br>$O(E) = \{f \in GL(E) \mid \forall x, y \in E, \langle f(x), f(y) \rangle = \langle x, y \rangle\}$
<br>$SO(E) = \{f \in O(E) \mid \det(f) = 1\}$
<br>$U(E) = \{f \in GL(E) \mid \forall x, y \in E, \langle f(x), f(y) \rangle = \langle x, y \rangle\}$
<br>$SU(E) = \{f \in U(E) \mid \det(f) = 1\}$
