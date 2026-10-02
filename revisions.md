<div align="center">

![Progression Globale](data/img/progression_globale.png)

![Progression Chapitres](data/img/progression_chapitres.png)

</div>

**63** Théorèmes à réviser sur **80** au total

# 📚 Révisions pour le 01/10/2026

**15** Théorèmes

## 1. Ensemble connexe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un espace topologique $E$ est connexe si
$$\nexists U, V \in \mathcal{P}(E), \quad U \text{ et } V \text{ ouverts non-vides}, \quad E = U \sqcup V.$$
De manière équivalente :
$$\forall A \subseteq E, \quad \left(A \text{ ouvert et fermé}\right) \implies A \in \{\emptyset, E\}.$$

---

</details>

## 2. Théorème des valeurs intermédiaires

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $a, b \in \mathbb{R}$ tels que $a < b$. Soit $f : [a, b] \to \mathbb{R}$ une fonction continue sur le segment $[a, b]$.
Pour tout réel $y$ compris entre $f(a)$ et $f(b)$, il existe au moins un réel $c \in [a, b]$ tel que :
$$f(c) = y$$
Autrement dit, l'image d'un intervalle par une fonction continue est un intervalle.

---

</details>

## 3. Lemme de Gauss

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $a, b, c \in \mathbb{Z}$. Si $a \mid bc$ et si $a$ est premier avec $b$, c'est-à-dire si $\operatorname{pgcd}(a,b)=1$, alors :
$$a \mid c.$$

---

</details>

## 4. Boules ouvertes, fermées, intérieur et adhérence

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 5. Factorisation de $a^n - b^n$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $a, b \in \mathbb{C}$ et $n \in \mathbb{N}^*$. On a :
$$a^n - b^n = (a-b) \sum_{k=0}^{n-1} a^{n-1-k} b^k$$

---

</details>

## 6. Théorème de Fubini-Tonelli pour les suites

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(a_{n,p})_{(n,p) \in \mathbb{N}^2}$ une famille de réels positifs ou nuls.
Alors on a toujours l'égalité suivante dans $[0, +\infty]$ :
$$\sum\limits_{n=0}^{\infty} \sum\limits_{p=0}^{\infty} a_{n,p} = \sum\limits_{p=0}^{\infty} \sum\limits_{n=0}^{\infty} a_{n,p}$$

---

</details>

## 7. Intérieur et adhérence des opérations ensemblistes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, d)$ un espace métrique. Pour toutes parties $A, B \subseteq E$ :
$$\mathring{E \setminus A} = E \setminus \overline{A}, \qquad \overline{E \setminus A} = E \setminus \mathring{A}$$
$$\mathring{A \setminus B} = \mathring{A} \setminus \overline{B}, \qquad \overline{A \setminus B} \subseteq \overline{A} \setminus \mathring{B}$$

De plus :
$$\mathring{A} \cup \mathring{B} \subseteq \mathring{A \cup B}, \qquad \overline{A \cup B} = \overline{A} \cup \overline{B}.$$
$$\mathring{A \cap B} = \mathring{A} \cap \mathring{B}, \qquad \overline{A \cap B} \subseteq \overline{A} \cap \overline{B}.$$

---

</details>

## 8. Formule de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert étoilé de $\mathbb{C}$ de centre $z_0$ et $f : U \to \mathbb{C}$ holomorphe. Alors :

- $f$ admet une primitive sur $U$ donnée par $F(z) = \int_{[z_0, z]} f(w) dw$. Cette intégrale ne dépend pas du chemin dans $U$ ;
- si $\gamma$ est un lacet $\mathcal{C}^1$ par morceaux et à valeurs dans $U$, alors $\int_{\gamma} f(z) dz = 0$ ;
- si de plus $z \in U \setminus \text{Im}(\gamma)$, alors $f(z) \text{Ind}_{\gamma}(z) = \frac{1}{2i\pi} \int_{\gamma} \frac{f(w)}{w-z} dw$.

---

</details>

## 9. Diamètre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, d)$ un espace métrique et $A \subseteq E$. Le diamètre de $A$ est défini par :
$$\text{diam}(A) = \sup\{d(x, y) : x, y \in A\}$$

