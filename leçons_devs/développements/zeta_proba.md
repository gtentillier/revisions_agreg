# Probabilités et Arithmétique

## I. Développement eulérien via la loi zéta

On souhaite retrouver le produit eulérien de la fonction $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ (pour $s > 1$) en utilisant une mesure de probabilité sur $\mathbb{N}^*$.

### 1. Définition de la probabilité $\mathbb{P}_s$

Soit $s > 1$. On définit une mesure de probabilité $\mathbb{P}_s$ sur $\Omega = \mathbb{N}^*$ par :
$$\forall n \in \mathbb{N}^*, \quad \mathbb{P}_s(\{n\}) = \frac{1}{\zeta(s) n^s}$$
On vérifie bien que $\sum_{n=1}^\infty \mathbb{P}_s(\{n\}) = \frac{1}{\zeta(s)} \sum_{n=1}^\infty \frac{1}{n^s} = 1$.

### 2. Divisibilité et indépendance

Pour tout $d \in \mathbb{N}^*$, on considère l'événement $E_d = \{ n \in \mathbb{N}^* : d|n \}$.
La probabilité qu'un entier soit divisible par $d$ est :
$$\mathbb{P}_s(E_d) = \sum_{k=1}^\infty \mathbb{P}_s(\{kd\}) = \sum_{k=1}^\infty \frac{1}{\zeta(s) (kd)^s} = \frac{1}{d^s \zeta(s)} \sum_{k=1}^\infty \frac{1}{k^s} = \frac{1}{d^s}$$

Soient $p_1, \dots, p_k$ des nombres premiers distincts. Un entier est divisible par $p_1, \dots, p_k$ si et seulement si il est divisible par leur produit $p_1 \dots p_k$ (car les $p_i$ sont premiers entre eux). On a alors :
$$\mathbb{P}_s(E_{p_1} \cap \dots \cap E_{p_k}) = \mathbb{P}_s(E_{p_1 \dots p_k}) = \frac{1}{(p_1 \dots p_k)^s} = \prod_{j=1}^k \frac{1}{p_j^s} = \prod_{j=1}^k \mathbb{P}_s(E_{p_j})$$
Cela montre l'indépendance de la famille d'événements $(E_p)_{p \in \mathcal{P}}$.

### 3. Retrouver le produit eulérien

On remarque que pour tout entier $n \geq 1$, on a l'équivalence :
$$n = 1 \iff \forall p \in \mathcal{P}, \quad p \nmid n$$
En termes d'événements, cela s'écrit $\{1\} = \bigcap_{p \in \mathcal{P}} \overline{E_p}$.

En utilisant l'indépendance des $(E_p)$ et les propriétés de la mesure (continuité décroissante ou produit infini pour des événements indépendants) :
$$\mathbb{P}_s(\{1\}) = \mathbb{P}_s\left( \bigcap_{p \in \mathcal{P}} \overline{E_p} \right) = \prod_{p \in \mathcal{P}} \mathbb{P}_s(\overline{E_p})$$
D'après la définition de $\mathbb{P}_s$ et le calcul précédent :
$$\frac{1}{\zeta(s)} = \prod_{p \in \mathcal{P}} \left( 1 - \mathbb{P}_s(E_p) \right) = \prod_{p \in \mathcal{P}} \left( 1 - \frac{1}{p^s} \right)$$

En prenant l'inverse, on retrouve le développement eulérien de la fonction $\zeta$ :
$$\zeta(s) = \prod_{p \in \mathcal{P}} \frac{1}{1 - \frac{1}{p^s}}$$

## II. Probabilité que deux entiers soient premiers entre eux

On cherche à estimer la probabilité que deux entiers pris au hasard soient premiers entre eux. Pour cela, on utilise une famille de modèles indexée par $m \in \mathbb{N}^*$, en choisissant une taille de population adéquate pour garantir l'indépendance.

### 1. Modèle et indépendance exacte

