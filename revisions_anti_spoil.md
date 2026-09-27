# Révisions - Anti-Spoil

Voici comment créer des sections "anti-spoil" en Markdown pour tes révisions en utilisant les balises HTML `<details>` et `<summary>`.

## 1. Exemple simple (Question/Réponse)

<details>
  <summary>Clique ici pour voir la capitale de la France</summary>
  La réponse est **Paris**.
</details>

## 2. Exemple avec du code ou des listes

<details>
  <summary>Comment inverser une liste en Python ?</summary>

Tu peux utiliser la méthode `.reverse()` ou le slicing :

```python
ma_liste = [1, 2, 3]
print(ma_liste[::-1]) # [3, 2, 1]
```

</details>

## 3. Plusieurs questions à la suite

<details>
  <summary>Question 1 : Quelle est la formule de la relativité ?</summary>
  $$E = mc^2$$
</details>

<details>
  <summary>Question 2 : Qui a découvert la pénicilline ?</summary>
  C'est **Alexander Fleming**.
</details>

---

_Note : Ces balises fonctionnent parfaitement dans l'aperçu Markdown de VS Code (Cmd+Shift+V) et sur GitHub._
