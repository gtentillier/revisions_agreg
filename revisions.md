<div align="center">

![Progression Globale](data/img/progression_globale.png)

![Progression Chapitres](data/img/progression_chapitres.png)

</div>

**157** Théorèmes à réviser sur **179** au total

# 📚 Révisions pour le 03/10/2026

**10** Théorèmes

## 1. Théorème chinois, version générale

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

## 2. Théorème de Heine

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

## 3. Théorème de continuité d'une intégrale à paramètre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Intégration sur un intervalle quelconque
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X\subset E$ un espace vectoriel normé de dimension finie et $I$ un intervalle de $\mathbb{R}$. Soit $f : X \times I \to \mathbb{C}$ telle que :

1. Pour tout $x \in X$, la fonction $t \mapsto f(x, t)$ est continue par morceaux sur $I$.
2. Pour tout $t \in I$, la fonction $x \mapsto f(x, t)$ est continue sur $X$.
3. Il existe $\varphi \in \mathcal{C}_{m}(I, \mathbb{R}^+)$ intégrable sur $I$ telle que pour tout $(x, t) \in X \times I$, $|f(x, t)| \le \varphi(t)$ (hypothèse de domination).

Alors la fonction $F : x \mapsto \int_I f(x, t) dt$ est définie et continue sur $X$.

---

</details>

## 4. Théorème de limite de la dérivée

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

## 5. Anneau euclidien

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un anneau commutatif intègre $A$ est dit **euclidien** s'il existe une application $\varphi : A \setminus \{0\} \to \mathbb{N}$, appelé stathme, tel que :
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

## 6. Homéomorphisme

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

## 7. Points intérieurs, adhérents, isolés et d'accumulation

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
$$\overline{A} = \text{Acc}(A) \sqcup \text{Isol}(A)$$

---

</details>

## 8. Théorème de dérivation d'une suite de fonctions

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

## 9. Lemme de Gauss

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

## 10. Algèbre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $R$ un anneau commutatif. Une $R$-**algèbre** est un anneau $A$ muni d'un morphisme d'anneaux $f : R \to A$ tel que $f(R) \subseteq Z(A)$.

---

</details>

<br>

# 📚 Révisions pour le 04/10/2026

**32** Théorèmes

## 1. Lemme des noyaux

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

## 2. Convergence absolue d'une série de fonctions

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

## 3. Adhérence d'un connexe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $E$ un espace métrique et $A$ une partie connexe de $E$.
Si $B$ est une partie telle que $A \subseteq B \subseteq \bar{A}$, alors $B$ est connexe. En particulier, l'adhérence $\bar{A}$ d'un connexe est connexe.

---

</details>

## 4. Convergence normale d'une série de fonctions

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

## 5. Boules ouvertes, fermées, intérieur et adhérence

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

## 6. Distance

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

## 7. Éléments associés, irréductibles, nilpotents d'un anneau

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

## 8. Lemme d'Euclide

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

## 9. Critère de Cauchy uniforme

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

## 10. Théorème d'intégration terme à terme d'une série de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $I$ un intervalle de $\mathbb{R}$ et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $\sum f_n$ une série de fonctions continues de $I$ vers $E$. On suppose que la série $\sum f_n$ converge uniformément sur tout segment de $I$ vers une fonction $S : I \to E$.

Alors $S$ est continue sur $I$, et pour tout $x_0 \in I$, la suite des sommes partielles des primitives $(\sum\limits_{k=0}^n \int_{x_0}^x f_k(t) dt)_{n \in \mathbb{N}}$ converge simplement et uniformément sur tout segment de $I$ vers la fonction $x \mapsto \int_{x_0}^x S(t) dt$.

On a notamment pour tout $[a, b] \subseteq I$ :
$$\int_a^b \left( \sum\limits_{n=0}^\infty f_n(t) \right) dt = \sum\limits_{n=0}^\infty \int_a^b f_n(t) dt$$

---

</details>

## 11. Norme

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

## 12. Théorème du point fixe de Banach

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

## 13. Intérieur et adhérence des opérations ensemblistes

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
$$\mathring{A} \cup \mathring{B} \subseteq \mathring{A \cup B}, \qquad \overline{A \cup B} = \overline{A} \cup \overline{B}$$
$$\mathring{A \cap B} = \mathring{A} \cap \mathring{B}, \qquad \overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$$

---

</details>

## 14. Image continue d'un compact

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f : E \to F$ une application continue d'un espace métrique $E$ dans un espace métrique $F$.
Si $K$ est un sous-ensemble compact de $E$, alors son image $f(K)$ est un sous-ensemble compact de $F$.

---

</details>

## 15. Caractérisation d'un corps avec les idéaux

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

## 16. Caractérisation du rang d'une matrice

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

## 18. Ensemble connexe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un espace métrique $E$ est connexe ssi :

- $\nexists (U, V) \in \mathcal{P}(E)^2, \quad U, V \text{ ouverts non-vides}, \quad E = U \sqcup V$
- $\forall A \subseteq E, \quad (A \text{ ouvert et fermé}) \implies A \in \{\emptyset, E\}$
- $f \in \mathcal{C}(E, \{0, 1\}) \implies f \text{ est constante}$

---

</details>

## 19. Factorisation de $a^n - b^n$

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

## 20. Théorème de convergence dominée

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

## 21. Diamètre

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

## 22. Idéal, premier, maximal et caractérisations

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

**Idéal premier** : Un idéal $I$ de $A$ est **premier** ssi $A/I$ est un anneau **intègre**

$\iff I \neq A$ et : $\forall a, b \in A, ab \in I \implies a \in I \text{ ou } b \in I$.

**Idéal maximal** : Un idéal $I$ de $A$ est **maximal** si $A/I$ est un **corps**

$\iff I \neq A$ et les seuls idéaux contenant $I$ sont $I$ et $A$.

_Propriétés_ :

- Si $A$ est intègre, pour $p \in A \setminus \{0\}$, si $(p)$ est premier, alors $p$ est irréductible.
- Tout idéal maximal est premier.

---

</details>

## 23. Convergence uniforme d'une suite de fonctions

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

## 24. Théorème du rang

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre Linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $E$ et $F$ deux espaces vectoriels sur un corps $\mathbb{k}$. Soit $u \in \mathcal{L}(E, F)$. Alors :
$$u \text{ induit un isomorphisme } \bar{u} :{E}/{\text{Ker}(u)} \cong \text{Im}(u)$$

Si de plus $E$ et $F$ sont de dimension finie, alors :
$$\dim(E) = \dim(\text{Ker}(u)) + \text{rg}(u)$$
où $\text{Ker}(u)$ est le noyau de $u$ et $\text{rg}(u) = \dim(\text{Im}(u))$ est le rang de $u$.

---

</details>

## 25. Formule de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert étoilé autour de $z_0$ dans $\mathbb{C}$ et $f : U \to \mathbb{C}$ holomorphe. Alors :

