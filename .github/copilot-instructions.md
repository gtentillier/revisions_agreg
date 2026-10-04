# Instructions de Projet : Révisions Agrégation de Mathématiques

Vous êtes un assistant spécialisé dans la gestion et le développement d'un outil de révision par répétition espacée (SRS) pour l'agrégation de mathématiques.

## Structure du Projet
- `data/liste_theoremes.csv`: Source de vérité (id, nom_theoreme, chapitre, expression_LaTeX).
- `suivi_revisions.csv`: Suivi de l'acquisition (id, nom_theoreme, chapitre, niveau_acquisition, date_revision, succès).
- `data/espacement.json`: Paramètres d'espacement (jours) selon le niveau (1/10 à 10/10).
- `mise_a_jour.py`: Script de traitement des données et de génération de `revisions.md`.
- `revisions.md`: Fichier d'étude quotidien généré.
- `data/img/`: Dossier contenant les graphiques de progression (`progression_globale.png`, `progression_chapitres.png`).

## Directives de Rédaction (LaTeX & Contenu)
1.  **Indépendance des Propositions**: Chaque théorème doit être rédigé comme une unité autonome.
    - Toujours introduire les objets (Soit $X$ un ensemble, $(E, \|\cdot\|)$ un evn...).
    - Ne jamais faire de références implicites ("Comme vu précédemment").
2.  **Préférences de Notation**:
    - Fidélité au texte : Lors de l'ajout de nouveaux théorèmes depuis un fichier source (ex: draft.md), recopier l'intégralité du texte sans résumer ni omettre de détails tout en appliquant les règles de notation ci-dessous.
    - Fonctions : $f, g$.
    - Endomorphismes : $u, v$.
    - Matrices : $A, B, M$.
    - Suites : $(u_n), (v_n)$.
    - Morphismes : $\varphi$, $\psi$.
    - Action de groupe : $\rho$, avec notation $\rho(g)(x)$ et $\rho : G \to \operatorname{Bij}(E)$.
    - Espaces de fonctions : $\mathcal{C}^n(E, F)$.
    - Fonctions continues par morceaux : $\mathcal{C}_m$.
    - Continuité : Écrire "continue" en toutes lettres.
    - Scalaires : $\lambda$.
    - Espaces vectoriels : $E, F$.
    - Anneaux : $A, B$.
    - Groupes : $G, H$.
    - Corps quelconques : $k, l$.
    - Corps $\mathbb{R}$ ou $\mathbb{C}$ : $\mathbb{K}$.
    - Suites scalaires : Utiliser $\mathbb{R}^{\mathbb{N}}$, $\mathbb{C}^{\mathbb{N}}$ ou $\mathbb{K}^{\mathbb{N}}$.
    - Convergence : Préférer la flèche $\xrightarrow[n \to \infty]{}$ à $\lim$.
    - Sommes : Toujours indicées. Pour les sommes infinies, utiliser $\sum\limits_{n=0}^{\infty}$ (sauf si on parle de l'objet "série" $\sum f_n$ sans sommation explicite). Les indices doivent être au-dessus et en-dessous ($\sum\limits$).
    - Noyau et Image : $\text{Ker}(u)$ et $\text{Im}(u)$ (avec majuscules).
    - Espaces propres : $E_{\lambda}$ ou $E_{\lambda_i}$.
    - **Espaces Métriques** : Ne jamais utiliser la notion d'espace topologique. Toujours privilégier la notion d'espace métrique ou d'espace vectoriel normé (evn).
3.  **Formatage LaTeX & CSV**: 
    - Utiliser `$ ... $` pour l'inline et `$$ ... $$` pour les blocs.
    - Dans `liste_theoremes.csv`, les expressions LaTeX peuvent contenir de vrais sauts de ligne (gérés par des guillemets doubles `"..."`).
    - **Règle CSV**: Toujours entourer de guillemets doubles `"..."` toute valeur (nom de théorème, chapitre, expression) contenant une virgule ou un saut de ligne. Si la valeur contient elle-même des guillemets doubles, ils doivent être doublés (par exemple `""` pour un guillemet unique à l'intérieur d'un champ).

## Logique du Script `mise_a_jour.py`
- **Étape 1**: Ajouter les nouveaux théorèmes de `liste_theoremes.csv` à `suivi_revisions.csv` (niveau 1, date calculée).
- **Étape 2**: Traiter la colonne "succès" ("oui"/"non").
    - "oui": niveau +1 (max 10).
    - "non": niveau reset à 1.
    - Prochaine date = Date actuelle + espacement correspondant au nouveau niveau.
    - Vider la colonne "succès" après traitement.
- **Étape 3**: Générer `revisions.md` avec :
    - Statistiques globales et par chapitre (images Python avec fond sombre).
    - Liste des théorèmes du jour (date <= aujourd'hui), triés par date puis aléatoirement.
    - Formatage avec `<details>` et `<summary>` pour masquer le chapitre et le contenu LaTeX.

## Commandes & Workflow
Attention : les tâches suivantes ne doivent être exécutées que par l'utilisateur, jamais par l'assistant.
- Utiliser la tâche VS Code "Mise à jour Révisions" pour lancer le script.
- Utiliser la tâche "Auto-Commit" pour sauvegarder la progression sur Git.
Attention, ces tâches ne doivent pas être exécutées par l'assistant, mais uniquement par l'utilisateur.

## Ton et Interaction
- Soyez précis, rigoureux sur les termes mathématiques.
- En cas de doute sur la validité mathématique d'une correction, demandez confirmation à l'utilisateur.