A est borné ssi $\text{diam}(A) < +\infty$
$$\iff \exists x_0 \in E, r > 0, \text{ tel que } A \subseteq B(x_0, r)$$
$$\iff \forall x_0 \in E, \exists r > 0, \text{ tel que } A \subseteq B(x_0, r)$$

---

</details>

## 10. Image continue d'un compact

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f : E \to F$ une application continue d'un espace topologique $E$ dans un espace topologique $F$.
Si $K$ est un sous-ensemble compact de $E$, alors son image $f(K)$ est un sous-ensemble compact de $F$.

---

</details>

## 11. Adhérence d'un connexe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $E$ un espace topologique et $A$ une partie connexe de $E$.
Si $B$ est une partie telle que $A \subseteq B \subseteq \bar{A}$, alors $B$ est connexe. En particulier, l'adhérence $\bar{A}$ d'un connexe est connexe.

---

</details>

## 12. Pivot de Gauss

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre Linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Le pivot de Gauss consiste à transformer une matrice par opérations élémentaires sur les lignes : échanger deux lignes, multiplier une ligne par un scalaire non nul ou ajouter à une ligne un multiple d'une autre.

---

### Calcul du rang

On choisit un pivot non nul et on annule les coefficients situés en dessous. Si le pivot est nul, on échange la ligne avec une ligne située plus bas. Le rang est alors le nombre de lignes non nulles de la forme échelonnée.

Par exemple, pour le système

$$
\begin{cases}
x+y+z=6,\\
2x-y+z=3,\\
x+2y-z=2,
\end{cases}
$$

la matrice augmentée, dont la dernière colonne contient le second membre, se réduit ainsi :

$$
\left(\begin{array}{ccc|c}
1 & 1 & 1 & 6\\
2 & -1 & 1 & 3\\
1 & 2 & -1 & 2
\end{array}\right)
\xrightarrow{\substack{L_2\leftarrow L_2-2L_1\\L_3\leftarrow L_3-L_1}}
\left(\begin{array}{ccc|c}
1 & 1 & 1 & 6\\
0 & -3 & -1 & -9\\
0 & 1 & -2 & -4
\end{array}\right)
\xrightarrow{L_3\leftarrow 3L_3+L_2}
\left(\begin{array}{ccc|c}
1 & 1 & 1 & 6\\
0 & -3 & -1 & -9\\
0 & 0 & -7 & -21
\end{array}\right).
$$

---

### Bases du noyau et de l'image

Considérons la matrice $3\times3$

$$
A=\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}
\quad\text{et l'application } f(X)=AX.
$$

La réduction donne

$$
\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}
\xrightarrow{\substack{L_2\leftarrow L_2-2L_1\\L_3\leftarrow L_3-3L_1}}
\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.
$$

Pour trouver le noyau, on résout $AX=0$ avec $X=(x,y,z)$. Il reste l'équation

$$
x+2y+3z=0.
$$

Les variables $y$ et $z$ sont libres. En posant $y=s$ et $z=t$, on obtient $x=-2s-3t$, donc

$$
X=\begin{pmatrix}x\\y\\z\end{pmatrix}
 =s\begin{pmatrix}-2\\1\\0\end{pmatrix}
 +t\begin{pmatrix}-3\\0\\1\end{pmatrix},
\quad\text{donc}\quad
\ker(f)=\operatorname{Vect}\left\{\begin{pmatrix}-2\\1\\0\end{pmatrix},\begin{pmatrix}-3\\0\\1\end{pmatrix}\right\}.
$$

La seule colonne pivot est la première. Une base de l'image est donc donnée par la première colonne de la matrice initiale :

$$
\operatorname{Im}(f)=\operatorname{Vect}\left\{\begin{pmatrix}1\\2\\3\end{pmatrix}\right\}.
$$

---

### Calcul d'un inverse

Chaque opération élémentaire revient à multiplier à gauche par une matrice élémentaire inversible. Ainsi, en partant de $(A\mid I_n)$, une suite d'opérations donne