- $f$ admet une primitive sur $U$ (donnée par $F(z) = \int_{[z_0, z]} f(w) dw$. Celle-ci s'annule en $z_0$. Cette intégrale ne dépend pas du chemin $C^1_{pm}$ entre $z_0$ et $z$ dans $U$)
- si $\gamma$ est un lacet $\mathcal{C}^1$ par morceaux et à valeurs dans $U$, alors $\int_{\gamma} f(z) dz = 0$
- si de plus $z \in U \setminus \text{Im}(\gamma)$, alors $f(z) \text{Ind}_{\gamma}(z) = \frac{1}{2i\pi} \int_{\gamma} \frac{f(w)}{w-z} dw$.

---

</details>

## 26. Inégalité de Taylor-Lagrange

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

## 27. Théorème de dérivation terme à terme d'une série de fonctions

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

## 28. Bon ordre

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

## 29. Sous-anneau

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

## 30. Pivot de Gauss

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

La solution est donc $(1, 2, 3)$.

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

> **Principe général** : Les opérations sur les lignes conservent les relations de dépendance linéaire entre les colonnes. Pour obtenir une base de $\text{Im}(A)$, on peut choisir n'importe quelle famille d'indices de colonnes qui forment une base de l'image de la matrice **échelonnée**, et extraire les colonnes correspondantes dans la matrice **initiale**.
>
> *Exemple* : Si la forme échelonnée est $U = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$, les colonnes 1 et 3 sont les colonnes pivots (base évidente), mais les colonnes 2 et 3 sont également libres dans $U$. On peut donc aussi former une base de $\text{Im}(A)$ en prenant les colonnes 2 et 3 de la matrice $A$ d'origine.

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

## 31. Applications lipschitziennes et isométries

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

## 32. Suite de Cauchy

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

<br>

# 📚 Révisions pour le 05/10/2026

**20** Théorèmes

## 1. Théorème de sommation L1

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

## 2. Valeurs d'adhérence et caractérisations

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(x_n)_{n \in \mathbb{N}}$ une suite d'éléments d'un espace métrique $(E, d)$. Un point $l \in E$ est une valeur d'adhérence de la suite $(x_n)$ si :
$$\forall \varepsilon > 0, \quad \{n \in \mathbb{N} : x_n \in B(l, \varepsilon)\} \text{ est infini}$$

**Caractérisation par les ensembles de restes** :
$$\text{Adh}(x_n) = \bigcap\limits_{n \in \mathbb{N}} \overline{\{x_m : m \ge n\}} \text{ est donc fermé}$$

**Caractérisation séquentielle** :
$$l \in \text{Adh}(x_n) \iff \exists \varphi \text{ extractrice telle que } x_{\varphi(n)} \to l$$

---

</details>

## 3. Endomorphismes qui commutent, sous-espaces stables

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $u, v \in \mathcal{L}(E)$ deux endomorphismes d'un espace vectoriel $E$ tels que $u \circ v = v \circ u$.

Alors les sous-espaces propres de $u$, $\text{Ker}(u)$ et $\text{Im}(u)$ sont stables par $v$.

---

</details>

## 4. Théorème de factorisation dans un anneau

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
  <img src="data/img/dessins théorèmes/anneaux_1.png" width="300">
</p>

En particulier, si $I = \ker f$, alors $\bar{f}$ induit un **isomorphisme** :
$$A/\ker f \simeq \text{Im } f$$

---

</details>

## 5. Cosinus de la somme

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

## 6. Morphismes d'anneaux, isomorphismes, endomorphismes, automorphismes

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

## 7. Inégalité des pentes

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

## 8. Théorème de la double limite pour les séries de fonctions

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E,d)$ un espace métrique et $(F, \|\cdot\|)$ un espace de Banach (espace vectoriel normé complet). Soit $a$ un point adhérent à $E$ (avec $a \in \overline{\mathbb{R}}$ si $E = \mathbb{R}$). Soit $\sum f_n$ une série de fonctions de $E$ vers $F$.
Supposons que :

1. Pour tout $n \in \mathbb{N}$, $f_n(x) \xrightarrow[x \to a]{} \lambda_n$ existe dans $F$.
2. La série de fonctions $\sum f_n$ converge uniformément sur $E$ vers une fonction $S : E \to F$.

Alors :

- La série numérique $\sum\limits_{n \in \mathbb{N}} \lambda_n$ converge vers une limite $\lambda \in F$.
- La fonction $S$ admet une limite en $a$ qui est égale à $\lambda$.

On a alors l'égalité : $\sum\limits_{n=0}^\infty f_n(x) \xrightarrow[x \to a]{} \sum\limits_{n=0}^\infty \lambda_n$.

---

</details>

## 9. Théorème de Fubini-Lebesgue pour les suites

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

## 10. Théorème de Liouville

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

## 11. Idéaux et Anneaux principaux

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

Un anneau unitaire commutatif intègre $A$ est dit **principal** si tout idéal de $A$ est principal.

---

</details>

## 12. Théorème de Fubini-Tonelli pour les suites

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

## 13. Théorème de Bolzano-Weierstrass

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

## 14. Dérivée de la fonction réciproque

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

## 15. Caractéristique

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

## 16. Théorème d'intégration d'une suite de fonctions

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

## 17. Formule de Grassmann

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $E$ un espace vectoriel et $F, G$ deux sous-espaces vectoriels de $E$. Alors :
$$\dim(F + G) = \dim(F) + \dim(G) - \dim(F \cap G)$$

---

</details>

## 18. Convergence uniforme d'une série de fonctions

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

## 20. Continuité et caractérisations

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $(E, d_E)$ et $(F, d_F)$ deux espaces métriques. Soit $f : E \to F$ une application, $x \in E$. Alors les assertions suivantes sont équivalentes :

1. $f$ est continue en $x$.
2. Pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que $f(B(x, \delta)) \subseteq B(f(x), \varepsilon)$.
3. Pour toute suite $(x_n)_{n \in \mathbb{N}}$ de $E$ convergeant vers $x$, la suite $(f(x_n))_{n \in \mathbb{N}}$ converge vers $f(x)$.

On dit que $f$ est continue sur $E$ ssi :

1. $f$ est continue en tout point de $E$.
2. Pour tout ouvert $O$ de $F$, $f^{-1}(O)$ est un ouvert de $E$.
3. Pour tout fermé $C$ de $F$, $f^{-1}(C)$ est un fermé de $E$.

---

</details>

<br>

# 📚 Révisions pour le 06/10/2026

**21** Théorèmes

## 1. Théorème des zéros isolés

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert connexe de $\mathbb{C}$ et soit $f : U \to \mathbb{C}$ une fonction holomorphe. Si l'ensemble
$$
f^{-1}(\{0\}) = \{z \in U \mid f(z) = 0\}
$$
admet un point d'accumulation dans $U$, alors $f$ est identiquement nulle sur $U$.

---

</details>

## 2. Commutant d'un endomorphisme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $u \in \mathcal{L}(E)$. Le commutant de $u$ est l'ensemble $C(u) = \{v \in \mathcal{L}(E) : u \circ v = v \circ u\}$. C'est une sous-algèbre de $\mathcal{L}(E)$.

Si $u$ est diagonalisable de valeurs propres $\lambda_1, \dots, \lambda_p$ et d'espaces propres associés $E_{\lambda_1}, \dots, E_{\lambda_p}$, alors l'application suivante est un isomorphisme d'algèbres :
$$\varphi : \begin{cases} C(u) \to \mathcal{L}(E_{\lambda_1}) \times \dots \times \mathcal{L}(E_{\lambda_p}) \\ v \mapsto (v_{|E_{\lambda_1}}, \dots, v_{|E_{\lambda_p}}) \end{cases}$$
En particulier, $\dim(C(u)) = \sum\limits_{i=1}^p \dim(E_{\lambda_i})^2$.