Soit $m \in \mathbb{N}^*$. On note $p_1, \dots, p_m$ les $m$ premiers nombres premiers et $N_m = \prod_{i=1}^m p_i$.
On considère $\Omega_m = \{1, \dots, N_m\}^2$ muni de la probabilité uniforme $\mathbb{P}_m$.
Soient $X, Y$ deux variables aléatoires indépendantes et uniformes sur $\{1, \dots, N_m\}$.

D'après le **Théorème des Restes Chinois**, l'application de réduction modulaire $x \mapsto (x \bmod p_1, \dots, x \bmod p_m)$ est une bijection de $\mathbb{Z}/N_m\mathbb{Z}$ dans $\prod \mathbb{Z}/p_i\mathbb{Z}$. Cela assure que les restes modulo les $p_i$ sont indépendants.
Ainsi, les événements $E_{p_i} = \{ p_i \mid X \wedge Y \}$ sont **strictement indépendants** et leur probabilité est exacte :
$$\mathbb{P}_m(E_{p_i}) = \mathbb{P}_m(p_i \mid X) \mathbb{P}_m(p_i \mid Y) = \left( \frac{N_m/p_i}{N_m} \right)^2 = \frac{1}{p_i^2}$$

On note $A_m$ l'événement : « $X$ et $Y$ n'ont aucun facteur premier commun parmi $\{p_1, \dots, p_m\}$ ».
Par indépendance :
$$\mathbb{P}_m(A_m) = \mathbb{P}_m\left( \bigcap_{i=1}^m \overline{E_{p_i}} \right) = \prod_{i=1}^m \left( 1 - \frac{1}{p_i^2} \right)$$

### 2. Contrôle du reste et encadrement

Soit $P_m = \mathbb{P}_m(X \wedge Y = 1)$. On a l'inclusion $\{X \wedge Y = 1\} \subset A_m$, donc $P_m \leq \mathbb{P}_m(A_m)$.
D'autre part, si l'événement $A_m$ est réalisé mais que $X \wedge Y \neq 1$, alors $X \wedge Y$ possède un facteur premier $p > p_m$.
Ainsi :
$$A_m \setminus \{X \wedge Y = 1\} \subset \bigcup_{p > p_m, p \in \mathcal{P}} \{p \mid X \wedge Y\}$$
En majorant la probabilité de l'union par la somme des probabilités :
$$\mathbb{P}_m(A_m) - P_m \leq \sum_{p > p_m, p \in \mathcal{P}} \mathbb{P}_m(p \mid X \wedge Y)$$
Pour $p > p_m$, le nombre de multiples de $p$ dans $\{1, \dots, N_m\}$ est $\lfloor N_m/p \rfloor$. Donc :
$$\mathbb{P}_m(p \mid X \wedge Y) = \left( \frac{\lfloor N_m/p \rfloor}{N_m} \right)^2 \leq \frac{1}{p^2}$$
On obtient l'encadrement :
$$\prod_{i=1}^m \left( 1 - \frac{1}{p_i^2} \right) - \sum_{p > p_m} \frac{1}{p^2} \leq P_m \leq \prod_{i=1}^m \left( 1 - \frac{1}{p_i^2} \right)$$

### 3. Conclusion par passage à la limite

Lorsque $m \to \infty$ :
1. Le terme d'erreur $\sum_{p > p_m} \frac{1}{p^2}$ tend vers $0$ car c'est le reste d'une série convergente.
2. Le produit fini tend vers le produit eulérien :
$$\lim_{m \to \infty} \prod_{i=1}^m \left( 1 - \frac{1}{p_i^2} \right) = \prod_{p \in \mathcal{P}} \left( 1 - \frac{1}{p^2} \right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2}$$

Par le théorème des gendarmes, la probabilité que deux entiers soient premiers entre eux est $\frac{6}{\pi^2} \approx 0,6079$.

## III. Convergence de $P_n$

On revient au modèle standard où $\Omega_n = \{1, \dots, n\}^2$ avec la probabilité uniforme $\mathbb{P}_n$. On cherche à établir la convergence de $P_n = \mathbb{P}_n(X \wedge Y = 1)$ vers $\frac{6}{\pi^2}$.

