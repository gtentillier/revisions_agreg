# Analyse complexe

# Propriété de la moyenne

Soit $U$ un ouvert de $\mathbb{C}$, $z_0 \in U$, $r > 0$ tel que $\overline{D(z_0, r)} \subseteq U$. Soit $f : U \to \mathbb{C}$ une fonction holomorphe. Alors

$$f(z_0) = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + re^{i\theta}) d\theta$$

et

$$f(z_0) = \frac{1}{\pi r^2} \int_{D(z_0, r)} f(z) dz$$

# Principe du maximum

Soit $U$ un ouvert connexe de $\mathbb{C}$, $f : U \to \mathbb{C}$ une fonction holomorphe.

1. Si $|f|$ atteint un maximum en un point $z_0 \in U$, alors $f$ est constante sur $U$.
2. Si $U$ est borné et que $f$ est continue sur $\overline{U}$, alors $|f|$ atteint un maximum sur le bord $\partial U$.

# Holomorphie des intégrales à paramètre

Soit $U$ un ouvert de $\mathbb{C}$, $f : U \times [a, b] \to \mathbb{C}$ telle que :

1. $\forall t \in [a, b]$, la fonction $z \mapsto f(z, t)$ est holomorphe sur $U$.
2. $\forall z \in U$, la fonction $t \mapsto f(z, t)$ est continue par morceaux sur $[a, b]$.
3. $\exists \varphi \in L^1([a, b], \mathbb{R}_+)$ telle que $\forall (z, t) \in U \times [a, b]$, $|f(z, t)| \leq \varphi(t)$.

Alors la fonction :
$$F(z) = \int_a^b f(z, t) dt$$
est holomorphe sur $U$ et on a $\forall k \in \mathbb{N}$, $\forall z \in U$ :
$$F^{(k)}(z) = \int_a^b \frac{\partial^k f}{\partial z^k}(z, t) dt$$