Si $u$ est diagonalisable, on a l'équivalence :
$$C(u) = \mathbb{K}[u] \iff u \text{ est à valeurs propres simples}$$
Dans ce cas, $\dim(C(u)) = n$.

Le **bicommutant** de $u$ est $C_2(u) = \{w \in \mathcal{L}(E) : \forall v \in C(u), v \circ w = w \circ v\}$.
On a toujours l'égalité :
$$C_2(u) = \mathbb{K}[u]$$

---

</details>

## 3. Convergence simple d'une suite de fonctions

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

## 4. Caractérisation racine d'un polynôme, lien nombre de racines / degré, degré d'un produit de polynômes

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

Si $A$ est intègre, alors le nombre de racines distinctes de $P$ dans $A$ est inférieur ou égal au degré de $P$.

$\forall P, Q \in A[X]$, $\deg(PQ) \le \deg(P) + \deg(Q)$.

Si $A$ est intègre, alors $\deg(PQ) = \deg(P) + \deg(Q)$.

---

</details>

## 5. Théorème du prolongement analytique

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert connexe de $\mathbb{C}$, $z_0 \in U$ et $f : U \to \mathbb{C}$ une fonction analytique.

$$\left[\forall n \in \mathbb{N},\ f^{(n)}(z_0)=0\right] \Longleftrightarrow f \equiv 0.$$

---

</details>

## 6. Théorème de Borel-Lebesgue

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

## 7. Caractérisation des matrices diagonalisables

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Une matrice $A \in \mathcal{M}_n(\mathbb{K})$ est diagonalisable sur $\mathbb{K}$ si et seulement si l'une des conditions suivantes est vérifiée :

1. Son polynôme caractéristique $\chi_A$ est scindé (ie. u est scindé) sur $\mathbb{K}$ et la dimension de chaque sous-espace propre est égale à la multiplicité de la valeur propre correspondante.
2. Son polynôme minimal $m_A$ est scindé à racines simples sur $\mathbb{K}$.

---

</details>

## 8. Endomorphismes cycliques

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un endomorphisme $u \in \mathcal{L}(E)$ est dit **cyclique** ssi $\exists x \in E$ tel que $(x, u(x), u^2(x), \dots, u^{n-1}(x))$ forme une base de $E$.

$$u \text{ est cyclique }$$
$$\iff m_u = \chi_u$$
$$\iff C(u) = \mathbb{K}[u]$$

Si $u$ est diagonalisable, alors $u$ est cyclique $\iff u$ est à valeurs propres simples.

---

</details>

## 9. Théorème spectral

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $E$ un espace euclidien (espace vectoriel réel muni d'un produit scalaire). Soit $u \in \mathcal{L}(E)$ un endomorphisme symétrique.

Alors il existe une base orthonormée de $E$ composée de vecteurs propres de $u$. En particulier, $u$ est diagonalisable.

Version matricielle :
Soit $A \in \mathcal{M}_n(\mathbb{R})$ une matrice symétrique. Alors il existe $P \in \mathcal{O}_n(\mathbb{R}), D \in \mathcal{D}_n(\mathbb{R})$ telles que :
$$ A = P^T D P$$

---

</details>

## 10. Théorème de Cayley-Hamilton

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $E$ un espace vectoriel de dimension finie $n$. Pour tout endomorphisme $u \in \mathcal{L}(E)$, son polynôme caractéristique $\chi_u$ est un polynôme annulateur de $u$ :
$$\chi_u(u) = 0_{\mathcal{L}(E)}$$

---

</details>

## 11. Théorème de prolongement d'une fonction uniformément continue

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E,d)$ et $(F, \delta)$ deux espaces métriques et $A \subseteq E$. On suppose que $F$ est complet. Soit $f : A \to F$ une fonction uniformément continue.

Alors il existe une unique fonction continue $\tilde{f} : \overline{A} \to F$ telle que $\tilde{f}_{|A} = f$. De plus, $\tilde{f}$ est uniformément continue.

---

</details>

## 12. Propriété de Borel-Lebesgue

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E,d)$ un espace métrique, $A \subseteq E$. Alors $A$ est compact si et seulement si toute famille d'ouverts de $E$ qui recouvre $A$ admet un sous-recouvrement fini.

Ceci équivaut à : de toute famille de fermés de $E$ dont l'intersection est vide dans $A$, on peut extraire une sous-famille finie dont l'intersection est vide dans $A$.

---

</details>

## 13. $1^{\text{er}}$ théorème d'isomorphisme pour les anneaux

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

## 14. Décomposition de Dunford

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $E$ un espace vectoriel de dimension finie sur $\mathbb{K}$. Soit $u \in \mathcal{L}(E)$ un endomorphisme dont le polynôme caractéristique est scindé sur $\mathbb{K}$.
Alors il existe un unique couple $(d, n) \in \mathcal{L}(E)^2$ tel que :

1. $u = d + n$
2. $d$ est diagonalisable et $n$ est nilpotent
3. $d$ et $n$ commutent ($d \circ n = n \circ d$)

De plus, $d$ et $n$ sont des polynômes en $u$.

---

</details>

## 15. Espace métrique séparable

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

## 16. Propriété de Bolzano-Weierstrass

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, d)$ un espace métrique. Alors une partie $A \subseteq E$ est séquentiellement compacte si et seulement si toute suite d'éléments de $A$ admet une sous-suite convergente vers un élément de $A$.

---

</details>

## 17. Polynôme

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

## 18. Limite uniforme de fonctions continues

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un espace métrique et $(E, \|\cdot\|)$ un espace vectoriel normé. Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $X$ vers $E$. Si chaque fonction $f_n$ est continue sur $X$ et si la suite $(f_n)$ converge uniformément vers une fonction $f : X \to E$, alors $f$ est continue sur $X$.

---

</details>

## 19. Limite uniforme de fonctions bornées

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

## 20. Caractérisation des matrices trigonalisables

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Une matrice $A \in \mathcal{M}_n(\mathbb{K})$ est trigonalisable sur $\mathbb{K}$ si et seulement si son polynôme caractéristique $\chi_A$ est scindé sur $\mathbb{K}$.

---

</details>

## 21. Théorème de Heine-Borel

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Topologie
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, d)$ un espace métrique. Alors une partie $A \subseteq E$ est compacte si et seulement si elle est séquentiellement compacte.

Propriété de Borel-Lebesgue $\iff$ Propriété de Bolzano-Weierstrass

---

</details>

<br>

# 📚 Révisions pour le 07/10/2026

**43** Théorèmes

## 1. Développement en série de Laurent

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Une série de Laurent est une série de fonctions s'écrivant
$$z \mapsto \sum\limits_{n \in \mathbb{Z}} a_n z^n := \sum\limits_{n=0}^{+\infty} a_n z^n + \sum\limits_{n=1}^{+\infty} a_{-n} z^{-n}$$
où $(a_n)_{n \in \mathbb{Z}} \in \mathbb{C}^{\mathbb{Z}}$. On dit que la série est convergente si les deux séries $\sum\limits_{n=0}^{+\infty} a_n z^n$ et $\sum\limits_{n=1}^{+\infty} a_{-n} z^{-n}$ convergent.

