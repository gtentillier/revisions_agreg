# Révisions Agrégation de Mathématiques

Outil de révision par répétition espacée (SRS) pour l'agrégation de mathématiques. Ce projet permet de suivre l'acquisition des théorèmes et de générer un programme de révision quotidien basé sur la performance passée.

## 🚀 Workflow de Révision

1. **Mettre à jour** :
   - Lancez la tâche VS Code **"Mise à jour Révisions"** (ou `python3 scripts/mise_a_jour.py`).
   - Le script va, pour chaque théorème :
     - Incrémenter le niveau d'acquisition de 1 si succès est à `oui` ou le réinitialiser à 1 si `non`.
     - Calculer la prochaine date de révision pour chaque théorème.
     - Vider la colonne `succès`.
     - Mettre à jour les graphiques de progression.
     - Générer le nouveau `revisions.md`.
2. **Ouvrir `revisions.md`** en mode preview : Consultez les théorèmes prévus pour aujourd'hui.
3. **Réviser** : Pour chaque théorème, essayez de retrouver le chapitre et l'énoncé, ainsi qu'avoir une idée de la preuve, puis s'auto-évaluer en regardant la solution.
4. **Noter le succès** :
   - Ouvrez `suivi_revisions.csv`.
   - Pour chaque théorème révisé, remplissez la colonne **`succès`** par `oui` ou `non`.
   - _Note : Le fichier est trié dans le même ordre que `revisions.md` pour faciliter la saisie._
5. **Mettre à jour** comme précédemment pour que la révision prenne effet dans le fichier de suivi.

## 📁 Structure du Projet

- **`liste_theoremes.csv`** : Source de vérité. Contient les colonnes `id` (entier unique), `nom_theoreme`, `chapitre`, et `expression_LaTeX`. C'est le seul fichier à modifier pour ajouter des théorèmes, via `scripts/extract_theorems.py`.
- **`suivi_revisions.csv`** : Suivi généré automatiquement. Contient le `niveau_acquisition` (1 à 10), la `date_revision`, et la colonne `succès` ("oui"/"non").
- **`espacement.json`** : Paramètres d'espacement (en jours) selon le niveau d'acquisition.
- **`scripts/mise_a_jour.py`** : Script principal qui traite les résultats du jour et génère le fichier de révision.
- **`scripts/extract_theorems.py`** : Script pour ajouter de nouveaux théorèmes à partir d'un fichier `draft.md`.
- **`revisions.md`** : Fichier d'étude généré via `scripts/mise_a_jour.py` contenant les noms des théorèmes à réviser, ainsi que leur chapitre et énoncé.
- **`img/`** : Graphiques de progression générés (`progression_globale.png` et `progression_chapitres.png`), et autres illustrations.
