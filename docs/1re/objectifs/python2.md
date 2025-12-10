% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
subject: "Informatique 2e année"
```

# Programmation en Python 2

Les objectifs de l'évaluation [](#eval-python1-1re) sont considérés comme acquis.

## Général

- Connaître les modules tels que `math`, `random` et savoir les importer.
- Savoir utiliser une boucle `while`.
- Savoir lire et comprendre un programme.
- Savoir compléter un programme.
- Savoir écrire un programme à partir d'un énoncé.

## Fonctions

- Savoir **appeler** une fonction avec ou sans paramètres.
- Savoir **définir** une fonction avec ou sans paramètres.
- Savoir utiliser les différentes fonctions de dessin (cf. liste ci-dessous).

## Fonctions de dessin

Cette liste de fonctions sera à disposition pendant l'évaluation.

```{py:method} creation_image(largeur, hauteur, couleur)
:no-index:
Crée une image.
:arg largeur,hauteur: Les dimensions de l'image.
:arg couleur: La couleur de fond de l'image.
```

```{py:method} rectangle(x, y, largeur, hauteur, remplissage, bord="transparent")
:no-index:
Ajoute un rectangle sur l'image.
:arg x,y: L'origine du rectangle (sommet en haut à gauche).
:arg largeur,hauteur: Les dimensions du rectangle.
:arg remplissage: La couleur de remplissage du rectangle.
:arg bord: La couleur du bord du rectangle (par défaut transparent).
```

```{py:method} triangle(point_1, point_2, point_3, remplissage, bord="transparent")
:no-index:
Ajoute un triangle sur l'image.
:arg point_1,point_2,point_3: Les coordonnées des trois sommets sous la forme `(x1, y1)`.
:arg remplissage: La couleur de remplissage du triangle.
:arg bord: La couleur du bord du triangle (par défaut transparent).
```

```{py:method} cercle(x, y, r, remplissage, bord="transparent")
:no-index:
Ajoute un cercle sur l'image.
:arg x,y: Les coordonnées du centre du cercle.
:arg r: Le rayon du cercle.
:arg remplissage: La couleur de remplissage du cercle.
:arg bord: La couleur du bord du cercle (par défaut transparent).
```

```{py:method} ellipse(x, y, rx, ry, remplissage, bord="transparent")
:no-index:
Ajoute une ellipse sur l'image.
:arg x,y: Les coordonnées du centre de l'ellipse.
:arg rx,ry: Les rayons horizontaux et verticaux de l'ellipse.
:arg remplissage: La couleur de remplissage de l'ellipse.
:arg bord: La couleur du bord de l'ellipse (par défaut transparent).
```

```{py:method} ligne(x1, y1, x2, y2, couleur, epaisseur)
:no-index:
Ajoute une ligne sur l'image.
:arg x1,y1: Les coordonnées du début de la ligne.
:arg x2,y2: Les coordonnées de la fin de la ligne.
:arg couleur: La couleur de la ligne.
:arg epaisseur: L'épaisseur de la ligne.
```

```{py:method} texte(x, y, texte, couleur, taille)
:no-index:
Ajoute du texte sur l'image.
:arg x,y: Les coordonnées du début du texte (ligne de base).
:arg texte: Le texte à afficher.
:arg couleur: La couleur du texte.
:arg epaisseur: La taille des caractères en pixels (px).
```