Si on note $R$ le rayon de convergence de la série entière $z \mapsto \sum\limits_{n=0}^{+\infty} a_n z^n$ et $1/r$ celui de la série entière $w \mapsto \sum\limits_{n=1}^{+\infty} a_{-n} w^n$, alors la série de Laurent $z \mapsto \sum\limits_{n \in \mathbb{Z}} a_n z^n$ converge dans l'anneau $A(0, r, R)$ où
$$A(z_0, r, R) := \{z \in \mathbb{C} \mid r < |z - z_0| < R\}$$
qui est non vide seulement si $R > r$.

En appliquant les résultats sur les séries entières à chacune de ces séries, on déduit que la convergence est normale sur tout anneau fermé $\overline{A}(0, r_1, r_2)$ tel que $r < r_1 < r_2 < R$, et que la somme d'une série de Laurent est holomorphe sur $A(0, r, R)$.

---

</details>

## 2. Composition de fonctions convexes

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

## 3. Sinus de la somme

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

## 4. Limite uniforme de fonctions holomorphes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$ et $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions holomorphes sur $U$. On suppose que $(f_n)$ converge uniformément sur tout compact de $U$ vers une fonction $f : U \to \mathbb{C}$.

Alors $f$ est holomorphe sur $U$ et on a $\forall k \in \mathbb{N}$, $(f_n^{(k)})_{n \in \mathbb{N}}$ converge uniformément sur tout compact de $U$ vers $f^{(k)}$.

---

</details>

## 5. Propriétés de l'exponentielle complexe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\exp : \mathbb{C} \to \mathbb{C}$ la fonction exponentielle complexe définie par $\exp(z) = \sum\limits_{n=0}^{\infty} \frac{z^n}{n!}$.
Cette fonction vérifie les propriétés suivantes :

1. Morphisme de groupes : $\exp$ est un morphisme du groupe additif $(\mathbb{C}, +)$ vers le groupe multiplicatif $(\mathbb{C}^*, \times)$. Autrement dit, pour tous $z, w \in \mathbb{C}$ :
$$\exp(z+w) = \exp(z)\exp(w)$$

2. Continuité : La fonction $\exp$ est continue sur $\mathbb{C}$.

3. Surjectivité : L'application $\exp : \mathbb{C} \to \mathbb{C}^*$ est surjective.

4. Non-injectivité : La fonction $\exp$ n'est pas injective. Elle est périodique de période $2i\pi$. Son noyau est :
$$\text{Ker}(\exp) = \{z \in \mathbb{C} \mid \exp(z) = 1\} = 2i\pi\mathbb{Z}$$

---

</details>

## 6. Règle de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\sum a_n z^n$ une série entière avec $a_n \neq 0$ pour $n$ assez grand.
Si $\lim_{n \to \infty} |a_n|^{1/n} = \ell \in [0, +\infty]$, alors le rayon de convergence $R$ de la série est :
$$R = \frac{1}{\ell}$$
(avec la convention $1/0 = +\infty$ et $1/\infty = 0$).

---

</details>

