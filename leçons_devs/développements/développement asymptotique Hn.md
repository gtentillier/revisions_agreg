# Développement Asymptotique de la série harmonique $H_n$

## Énoncé et notations
Soit $H_n = \sum\limits_{k=1}^n \frac{1}{k}$ la $n$-ième somme partielle de la série harmonique. Nous allons montrer que $H_n = \ln n + \gamma + \frac{1}{2n} + O\left(\frac{1}{n^2}\right)$ où $\gamma$ est la constante d'Euler.

## Étape 1 : Équivalent de $H_n$
Puisque la fonction $t \mapsto \frac{1}{t}$ est décroissante sur $[1, +\infty[$, on a pour tout $k \geq 2$ :
$$ \int_{k}^{k+1} \frac{dt}{t} \leq \frac{1}{k} \leq \int_{k-1}^{k} \frac{dt}{t} $$
En sommant cette relation pour $k$ allant de $2$ à $n$, puis en ajoutant $1$, on obtient :
$$ 1 + \int_{2}^{n+1} \frac{dt}{t} \leq H_n \leq 1 + \int_{1}^{n} \frac{dt}{t} $$
En calculant les intégrales, on trouve :
$$ 1 + \ln(n+1) - \ln(2) \leq H_n \leq \ln(n) + 1 $$
On en déduit que $\frac{H_n}{\ln n} \xrightarrow[n \to \infty]{} 1$, et donc $H_n \sim \ln n$.

## Étape 2 : Convergence de $u_n = H_n - \ln n$
Soit $v_n = u_{n+1} - u_n$. On a :
$$ v_n = H_{n+1} - \ln(n+1) - H_n + \ln(n) = \frac{1}{n+1} - \ln(n+1) + \ln(n) $$
$$ v_n = \frac{1}{n+1} + \ln\left(1 - \frac{1}{n+1}\right) $$
En utilisant un développement limité à l'ordre 2 :
$$ v_n = \frac{1}{n+1} - \left( \frac{1}{n+1} + \frac{1}{2(n+1)^2} + O\left(\frac{1}{(n+1)^2}\right) \right) $$
$$ v_n = -\frac{1}{2(n+1)^2} + O\left(\frac{1}{(n+1)^2}\right) $$
Ainsi, $v_n \sim -\frac{1}{2n^2}$. La série $\sum v_n$ est donc convergente par comparaison avec une série de Riemann.<br>
Comme $\sum_{k=1}^{n-1} v_k = u_n - u_1$, la suite $(u_n)$ converge vers une limite réelle notée $\gamma$.

## Étape 3 : Reste de la série harmonique
Soit $R_n = \sum\limits_{k=n}^{\infty} \frac{1}{k^2}$. On peut estimer ce reste par deux méthodes :

**Méthode 1 : Comparaison intégrale**
Par comparaison intégrale :
$$ \int_{n}^{n+1} \frac{dt}{t^2} \leq \frac{1}{k^2} \leq \int_{k-1}^{k} \frac{dt}{t^2} $$
En sommant pour $k$ de $n$ à $+\infty$ :
$$ \frac{1}{n} = \int_{n}^{+\infty} \frac{dt}{t^2} \leq R_n \leq \int_{n-1}^{+\infty} \frac{dt}{t^2} = \frac{1}{n-1} $$
D'où $R_n \sim \frac{1}{n}$.

**Méthode 2 : Télescopage d'équivalents**
On remarque que $\frac{1}{k^2} \sim \frac{1}{k(k+1)}$. Comme la série $\sum \frac{1}{k^2}$ converge, on peut sommer les équivalents :
$$ R_n = \sum_{k=n}^{\infty} \frac{1}{k^2} \sim \sum_{k=n}^{\infty} \frac{1}{k(k+1)} $$
Par décomposition en éléments simples, $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$. La somme se téléscope :
$$ \sum_{k=n}^{N} \left( \frac{1}{k} - \frac{1}{k+1} \right) = \frac{1}{n} - \frac{1}{N+1} \xrightarrow[N \to \infty]{} \frac{1}{n} $$
On retrouve bien $R_n \sim \frac{1}{n}$.

## Étape 4 : Précision du développement
Soit $w_n$ tel que $H_n = \ln n + \gamma + w_n$. On sait que $w_n \xrightarrow[n \to \infty]{} 0$.<br>
Posons $t_n = w_{n+1} - w_n = v_n = -\frac{1}{2(n+1)^2} + O\left(\frac{1}{n^2}\right)$, soit $t_n \sim -\frac{1}{2n^2}$.<br>
La série $\sum t_n$ converge, et par comparaison des restes de séries à termes négatifs :
$$ \sum_{k=n}^{\infty} (w_{k+1} - w_k) \sim \sum_{k=n}^{\infty} -\frac{1}{2k^2} $$
Or, $\sum_{k=n}^{N} (w_{k+1} - w_k) = w_{N+1} - w_n \xrightarrow[N \to \infty]{} -w_n$ car $w_N \to 0$.<br>
En utilisant $R_n \sim \frac{1}{n}$, on obtient :
$$ -w_n \sim -\frac{1}{2n} \implies w_n = \frac{1}{2n} + O\left(\frac{1}{n}\right) $$
D'où le résultat final :
$$ H_n = \ln n + \gamma + \frac{1}{2n} + O\left(\frac{1}{n}\right) $$
