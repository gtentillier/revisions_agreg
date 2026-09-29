<div align="center">

![Progression Globale](img/progression_globale.png)

![Progression Chapitres](img/progression_chapitres.png)

</div>

**19** Théorèmes à réviser sur **38**

# 📚 20/09/2026

**10** Théorèmes

## 1. Sinus de la somme

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
$$\sin(a+b) = \sin(a)\cos(b) + \cos(a)\sin(b)$$
En particulier, pour $b=a$ :
$$\sin(2a) = 2\sin(a)\cos(a)$$

---

</details>

## 2. Formule de Taylor avec reste intégral

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

## 3. Formule de Taylor-Young

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

## 4. Formule de Cauchy

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

## 5. Règle de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse complexe
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $\sum a_n z^n$ une série entière.
Si $\lim_{n \to \infty} |a_n|^{1/n} = \ell \in [0, +\infty]$, alors le rayon de convergence $R$ de la série est :
$$R = \frac{1}{\ell}$$
(avec la convention $1/0 = +\infty$ et $1/\infty = 0$).

---

</details>

## 6. Cosinus de la somme

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
$$\cos(a+b) = \cos(a)\cos(b) - \sin(a)\sin(b)$$
En particulier, pour $b=a$ :
$$\cos(2a) = \cos^2(a) - \sin^2(a)$$

---

</details>

## 7. Théorème fondamental de l'algèbre (D'Alembert-Gauss)

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

## 8. Théorème de Liouville

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

## 9. Règle de D'Alembert

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

## 10. Inégalité de Taylor-Lagrange

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

<br>

# 📚 30/09/2026

**9** Théorèmes

## 1. Inégalité des pentes

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

## 2. Dérivée de la fonction réciproque

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

## 3. Composition de fonctions convexes

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

## 4. Théorème de convergence dominée

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
$$\lim_{n \to \infty} \int_I f_n(t) dt = \int_I f(t) dt$$

---

</details>

## 5. Théorème de la limite monotone

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

## 6. Théorème de Bolzano-Weierstrass

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

## 7. Suite de Cauchy

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Analyse réelle
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $(E, d)$ un espace métrique. Une suite $(u_n)_{n \in \mathbb{N}}$ d'éléments de $E$ est dite de Cauchy si :
$$\forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall p, q \ge N, d(u_p, u_q) < \varepsilon$$

---

</details>

## 8. Théorème du point fixe de Banach

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

## 9. Théorème de dérivation d'une intégrale à paramètre

<details>
<summary><b>Chapitre</b></summary>
<blockquote>
Intégration sur un intervalle quelconque
</blockquote>
</details>

<details>
<summary><b>Énoncé</b></summary>

---

Soit $X$ un ouvert d'un espace vectoriel normé de dimension finie et $I$ un intervalle de $\mathbb{R}$. Soit $f : X \times I \to \mathbb{C}$ telle que :

1. Pour tout $x \in X$, la fonction $t \mapsto f(x, t)$ est continue par morceaux et intégrable sur $I$.
2. La fonction $f$ admet une dérivée partielle selon $x$, notée $\frac{\partial f}{\partial x}$, telle que :
   - Pour tout $x \in X$, $t \mapsto \frac{\partial f}{\partial x}(x, t)$ est continue par morceaux sur $I$.
   - Pour tout $t \in I$, $x \mapsto \frac{\partial f}{\partial x}(x, t)$ est continue sur $X$.
3. Il existe $\varphi \in \mathcal{C}_{m}(I, \mathbb{R}^+)$ intégrable sur $I$ telle que pour tout $(x, t) \in X \times I$, $|\frac{\partial f}{\partial x}(x, t)| \le \varphi(t)$ (hypothèse de domination).

Alors $F : x \mapsto \int_I f(x, t) dt$ est de classe $\mathcal{C}^1$ sur $X$ et :
$$F'(x) = \int_I \frac{\partial f}{\partial x}(x, t) dt$$

---

</details>