$$
(A\mid I_n)\longmapsto(PA\mid P),
$$

Si la partie gauche devient $I_n$, alors $P=A^{-1}$ : on lit l'inverse à droite.

Par exemple, $L_2\leftarrow L_2-3L_1$ correspond à la matrice élémentaire inversible

$$
E=\begin{pmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix},
\qquad
E^{-1}=\begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.
$$

L'inverse correspond à l'opération réciproque $L_2\leftarrow L_2+3L_1$.

Exemple en dimension $3$ : considérons

$$
B=\begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}.
$$

La méthode de Gauss-Jordan donne :

$$
\left(\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0\\
0 & 1 & 1 & 0 & 1 & 0\\
0 & 0 & 1 & 0 & 0 & 1
\end{array}\right)
\xrightarrow{L_2\leftarrow L_2-L_3}
\left(\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0\\
0 & 1 & 0 & 0 & 1 & -1\\
0 & 0 & 1 & 0 & 0 & 1
\end{array}\right)
\xrightarrow{L_1\leftarrow L_1-L_2}
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 1 & -1 & 1\\
0 & 1 & 0 & 0 & 1 & -1\\
0 & 0 & 1 & 0 & 0 & 1
\end{array}\right).
$$

Ainsi,

$$
B^{-1}=\begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{pmatrix}.
$$

---

### Exercice

Soit $A$ la matrice définie par

$$
A = \begin{pmatrix}
1 & 10 & 3 & 1 \\
2 & 5 & 1 & -3 \\
-1 & -1 & 0 & 2
\end{pmatrix}.
$$

Calculer le rang de $A$, déterminer une base de son image et une base de son noyau.

<details>
<summary>Solution</summary>

---

- $\operatorname{rg}(A)=2$ ;
- une base de $\operatorname{Im}(A)$ est formée par les deux premières colonnes :
  $$\big((1,2,-1),(10,5,-1)\big)$$
- une base de $\ker(A)$ est :
  $$\big((1,-1,3,0),(7,-1,0,3)\big).$$

</details>

---

</details>

## 13. Inégalité de Taylor-Lagrange

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f \in \mathcal{C}^n([a, b], E)$ telle que $f^{(n)}$ soit dérivable sur $]a, b[$.
Alors :
$$\left\| f(b) - \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (b-a)^k \right\| \le \frac{(b-a)^{n+1}}{(n+1)!} \sup_{t \in ]a, b[} \|f^{(n+1)}(t)\|$$

---

</details>

## 14. Théorème de Fubini-Lebesgue pour les suites

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(a_{n,p})_{(n,p) \in \mathbb{N}^2}$ une famille de nombres complexes.
On suppose que la famille est sommable, c'est-à-dire que l'une des sommes itérées des modules converge :
$$\sum\limits_{n=0}^{\infty} \sum\limits_{p=0}^{\infty} |a_{n,p}| < +\infty$$
Alors les sommes itérées convergent absolument et on a l'égalité :
$$\sum\limits_{n=0}^{\infty} \sum\limits_{p=0}^{\infty} a_{n,p} = \sum\limits_{p=0}^{\infty} \sum\limits_{n=0}^{\infty} a_{n,p}$$

---

</details>

## 15. Théorème de sommation L1

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Intégration sur un intervalle quelconque
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\sum f_n$ une série de fonctions de $\mathcal{C}_{m}(I, \mathbb{C})$.
Supposons que :

1. $\sum f_n$ converge simplement vers $S \in \mathcal{C}_{m}(I, \mathbb{C})$.
2. Chaque $f_n$ est intégrable sur $I$.
3. $\sum\limits_{n=0}^{\infty} \int_I |f_n| < +\infty$.
   Alors $S$ est intégrable sur $I$ et :
   $$\int_I \left( \sum_{n=0}^{\infty} f_n(t) \right) dt = \sum\limits_{n=0}^{\infty} \int_I f_n(t) dt$$

---

</details>

<br>

# 📚 Révisions pour le 02/10/2026

**48** Théorèmes

## 1. Dérivée de la fonction réciproque

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f : A \to B$ une bijection dérivable sur $A$. Soit $a \in A$.
Si $f'(a) \neq 0$ et si $f^{-1}$ est continue en $b = f(a)$, alors $f^{-1}$ est dérivable en $b$ et :
$$(f^{-1})'(b) = \frac{1}{f'(a)} = \frac{1}{f'(f^{-1}(b))}$$

---

</details>

## 2. Caractérisation d'un élément irréductible dans un anneau principal

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau principal. Soit $p \in A \setminus \{0\}$.
Les assertions suivantes sont équivalentes :

1. $p$ est irréductible.
2. L'idéal $(p)$ est premier.
3. L'idéal $(p)$ est maximal.

---

</details>

## 3. Théorème de limite de la dérivée

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, \|\cdot\|)$ un $\mathbb{K}$-espace vectoriel de dimension finie. Soit $I$ un intervalle de $\mathbb{R}$ et $a \in I$. Soit $f : I \to E$ une fonction continue sur $I$ et dérivable sur $I \setminus \{a\}$.
Si $f'(x) \xrightarrow[x \to a]{} l$ existe (avec $l \in E$), alors $f$ est dérivable en $a$ et $f'(a) = l$.
La fonction $f'$ est alors continue en $a$.