### 1. Formule du crible et fonction de Möbius

Soit $n \in \mathbb{N}^*$. On cherche à compter le nombre de couples $(x,y) \in \{1, \dots, n\}^2$ tels que $x \wedge y = 1$.
Soient $p_1, \dots, p_k$ les nombres premiers inférieurs ou égaux à $n$. On note $E_i = \{ (x,y) : p_i \mid x \wedge y \}$.
L'événement "être premiers entre eux" correspond à $\bigcap_{i=1}^k \overline{E_i}$. Par la formule du crible :
$$ P_n = 1 - \mathbb{P}_n \left( \bigcup_{i=1}^k E_i \right) = 1 - \sum_{\emptyset \neq J \subset \{1, \dots, k\}} (-1)^{|J|-1} \mathbb{P}_n \left( \bigcap_{j \in J} E_j \right) = \sum_{J \subset \{1, \dots, k\}} (-1)^{|J|} \mathbb{P}_n \left( \bigcap_{j \in J} E_j \right) $$
On a $\bigcap_{j \in J} E_j = \{ (x,y) : (\prod_{j \in J} p_j) \mid x \text{ et } (\prod_{j \in J} p_j) \mid y \}$. Le cardinal de cet ensemble est $\lfloor n/d \rfloor^2$ où $d = \prod_{j \in J} p_j$. 
En effet, dire que $d$ divise le PGCD $x \wedge y$ équivaut à dire que $d \mid x$ et $d \mid y$. Pour chacune des deux composantes, il y a exactement $\lfloor n/d \rfloor$ multiples de $d$ compris entre $1$ et $n$. Par indépendance du choix de $x$ et $y$ (loi uniforme sur $\{1, \dots, n\}^2$), on obtient :
$$ \mathbb{P}_n \left( \bigcap_{j \in J} E_j \right) = \frac{\text{Card} \left( \bigcap_{j \in J} E_j \right)}{n^2} = \frac{\lfloor n/d \rfloor^2}{n^2} $$
Le terme $(-1)^{|J|}$ correspond exactement à $\mu(d)$ pour ces entiers sans facteur carré. Pour les autres entiers $d$ (ayant un facteur carré), $\mu(d) = 0$. On peut donc sommer sur tous les entiers $d$ de $1$ à $n$, d'où l'expression de la probabilité :
$$ P_n = \sum_{d=1}^n \frac{\mu(d)}{n^2} \lfloor n/d \rfloor^2 $$

### 2. Convergence de $P_n$

On remarque que $\frac{1}{n^2} \lfloor n/d \rfloor^2 \xrightarrow[n \to \infty]{} \frac{1}{d^2}$. On s'attend donc à ce que $P_n \to \sum_{d=1}^\infty \frac{\mu(d)}{d^2} = \frac{1}{\zeta(2)}$.

#### Méthode 1 : Convergence dominée (élégante)
On écrit $P_n = \sum_{d=1}^\infty f_n(d)$ avec $f_n(d) = \frac{\mu(d)}{n^2} \lfloor n/d \rfloor^2$.
- Convergence simple : Pour tout $d \in \mathbb{N}^*$, $f_n(d) \xrightarrow[n \to \infty]{} \frac{\mu(d)}{d^2}$
- Domination : $|f_n(d)| \le \frac{1}{n^2} (n/d)^2 = \frac{1}{d^2}$. La série $\sum \frac{1}{d^2}$ converge.
Par le théorème de convergence dominée, $P_n \to \sum_{d=1}^\infty \frac{\mu(d)}{d^2} = \frac{6}{\pi^2}$.

