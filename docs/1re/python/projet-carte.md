% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Projet - Carte de voeux

Dans ce projet, vous allez créer un carte de voeux en utilisant les fonctions
prédéfinies dans la section [](fonctions-dessin.md), vos connaissances en Python
et votre imagination.

## Consignes

| Critères | Points |
| :------- | :----: |
|**Le dessin contient** | |
|un ou plusieurs motifs qui se répètent| **1 pt**|
|au moins un motif répété avec des nuances (changement de couleur, de taille, etc.) effectués au moyen de paramètres| **1 pt**|
|au moins une forme avec une bordure | **0.5 pt** |
|des couleurs personnalisées |**0.5 pt** |
|des variables avec des noms appropriés| **1 pt** |
|des fonctions avec/sans paramètres| **3 pts** |
|des boucles pour éviter les répétitions| **2 pts**|
|des instructions conditionnelles| **2 pts** |
|au moins une interaction avec l'utilisateur| **2 pts**|
|**Le code doit être**|
|organisé correctement (import, définitions de fonction, programme principal) | **1 pt**|
|modulaire (décomposition en fonctions avec/sans paramètres) | **2 pts** |
|commenté | **1 pt**|
|fonctionnel (sans bogue majeur)| **1 pt**|
|**Fonctionnalités additionnelles** | |
|une partie aléatoire (fonction `randint` du module `random`)| **2 pts** |
|un élément animé (déplacement, clignotement, etc.)| **2 pts** |
| Le dessin est dans le thème, suffisamment complexe et original | **3 pts** |
|**Total** | **25 pts** |

```{exec} python
:name: fonctions_carte
:class: hidden
:when: never
from tdoc import svg

def creation_image(largeur, hauteur, couleur):
  global img
  img = svg.Image(largeur, hauteur, stroke='black', style='width: 100%; height: 100%')
  rectangle(0, 0, largeur, hauteur, couleur)

def rectangle(x, y, largeur, hauteur, remplissage, bord="transparent"):
  img.rect(x, y, largeur, hauteur, stroke=bord, fill=remplissage)

def triangle(point_1, point_2, point_3, remplissage, bord="transparent"):
  img.polygon(point_1, point_2, point_3, stroke=bord, fill=remplissage)

def cercle(centre_x, centre_y, rayon, remplissage, bord="transparent"):
  img.circle(centre_x, centre_y, rayon, stroke=bord, fill=remplissage)

def ellipse(centre_x, centre_y, rayon_x, rayon_y, remplissage, bord="transparent"):
  img.ellipse(centre_x, centre_y, rayon_x, rayon_y, stroke=bord, fill=remplissage)

def ligne(x1, y1, x2, y2, couleur, epaisseur):
  img.line(x1, y1, x2, y2, stroke=svg.Stroke(couleur, width=epaisseur))

def texte(x, y, texte, couleur, taille):
  font = f"font: bold italic {taille}px serif"
  img.text(x, y, texte, stroke='transparent', fill=couleur, style=font)
```

```{exec} python
:name: rendu
:class: hidden
:when: never

# Affiche l'image
render(img)
```

````{solution}
```{exec} python
:after: fonctions_carte
:then: rendu
:class: hidden
:when: load
from tdoc import svg
from math import sqrt
from random import randint

def triangle_isocele(pos_x, pos_y, base, hauteur, couleur_remplissage, couleur_bordure="transparent"):
  triangle((pos_x, pos_y), (pos_x + base, pos_y), (pos_x + base / 2, pos_y - hauteur), couleur_remplissage, couleur_bordure)


def sapin(pos_x, pos_y, base, hauteur, larg_tronc, couleur):
  n_triangles = randint(3, 5)
  x = pos_x
  y = pos_y
  hauteur_tronc = 1.5 * larg_tronc
  rectangle(x, y, larg_tronc, hauteur_tronc, "brown")
  x = pos_x  - 0.5 * (base - larg_tronc)
  for _ in range(n_triangles):
    triangle_isocele(x, y, base, hauteur, couleur)
    y -= 0.4 * hauteur

def etoile(longueur, couleur):
  pos_x = randint(0, 560)
  pos_y = randint(20, 150)
  triangle((pos_x, pos_y), (pos_x + longueur, pos_y), (pos_x + longueur / 2, pos_y - longueur / sqrt(2)), couleur, couleur)
  triangle((pos_x, pos_y - longueur / 2), (pos_x + longueur, pos_y - longueur / 2 ), (pos_x + longueur / 2, pos_y - longueur / 2 + longueur / sqrt(2)), couleur, couleur)

def cadeau(pos_x, pos_y, longueur, hauteur, couleur, couleur_ruban):
  rectangle(pos_x, pos_y, longueur, hauteur, couleur, couleur)
  ligne(pos_x, pos_y + hauteur/2, pos_x + longueur, pos_y + hauteur/2, couleur_ruban, 5)
  ligne(pos_x + longueur/2, pos_y, pos_x + longueur/2, pos_y + hauteur, couleur_ruban, 5)

def bonhomme(pos_x, pos_y, rayon):
  ellipse(pos_x+rayon+20, pos_y+rayon, rayon*1.5, rayon/2, "gray", "gray")
  ellipse(pos_x+rayon+20+1.5*rayon*1.5+10, pos_y+rayon, 2/3*rayon*1.5, 2/3*rayon/2, "gray", "gray")
  cercle(pos_x, pos_y, rayon, "white", "white")
  r = 2/3*rayon
  cercle(pos_x, pos_y - (rayon + r), r, "white", "white")

def guirlande(position_x, position_y, rayon):
  for i in range(6):
    ligne(position_x, position_y, position_x + 50, position_y + 25, "black", 4)
    ligne(position_x + 50, position_y + 25, position_x + 100, position_y, "black", 4)
    if i % 2 == 0:
      couleur = "red"
    else:
      couleur = "green"
    cercle(position_x + 50, position_y + 25 + rayon, rayon, couleur)
    position_x += 100

# Create the image.
creation_image(600, 400, "#7dcbf0")

for i in range(12):
  etoile(30, "yellow")
sapin(100, 200, 100, 60, 20, "#16401E")
sapin(200, 250, 120, 70, 20, "#1E9C38")
sapin(50, 230, 80, 40, 10, "green")
sapin(140, 260, 80, 40, 10, "#26C946")
cadeau(430, 120, 100, 70, "pink", "violet")
cadeau(410, 160, 60, 40, "orange", "red")
cadeau(510, 170, 50, 35, "#2367CF", "#6E23CF")
bonhomme(350, 300, 50)
guirlande(0, 20, 10)

texte(50, 310, "Joyeux Noël", "blue", "40")
texte(130, 350, "et", "blue", "40")
texte(30, 390, "Bonne année!", "blue", "40")
```
````