---

</details>

## 4. Convergence simple d'une suite de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$. On dit que la suite $(f_n)$ converge simplement vers une fonction $f : X \to E$ si :
$$\forall x \in X, f_n(x) \xrightarrow[n \to \infty]{} f(x)$$

---

</details>

## 5. Critère de Cauchy uniforme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). On dit qu'une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ de $X$ vers $E$ vérifie le critère de Cauchy uniforme sur $X$ si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, \forall x \in X, \|f_p(x) - f_q(x)\| < \varepsilon$$
Une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ converge uniformément sur $X$ vers une fonction $f : X \to E$ si et seulement si elle vérifie le critère de Cauchy uniforme sur $X$.

---

</details>

## 6. Théorème d'intégration terme à terme d'une série de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions continues de $I$ vers $E$. Si la série $\sum f_n$ converge uniformément sur tout segment de $I$ vers une fonction $S : I \to E$, alors pour tout $x_0 \in I$, la suite des sommes partielles des primitives $(\sum\limits_{k=0}^n \int_{x_0}^x f_k(t) dt)_{n \in \mathbb{N}}$ converge simplement et uniformément sur tout segment de $I$ vers la fonction $x \mapsto \int_{x_0}^x S(t) dt$.

On a notamment pour tout $[a, b] \subseteq I$ :
$$\int_a^b \left( \sum\limits_{n=0}^\infty f_n(t) \right) dt = \sum\limits_{n=0}^\infty \int_a^b f_n(t) dt$$

---

</details>