#### Méthode 2 : Majoration directe (plus élémentaire)
On retranche la série limite et on utilise $\lfloor x \rfloor = x - \{x\}$ :
$$ |P_n - \sum_{d=1}^\infty \frac{\mu(d)}{d^2}| \le |\sum_{d=1}^n \mu(d) \left( \frac{\lfloor n/d \rfloor^2}{n^2} - \frac{1}{d^2} \right)| + |\sum_{d=n+1}^\infty \frac{\mu(d)}{d^2}| $$
Le deuxième terme est le reste d'une série convergente, il tend vers $0$. Pour le premier, on utilise $x^2 - y^2 = (x-y)(x+y)$ avec $x = \frac{\lfloor n/d \rfloor}{n}$ et $y = \frac{1}{d}$ :
$$ |\frac{\lfloor n/d \rfloor^2}{n^2} - \frac{1}{d^2}| = |\frac{\lfloor n/d \rfloor}{n} - \frac{1}{d}| \cdot |\frac{\lfloor n/d \rfloor}{n} + \frac{1}{d}| \le \frac{1}{n} \cdot \frac{2}{d} $$
En sommant :
$$ \sum_{d=1}^n |\frac{\mu(d)}{n^2} \lfloor n/d \rfloor^2 - \frac{\mu(d)}{d^2}| \le \frac{2}{n} \sum_{d=1}^n \frac{1}{d} \le \frac{2(1 + \ln n)}{n} \xrightarrow[n \to \infty]{} 0 $$
Ainsi $P_n \to \frac{6}{\pi^2}$.

## IV. Preuve du lien entre $\zeta(s)$ et la fonction de Möbius

On a vu que pour $s > 1$, $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ et que $\frac{1}{\zeta(s)} = \prod_{p \in \mathcal{P}} (1 - p^{-s})$. 
On souhaite démontrer rigoureusement, via une sommation par paquets, que :
$$\frac{1}{\zeta(s)} = \sum_{n=1}^\infty \frac{\mu(n)}{n^s}$$

### 1. Développement du produit fini

Soit $n \in \mathbb{N}^*$ et $\mathcal{P}_n = \{p_1, \dots, p_n\}$ l'ensemble des $n$ premiers nombres premiers. Considérons le produit partiel :
$$\Pi_n = \prod_{p \in \mathcal{P}_n} \left( 1 - \frac{1}{p^s} \right)$$
Par distributivité, ce produit se développe en une somme de termes de la forme $(-1)^k \frac{1}{(q_1 \dots q_k)^s}$, où $\{q_1, \dots, q_k\}$ est un sous-ensemble de $\mathcal{P}_n$. 
Notons $\mathcal{D}_n$ l'ensemble des entiers dont tous les diviseurs premiers appartiennent à $\mathcal{P}_n$ et qui sont sans facteur carré. Chaque tel entier $d$ s'écrit de manière unique comme un produit de nombres premiers distincts de $\mathcal{P}_n$. On reconnaît alors la définition de la fonction de Möbius $\mu(d)$ :
$$\Pi_n = \sum_{d \in \mathcal{D}_n} \frac{\mu(d)}{d^s}$$
Comme $\mu(m) = 0$ dès que $m$ possède un facteur carré, on peut étendre la somme à l'ensemble $S_n$ des entiers dont tous les facteurs premiers sont dans $\mathcal{P}_n$ :
$$\Pi_n = \sum_{m \in S_n} \frac{\mu(m)}{m^s}$$

### 2. Passage à la limite

On veut comparer cette somme avec la série totale $M(s) = \sum_{m=1}^\infty \frac{\mu(m)}{m^s}$. Étudions la différence :
$$\left| M(s) - \Pi_n \right| = \left| \sum_{m=1}^\infty \frac{\mu(m)}{m^s} - \sum_{m \in S_n} \frac{\mu(m)}{m^s} \right| = \left| \sum_{m \notin S_n} \frac{\mu(m)}{m^s} \right| \leq \sum_{m \notin S_n} \frac{1}{m^s}$$
Un entier $m \notin S_n$ possède nécessairement au moins un facteur premier $p > p_n$. En particulier, $m > p_n$. Ainsi :
$$\sum_{m \notin S_n} \frac{1}{m^s} \leq \sum_{m=p_n+1}^\infty \frac{1}{m^s}$$
Comme $s > 1$, la série $\sum \frac{1}{m^s}$ converge. Le reste de cette série tend vers $0$ lorsque son premier indice tend vers l'infini. Or $p_n \xrightarrow[n \to \infty]{} \infty$, donc :
$$\lim_{n \to \infty} \left| M(s) - \Pi_n \right| = 0$$

