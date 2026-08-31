% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Python 2

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Attention au soin.**
```
---

## Question {nump}`question`{points}`2`

Qu'affiche le programme suivant?

```{exec} python
:when:
n = 4
while n < 9:
  n += 2
  print(n)
```

{vspace}`4.5lh`


````{solution}
0.5 pt: print dans la boucle / 0.5 pt: saut de 2 / 1 pt: tout correct
```{exec} python
n = 4
while n < 9:
  n += 2
  print(n)
```
````

## Question {nump}`question`{points}`4`

Écrivez un programme qui fait le décompte des secondes avant le départ d'une
course. Le décompte débute à 5. Votre programme doit contenir une boucle `while`
et une instruction conditionnelle et doit afficher exactement le résultat
suivant:

```{code} text
5
4
3
2
1 Prêts
Partez!
```

````{solution}
0.5 pt: initialisation / 2 pts: while (condition + décrémentation) /  1 pt: if-else / 0.5 pt: print
```{exec} python
decompte = 5
while decompte > 0:
  if decompte > 1:
    print(decompte)
  else:
    print(decompte, "Prêts")
  decompte -= 1
print("Partez!")
```
````

## Question {nump}`question`{points}`4`

Qu'affiche le programme suivant?

```{exec} python
:when:
def mystere_1(nombre):
  if nombre <= 4:
    print("bleu")
  else:
    print("jaune")

def mystere_2(nombre):
  if nombre > 3:
    print("rose")
  if nombre > 2:
    print("vert")
  else:
    print("rouge")

mystere_1(6)
mystere_1(3)
mystere_2(6)
mystere_2(1)
```

{vspace}`9lh`

````{solution}
1 pt: par appel de fonction
```{exec} python
def mystere_1(nombre):
  if nombre <= 4:
    print("bleu")
  else:
    print("jaune")

def mystere_2(nombre):
  if nombre > 3:
    print("rose")
  if nombre > 2:
    print("vert")
  else:
    print("rouge")

mystere_1(6)
mystere_1(3)
mystere_2(6)
mystere_2(1)
```
````

## Question {nump}`question`{points}`3`

Complétez le programme suivant uniquement où il y a les .......... pour qu'il
calcule l'aire d'un carré de côté 10.

```{exec} python
:when:
def aire_carre(.................):
  aire = cote ..... 2
  print(aire)

................. = 10

aire_carre(base)
```

````{solution}
1 pt: par réponse
```{exec} python
:when:
def aire_carre(cote):
  aire = cote ** 2
  print(aire)

base = 10

aire_carre(base)
```
````

## Question {nump}`question`{points}`4`

Écrivez la partie du programme qui permet de dessiner les 10 disques rouges
suivants sans répétition de code. Ne pas s'occuper de la création de l'image.

```{figure} images/cercles.png
:width: 80%
```

{vspace}`5lh`

````{solution}
1 pt: dessin d'un cercle / 1 pt: x / 1 pt: boucle for / 1 pt: résultat correct
```{exec} python
:when:
x = 30
for _ in range(10):
  cercle(x, 200, 30, "red")
  x += 60
```
````

## Question {nump}`question`{points}`8`

Définissez une fonction `maison` avec les paramètres nécessaires qui permet de
reproduire le dessin suivant. Appelez la fonction pour que le dessin s'affiche
comme ci-dessous.

```{figure} images/maison.png
:width: 80%
```

````{solution}
1 pt: rectangle / 1 pt: triangle / 1 pt: définition de la fct / 1 pt: paramètres
x et y / 1 pt: paramètre couleur / 1 pt: pour l'utilisation des paramètres /
1 pt: appels de la fonction / 1 pt: dessin correct

```{exec} python
:when:
def maison(x, y, couleur):
  rectangle(x, y, 100, 100, couleur)
  triangle((x, y), (x + 100, y), (x + 50, y - 50), couleur, "black")

# programme principal
creation_image(600, 400, "white")

# Ajoute des éléments à l'image
maison(100, 200, "green")
maison(250, 150, "yellow")
maison(400, 250, "blue")
```
````

