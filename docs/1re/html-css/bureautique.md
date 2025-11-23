% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{role} html(code)
:language: html
```

# Traitement de texte

Dans ce chapitre, nous avons appris que le HTML permet de décrire le contenu et
la structure d'une page Web et que le CSS permet de mettre en forme le document
HTML.

Dans cette partie, nous allons faire le lien entre le HTML-CSS et l'utilisation
d'un logiciel de traitement de texte.

Voici les éléments principaux d'un texte:

| Document texte       | Document HTML       |
| :------------------: | :-----------------: |
| titre                | `<h1>`              |
| sous-titre           | `<h2>`, `<h3>`, ... |
| paragraphe           | `<p>`               |
| liste numérotée      | `<ol><li>`          |
| liste à puces        | `<ul><li>`          |
| hyperlien            | `<a href=...>`      |
| image                | `<img src=...>`     |

Un logiciel de traitement de texte n'a pas de fichier CSS, mais il y des styles
qui permet de styliser tous ces éléments de la même manière que le faut le
fichier CSS.

## Exercice {num2}`exercice`

But: Mettre en forme un document texte avec des styles.

1. Téléchargez le [`document sans les styles`](document-sans-styles.docx).
2. Ouvrez-le document, activez les modifications et sauvegardez le document en
sélectionnant `Enregistrer sous` et en suivant les instructions données
par l'enseignant(e) pour le nom du fichier et l'emplacement de la sauvegarde.

Voici la page Web du document, vous devez mettre en forme le document Word **en
utilisant les styles** en suivant les indications suivantes:

```{exec} html
:when: load
:class: hidden
:include: bureautique.html
```

% Forcer Sphinx à copier l'image.
![image](images/bureautique.png){.hidden}

3. Titres et les sous-titres
    Le type de police de caractères de tous les titres et sous-titres soit être
    "Arial".

    - Le titre `<h1>` doit être en gras et centré. De plus, il faut ajouter un
      espace d'au moins 12 pt après.
    - Les sous-titres `<h2>` doit être en gras De plus, il faut ajouter un
      espace d'au moins 12 pt avant.
    - Les sous-titres `<h3>` peuvent conserver le formatage standard, mais en
      "Arial".

4. Paragraphes

    - Pour le premier paragraphe, créez un nouveau style `Intro` dont le texte
      est en italique.
    - Les autres paragraphes peuvent conserver le formatage standard.

5. Listes

    - La première liste est numérotée.
    - La deuxième liste est une liste à puces.

6. Image

    - Modifiez sa taille.
    - Elle doit être centrée par rapport au texte.

7. Hyperlien

    - L'apparence doit être la même que sur la page Web.

Vérifiez que les paragraphes ne sont pas coupés par un passage à la page
suivante, sinon ajoutez un saut de page.




