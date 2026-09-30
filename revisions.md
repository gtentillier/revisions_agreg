<div align="center">

![Progression Globale](img/progression_globale.png)

![Progression Chapitres](img/progression_chapitres.png)

</div>

**32** Théorèmes à réviser sur **69**

# 📚 01/10/2026

**32** Théorèmes

## 1. Formule de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert étoilé de $\mathbb{C}$ et $f : U \to \mathbb{C}$ holomorphe. Alors :
- $f$ admet une primitive sur $U$ ;
- si $\gamma$ est un lacet $\mathcal{C}^1$ par morceaux et à valeurs dans $U$, alors $\int_{\gamma} f(z) dz = 0$ ;
- si de plus $z \in U \setminus \text{Im}(\gamma)$, alors $f(z) \text{Ind}_{\gamma}(z) = \frac{1}{2i\pi} \int_{\gamma} \frac{f(w)}{w-z} dw$.

---

</details>

## 2. Algèbre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $R$ un anneau commutatif. Une $R$-**algèbre** est un anneau $A$ muni d'un morphisme d'anneaux $f : R \to A$ tel que $f(R) \subseteq Z(A)$, où $Z(A)$ désigne le centre de l'anneau $A$.

---

</details>

## 3. Intérieur et adhérence des opérations ensemblistes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Pour toutes parties $A, B \subseteq E$ :
$$\mathring{E \setminus A} = E \setminus \overline{A}, \qquad \overline{E \setminus A} = E \setminus \mathring{A}.$$
$$\mathring{A} \cup \mathring{B} \subseteq \mathring{A \cup B}, \qquad \overline{A \cup B} = \overline{A} \cup \overline{B}.$$
$$\mathring{A \cap B} = \mathring{A} \cap \mathring{B}, \qquad \overline{A \cap B} \subseteq \overline{A} \cap \overline{B}.$$

---

</details>

## 4. Pivot de Gauss

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

## 5. Lemme de Gauss

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $a, b, c \\in \\mathbb{Z}$. Si $a \\mid bc$ et si $a$ est premier avec $b$, c'est-à-dire si $\\operatorname{pgcd}(a,b)=1$, alors :
$$a \\mid c.$$

---

</details>

## 6. Image continue d'un compact

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

## 7. Sous-anneau

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Une partie $S$ d'un anneau $A$ est un **sous-anneau** ssi :

- $(i)$ $(S, +)$ est un sous-groupe de $(A, +)$
- $(ii)$ $S$ est stable par $\times$
- $(iii)$ $1_A \in S$

---

</details>

## 8. Théorème de convergence dominée

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Intégration sur un intervalle quelconque
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions $\mathcal{C}_{m}(I, \mathbb{C})$ où $I$ est un intervalle de $\mathbb{R}$.
Supposons que :

1. La suite $(f_n)$ converge simplement sur $I$ vers une fonction $f$ continue par morceaux sur $I$.
2. Il existe $\varphi \in \mathcal{C}_{m}(I, \mathbb{R}^+)$ intégrable sur $I$ telle que pour tout $n \in \mathbb{N}$ et tout $x \in I$, $|f_n(x)| \le \varphi(x)$.

Alors $f$ et les $f_n$ sont intégrables sur $I$ et :
$$\int_I f_n(t) dt \xrightarrow[n \to \infty]{} \int_I f(t) dt$$

---

</details>

## 9. Théorème du rang

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre Linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $E$ et $F$ deux espaces vectoriels de dimension finie sur un corps $\mathbb{K}$. Soit $u \in \mathcal{L}(E, F)$ une application linéaire de $E$ dans $F$.
Alors :
$$\dim(E) = \dim(\text{Ker}(u)) + \text{rg}(u)$$
où $\text{Ker}(u)$ est le noyau de $u$ et $\text{rg}(u) = \dim(\text{Im}(u))$ est le rang de $u$.

---

</details>

## 10. Éléments associés, irréductibles, nilpotents d'un anneau

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

- **Élément associé** : $a, b \in A$ sont associés s'il existe $u \in A^\times$ tel que $a = ub$.
- **Élément irréductible** : $p \in A \setminus A^\times$ est irréductible si ses seuls diviseurs sont les éléments inversibles et les associés de $p$ (i.e. $p=ab \implies a \in A^\times$ ou $b \in A^\times$).
- **Élément nilpotent** : $x \in A$ est nilpotent s'il existe $n \in \mathbb{N}^*$ tel que $x^n = 0$.

Un anneau est dit **réduit** si seul $0$ est nilpotent.

---

</details>

## 11. Points intérieurs, adhérents, isolés et d'accumulation

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 12. Théorème de Borel-Lebesgue / Heine-Borel

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

## 13. Théorème de Heine

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f : E \to F$ une application continue d'un espace métrique compact $E$ dans un espace métrique $F$.
Alors $f$ est uniformément continue sur $E$, c'est-à-dire :
$$\forall \varepsilon > 0, \exists \delta > 0, \forall x, y \in E, d_E(x, y) < \delta \implies d_F(f(x), f(y)) < \varepsilon$$

