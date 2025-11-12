% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Fonctions - dessin

Python peut être utilisé pour faire des dessins.

## Fonctions à disposition

```{exec} python
:name: fonctions_dessin_svg
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

Voici la définition de fonctions de base pour dessiner des rectangles, des
triangles, des cercles, des lignes, etc.

```{py:method} creation_image(largeur, hauteur, couleur)
Crée une image.
:arg largeur,hauteur: Les dimensions de l'image.
:arg couleur: La couleur de fond de l'image.
```

```{py:method} rectangle(x, y, largeur, hauteur, remplissage, bord="transparent")
Ajoute un rectangle sur l'image.
:arg x,y: L'origine du rectangle (sommet en haut à gauche).
:arg largeur,hauteur: Les dimensions du rectangle.
:arg remplissage: La couleur de remplissage du rectangle.
:arg bord: La couleur du bord du rectangle (par défaut transparent).
```

```{py:method} triangle(point_1, point_2, point_3, remplissage, bord="transparent")
Ajoute un triangle sur l'image.
:arg point_1,point_2,point_3: Les coordonnées des trois sommets sous la forme `(x1, y1)`.
:arg remplissage: La couleur de remplissage du triangle.
:arg bord: La couleur du bord du triangle (par défaut transparent).
```

```{py:method} cercle(x, y, r, remplissage, bord="transparent")
Ajoute un cercle sur l'image.
:arg x,y: Les coordonnées du centre du cercle.
:arg r: Le rayon du cercle.
:arg remplissage: La couleur de remplissage du cercle.
:arg bord: La couleur du bord du cercle (par défaut transparent).
```

```{py:method} ellipse(x, y, rx, ry, remplissage, bord="transparent")
Ajoute une ellipse sur l'image.
:arg x,y: Les coordonnées du centre de l'ellipse.
:arg rx,ry: Les rayons horizontaux et verticaux de l'ellipse.
:arg remplissage: La couleur de remplissage de l'ellipse.
:arg bord: La couleur du bord de l'ellipse (par défaut transparent).
```

```{py:method} ligne(x1, y1, x2, y2, couleur, epaisseur)
Ajoute une ligne sur l'image.
:arg x1,y1: Les coordonnées du début de la ligne.
:arg x2,y2: Les coordonnées de la fin de la ligne.
:arg couleur: La couleur de la ligne.
:arg epaisseur: L'épaisseur de la ligne.
```

```{py:method} texte(x, y, texte, couleur, taille)
Ajoute du texte sur l'image.
:arg x,y: Les coordonnées du début du texte (ligne de base).
:arg texte: Le texte à afficher.
:arg couleur: La couleur du texte.
:arg epaisseur: La taille des caractères en pixels (px).
```

## Exercice {num2}`exercice`

````{tab-set}
:sync-group: etape
```{tab-item} Étape 1
:sync: etape1
Changez la couleur:
  1. du fond de l'image,
  2. de la maison,
  3. du toit.

Il existe une liste de couleurs de base définies: "black", "white", "blue",
"red", "yellow", "green", gray", etc.

