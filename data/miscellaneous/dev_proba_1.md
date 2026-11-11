C'est **exactement la clé** ! Votre intuition est remarquable : choisir $N_m = p_1 p_2 \dots p_m$ (le produit des $m$ premiers nombres premiers, parfois appelé la primorielle $p_m\#$) est l'astuce classique qui **restaure une indépendance parfaite et exacte** sans avoir à gérer des parties entières bilatérales.

En posant $N_m = \prod_{i=1}^m p_i$, on s'affranchit de tous les effets de bord de la partie entière sur le pavé $\{1, \dots, N_m\}^2$.

---

### 1. Pourquoi l'indépendance devient stricte et exacte sur $\{1, \dots, N_m\}$

Considérons un entier $X$ choisi uniformément au hasard dans $\{1, 2, \dots, N_m\}$.

D'après le **Théorème des Restes Chinois**, l'application de réduction modulaire :

$$\mathbb{Z} / N_m \mathbb{Z} \longrightarrow (\mathbb{Z} / p_1 \mathbb{Z}) \times (\mathbb{Z} / p_2 \mathbb{Z}) \times \dots \times (\mathbb{Z} / p_m \mathbb{Z})$$

$$x \bmod N_m \longmapsto (x \bmod p_1, \, x \bmod p_2, \, \dots, \, x \bmod p_m)$$

est un **bijection**.

Cela signifie que le reste de $X$ modulo $p_i$ est **totalement indépendant** de son reste modulo $p_j$ (pour $i \neq j$).

Ainsi, pour deux entiers $A$ et $B$ choisis indépendamment et uniformément dans $\{1, \dots, N_m\}$ :

1. La probabilité que $p_i$ divise $A$ vaut **exactement** $\frac{1}{p_i}$ (car il y a exactement $\frac{N_m}{p_i}$ multiples de $p_i$ dans $\{1, \dots, N_m\}$).
2. La probabilité que $p_i$ divise $A$ **et** $B$ vaut **exactement** $\frac{1}{p_i^2}$.
3. L'événement $E_i = \text{« } p_i \text{ ne divise pas simultanément } A \text{ et } B \text{ »}$ a une probabilité exacte :

$$\mathbb{P}(E_i) = 1 - \frac{1}{p_i^2}$$


4. **Grâce au théorème des restes chinois, les événements $(E_1, E_2, \dots, E_m)$ sont strictement indépendants.**

La probabilité que $A$ et $B$ n'aient **aucun facteur premier commun parmi $\{p_1, \dots, p_m\}$** s'écrit donc **exactement** comme un produit :

$$\mathbb{P}\big(\forall i \le m, \, p_i \nmid \text{pgcd}(A,B)\big) = \prod_{i=1}^m \left(1 - \frac{1}{p_i^2}\right)$$

Ici, **aucun reste ni partie entière**, l'égalité est exacte !

---

### 2. Le passage à la limite quand $m \to \infty$

Pour transformer cette égalité sur les premiers jusqu'à $p_m$ en la probabilité absolue que $\text{pgcd}(A,B) = 1$, il reste un seul détail : contrôler les facteurs premiers strictement supérieurs à $p_m$.

Soit $A, B \in \{1, \dots, N_m\}$. Ils ne sont **pas** premiers entre eux si et seulement si :

* **Cas 1 :** Ils ont un facteur commun $p \le p_m$.
* **Cas 2 :** Ils ont un facteur commun $p > p_m$.

Notons $P_m$ la probabilité que $\text{pgcd}(A,B) = 1$ dans $\{1, \dots, N_m\}^2$. On peut l'encadrer ainsi :

$$\prod_{i=1}^m \left(1 - \frac{1}{p_i^2}\right) - \mathbb{P}(\text{facteur commun } > p_m) \le P_m \le \prod_{i=1}^m \left(1 - \frac{1}{p_i^2}\right)$$

#### Majoration du risque pour $p > p_m$ :

La probabilité qu'un nombre premier $p > p_m$ divise à la fois $A$ et $B$ dans $\{1, \dots, N_m\}$ est majorée par $\frac{1}{p^2}$ (en comptant les multiples). Donc :

$$\mathbb{P}(\text{facteur commun } > p_m) \le \sum_{p > p_m} \frac{1}{p^2} \le \sum_{k = p_m + 1}^\infty \frac{1}{k^2} \le \frac{1}{p_m}$$

On obtient l'encadrement parfait :

$$\prod_{i=1}^m \left(1 - \frac{1}{p_i^2}\right) - \frac{1}{p_m} \le P_m \le \prod_{i=1}^m \left(1 - \frac{1}{p_i^2}\right)$$

---

### 3. Conclusion de la preuve

Lorsque $m \to \infty$ :

1. $p_m \to \infty$, donc le terme d'erreur $\frac{1}{p_m} \to 0$.
2. Le produit fini tend vers le produit d'Euler infini :

$$\lim_{m \to \infty} \prod_{i=1}^m \left(1 - \frac{1}{p_i^2}\right) = \prod_{p \in \mathcal{P}} \left(1 - \frac{1}{p^2}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2}$$



Par le théorème des gendarmes, la probabilité asymptotique $P$ vaut exactement $\frac{6}{\pi^2}$.

En choisissant $N = p_1 p_2 \dots p_m$, vous avez utilisé la structure d'anneau de $\mathbb{Z}/N\mathbb{Z}$ pour obtenir une véritable indépendance probabiliste. C'est une démonstration élégante et rigoureuse.