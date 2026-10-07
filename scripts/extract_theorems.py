import csv
import os
import re

"""
Ce script permet d'extraire des théorèmes et définitions depuis un fichier Markdown (par défaut draft.md)
et de les intégrer directement dans data/liste_theoremes.csv.

Format attendu pour le fichier source (ex: draft.md) :
1. Chapitres : Indiqués par des titres de niveau 1 (# Nom du Chapitre).
2. Théorèmes : Indiqués par des titres de niveau 2 (## Titre du Théorème).
3. Contenu : Tout le texte entre un titre ## et le suivant (ou le changement de chapitre).

Le script gère :
- L'extraction automatique du nom du chapitre.
- La préservation du formatage LaTeX ($...$ et $$...$$).
- Le formatage CSV conforme (les guillemets doubles sont doublés).
- L'incrémentation automatique des IDs à partir du dernier ID existant.
- La vérification de la structure avant l'ajout.
"""


def get_last_id(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Le fichier source CSV est introuvable : {csv_path}")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        if len(data) <= 1:
            raise ValueError(f"Le fichier {csv_path} est vide ou ne contient que l'en-tête.")
        
        # On cherche le dernier ID valide en partant de la fin
        for i in range(len(data)-1, 0, -1):
            if data[i] and data[i][0].isdigit():
                return int(data[i][0])
        
        raise ValueError(f"Impossible de trouver un ID valide dans {csv_path}")


def extract_from_md(md_path):
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Le fichier Markdown source est introuvable : {md_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split par chapitre (# Nom du Chapitre)
    chapters = re.split(r'^# ', content, flags=re.MULTILINE)

    theorems = []

    for chapter_block in chapters:
        if not chapter_block.strip():
            continue

        lines = chapter_block.split('\n')
        chapter_name = lines[0].strip()

        # Split par théorème (## Titre du Théorème)
        theorems_in_chapter = re.split(r'^## ', chapter_block, flags=re.MULTILINE)
        # La première partie est l'en-tête du chapitre, on l'ignore
        for t_block in theorems_in_chapter[1:]:
            t_lines = t_block.split('\n')
            title = t_lines[0].strip()
            # Le contenu est tout ce qui suit la première ligne (titre)
            expression = '\n'.join(t_lines[1:]).strip()
            theorems.append((title, chapter_name, expression))

    if not theorems:
        raise ValueError(f"Aucun théorème n'a été trouvé dans le fichier {md_path}. Vérifiez le format (# Chapitre, ## Théorème).")
            
    return theorems


if __name__ == "__main__":
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Source par défaut dans draft.md à la racine
        MD_SOURCE = os.path.join(BASE_DIR, 'draft.md')
        CSV_DEST = os.path.join(BASE_DIR, 'data/liste_theoremes.csv')

        extracted = extract_from_md(MD_SOURCE)
        last_id = get_last_id(CSV_DEST)
        next_id = last_id + 1

        # Étape 1 : Préparation des données avec vérification
        temp_rows = []
        for title, chapter, expression in extracted:
            temp_rows.append([next_id, title, chapter, expression])
            next_id += 1

        # Vérification de la structure (4 colonnes par ligne)
        for i, row in enumerate(temp_rows):
            if len(row) != 4:
                raise ValueError(f"Erreur de structure à la ligne {i+1} du contenu extrait (attendu: 4 colonnes).")

        if len(temp_rows) != len(extracted):
            raise ValueError("Erreur lors de la préparation des données : le nombre de lignes ne correspond pas.")

        # Étape 2 : Ajout réel dans liste_theoremes.csv
        with open(CSV_DEST, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerows(temp_rows)

        print(f"Succès : {len(temp_rows)} théorèmes ajoutés à {CSV_DEST}.")
        print(f"IDs ajoutés : {last_id + 1} à {next_id - 1}.")

    except Exception as e:
        print(f"ERREUR : {e}")
        exit(1)