## Développement et rendu du projet

```{exec} python
:after: fonctions_carte
:then: rendu
:editor: 5139828d-3e35-495e-bae3-9c95e5dcb1fe
# Écrivez le programme ici
```



%````{solution}
%```{exec} python
%:after: fonctions_carte
%:then: rendu
%:when: load
%:class: hidden
%from tdoc import svg
%from math import sqrt
%
%def noeud(pos_x, pos_y, longueur, hauteur, couleur, couleur_ruban):
%  r = longueur/50
%  img.circle(pos_x + longueur/2, pos_y, r, fill=couleur_ruban, stroke=couleur_ruban)
%  img.line(pos_x + longueur/2, pos_y, pos_x + longueur/2 - longueur/5, pos_y + longueur/5, stroke=svg.Stroke(couleur_ruban, width=longueur/20))
%  img.line(pos_x + longueur/2, pos_y, pos_x + longueur/2 + longueur/5, pos_y + longueur/5, stroke=svg.Stroke(couleur_ruban, width=longueur/20))
%  img.ellipse(pos_x + longueur/2, pos_y, hauteur/10, longueur/10, stroke=svg.Stroke(couleur_ruban, width=longueur/20), fill='transparent',
%  transform=svg.translate(0, -longueur/10).rotate(-50, pos_x + longueur/2, pos_y).translate(-hauteur/12,-longueur/12))
%  img.ellipse(pos_x + longueur/2, pos_y, hauteur/10, longueur/10, stroke=svg.Stroke(couleur_ruban, width=longueur/20), fill='transparent',
%  transform=svg.translate(0, -longueur/10).rotate(50, pos_x + longueur/2, pos_y).translate(hauteur/12,-longueur/12))
%
%def cadeau(pos_x, pos_y, longueur, hauteur, couleur, couleur_ruban):
%  img.rect(pos_x, pos_y, longueur, hauteur, fill=couleur)
%  img.line(pos_x, pos_y + hauteur/2, pos_x + longueur, pos_y + hauteur/2, stroke=svg.Stroke(couleur_ruban, width=longueur/20))
%  img.line(pos_x + longueur/2, pos_y, pos_x + longueur/2, pos_y + hauteur, stroke=svg.Stroke(couleur_ruban, width=longueur/20))
%  noeud(pos_x, pos_y, longueur, hauteur, couleur, couleur_ruban)
%
%# Create the image.
%creation_image(300, 200, "#7dcbf0")
%
%cadeau(150, 75, 100, 70, "pink", "violet")
%cadeau(100, 120, 60, 40, "orange", "red")
%cadeau(230, 130, 50, 35, "#2367CF", "#6E23CF")
%```
%````

%````{solution}
%```{exec} python
%:after: fonctions_carte
%:then: rendu
%:when: load
%:class: hidden
%from tdoc import svg
%
%def maison(x, y):
%  rectangle(x, y, 150, 150, "gray", "black")
%  triangle((x, y), (x+150, y), (x+80, y-100), "brown")
%
%creation_image(600, 400, "#f0ffffff")
%
%x = 0
%while True:
%  maison(x, 200)
%  render(img)
%  creation_image(600, 400, "#f0ffffff")
%  x += 10
%  sleep(1)
%````