## 7. Théorème de Bolzano-Weierstrass

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Toute suite bornée de réels (ou d'éléments de $\mathbb{R}^n$) admet au moins une valeur d'adhérence. Autrement dit, on peut en extraire une sous-suite convergente.

---

</details>

## 8. Théorème de la double limite

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $a \in \overline{X}$ (avec $a \in \overline{\mathbb{R}}$ si $E = \mathbb{R}$). Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$.
Supposons que :

1. Pour tout $n \in \mathbb{N}$, $\lim_{x \to a} f_n(x) = \lambda_n$ existe dans $E$.
2. La suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$.

Alors :

- La suite $(\lambda_n)_{n \in \mathbb{N}}$ converge vers une limite $\lambda \in E$.
- La fonction $f$ admet une limite en $a$ qui est égale à $\lambda$.

On a alors l'égalité : $\lim_{n \to \infty} \lim_{x \to a} f_n(x) = \lim_{x \to a} \lim_{n \to \infty} f_n(x)$.

---

</details>

## 9. Convergence absolue d'une série de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions de $X$ vers $E$. On dit que la série $\sum f_n$ converge absolument si pour tout $x \in X$, la série numérique $\sum\limits_{n=0}^{\infty} \|f_n(x)\|$ converge.

---

</details>

## 10. Théorème de la double limite pour les séries de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $a$ un point adhérent à $X$ (avec $a \in \overline{\mathbb{R}}$ si $E = \mathbb{R}$). Soit $\sum f_n$ une série de fonctions de $X$ vers $E$.
Supposons que :

1. Pour tout $n \in \mathbb{N}$, $f_n(x) \xrightarrow[x \to a]{} \lambda_n$ existe dans $E$.
2. La série de fonctions $\sum f_n$ converge uniformément sur $X$ vers une fonction $S : X \to E$.

Alors :

- La série numérique $\sum\limits_{n \in \mathbb{N}} \lambda_n$ converge vers une limite $\lambda \in E$.
- La fonction $S$ admet une limite en $a$ qui est égale à $\lambda$.

On a alors l'égalité : $\sum\limits_{n=0}^\infty f_n(x) \xrightarrow[x \to a]{} \sum\limits_{n=0}^\infty \lambda_n$.

---

</details>

## 11. $1^{\text{er}}$ théorème d'isomorphisme pour les anneaux

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $A, B$ deux anneaux et $\varphi : A \to B$ un morphisme d'anneaux.
Alors $\text{Ker}(\varphi)$ est un idéal de $A$, $\text{Im}(\varphi)$ est un sous-anneau de $B$, et $\varphi$ induit un isomorphisme d'anneaux :
$$\bar{\varphi} : A/\text{Ker}(\varphi) \xrightarrow{\sim} \text{Im}(\varphi)$$

---

</details>

## 12. Morphismes d'anneaux, isomorphismes, endomorphismes, automorphismes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Une application $\varphi : A \to B$ est un **morphisme d'anneaux** si :

- $\forall x, y \in A, \varphi(x+y) = \varphi(x) + \varphi(y)$
- $\forall x, y \in A, \varphi(xy) = \varphi(x)\varphi(y)$
- $\varphi(1_A) = 1_B$

$\ker \varphi = \{x \in A, \varphi(x) = 0_B\}$ est un **idéal** de $A$.

On parle d'**isomorphisme**, **endomorphisme** ou **automorphisme** selon les propriétés usuelles.

---

</details>

## 13. Règle de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\sum a_n z^n$ une série entière with $a_n \neq 0$ pour $n$ assez grand.
Si $\lim_{n \to \infty} |a_n|^{1/n} = \ell \in [0, +\infty]$, alors le rayon de convergence $R$ de la série est :
$$R = \frac{1}{\ell}$$
(avec la convention $1/0 = +\infty$ et $1/\infty = 0$).

---

</details>

## 14. Théorème fondamental de l'algèbre (D'Alembert-Gauss)

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Toute fonction polynomiale non constante à coefficients complexes admet au moins une racine complexe.

---

</details>

## 15. Théorème de dérivation terme à terme d'une série de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $\sum f_n$ une série de fonctions de classe $\mathcal{C}^1$ de $I$ vers $E$. Supposons que :

1. Il existe un point $x_0 \in I$ tel que la série numérique $\sum\limits_{n=0}^{\infty} f_n(x_0)$ converge dans $E$.
2. La série des dérivées $\sum f_n'$ converge uniformément sur tout segment de $I$ vers une fonction $g : I \to E$.

Alors :

- La série $\sum f_n$ converge uniformément sur tout segment de $I$ vers une fonction $S : I \to E$.
- La fonction $S$ est de classe $\mathcal{C}^1$ sur $I$ et sa dérivée est $S' = \sum\limits_{n=0}^\infty f_n' = g$.

---

</details>

## 16. Caractérisation racine d'un polynôme, lien nombre de racines / degré, degré d'un produit de polynômes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau commutatif et $P \in A[X]$. Alors $a \in A$ est racine de $P$ si et seulement si $(X - a) \mid P$ dans $A[X]$.

Si de plus $A$ est intègre, alors le nombre de racines distinctes de $P$ dans $A$ est inférieur ou égal au degré de $P$.

---

</details>

## 17. Espace métrique séparable

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un espace métrique $(E, d)$ est dit **séparable** s'il existe une partie de $E$ dénombrable dense.

---

</details>

## 18. Sinus de la somme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $a, b \in \mathbb{C}$. On a :
Moyen mnémotechnique : "sico cosi coco moins sisi"
$$\sin(a+b) = \sin(a)\cos(b) + \cos(a)\sin(b)$$

En particulier, pour $b=a$ :
$$\sin(2a) = 2\sin(a)\cos(a)$$

---

</details>

## 19. Lemme d'Euclide

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau principal. Soit $p \in A$ un élément irréductible. Soient $a, b \in A$.
Si $p | ab$, alors $p | a$ ou $p | b$.

---

</details>

## 20. Théorème de factorisation dans un anneau

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f : A \to B$ un morphisme d'anneaux et $I$ un idéal de $A$.

$I \subseteq \ker f$ $\iff$ $\exists!$ morphisme d'anneaux $\bar{f} : A/I \to B$ tel que $f = \bar{f} \circ \pi$, où $\pi : A \to A/I$ est la projection canonique, c'est-à-dire tel que le diagramme suivant commute :

<p align="center">
  <img src="img/dessins théorèmes/anneaux_1.png" width="300">
</p>

En particulier, si $I = \ker f$, alors $\bar{f}$ induit un **isomorphisme** :
$$A/\ker f \simeq f(A)$$

---

</details>

## 21. Anneau euclidien

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 22. Limite uniforme de fonctions continues

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un espace topologique et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$. Si chaque fonction $f_n$ est continue sur $X$ et si la suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$, alors $f$ est continue sur $X$.

---

</details>

## 23. Inégalité des pentes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $I$ un intervalle de $\mathbb{R}$ et $f : I \to \mathbb{R}$ une fonction convexe. Soient $a, b, c \in I$ tels que $a < b < c$.
Alors :
$$\frac{f(b)-f(a)}{b-a} \le \frac{f(c)-f(a)}{c-a} \le \frac{f(c)-f(b)}{c-b}$$
Autrement dit, la fonction taux d'accroissement $T_f : (x, y) \mapsto \frac{f(y)-f(x)}{y-x}$ définie sur $\{(x, y) \in I^2, x \neq y\}$ est croissante par rapport à chacune de ses variables.

---

</details>

## 24. Caractérisation de l'égalité des idéaux engendrés par deux éléments

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau commutatif intègre, $a, b \in A$.
$$(a) = (b) \iff a \text{ et } b \text{ sont associés (i.e. } \exists u \in A^\times, a = ub)$$

---

</details>

## 25. Théorème de Liouville

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Toute fonction holomorphe sur $\mathbb{C}$ bornée est constante.

---

</details>

## 26. Diviseurs de zéro dans un anneau

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un élément $x \in A \setminus \{0\}$ est un **diviseur de zéro** s'il existe $y \in A \setminus \{0\}$ tel que $xy = 0$ ou $yx = 0$.

---

</details>

## 27. Théorème de Borel-Lebesgue / Heine-Borel

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Dans un espace vectoriel normé de dimension finie, les fermés bornés sont compacts.

---

</details>

## 28. Convergence normale d'une série de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions de $X$ vers $E$. On dit que la série $\sum f_n$ converge normalement sur $X$ si chaque fonction $f_n$ est bornée sur $X$ et si la série numérique $\sum\limits_{n=0}^{\infty} \sup_{x \in X} \|f_n(x)\|$ converge.

---

</details>

## 29. Idéaux et Anneaux principaux

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un idéal $I$ d'un anneau $A$ est dit **principal** s'il existe un élément $a \in A$ tel que $I = (a) = \{ax : x \in A\}$.

Un anneau $A$ est dit **principal** si tout idéal de $A$ est principal.

---

</details>

## 30. Convergence uniforme d'une suite de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$. On dit que la suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$ si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall n \ge N, \forall x \in X, \|f_n(x) - f(x)\| < \varepsilon$$
Ceci est équivalent à dire que $\sup_{x \in X} \|f_n(x) - f(x)\| \xrightarrow[n \to \infty]{} 0$.

---

</details>

## 31. Théorème chinois, version générale

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 32. Théorème de dérivation d'une suite de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de classe $\mathcal{C}^1$ de $I$ vers $E$. Supposons que :

1. Il existe un point $x_0 \in I$ tel que la suite $(f_n(x_0))_{n \in \mathbb{N}}$ converge dans $E$.
2. La suite des dérivées $(f_n')_{n \in \mathbb{N}}$ converge uniformément sur tout segment de $I$ vers une fonction $g : I \to E$.

Alors :

- La suite $(f_n)_{n \in \mathbb{N}}$ converge uniformément sur tout segment de $I$ vers une fonction $f : I \to E$.
- La fonction $f$ est de classe $\mathcal{C}^1$ sur $I$ et sa dérivée est $f' = g$.

---

</details>

## 33. Caractéristique

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

La **caractéristique** d'un anneau unitaire $A$ est l'unique $n \in \mathbb{N}$ tel que $\ker \varphi = n\mathbb{Z}$, où $\varphi : \mathbb{Z} \to A, k \mapsto k \cdot 1_A$ est le morphisme canonique.

C'est donc le plus petit entier $n > 0$ tel que $n \cdot 1_A = 0_A$ s'il existe, et $0$ sinon.

---

</details>

## 34. Théorème de la limite monotone

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f : ]a, b[ \to \mathbb{R}$ une fonction croissante.

1. Si $f$ est majorée, alors $f$ admet une limite finie en $b^-$.
2. Sinon, $\lim_{x \to b^-} f(x) = +\infty$.

De même pour la limite en $a^+$.

---

</details>

## 35. Éléments inversibles d'un anneau

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un élément $x \in A$ est **inversible** s'il existe $y \in A$ tel que $xy = yx = 1_A$. L'ensemble des éléments inversibles est noté $A^\times$ ou $U(A)$.

---

</details>

## 36. Bon ordre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Théorie des ensembles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un ordre sur un ensemble $E$ est dit **bon** si toute partie non vide de $E$ possède un minimum.

---

</details>

## 37. Polynôme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau commutatif. L'anneau des polynômes à une indéterminée $X$ à coefficients dans $A$ est l'ensemble :
$$A[X] = \left\{ \sum_{i=0}^n a_i X^i : n \in \mathbb{N}, a_i \in A \right\}$$

---

</details>

## 38. Anneau, unitaire, commutatif, intègre, réduit

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un **anneau** $(A, +, \times)$ est un ensemble muni de deux lois de composition interne telles que :

$(i)$ $(A, +)$ est un groupe abélien

$(ii)$ $\times$ est associative

$(iii)$ $\times$ est distributive à gauche et à droite par rapport à $+$

- **Unitaire** : s'il possède un élément neutre pour $\times$ (noté $1_A$), tous les anneaux sont supposés unitaires pour le cours.
- **Commutatif** : si la loi $\times$ est commutative.
- **Intègre** : non réduit au singleton $\{0\}$ et $\forall x, y \in A, xy = 0 \implies x = 0 \text{ ou } y = 0$.
- **Réduit** : son seul élément nilpotent est 0 (i.e. $x^n = 0 \implies x = 0$).

---

</details>

## 39. Règle de D'Alembert

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\sum a_n z^n$ une série entière with $a_n \neq 0$ pour $n$ assez grand.
Si $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = \ell \in [0, +\infty]$, alors le rayon de convergence $R$ de la série est :
$$R = \frac{1}{\ell}$$
(avec la convention $1/0 = +\infty$ et $1/\infty = 0$).

---

</details>

## 40. Limite uniforme de fonctions bornées

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions bornées de $X$ vers $E$. Si la suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$, alors $f$ est bornée sur $X$.

---

</details>

## 41. Convergence uniforme d'une série de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ensemble et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions de $X$ vers $E$. On dit que la série $\sum f_n$ converge uniformément sur $X$ si la suite de ses sommes partielles $(S_n)_{n \in \mathbb{N}}$ converge uniformément sur $X$ vers une fonction $S : X \to E$.

---

</details>

## 42. Formule de Taylor avec reste intégral

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f \in \mathcal{C}^{n+1}(I, E)$. Soient $a, b \in I$.
Alors :
$$f(b) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (b-a)^k + \int_a^b \frac{(b-t)^n}{n!} f^{(n+1)}(t) dt$$

---

</details>

## 43. Théorème de dérivation d'une intégrale à paramètre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Intégration sur un intervalle quelconque
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ et $I$ deux intervalles de $\mathbb{R}$. Soit $f : X \times I \to \mathbb{C}$ telle que :

1. Pour tout $x \in X$, la fonction $t \mapsto f(x, t)$ est continue par morceaux et intégrable sur $I$.
2. La fonction $f$ admet une dérivée partielle selon $x$, notée $\frac{\partial f}{\partial x}$, telle que :
   - Pour tout $x \in X$, $t \mapsto \frac{\partial f}{\partial x}(x, t)$ est continue par morceaux sur $I$.
   - Pour tout $t \in I$, $x \mapsto \frac{\partial f}{\partial x}(x, t)$ est continue sur $X$.
3. Il existe $\varphi \in \mathcal{C}_{m}(I, \mathbb{R}^+)$ intégrable sur $I$ telle que pour tout $(x, t) \in X \times I$, $|\frac{\partial f}{\partial x}(x, t)| \le \varphi(t)$ (hypothèse de domination).

Alors $F : x \mapsto \int_I f(x, t) dt$ est de classe $\mathcal{C}^1$ sur $X$ et :
$$F'(x) = \int_I \frac{\partial f}{\partial x}(x, t) dt$$

---

</details>

## 44. Caractérisation d'un corps avec les idéaux

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau commutatif. Alors $A$ est un corps ssi les seuls idéaux de $A$ sont $\{0\}$ et $A$.

---

</details>

## 45. Cosinus de la somme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $a, b \in \mathbb{C}$. On a :
Moyen mnémotechnique : "sico cosi coco moins sisi"

$$\cos(a+b) = \cos(a)\cos(b) - \sin(a)\sin(b)$$
En particulier, pour $b=a$ :
$$\cos(2a) = \cos^2(a) - \sin^2(a)$$

---

</details>

## 46. Idéal, premier, maximal et caractérisations

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau commutatif. Une partie $I$ est un **idéal** de $A$ si :

$(i)$ $(I, +)$ est un sous-groupe de $(A, +)$

$(ii)$ $\forall a \in A, \forall x \in I, ax \in I$.

---

- **Idéal premier** : Un idéal $I$ de $A$ est **premier** si $A/I$ est un anneau **intègre**.
  C'est équivalent à dire que $I \neq A$ et : $\forall a, b \in A, ab \in I \implies a \in I \text{ ou } b \in I$.
  _Propriété_ : Si $A$ est intègre, pour $p \in A \setminus \{0\}$, si $(p)$ est premier, alors $p$ est irréductible.

- **Idéal maximal** : Un idéal $I$ de $A$ est **maximal** si $A/I$ est un **corps**.
  C'est équivalent à dire que $I \neq A$ et les seuls idéaux contenant $I$ sont $I$ et $A$.

En particulier, tout idéal maximal est premier.

---

</details>

## 47. Composition de fonctions convexes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $I$ et $J$ deux intervalles de $\mathbb{R}$. Soit $f : I \to J$ et $g : J \to \mathbb{R}$ deux fonctions.
Si $f$ est convexe, $g$ est convexe et $g$ est croissante, alors $g \circ f$ est convexe sur $I$.

---

</details>

## 48. Théorème d'intégration d'une suite de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions continues de $I$ vers $E$. Si la suite $(f_n)$ converge uniformément sur tout segment de $I$ vers une fonction $f$ :

Alors :

1. $f$ est continue
2. $\forall x_0 \in I$, la suite des primitives $(F_n)$ définies par $F_n(x) = \int_{x_0}^x f_n(t) dt$ converge simplement et uniformément sur tout segment de $I$ vers la fonction $F : x \mapsto \int_{x_0}^x f(t) dt$.

On a notamment pour tout $[a, b] \subseteq I$ :
$$\int_a^b f_n(t) dt \xrightarrow[n \to \infty]{} \int_a^b f(t) dt$$

---

</details>