## 7. Existence et unicité du développement en série de Laurent

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $f$ holomorphe sur un anneau $A(z_0, r, R)$. Alors $f$ admet un unique développement en série de Laurent : il existe une unique suite $(a_n)_{n \in \mathbb{Z}}$ telle que
$$\forall z \in A(z_0, r, R), \quad f(z) = \sum\limits_{n = -\infty}^{+\infty} a_n (z - z_0)^n$$
De plus, les coefficients sont donnés par :
$$\forall n \in \mathbb{Z}, \quad a_n = \frac{1}{2i\pi} \int_{\mathcal{C}(z_0, r')} \frac{f(w)}{(w - z_0)^{n+1}} dw$$
pour n'importe quel $r' \in ]r, R[$, où $\mathcal{C}(z_0, r')$ est le cercle de centre $z_0$ et de rayon $r'$ orienté positivement.

---

</details>

## 8. Théorème chinois dans un anneau principal

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau principal, et $a, b \in A$ deux éléments premiers entre eux (i.e. tels que $\text{pgcd}(a, b) = 1$).
Alors le morphisme naturel
$$ \varphi : A/(ab) \to A/(a) \times A/(b) $$
est un isomorphisme d'anneaux, dont on peut expliciter la réciproque à l'aide d'une relation de Bézout entre $a$ et $b$ : si $au + bv = 1$, l'antécédent de $(\bar{x}, \bar{y}) \in A/(a) \times A/(b)$ par ce morphisme est la classe de $auy + bvx$ dans $A/(ab)$.

Par récurrence, on peut étendre ce résultat à $a_1, \dots, a_n$ deux-à-deux premiers entre eux.

---

</details>

## 9. Théorème de la double limite

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Fonctions vectorielles
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E,d)$ un espace métrique et $(F,\delta)$ un espace métrique complet. Soit $a \in \overline{E}$ (avec $a \in \overline{\mathbb{R}}$ si $E = \mathbb{R}$). Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions de $E$ vers $F$.
Supposons que :

1. Pour tout $n \in \mathbb{N}$, $\lim_{x \to a} f_n(x) = \lambda_n$ existe dans $F$.
2. La suite $(f_n)$ converge uniformément vers une fonction $f : E \to F$.

Alors :

- La suite $(\lambda_n)_{n \in \mathbb{N}}$ converge vers une limite $\lambda \in F$.
- La fonction $f$ admet une limite en $a$ qui est égale à $\lambda$.

On a alors l'égalité : $\lim_{n \to \infty} \lim_{x \to a} f_n(x) = \lim_{x \to a} \lim_{n \to \infty} f_n(x)$.

---

</details>

## 10. Indice d'un lacet

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\gamma : [a,b] \to \mathbb{C}$ un lacet de classe $C^1_pm$. Pour tout point $z \in \mathbb{C} \setminus \text{Im}(\gamma)$, on définit l'indice de $\gamma$ par rapport à $z$ par :
$$ \text{ind}_{\gamma}(z) = \frac{1}{2i\pi} \int_{\gamma} \frac{dw}{w-z} $$
L'application $\text{ind}_{\gamma} : \mathbb{C} \setminus \text{Im}(\gamma) \to \mathbb{C}$ est continue et à valeurs dans $\mathbb{Z}$.

---

</details>

## 11. Générateurs et inversibles de $\mathbb{Z}/n\mathbb{Z}$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $n \ge 1$ et $k \in \mathbb{Z}$. On note $\bar{k}$ la classe de $k$ dans $\mathbb{Z}/n\mathbb{Z}$. Les assertions suivantes sont équivalentes :

1. $\bar{k}$ est un générateur du groupe ($\mathbb{Z}/n\mathbb{Z}$, +).
2. Il existe $d \in \mathbb{Z}$ tel que $d\bar{k} = \bar{1}$ dans $\mathbb{Z}/n\mathbb{Z}$ (on dit que $\bar{k}$ est inversible dans l'anneau $\mathbb{Z}/n\mathbb{Z}$).
3. $k$ et $n$ sont premiers entre eux.

---

</details>

## 12. Développement limité du cosinus

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse Réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $n \in \mathbb{N}$. Au voisinage de $0$, on a :
$$ \cos(x) = \sum\limits_{k=0}^{n} (-1)^k \frac{x^{2k}}{(2k)!} + O(x^{2n+2}) $$

---

</details>

## 13. Algorithme d'Euclide (étendu)

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau euclidien muni d'un stathme $\varphi$. L'algorithme d'Euclide permet de calculer un pgcd de deux éléments $a, b \in A$.
En effectuant des divisions euclidiennes successives :
$$ a = bq_1 + r_1, \quad \varphi(r_1) < \varphi(b) $$
$$ b = r_1 q_2 + r_2, \quad \varphi(r_2) < \varphi(r_1) $$
$$ r_1 = r_2 q_3 + r_3, \quad \varphi(r_3) < \varphi(r_2) $$
L'algorithme s'arrête lorsque le reste est nul. Le dernier reste non nul est un pgcd de $a$ et $b$.

L'algorithme d'Euclide étendu permet, en remontant les égalités ou en maintenant des suites de coefficients, de déterminer deux éléments $u, v \in A$ tels que :
$$ au + bv = \text{pgcd}(a, b) $$
Cette relation est appelée relation de Bézout.

---

</details>

## 14. Propriété de la moyenne

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$, $z_0 \in U$, $r > 0$ tel que $\overline{D(z_0, r)} \subseteq U$. Soit $f : U \to \mathbb{C}$ une fonction holomorphe. Alors

$$f(z_0) = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + re^{i\theta}) d\theta$$

et

$$f(z_0) = \frac{1}{\pi r^2} \int_{D(z_0, r)} f(z) dz$$

---

</details>

## 15. Théorème de prolongement holomorphe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$, $z_0 \in U$ et $f : U \setminus \{z_0\} \to \mathbb{C}$ une fonction holomorphe.

Si $f$ est bornée au voisinage de $z_0$, alors $f$ admet un prolongement holomorphe sur $U$.

---

</details>

## 16. Principe du maximum

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert connexe de $\mathbb{C}$, $f : U \to \mathbb{C}$ une fonction holomorphe.

1. Si $|f|$ atteint un maximum local en un point $z_0 \in U$, alors $f$ est constante sur $U$.
2. Si de plus $U$ est borné et que $f$ est continue sur $\overline{U}$, alors $|f|$ atteint son maximum sur $\partial U$, ie
   $$\max_{z \in \overline{U}} |f(z)| = \max_{z \in \partial U} |f(z)|$$

---

</details>

## 17. Inégalités de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$, $z_0 \in U$, $r > 0$ tel que $\overline{D(z_0, r)} \subseteq U$. Soit $f : U \to \mathbb{C}$ une fonction holomorphe. Alors
$$\forall n \in \mathbb{N} , |f^{(n)}(z)| \le \frac{n!}{r^n} \sup_{C(z_0, r)} |f|$$

---

</details>

## 18. Existence d'un élément maximal dans une famille d'idéaux

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau principal, $K \not ={\emptyset}$. Toute famille d'idéaux \{I_\alpha\}_{\alpha \in K} de $A$ admet un idéal maximal pour l'inclusion.
En particulier, tout idéal propre de $A$ est contenu dans un idéal maximal.

---

</details>

## 19. Théorème fondamental de l'algèbre (D'Alembert-Gauss)

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

## 20. Éléments inversibles d'un anneau

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

## 21. Développement limité du logarithme

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse Réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $n \in \mathbb{N}^*$. Au voisinage de $0$, on a :
$$ \ln(1+x) = \sum\limits_{k=1}^{n} (-1)^{k-1} \frac{x^k}{k} + O(x^{n+1}) $$

---

</details>

## 22. Longueur d'un chemin

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$ et $\gamma : [a,b] \to U$ un chemin de classe $C^1$. La longueur du chemin $\gamma$ est définie par :
$$ Long(\gamma) = \int_a^b |\gamma'(t)| \, dt $$

---

</details>

## 23. Résidus

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$, $z_0 \in U$, et $f : U \setminus \{z_0\} \to \mathbb{C}$ holomorphe. On note
$$f(z) = \sum\limits_{n=-\infty}^{+\infty} a_n(z - z_0)^n$$
le développement en série de Laurent de $f$ en $z_0$. On définit le **résidu** de $f$ en $z_0$ par :
$$\text{Res}(f, z_0) = a_{-1}$$

---

</details>

## 24. Chemin opposé

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$ et $\gamma : [a,b] \to U$ un chemin. On définit le chemin opposé $\tilde{\gamma} : [-b,-a] \to U$ par :
$$ \tilde{\gamma}(t) = \gamma(-t) $$
Alors $\int_{\tilde{\gamma}} f(z) \, dz = -\int_\gamma f(z) \, dz$.

---

</details>

## 25. Indicatrice d'Euler

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

On note $\varphi(n)$ le nombre d'entiers $k$ tels que $1 \le k < n$ et $\text{pgcd}(k, n) = 1$. La fonction $\varphi$ est appelée l'indicatrice d'Euler.

Le groupe $\mathbb{Z}/n\mathbb{Z}$ (et donc tout groupe cyclique d'ordre $n$) admet exactement $\varphi(n)$ générateurs.

On a la formule de Möbius :
$$ n = \sum\limits_{d|n} \varphi(d) $$

La fonction indicatrice d'Euler est multiplicative, au sens suivant : si $m, n \in \mathbb{N}^*$ sont deux entiers premiers entre eux, alors $\varphi(mn) = \varphi(m)\varphi(n)$.

Propriétés de calcul :
— Pour tout $p$ premier et $k \ge 1$, $\varphi(p^k) = p^{k-1}(p-1)$.
— Pour tout $n \ge 1$, si $n = \prod\limits_{i=1}^{r} p_i^{k_i}$ est la décomposition de $n$ en facteurs premiers, alors :
$$ \varphi(n) = \prod\limits_{i=1}^r p_i^{k_i-1} (p_i-1) $$
ou autrement dit :
$$ \frac{\varphi(n)}{n} = \prod\limits_{i=1}^r \left( 1 - \frac{1}{p_i} \right) $$

---

</details>

## 26. Caractérisation d'un élément irréductible dans un anneau principal

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

## 27. Lemme de Gauss

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau principal.

Pour tous $a, b, c \in A$, si $a$ divise $bc$ et $\text{pgcd}(a, b) = 1$, alors $a$ divise $c$.

---

</details>

## 28. Holomorphie des intégrales à paramètre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$, $f : U \times [a, b] \to \mathbb{C}$ telle que :

1. $\forall t \in [a, b]$, la fonction $z \mapsto f(z, t)$ est holomorphe sur $U$.
2. $\forall z \in U$, la fonction $t \mapsto f(z, t)$ est continue par morceaux sur $[a, b]$.
3. $\exists \varphi : [a,b] \to \mathbb{R}_+$ intégrable telle que $\forall (z, t) \in U \times [a, b]$, $|f(z, t)| \leq \varphi(t)$.

Alors la fonction :
$$F(z) = \int_a^b f(z, t) dt$$
est holomorphe sur $U$ et on a $\forall k \in \mathbb{N}$, $\forall z \in U$ :
$$F^{(k)}(z) = \int_a^b \frac{\partial^k f}{\partial z^k}(z, t) dt$$

---

</details>

## 29. Intégrale d'une fonction continue selon un chemin $C^1_pm$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$ et $\gamma : [a,b] \to U$ un chemin de classe $C^1$ par morceaux. Soit $f : U \to \mathbb{C}$ une fonction continue. On définit l'intégrale de $f$ selon $\gamma$ par :
$$ \int_{\gamma} f(z) \, dz = \int_a^b f(\gamma(t)) \cdot \gamma'(t) \, dt $$

---

</details>

## 30. Développement limité de l'exponentielle

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse Réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $n \in \mathbb{N}$. Au voisinage de $0$, on a :
$$ e^x = \sum\limits_{k=0}^{n} \frac{x^k}{k!} + O(x^{n+1}) $$

---

</details>

## 31. Caractérisation de l'existance d'une primitive d'une fonction complexe continue

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$ et $f : U \to \mathbb{C}$ une fonction continue. Alors $f$ admet une primitive sur $U$ si et seulement si pour tout lacet $\gamma : [a,b] \to U$ de classe $C^1$ par morceaux, on a :
$$ \int_{\gamma} f(z) \, dz = 0 $$

---

</details>

## 32. Théorème de la limite monotone

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

## 33. Définition, existence et unicité du pgcd

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $a, b \in \mathbb{A}$ commutatif. On appelle un **pgcd** de $a$ et $b$ un élément $d \in \mathbb{A}$ tel que :

1. $d$ divise $a$ et $b$.
2. Pour tout $c \in \mathbb{A}$ qui divise $a$ et $b$, on a $c$ divise $d$.

On généralise cette notion à toute famille d'éléments de $\mathbb{A}$ : soit $(a_i)_{i \in I}$ une famille d'éléments de $\mathbb{A}$. On appelle un **pgcd** de la famille $(a_i)_{i \in I}$ un élément $d \in \mathbb{A}$ tel que :

1. $d$ divise tous les $a_i$.
2. Pour tout $c \in \mathbb{A}$ qui divise tous les $a_i$, on a $c$ divise $d$.

Si $\mathbb{A}$ est un anneau principal, alors pour toute famille $(a_i)_{i \in I}$ d'éléments de $\mathbb{A}$, il existe un pgcd de cette famille, et il est unique à multiplication par un élément inversible près.

En particulier, si $a, b \in \mathbb{A}$, il existe un pgcd de $a$ et $b$, et il est unique à multiplication par un élément inversible près.

Plus précisément, un élément $d \in \mathbb{A}$ est un pgcd des $(a_i)$ si et seulement si on a l'égalité d'idéaux $(d) = (a_i, i \in I)$.

---

</details>

## 34. Classification des singularités

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$, $z_0 \in U$ et $f : U \setminus \{z_0\} \to \mathbb{C}$ une fonction holomorphe. Seuls 3 cas sont possibles :

1. $f$ admet un prolongement holomorphe sur $U$. Dans ce cas, on dit que $z_0$ est une singularité **effaçable** de $f$.
2. $\lim_{z \to z_0} |f(z)| = +\infty$. Dans ce cas, il existe un entier $n \in \mathbb{N}^*$, $g$ holomorphe sur $U$ tels que :
   $$ \forall z \in U \setminus \{z_0\}, \text{ } f(z) = \frac{g(z)}{(z - z_0)^n} \text{ et } g(z_0) \neq 0 $$
    On dit que $z_0$ est un **pôle** d'ordre $n$ pour $f$.

3. L'image par $f$ de tout disque épointé $D(z_0, r) \setminus \{z_0\} \subset U$ est dense dans $\mathbb{C}$. Dans ce cas, on dit que $z_0$ est une singularité **essentielle** de $f$.

---

</details>

## 35. Théorème de Bézout

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau principal et $(a_i)_{i \in I}$ une famille d'éléments de $A$.
Si $d$ est un pgcd des $(a_i)$, alors il existe une famille $(u_i)_{i \in I}$ à support fini telle que :
$$ d = \sum_{i \in I} u_i a_i $$
Plus concrètement, pour tous $a, b \in A$, il existe $u, v \in A$ tels que :
$$ \text{pgcd}(a, b) = au + bv $$

---

</details>

## 36. Fonctions holomorphes et équations de Cauchy-Riemann

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert de $\mathbb{C}$. On dit qu'une fonction $f : U \to \mathbb{C}$ est holomorphe sur $U$ si elle est $\mathbb{C}$-dérivable en tout point de $U$.

Soit $f : U \to \mathbb{C}$ une fonction. On écrit $f = P + iQ$ où $P, Q : U \to \mathbb{R}$ sont les parties réelle et imaginaire de $f$. On identifie $U$ à un ouvert de $\mathbb{R}^2$.
La fonction $f$ est holomorphe sur $U$ si et seulement si $P$ et $Q$ sont différentiables sur $U$ et vérifient les équations de Cauchy-Riemann :
$$ \frac{\partial P}{\partial x} = \frac{\partial Q}{\partial y} \quad \text{et} \quad \frac{\partial P}{\partial y} = -\frac{\partial Q}{\partial x} $$

---

</details>

## 37. Factorisation en irréductibles

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $A$ un anneau principal. Pour tout $a \in A \setminus \{0\}$, il existe $u \in A^\times$ (un inversible) et $p_1, \dots, p_n \in A$ des éléments irréductibles tels que :
$$ a = u \prod\limits_{i=1}^n p_i $$
De plus, cette décomposition est unique à l'ordre près des facteurs et à multiplication près par des inversibles de $A$.

---

</details>

## 38. Théorème des résidus

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $U$ un ouvert étoilé de $\mathbb{C}$ et $\{z_1, z_2, \dots, z_p\}$ un nombre fini de points de $U$ deux à deux distincts. Soit $f : U \setminus \{z_1, z_2, \dots, z_p\} \to \mathbb{C}$ holomorphe. Soit $\gamma$ un lacet $\mathcal{C}^1$ par morceaux à valeurs dans $U \setminus \{z_1, z_2, \dots, z_p\}$. Alors

$$\frac{1}{2i\pi} \int_\gamma f(z) dz = \sum\limits_{k=1}^p \text{Ind}_\gamma(z_k) \text{Res}(f, z_k)$$

---

</details>

## 39. Anneau, unitaire, commutatif, intègre, réduit

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

## 40. Sous-groupes finis du groupe multiplicatif d'un corps

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Anneaux
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $k$ un corps (ou même un anneau intègre) et $G$ un sous-groupe fini de $(k^*, \times)$.
Alors $G$ est cyclique.
En particulier, le groupe des inversibles d'un corps fini est cyclique.

---

</details>

## 41. Diviseurs de zéro dans un anneau

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

## 42. Théorème de dérivation d'une intégrale à paramètre

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

## 43. Développement limité du sinus

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse Réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $n \in \mathbb{N}$. Au voisinage de $0$, on a :
$$ \sin(x) = \sum\limits_{k=0}^{n} (-1)^k \frac{x^{2k+1}}{(2k+1)!} + O(x^{2n+3}) $$

---

</details>

<br>

# 📚 Révisions pour le 08/10/2026

**31** Théorèmes

## 1. Éléments de torsion et sous-groupe de torsion

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe. Un élément $g \in G$ est un **élément de torsion** si son ordre est fini, i.e. si $g^n = e$ pour un certain entier $n \ge 1$.

Si $G$ est abélien, l'ensemble des éléments de torsion de $G$ forme un sous-groupe de $G$, appelé le **sous-groupe de torsion** de $G$.

---

</details>

## 2. Action de groupe, fidèle, transitive

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe et $E$ un ensemble. Une action de $G$ sur $E$ est un morphisme de groupes
$$\rho : G \to \operatorname{Bij}(E)$$

L'action est dite **fidèle** si $\rho$ est injectif, c'est-à-dire si :
$$\operatorname{Ker}(\rho) = \{e_G\}$$

L'action est dite **transitive** si pour tout $x, y \in E$, il existe $g \in G$ tel que $\rho(g)(x) = y$.

---

</details>

## 3. Formule des classes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe agissant sur un ensemble $E$. Alors l'ensemble des orbites de $E$ sous l'action de $G$ forme une partition de $E$, et on a la formule suivante :
$$|E| = \sum_{x \in \mathcal{R}} |O_x|$$
où $\mathcal{R}$ est l'espace quotient, c'est-à-dire un ensemble de représentants des orbites de $E$ sous l'action de $G$.

---

</details>

## 4. Générateurs de $\mathfrak{S}_n$ et $\mathfrak{A}_n$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

1. Le groupe symétrique $\mathfrak{S}_n$ est engendré par les transpositions $(i, j)$. Il est aussi engendré par les transpositions élémentaires $(i, i+1)$.
2. Le groupe alterné $\mathfrak{A}_n$ est engendré par les 3-cycles $(i, j, k)$.

---

</details>

## 5. Formule de Burnside

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe fini agissant sur un ensemble fini $E$. Alors le nombre d'orbites de $E$ sous l'action de $G$ est donné par la formule de Burnside :
$$\frac{1}{|G|} \sum_{g \in G} |E^g|$$
où $E^g = \{x \in E \mid g \cdot x = x\}$ est l'ensemble des points fixes de $g$.

---

</details>

## 6. Produit semi-direct

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $N$ et $H$ deux groupes et $\rho : H \to \text{Aut}(N)$ un morphisme de groupes. Le produit semi-direct $N \rtimes_\rho H$ est le groupe dont l'ensemble sous-jacent est $N \times H$ muni de la loi :
$$ (n, h) \cdot (n', h') = (n \rho(h)(n'), hh') $$

---

</details>

## 7. Groupe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un **groupe** est un ensemble $G$ muni d'une loi de composition interne $\cdot : G \times G \to G$ vérifiant les axiomes suivants :

1. **Associativité** : $\forall x, y, z \in G$, $(x \cdot y) \cdot z = x \cdot (y \cdot z)$.
2. **Élément neutre** : Il existe un élément $e \in G$ tel que $\forall x \in G$, $e \cdot x = x \cdot e = x$.
3. **Inverse** : $\forall x \in G$, il existe un élément $x^{-1} \in G$ tel que $x \cdot x^{-1} = x^{-1} \cdot x = e$.

---

</details>

## 8. Quatre exemples de produits semi-directs

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 9. Théorème de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe fini et $p$ un nombre premier divisant l'ordre de $G$.
Alors il existe un élément de $G$ d'ordre $p$.

---

</details>

## 10. Décomposition d'une permutation

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Toute permutation $\sigma \in \mathfrak{S}_n$ peut s'écrire de manière unique (à l'ordre des cycles près) comme un produit de cycles disjoints :
$$\sigma = c_1 c_2 \dots c_k$$

---

</details>

## 11. Topologie de $GL_n(\mathbb{K})$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 12. Simplicité de $\mathfrak{A}_n$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

$\forall n \ge 5$, le groupe alterné $\mathfrak{A}_n$ est un groupe simple (il n'admet aucun sous-groupe distingué propre non trivial).

Ainsi, pour $n \ge 5$, le groupe symétrique $\mathfrak{S}_n$ n'admet aucun sous-groupe distingué propre non trivial autre que $\mathfrak{A}_n$.

---

</details>

## 13. p-groupe, p-sous-groupe, p-Sylow

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un **p-groupe** est un groupe fini tel que : $|G| = p^n$ avec $n \ge 1$ et $p$ premier.

Un **p-sous-groupe** d'un groupe $G$ est un sous-groupe $H$ de $G$ tel que $|H| = p^m$ avec $m \ge 1$ et $p$ premier.

Un **p-sous-groupe de Sylow**, ou **p-Sylow** d'un groupe fini $G$ est un p-sous-groupe maximal de $G$, c'est-à-dire un p-sous-groupe $P$ tel que $|P| = p^n$ avec $p^n$ le plus grand facteur premier de l'ordre de $G$.

---

</details>

## 14. Orbites, Stabilisateurs, Points fixes et propriétés

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

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

---

</details>

## 15. Théorème de structure des groupes abéliens finis

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Tout groupe abélien fini $G$ est isomorphe à un produit direct de groupes cycliques :
$$G \cong \mathbb{Z}/n_1\mathbb{Z} \times \mathbb{Z}/n_2\mathbb{Z} \times \dots \times \mathbb{Z}/n_k\mathbb{Z}$$
où $n_1 | n_2 | \dots | n_k$. La suite d'entiers $(n_1, \dots, n_k)$ est unique et ses éléments sont appelés les facteurs invariants de $G$.

---

</details>

## 16. Symétries orthogonales en dimension $n$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, \langle \cdot, \cdot \rangle)$ un espace euclidien de dimension $n$.
Un endomorphisme $u \in \mathcal{L}(E)$ est une **symétrie orthogonale** si $u^2 = \operatorname{id}_E$ et $u$ est un automorphisme orthogonal ($u \in O(E)$).

Cela équivaut à dire que $u$ est la symétrie par rapport à l'espace des points fixes $\operatorname{Ker}(u - \operatorname{id}_E)$ parallèlement à l'espace propre $\operatorname{Ker}(u + \operatorname{id}_E)$.
On a alors la décomposition : $E = \operatorname{Ker}(u - \operatorname{id}_E) \oplus^\perp \operatorname{Ker}(u + \operatorname{id}_E)$.

1. Si $\dim(\operatorname{Ker}(u + \operatorname{id}_E)) = 1$, $u$ est appelée une **réflexion** (ou symétrie hyperplane).
2. Si $u = -\operatorname{id}_E$, $u$ est la **symétrie centrale** par rapport à l'origine.

---

</details>

## 17. Sous-groupe distingué/normal

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un sous-groupe $N$ d'un groupe $G$ est dit **distingué** (ou **normal**) ie. $N \triangleleft G$ ssi l'une des conditions équivalentes suivantes est vérifiée :

1. $gNg^{-1} = N$ pour tout $g \in G$.
2. $gN = Ng$ pour tout $g \in G$.
3. Il existe un morphisme de groupes $f : G \to H$ tel que $N = \operatorname{Ker}(f)$.
4. Il existe une structure de groupe sur l'ensemble quotient $G/N$ compatible avec la loi de G, ie. la projection canonique $\pi : G \to G/N$ est un morphisme de groupes.

---

</details>

## 18. Caractérisation de l'égalité des idéaux engendrés par deux éléments

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

## 19. Groupe orthogonal $O_n(\mathbb{R})$ et unitaire $U_n(\mathbb{C})$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Version matricielle : <br>$O_n(\mathbb{R}) = \{M \in GL_n(\mathbb{R}) \mid M^T M = I_n\}$
<br>$SO_n(\mathbb{R}) = \{M \in O_n(\mathbb{R}) \mid \det(M) = 1\}$
<br>$U_n(\mathbb{C}) = \{M \in GL_n(\mathbb{C}) \mid M^* M = I_n\}$
<br>$SU_n(\mathbb{C}) = \{M \in U_n(\mathbb{C}) \mid \det(M) = 1\}$

Version fonctionnelle : <br>$O(E) = \{f \in GL(E) \mid \forall x, y \in E, \langle f(x), f(y) \rangle = \langle x, y \rangle\}$
<br>$SO(E) = \{f \in O(E) \mid \det(f) = 1\}$
<br>$U(E) = \{f \in GL(E) \mid \forall x, y \in E, \langle f(x), f(y) \rangle = \langle x, y \rangle\}$
<br>$SU(E) = \{f \in U(E) \mid \det(f) = 1\}$

---

</details>

## 20. Produit semi-direct par conjugaison

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Si $N$ est un sous-groupe distingué de $G$ et $H$ un sous-groupe de $G$ tels que $N \cap H = \{e\}$ et $G = NH$, alors $G$ est isomorphe au produit semi-direct de $N$ par $H$ pour l'action de conjugaison de $H$ sur $N$ : $\rho(h)(n) = hnh^{-1}$.

---

</details>

## 21. Théorème de Lagrange

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe fini et $H$ un sous-groupe de $G$.
Alors l'ordre de $H$ divise l'ordre de $G$ :
$$|G| = |H| \times [G:H]$$
où $[G:H]$ est l'indice de $H$ dans $G$ (le nombre de classes à gauche).

---

</details>

## 22. Formule de Taylor avec reste intégral

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

## 23. Théorème de factorisation dans un groupe

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\varphi : G \to H$ un morphisme de groupes et $N \triangleleft G$.

$N \subseteq \text{Ker}(\varphi)$ $\iff$ $\exists!$ morphisme de groupes $\bar{\varphi} : G/N \to H$ tel que $\varphi = \bar{\varphi} \circ \pi$, où $\pi : G \to G/N$ est la projection canonique, c'est-à-dire tel que le diagramme suivant commute :

<p align="center">
  <img src="data/img/dessins théorèmes/diagramme_groupes.png" width="300">
</p>

En particulier, si $N = \text{Ker}(\varphi)$, alors $\bar{\varphi}$ induit un **isomorphisme** :
$$G/\text{Ker}(\varphi) \simeq \text{Im}(\varphi)$$

---

</details>

## 24. Matrices de $O_2(\mathbb{R})$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Algèbre linéaire
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, \langle \cdot, \cdot \rangle)$ un espace euclidien de dimension 2 orienté.

1. Les **rotations** (ou automorphismes orthogonaux directs) de $E$ ont pour matrice dans une base orthonormée directe :
   $$R_\theta = \begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix} \quad \text{avec } \theta \in \mathbb{R}$$
   Elles forment le groupe spécial orthogonal $SO_2(\mathbb{R})$.
2. Les **symétries orthogonales par rapport à une droite** (ou réflexions) ont pour matrice dans une base orthonormée directe :
   $$S_\theta = \begin{pmatrix} \cos(\theta) & \sin(\theta) \\ \sin(\theta) & -\cos(\theta) \end{pmatrix} \quad \text{avec } \theta \in \mathbb{R}$$
   Il s'agit de la symétrie par rapport à la droite vectorielle faisant un angle $\theta/2$ avec le premier vecteur de la base.
   Elles appartiennent à $O_2(\mathbb{R}) \setminus SO_2(\mathbb{R})$ et sont de déterminant $-1$.

---

</details>

## 25. Théorème de structure des groupes abéliens de type fini

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe abélien de type fini. Alors il existe un entier $r \ge 0$ et des entiers $n_1, \dots, n_k \ge 2$ tels que :
$$G \cong \mathbb{Z}^r \times \mathbb{Z}/n_1\mathbb{Z} \times \dots \times \mathbb{/Z}/n_k\mathbb{Z}$$
où $n_1 | n_2 | \dots | n_k$. La suite d'entiers $(n_1, \dots, n_k)$ est unique et ses éléments sont appelés les facteurs invariants de $G$.

---

</details>

## 26. Règle de D'Alembert

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\sum a_n z^n$ une série entière avec $a_n \neq 0$ pour $n$ assez grand.
Si $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = \ell \in [0, +\infty]$, alors le rayon de convergence $R$ de la série est :
$$R = \frac{1}{\ell}$$
(avec la convention $1/0 = +\infty$ et $1/\infty = 0$).

---

</details>

## 27. 1er théorème d'isomorphisme pour les groupes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soient $G, H$ deux groupes et $\varphi : G \to H$ un morphisme de groupes.
Alors $\text{Ker}(\varphi) \triangleleft G$, $\text{Im}(\varphi)$ est un sous-groupe de $H$, et $\varphi$ induit un isomorphisme de groupes :
$$\bar{\varphi} : G/\text{Ker}(\varphi) \xrightarrow{\sim} \text{Im}(\varphi)$$

---

</details>

## 28. Morphisme de groupes

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un **morphisme de groupes** est une application $f : G \to H$ entre deux groupes $(G, \cdot)$ et $(H, *)$ telle que :
$$\forall x, y \in G, \quad f(x \cdot y) = f(x) * f(y)$$

De plus, on peut montrer que :
$$f(e_G) = e_H \quad \text{et} \quad f(x^{-1}) = f(x)^{-1} \quad \text{pour tout } x \in G.$$

On parle d'**isomorphisme**, d'**endomorphisme** ou d'**automorphisme** selon que $f$ est bijective, de $G$ dans lui-même, ou bijective de $G$ dans lui-même.

---

</details>

## 29. Groupe de type fini, monogène, cyclique, simple

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Un groupe $G$ est dit **de type fini** s'il existe un ensemble fini $X \subset G$ tel que $G = \langle X \rangle$.

Un groupe $G$ est dit **monogène** s'il existe un élément $g \in G$ tel que $G = \langle g \rangle$.

Un groupe monogène fini est dit **cyclique**.

Un groupe $G$ est dit **simple** s'il est non trivial et n'admet aucun sous-groupe distingué propre non trivial.<br>
En particulier, tout groupe abélien simple est isomorphe à $\mathbb{Z}/p\mathbb{Z}$ avec $p$ premier.

---

</details>

## 30. Sous-groupe engendré par une partie

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $G$ un groupe et $X \subset G$. Le **sous-groupe engendré par $X$**, noté $\langle X \rangle$, est le plus petit sous-groupe de $G$ contenant $X$.

$$ \langle X \rangle = \bigcap_{\substack{H \le G \\ X \subset H}} H $$

$$\langle X \rangle = \{x_1 \cdot x_2 \cdot \ldots \cdot x_n \mid n \in \mathbb{N}, x_i \in X \cup X^{-1}\}$$

---

</details>

## 31. Conjugaison d'un cycle par un élément de $\mathfrak{S}_n$

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Groupes
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\sigma \in \mathfrak{S}_n$ et $(i_1, i_2, \dots, i_k)$ un cycle de $\mathfrak{S}_n$. Alors :
$$\sigma (i_1, i_2, \dots, i_k) \sigma^{-1} = (\sigma(i_1), \sigma(i_2), \dots, \sigma(i_k))$$

---

</details>

