import csv
import json
import os
import random
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

# Files configuration
LISTE_THEOREMES = "liste_theoremes.csv"
SUIVI_REVISIONS = "suivi_revisions.csv"
ESPACEMENT_JSON = "espacement.json"
REVISIONS_MD = "revisions.md"
IMG_DIR = "img"


def load_espacement():
    with open(ESPACEMENT_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_csv(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def save_suivi(data):
    fieldnames = ["id", "nom_théorème", "chapitre", "niveau_acquisition", "date_revision", "succès"]
    with open(SUIVI_REVISIONS, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def mise_a_jour():
    espacement = load_espacement()
    liste_theoremes = load_csv(LISTE_THEOREMES)
    suivi_revisions = load_csv(SUIVI_REVISIONS)

    suivi_ids = {row['id'] for row in suivi_revisions}
    today = datetime.now()

    # Etape 1: Ajouter nouveaux théorèmes
    for row in liste_theoremes:
        if row['id'] not in suivi_ids:
            days = espacement.get("days_knowledge_1/10", 1)
            next_date = today + timedelta(days=days)
            new_row = {"id": row['id'], "nom_théorème": row['nom_theoreme'], "chapitre": row['chapitre'], "niveau_acquisition": 1, "date_revision": next_date.strftime("%d/%m/%Y"), "succès": ""}
            suivi_revisions.append(new_row)

    # Etape 2: Traiter les succès/échecs
    for row in suivi_revisions:
        succes = row['succès'].strip().lower()
        if succes:
            if succes not in ['oui', 'non']:
                raise ValueError(f"Valeur invalide dans 'succès' pour l'id {row['id']}: {succes}")

            niveau = int(row['niveau_acquisition'])
            if succes == 'oui':
                niveau = min(10, niveau + 1)
            else:
                niveau = 1

            row['niveau_acquisition'] = niveau
            days = espacement.get(f"days_knowledge_{niveau}/10", 1)
            next_date = today + timedelta(days=days)
            row['date_revision'] = next_date.strftime("%d/%m/%Y")
            row['succès'] = ""

    # Generate visualisations
    generate_visualisations(suivi_revisions)

    # Sort for revisions.md and save
    # "le fichier suivi_revisions.csv sera trié par ordre d'affichage des théorèmes à réviser de revisions.md"
    # Order: date_revision ASC, then random within same date

    def parse_date(d_str):
        return datetime.strptime(d_str, "%d/%m/%Y")

    # To ensure random order within same date, we first shuffle the whole list
    random.shuffle(suivi_revisions)
    # Then sort by date
    suivi_revisions.sort(key=lambda x: parse_date(x['date_revision']))

    save_suivi(suivi_revisions)

    # Etape 3: Rédiger revisions.md
    write_revisions_md(suivi_revisions, liste_theoremes)


def generate_visualisations(suivi_revisions):
    if not suivi_revisions:
        return

    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)

    df = pd.DataFrame(suivi_revisions)
    df['niveau_acquisition'] = df['niveau_acquisition'].astype(int)

    total_theoremes = len(df)
    total_acquisition = df['niveau_acquisition'].sum()
    max_possible = total_theoremes * 10
    global_progress = (total_acquisition / max_possible) * 100 if max_possible > 0 else 0

    # Global progress plot
    plt.style.use('dark_background')
    bg_color = (31 / 255, 31 / 255, 31 / 255)
    fig, ax = plt.subplots(figsize=(6, 2))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.barh(['Progression Globale'], [global_progress], color='skyblue')
    ax.set_xlim(0, 100)
    # ax.set_xlabel('Pourcentage (%)')
    ax.set_title(f'Progression Totale: {global_progress:.0f}%')
    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'progression_globale.png'), facecolor=fig.get_facecolor())
    plt.close()

    # Chapter progress plot
    chapter_stats = df.groupby('chapitre')['niveau_acquisition'].agg(['sum', 'count'])
    chapter_stats['progress'] = (chapter_stats['sum'] / (chapter_stats['count'] * 10)) * 100

    fig, ax = plt.subplots(figsize=(8, max(2, len(chapter_stats) * 0.5)))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    colors = plt.cm.viridis(chapter_stats['progress'] / 100)
    bars = ax.barh(chapter_stats.index, chapter_stats['progress'], color=colors)
    ax.set_xlim(0, 100)
    # ax.set_xlabel('Pourcentage (%)')
    ax.set_title('Progression par Chapitre')

    for i, bar in enumerate(bars):
        legend = f"{chapter_stats['sum'].iloc[i]}/{chapter_stats['count'].iloc[i]*10}"
        # legend += f"({chapter_stats['progress'].iloc[i]:.0f}%)"
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, legend, va='center')

    plt.tight_layout()
    plt.savefig(os.path.join(IMG_DIR, 'progression_chapitres.png'), facecolor=fig.get_facecolor())
    plt.close()


def write_revisions_md(suivi_revisions, liste_theoremes):
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    def parse_date(d_str):
        return datetime.strptime(d_str, "%d/%m/%Y")

    to_revise = [row for row in suivi_revisions if parse_date(row['date_revision']) <= today]
    total_theoremes = len(suivi_revisions)

    df = pd.DataFrame(suivi_revisions)
    df['niveau_acquisition'] = df['niveau_acquisition'].astype(int)
    total_acquisition = df['niveau_acquisition'].sum()
    max_possible = total_theoremes * 10
    global_progress = (total_acquisition / max_possible) * 100 if max_possible > 0 else 0

    # Map id to LaTeX
    latex_map = {row['id']: row['expression_LaTeX'] for row in liste_theoremes}

    with open(REVISIONS_MD, 'w', encoding='utf-8') as f:
        f.write(f"![Progression Globale](img/progression_globale.png)\n\n")
        f.write(f"![Progression Chapitres](img/progression_chapitres.png)\n\n")
        f.write(f"**{len(to_revise)}** Théorèmes à réviser sur **{total_theoremes}**\n\n")

        # Group by date
        dates = sorted(list({row['date_revision'] for row in to_revise}), key=parse_date)

        for i, d_str in enumerate(dates):
            if i > 0:
                f.write("<br>\n\n")
            f.write(f"# 📚 {d_str}\n\n")
            current_date_theorems = [row for row in to_revise if row['date_revision'] == d_str]
            # They are already shuffled in suivi_revisions, but let's be safe
            random.shuffle(current_date_theorems)

            f.write(f"**{len(current_date_theorems)}** Théorèmes\n\n")

            for i, row in enumerate(current_date_theorems, 1):
                f.write(f"## {i}. {row['nom_théorème']}\n\n")
                f.write(f"<details>\n<summary><b>Chapitre</b></summary>\n<blockquote>\n{row['chapitre']}\n</blockquote>\n</details>\n\n")

                latex = latex_map.get(row['id'], "Expression non trouvée")
                f.write(f"<details>\n<summary><b>Énoncé</b></summary>\n\n---\n\n{latex}\n\n---\n\n</details>\n\n")


if __name__ == "__main__":
    mise_a_jour()