Pour avoir un plus grand choix, utilisez la valeur hexadécimale, par exemple
"#AFEEEE" pour du turquoise pale.
[Liste des couleurs](https://www.rapidtables.com/web/color/RGB_Color.html)
```
```{tab-item} Étape 2
:sync: etape2
Ajoutez du gazon devant la maison (rectangle) et un soleil (cercle).
```
```{tab-item} Étape 3
:sync: etape3
Ajoutez une porte et une fenêtre à la maison. Cet ajout doit se faire dans la
fonction `maison`.
```
```{tab-item} Étape 4
:sync: etape4
Ajoutez une cheminée et de la fumée.\
Pour la fumée, créez une fonction `fumee` qui demande à l'utilisateur le nombre
de nuages de fumée (entre 1 et 4).

Vérifiez que l'utilisateur a bien donné une réponse entre 1 et 4.

L'ordre de dessin des éléments a de l'importance.
```
```{tab-item} Étape 5
:sync: etape5
Ajoutez un texte sur l'image.
```
```{tab-item} Étape 6
:sync: etape6
Ajoutez un pommier en définissant une nouvelle fonction `pommier`.

Ajoutez 5 pommes sur l'arbre qui apparaissent de manière aléatoire sur le
pommier à chaque exécution.

```
```{tab-item} Étape 7
:sync: etape7
Ajoutez une barrière en définissant une nouvelle fonction `barriere`.

- Évitez les répétitions en utilisant une boucle.
- Utilisez des paramètres pour pouvoir modifier:
    - son emplacement
    - sa longueur
    - sa couleur
```
````



```{exec} python
:name: maison_exercice
:after: fonctions_dessin_svg
:then: rendu
:editor: a72b3183-cb55-400c-8016-4317ee41ace5
# définition des fonctions
def maison():
  rectangle(100, 200, 150, 150, "#F7E4E1", "black")
  triangle((80, 200), (270, 200), (175, 100), "brown")

# programme principal
creation_image(600, 400, "#CCFFFF")

# Ajoute des éléments à l'image
maison()
```

````{solution}
```{exec} python
:name: maison_solution
:after: fonctions_dessin_svg
:then: rendu
:when: load
# imports
from random import randint

# définition des fonctions
# Cette fonction affiche ou non les pommes de manière aléatoire
def pommes():
  if randint(0,1) == 0:
    cercle(360, 200, 10, "red")
  if randint(0,1) == 0:
    cercle(420, 190, 10, "red")
  if randint(0,1) == 0:
    cercle(400, 220, 10, "red")
  if randint(0,1) == 0:
    cercle(370, 250, 10, "red")
  if randint(0,1) == 0:
    cercle(410, 260, 10, "red")

def pommier():
  taille = 120
  x = 370
  y = 220
  larg_tronc = taille/3
  rayon = taille * 1/2
  # tronc
  rectangle(x, y, larg_tronc, taille, "#8B4513")
  # feuilles
  cercle(x + larg_tronc/2, y, rayon, "#228B22" )
  pommes()

def barriere(x, y, longueur, couleur):
  # les deux barres horizontales
  rectangle(x, y, longueur, 10, couleur)
  rectangle(x, y+25, longueur, 10, couleur)
  # les barres horizontales
  poteau_x = x + 10
  while poteau_x < x + longueur - 10:
    rectangle(poteau_x, y-10, 15, 65, couleur)
    poteau_x += 20

def fumee():
  # demande un nombre à l'utilisateur et vérifie que la valeur est ok
  n = int(input("Nombre de nuages de fumée (entre 1 et 4)?"))
  while n < 1 or n > 4:
    n = int(input("Nombre de nuages de fumée (entre 1 et 4)?"))
  # position du nuage de fumée
  x = 220
  y = 100
  # dimension du nuage de fumée
  rx = 10
  ry = 5
  for i in range(n):
    ellipse(x, y, rx, ry, "white")
    # le nuage se déplace vers la droite et vers le haut
    x += 10
    y -= 20
    # le nuage grossit
    rx += 4
    ry += 2

def cheminee():
  rectangle(200, 110, 20, 40, "gray")
  fumee()

def maison():
  rectangle(100, 200, 150, 150, "#E8AF35")
  # toit
  cheminee()
  triangle((80, 200), (270, 200), (175, 100), "silver")
  # porte
  rectangle(120, 280, 50, 70, "#FF4500")
  # fenêtres
  rectangle(190, 280, 40, 40, "white", "black")
  rectangle(125, 220, 40, 40, "white", "black")
  rectangle(190, 220, 40, 40, "white", "black")


# programme principal
creation_image(600,400, "#DAF5F3")

# Ajoute des éléments à l'image
# soleil
cercle(530, 70, 50, "yellow")
# gazon
rectangle(0, 300, 600, 150, "#006400")
maison()
texte(140, 190, "Bienvenue", "black", 15)
barriere(300, 250, 250, "#8B0000")
barriere(10, 250, 80, "#8B4513")
pommier()
```