### 3. Conclusion

On en déduit que :
$$\sum_{n=1}^\infty \frac{\mu(n)}{n^s} = \lim_{n \to \infty} \Pi_n = \prod_{p \in \mathcal{P}} \left( 1 - \frac{1}{p^s} \right) = \frac{1}{\zeta(s)}$$

## V. Divergence de la série $\sum_{p \in \mathcal{P}}\frac{1}{p}$

On a vu que pour $s > 1$, $\prod_{p \in \mathcal{P}} (1 - p^{-s}) = \frac{1}{\zeta(s)}$.

Pour $s > 1$, la fonction $x \mapsto \frac{1}{x^s}$ est décroissante sur $[1, +\infty[$. Par comparaison série-intégrale, on a :
$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} \geq \int_1^\infty \frac{dx}{x^s} = \left[ \frac{x^{1-s}}{1-s} \right]_1^\infty = \frac{1}{s-1}$$
Comme $\frac{1}{s-1} \xrightarrow[s \to 1^+]{} +\infty$, on en déduit que $\zeta(s) \xrightarrow[s \to 1^+]{} +\infty$.

Ainsi, $\prod_{p \in \mathcal{P}} (1 - p^{-s}) \to 0$ lorsque $s \to 1^+$.

Par théorème d'encadrement, pour tout $s > 1$ :
$$\prod_{p \in \mathcal{P}} (1 - p^{-s}) \geq \prod_{p \in \mathcal{P}} (1 - p^{-1}) \geq 0$$

Ce qui donne en faisant tendre $s \to 1^+$ :
$$\prod_{p \in \mathcal{P}} (1 - p^{-1}) = 0$$

Passons au log sur un produit partiel :
$$\ln \left( \prod_{1 \leq i \leq n} (1 - p^{-1}_i) \right) = \sum_{1 \leq i \leq n} \ln(1 - p^{-1}_i) \xrightarrow[n \to \infty]{} -\infty$$
Or
$$\ln(1 - p^{-1}_i) \underset{i \to +\infty}{\sim} -p^{-1}_i$$

Donc par sommation des équivalents :
$$\sum_{1 \leq i \leq n} \ln(1 - p^{-1}_i) \underset{n \to +\infty}{\sim} -\sum_{1 \leq i \leq n} p^{-1}_i$$
La série $\sum_{p \in \mathcal{P}} \frac{1}{p}$ diverge.

## VI. Il n'y a pas de probabilité naturelle sur $\mathbb{N}^*$

Il est rapide de vérifier qu'il n'y a pas de probabilité uniforme sur $\mathbb{N}^*$. En effet, si une telle probabilité $\mathbb{P}$ existait, on aurait pour tout $n \in \mathbb{N}^*$ :
$$\mathbb{P}(\{n\}) = c$$
pour une constante $c > 0$. Alors :
$$1 = \mathbb{P}(\mathbb{N}^*) = \sum_{n=1}^\infty \mathbb{P}(\{n\}) = \sum_{n=1}^\infty c = +\infty$$
ce qui est absurde.

On peut se demander s'il existe une probabilité $\mathbb{P}$ sur $\mathbb{N}^*$ telle que pour tout $d \in \mathbb{N}^*$, $\mathbb{P}(d\mathbb{N}) = \frac{1}{d}$

Si une telle probabilité existe :

Les événements $p\mathbb{N}$ sont indépendants pour $p$ premier. Soit $n \in \mathbb{N}^*$. par indépendance puis décroissance séquentielle :

$$\mathbb{P}(\{n\}) \leq \mathbb{P}(\bigcap_{p>n} \overline{p\mathbb{N}}) = \prod_{p>n} (1 - \frac{1}{p}) = 0$$

Ce qui aboutit à $\mathbb{P}(\mathbb{N}^*) = \sum_{n=1}^\infty \mathbb{P}(\{n\}) = 0$, ce qui est absurde.