---

</details>

## 14. Inégalité de Taylor-Lagrange

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

## 15. Factorisation de $a^n - b^n$

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

## 16. Adhérence d'un connexe

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

## 17. Formule de Taylor-Young

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f \in \mathcal{C}^n(I, E)$ où $E$ est un espace vectoriel normé de dimension finie. Soit $a \in I$.

Alors, au voisinage de $h=0$ tel que $a+h \in I$ :
$$f(a+h) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} h^k + o(h^n)$$

---

</details>

## 18. Caractérisation du rang d'une matrice

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre Linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A \in \mathcal{M}_{m,n}(\mathbb{K})$. Le rang de $A$, noté $\operatorname{rg}(A)$, est caractérisé par les propriétés équivalentes suivantes :

1. $\operatorname{rg}(A)$ est la dimension de l'espace engendré par les colonnes de $A$ ; c'est aussi la dimension de l'espace engendré par ses lignes.
2. $\operatorname{rg}(A)$ est le nombre maximal de colonnes linéairement indépendantes de $A$ ; c'est aussi le nombre maximal de lignes linéairement indépendantes de $A$.
3. $\operatorname{rg}(A)$ est le plus grand entier $r$ tel que $A$ possède une sous-matrice carrée inversible de taille $r \times r$.

---

</details>

## 19. Théorème des valeurs intermédiaires

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

## 20. Théorème de Fubini-Tonelli pour les suites

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

## 21. Théorème de sommation L1

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

## 22. Homéomorphisme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Une application $f : E \to F$ entre deux espaces topologiques est un homéomorphisme si :

$(i)$ $f$ est bijective

$(ii)$ $f$ est continue

$(iii)$ $f^{-1}$ est continue

---

</details>

## 23. Diamètre

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

## 24. Suite de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, d)$ un espace métrique. Une suite $(u_n)_{n \in \mathbb{N}}$ d'éléments de $E$ est dite de Cauchy si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, d(u_p, u_q) < \varepsilon$$

---

</details>

## 25. Applications lipschitziennes et isométries

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $(E, d_E)$ et $(F, d_F)$ deux espaces métriques. Une application $f : E \to F$ est dite $L$-lipschitzienne, où $L \ge 0$, si
$$\forall x, y \in E, \quad d_F(f(x), f(y)) \le L d_E(x, y).$$

Une application $f : E \to F$ est une isométrie si elle préserve les distances, c'est-à-dire si
$$\forall x, y \in E, \quad d_F(f(x), f(y)) = d_E(x, y).$$
Toute isométrie est injective et $1$-lipschitzienne. Si elle est bijective, on parle d'une isométrie de $E$ sur $F$.

---

</details>

## 26. Théorème de Fubini-Lebesgue pour les suites

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

## 27. Norme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $E$ un espace vectoriel sur $\mathbb{K}$. Une norme sur $E$ est une application $\|\cdot\| : E \to \mathbb{R}_+$ vérifiant :

1. Séparation : $\|x\| = 0 \iff x = 0$
2. Homogénéité : $\|\lambda x\| = |\lambda| \|x\|$
3. Inégalité triangulaire : $\|x+y\| \le \|x\| + \|y\|$

---

</details>

## 28. Ensemble connexe

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

## 29. Distance

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 30. Boules ouvertes, fermées, intérieur et adhérence

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

## 31. Théorème du point fixe de Banach

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, d)$ un espace métrique complet non vide. Soit $f : E \to E$ une application contractante, c'est-à-dire qu'il existe $k \in [0, 1[$ tel que :
$$\forall x, y \in E, d(f(x), f(y)) \le k d(x, y)$$
Alors :

1. $f$ admet un unique point fixe $x^* \in E$ (tel que $f(x^*) = x^*$).
2. Pour tout point de départ $u_0 \in E$, la suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_{n+1} = f(u_n)$ converge vers $x^*$.
3. On a l'estimation de la vitesse de convergence suivante : $d(u_n, x^*) \le \frac{k^n}{1-k} d(u_1, u_0)$.

---

</details>

## 32. Lemme des noyaux

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre Linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $E$ un espace vectoriel sur un corps $\mathbb{K}$ et $u \in \mathcal{L}(E)$ un endomorphisme de $E$. Soient $P_1, \dots, P_n \in \mathbb{K}[X]$ des polynômes deux à deux premiers entre eux. On note $P = \prod_{i=1}^n P_i$.
Alors :
$$\text{Ker}(P(u)) = \bigoplus_{i=1}^n \text{Ker}(P_i(u))$$
De plus, la projection sur $\text{Ker}(P_i(u))$ parallèlement à $\bigoplus_{j \neq i} \text{Ker}(P_j(u))$ est donnée par la restriction à $\text{Ker}(P(u))$ d'un polynôme en $u$.

---

</details>

