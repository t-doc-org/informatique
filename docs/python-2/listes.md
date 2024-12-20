% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Listes

```{metadata}
hide-solutions: true
```

En Python, une liste est une variable dans laquelle il est possible de stocker
plusieurs valeurs (de types différents).

```{code-block} text
matieres = [ "français", "informatique", "allemand"]
notes = [5.7, 4.3, 5.1]
eleves = ["2F4", "Économie et droit", 5.0, 2007]
```

La liste `matieres` ne contient que des éléments de type `str`. La liste `notes`
ne contient que des éléments de type `float`. Mais la liste `eleves` contient
des éléments de types différents 'str', 'float' et 'int'.

## Création d'une liste

Une liste est déclarée par une suite de valeurs, séparées par des virgules et
le tout encadré par des crochets.

### Exemple {num}`ex-py2`

```{exec} python
:editor:
matieres = [ "français", "informatique", "allemand"]
notes = [5.7, 4.3, 5.1]
eleves = ["2F4", "Économie et droit", 5.0, 2007]
print(matieres)
print(notes)
print(eleves)
```

```{tip}
Pour écrire des crochets sur :

Windows
: `[` {kbd}`AltGr`+ {kbd}`è` ou `]` {kbd}`AltGr`+ {kbd}`!`

Mac
: `[` {kbd}`Option`+ {kbd}`5` ou `]` {kbd}`Option`+ {kbd}`6`
```

Il est aussi possible de créer une liste vide. Il suffit d'écrire les deux
crochets sans rien à l'intérieur.

```{exec} python
:linenos:
:when: never
liste_vide = []
```

### Exercice {num}`exo-py2`

1. Créer les listes suivantes en Python :
    - Les salles de classe dans lesquelles tu as des cours
    - Les années de naissance des membres de ta famille
    - La taille en mètres de tes amis

2. Afficher les trois listes.

```{exec} python
:editor: bda26e73-b3dc-4d27-807c-e90f97d2ea25
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
# Créations des listes
salles = ["P207", "G107", "P214", "P-107"]
annees_naissance = [1941, 1966, 1974, 1975, 1978, 2006]
tailles = [1.8, 1.9, 1.96]

#Affichage des listes
print(salles)
print(annees_naissance)
print(tailles)
```
````

## Accès à un élément d'une liste: indexation

Un `index`est attribué automatiquement à chaque élément d'une liste et
correspond à sa position dans la liste en partant de 0 depuis la gauche.

```{exec} python
:linenos:
:when: never
notes = [5.5, 4.8, 6.0, 6.0, 3.5, 4.5]
```

| notes | 5.5   | 4.8   | 6.0   | 6.0   | 3.5   | 4.5   |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| index | **0** | **1** | **2** | **3** | **4** | **5** |

```{important}
Le premier élément d'une liste est toujours à l'**index 0**.
Dans une liste de n élément, le dernier élément sera à l'**index n-1**.
```

L'accès à un élément donné d'une liste se fait grâce à l'indexation :
`liste[index]`

```{exec} python
:editor:
coureurs = ["Bolt", "Powell", "Gatlin", "Montgommery", "Lewis"]
premier = coureurs[0]
print("En 1ère place:", premier)
print("En dernière place:", coureurs[4])
coureurs[3] = "Burrell"
print("La liste d'arrivée des coureurs est:", coureurs)
```

### Exercice {num}`exo-py2`

Ajouter les instructions nécessaires pour que l'affichage de la liste soit le
suivant :

```{code-block} text
['B', 'B', 'W', 'D', 'E', 'X']
```

```{exec} python
:editor: b0091579-35b5-41d7-9316-81f642ff24c0
lettres = ["A", "B", "C", "D", "E", "F"]
# ajouter le code ici
print(lettres)
```

````{solution}
```{exec} python
:linenos:
lettres = ["A", "B", "C", "D", "E", "F"]
# modification de la première lettre
lettres[0] = "B"
# modification de la troisième lettre
lettres[2] = "W"
# modification de la sixième lettre
lettres[5] = "X"
print(lettres)
```
````

## Fonctions sur les listes

En Python, il existe beaucoup de fonctions prédéfinies qui permettent de
manipuler les listes. Nous en avons vu déjà rencontrées certaines dans
[](listes-lab2.md).

len(ma_liste)
: retourne le nombre d'éléments de  la liste

ma_liste.apppend(mon_element)
: ajoute `mon_element` à la fin de `ma_liste`

ma_liste.insert(index, mon_element)
: ajoute `mon_element` à l'`index` spécifié

ma_liste.remove(mon_element)
: efface la première occurence de `mon_element`

del ma_liste[index]
: supprime l'élément de `ma_liste` qui se trouve à l'`index` spécifié

ma_liste.index(mon_element)
: retourne l'index de la première occurance de `mon_element`

sum(ma_liste)
: retourne la somme de tous les éléments de la liste

ma_liste.sort()
: trie la liste par ordre croissant

ma_liste.reverse()
: inverse l'ordre des éléments

ma_liste.count(mon_element)
: retourne le nombre d'apparition de `mon_element` dans `ma_liste`


### Exercice {num}`exo-py2`

1.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    print(liste[4])
    ```

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Que va afficher ce programme? ")
      if resp.replace(" ", "") == "7": break
      print("\x0cLe premier élément se trouve à l'index 0.")
    print("\x0cBravo!")
    ```

2.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste[5] = 6
    print(liste)
    ```

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Que va afficher ce programme? ")
      if resp.replace(" ", "") == "[1,5,4,12,7,6,10,2]": break
      print("\x0cLe premier élément se trouve à l'index 0.")
    print("\x0cBravo!")
    ```

3.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste.remove(5)
    print(liste)
    ```

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Que va afficher ce programme? ")
      if resp.replace(" ", "") == "[1,4,12,7,6,10,2]": break
      print("\x0cLa fonction remove(element) efface la première occurecce de l'élément donné entre parenthèse.")
    print("\x0cBravo!")
    ```

4.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste.sort()
    print(liste)
    ```

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Que va afficher ce programme? ")
      if resp.replace(" ", "") == "[1,2,4,5,7,9,10,12]": break
      print("\x0cLa fonction sort() trie les éléments par ordre croissant.")
    print("\x0cBravo!")
    ```

5.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    del liste[2]
    print(liste)
    ```

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Que va afficher ce programme? ")
      if resp.replace(" ", "") == "[1,5,12,7,9,10,2]": break
      print("\x0cdel efface l'élément donné.")
    print("\x0cBravo!")
    ```

5.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste.insert(1, 6)
    print(liste)
    ```

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Que va afficher ce programme? ")
      if resp.replace(" ", "") == "[1,6,5,4,12,7,9,10,2]": break
      print("\x0cLa fonction insert(1, 6) insère l'élément 6 à l'index 1.")
    print("\x0cBravo!")
    ```

### Exercice {num}`exo-py2`

1. Créer une liste, nommée `sports` avec les éléments suivants: `kayak`,
`escrime` et `escalade`.
2. Afficher la liste et son nombre d'éléments.
3. Demander cinq sports à l'utilisateur et les ajouter à la liste `sports`.
4. Afficher la liste et son nombre d'éléments.
5. Ajouter l'élément `tennis de table` à l'index 3.
6. Afficher la liste et son nombre d'éléments.
7. Effacer l'élément `escalade`.
8. Afficher la liste et son nombre d'éléments.
9. Quel est l'index d'`escrime`? Afficher l'index d'`escrime`.
10. Effacer le cinquième élément de la liste.
11. Afficher la liste et son nombre d'éléments.

```{exec} python
:editor: f9da8abf-19a5-4eba-aafd-b21e58273901
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
sports = ["kayak", "escrime", "escalade"]
print(sports, len(sports))
for _ in range(5):
  sport = await input_line("Entrer un sport: ")
  sports.append(sport)
print(sports, len(sports))
sports.insert(3, "tennis de table")
print(sports, len(sports))
sports.remove("escalade")
print(sports, len(sports))
print(sports.index("escrime"))
del sports[4]
print(sports, len(sports))
```
````

### Exercice {num}`exo-py2`

1. Demander à l'utilisateur d'entrer 6 nombres et les stocker dans la liste
'nombres'.
2. Afficher la liste.
3. Trier la liste.
4. Afficher la liste.
5. Inverser l'ordre des éléments.
6. Afficher la somme des éléments.

```{exec} python
:editor: 1d0149fa-92a5-4cd1-8984-1b83ed61054d
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
nombres = []
for _ in range(5):
  n = float(await input_line("Entrer un nombre: "))
  nombres.append(n)
print(nombres, len(nombres))
nombres.sort()
print(nombres, len(nombres))
nombres.reverse()
print(nombres, len(nombres))
print(sum(nombres))
```
````

### Exercice {num}`exo-py2`

Sans exécuter le code, répondre aux questions suivantes:
1. Que va retourner `nombres.index(5)`?
2. Que va retourner `nombres.index(3)`?
2. Que va retourner `nombres.count(1)`?
3. Quelle sera la liste après l'instruction `nombres.remove(4)`?
4. Quelle sera la liste après l'instruction `nombres.reverse()`?
5. Quelle sera la liste après l'instruction `nombres.sort()?


```{exec} python
:editor: 5e39f143-2a7d-4e04-a373-81b744d6015c
# Compléter le code pour tester vos réponses
nombres = [1, 4, 2, 1, 5, 7, 3, 1, 4, 5, 3, 1, 3, 1, 2, 5]
```

````{solution}
```{exec} python
:linenos:
nombres = [1, 4, 2, 1, 5, 7, 3, 1, 4, 5, 3, 1, 3, 1, 2, 5]
print(nombres.index(5))
print(nombres.index(3))
print(nombres.count(1))
nombres.remove(4)
print(nombres)
nombres.reverse()
print(nombres)
nombres.sort()
print(nombres)
```
````

### Exercice {num}`exo-py2`

Dans le programme suivant, les ingrédients d'une pizza devraient pouvoir être
ajoutés petit à petit par l'utilisateur dans la liste `ingredients` qui contient
la sauce tomate et la mozzarella comme base. Cet ajout se termine lorsque
l'utilisateur écrit le texte "stop", puis tous les ingrédients sont affichés.

ATTENTION: le mot stop ne doit jamais entrer dans la liste des ingrédients!

Compléter le programme de manière que celui-ci corresponde à cette description.

```{exec} python
:editor: 88e9572e-051f-4e67-8244-06e475aa0133
ingredients = ["sauce tomate", "mozzarella"]
choix = await input_line("Ajouter un ingrédient: ")

while choix != "stop":
  # à compléter

print(ingredients)
```

````{solution}
```{exec} python
:linenos:
ingredients = ["sauce tomate", "mozzarella"]
choix = await input_line("Ajouter un ingrédient: ")

while choix != "stop":
  ingredients.append(choix)
  choix = await input_line("Ajouter un ingrédient: ")

print(ingredients)
```
````

### Exercice {num}`exo-py2`

Une liste nommée meteo_semaine doit contenir les prévisions météos pour les 7
jours d'une semaine. Cette liste doit contenir 7 éléments, chacun étant un texte
de prévision météorologique pour un jour différent.

Ces textes ont tous le format suivant:

"JOUR_DE_LA_SEMAINE il fera TEMPERATURE °C" où JOUR_DE_LA_SEMAINE et PREVISION
sont remplacés par de vraies valeurs. Par exemple, pour un mardi à 13°C, le
texte de prévision serait "Mardi il fera 13 °C".

Afin de simplifier la création de cette liste, compléter la fonction
`ajoute_prevision` afin que celle-ci ajoute la prévision correcte à la liste
donnée en paramètre en fonction des paramètres du jour et de la température.

```{exec} python
:editor: 14a7fcdd-ed8e-4a60-97ba-6306e81a969f
def ajoute_prevision(liste_prevision, jour_de_la_semaine, temperature):
  # à compléter

meteo_semaine = []

# ajout des prévision
ajoute_prevision(meteo_semaine, "Lundi", "12")
ajoute_prevision(meteo_semaine, "Mardi", "15")
ajoute_prevision(meteo_semaine, "Mercredi", "14")
ajoute_prevision(meteo_semaine, "Jeudi", "14")
ajoute_prevision(meteo_semaine, "Vendredi", "12")
ajoute_prevision(meteo_semaine, "Samedi", "10")
ajoute_prevision(meteo_semaine, "Lundi", "8")

print(meteo_semaine)
```

````{solution}
```{exec} python
:linenos:
def ajoute_prevision(liste_previsions, jour_de_la_semaine, temperature):
    prevision = jour_de_la_semaine + " il fera " + temperature + " °C"
    liste_previsions.append(prevision)

meteo_semaine = []

ajoute_prevision(meteo_semaine, "Lundi", "12")
ajoute_prevision(meteo_semaine, "Mardi", "15")
ajoute_prevision(meteo_semaine, "Mercredi", "14")
ajoute_prevision(meteo_semaine, "Jeudi", "14")
ajoute_prevision(meteo_semaine, "Vendredi", "12")
ajoute_prevision(meteo_semaine, "Samedi", "10")
ajoute_prevision(meteo_semaine, "Lundi", "8")

print(meteo_semaine)
```
````

### Exercice {num}`exo-py2`

1. Écrire une programme qui génère une liste de 1000 nombres entiers tirés au
hasard entre 1 et 10.
2. Déterminer le nombre d'occurences de chaque nombre.

```{tip}
Dans le module `random`, la fonction `randint(a, b)` permet de généré des
nombres entiers aléatroires entre a (compris) et b (compris).

Ne pas oublier l'import: `from random import randint`
```

```{exec} python
:editor: b696c9ff-f357-4db6-b4e9-ff0d89d501c9
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
from random import randint

nombres = []

# Genère la liste de 50 nombres entiers
for _ in range(1000):
  nombres.append(randint(1, 10))

for i in range(1, 11):
  print("Nombre d'occurences de", i, ":", nombres.count(i))
```
````

## Élément appartenant à une liste

Il est possible de savoir si un élément appartient à une liste en utilisant
l'expression suivante `element in liste` qui revoie `True` si l'élément est dans
la liste et `False` sinon.

### Exemple {num}`ex-py2`

```{exec} python
:editor:
notes = [5, 5.5, 4, 5.5, 6]

note = 5

if note in notes:
    print(note, "est dans la liste")
else:
    print(note, "n'est pas dans la liste")
```

### Exercice {num}`exo-py2`

Le programme ci-dessous demande à l'utilisateur quel moyen de locomotion il u
tilise pour se rendre au travail et affiche un message en conséquence.

- "C'est très écologique!" lorsque l'utilisateur entre la valeur "à pied",
"trottinette", "skateboard", ou "vélo"
- "C'est un bon geste!" lorsque l'utilisateur entre la valeur "bus", "train", ou
"tram"
- "C'est acceptable!" s'il entre la valeur "voiture", "moto", "scooter",
"sidecar", ou "vespa".
- "Sans commentaire." s'il entre la valeur "avion"
- "Sans avis." s'il entre une autre valeur

Utilisez pour cela la notation `if ... in ...` quand cela est nécessaire.

```{exec} python
:editor: 21b10226-a456-4ab1-b04d-df9cef3aaf81
locomotion = await input_line("Quel moyen de locomotion utilises-tu pour te rendre au travail: ")

# Compléter le programme
print("C'est très écologique!")
print("C'est un bon geste!")
print("C'est acceptable!")
print("Sans commentaire.")
print("Sans avis.")
```

````{solution}
```{exec} python
:linenos:
locomotion = await input_line("Quel moyen de locomotion utilises-tu pour aller au travail: ")

if locomotion in ["à pied", "trottinette", "skateboard", "vélo"]:
    print("C'est très écologique!")
elif locomotion in ["bus", "train", "tram"]:
    print("C'est un bon geste!")
elif locomotion in ["voiture", "sidecar", "vespa", "moto", "scooter"]:
    print("C'est acceptable!")
elif locomotion == "avion":
    print("Sans commentaire.")
else:
    print("Sans avis.")
```
````

### Exercice {num}`exo-py2`

Depuis la station de métro où l'utilisateur se trouve, il peut se rendre aux
arrêts qui se trouvent dans la liste `ligne_sud` et `ligne_nord`. Lorsque
celui-ci entre sa destination, afficher s'il doit prendre la ligne sud, la
ligne nord, ou s'il ne peut pas se rendre à sa destination.

```{exec} python
:editor: e77565d0-b927-412b-b3e5-e6e7e8a00c72
destination = await input_line("Où veux-tu aller: ")
ligne_nord = ["Châtelet", "Opéra", "République", "Bastille"]
ligne_sud = ["Gare du Nord", "Gare de Lyon", "Saint-Michel Notre-Dame", "Auber", "Porte d'Italie"]

print("Prends la ligne nord.")
print("Prends la ligne sud.")
print("Tu ne peux pas te rendre à cet arrêt.")
```

````{solution}
```{exec} python
:linenos:
destination = await input_line("Où veux-tu aller: ")

ligne_nord = ["Châtelet", "Opéra", "République", "Bastille"]
ligne_sud = ["Gare du Nord", "Gare de Lyon", "Saint-Michel Notre-Dame",
             "Auber", "Porte d'Italie"]

if destination in ligne_nord:
    print("Prends la ligne nord.")
elif destination in ligne_sud:
    print("Prends la ligne sud.")
else:
    print("Tu ne peux pas te rendre à cet arrêt.")
```
````

### Exercice {num}`exo-py2`

Compléter le programme ci-dessous afin que l'utilisateur puisse petit à petit
créer une liste avec les codes postaux dans lesquels il souhaite se rendre.
Cette liste de code postal ne doit jamais contenir de doublons! Si l'utilisateur
essaie d'en entrer un, le programme affichera "Erreur, ce code postal est déjà
dans la liste" et continuera ensuite normalement. Le programme s'arrête quand
l'utilisateur entre un code postal négatif. À ce moment, la liste des codes
postaux est simplement affichée.

```{exec} python
:editor: 61ad2b94-75ec-449a-9bb9-a9f5691fe626
code_postaux = []

code_postal = int(await input_line("Entre un code postal: "))

print("Erreur, ce code postal est déjà dans la liste.")

print(code_postaux)
```

````{solution}
```{exec} python
:linenos:
code_postaux = []
code_postal = int(await input_line("Entre un code postal : "))
while code_postal >= 0:
    if code_postal in code_postaux:
        print("Erreur, ce code postal est déjà dans la liste.")
    elif code_postal >= 0:
        code_postaux.append(code_postal)
    code_postal = int(await input_line("Entre un code postal : "))

print(code_postaux)
```
````

## Boucles `for` avec les listes

La boucle `for` permet d'accéder à tous les éléments d'une liste l'un après
l'autre.

### Par position

Dans ce cas, les éléments sont parcourus au moyen de leur index. Pour déterminer
l'index du dernier élément et éviter une erreur lors de l'exécution, nous
utilisons la fonction 'len(liste)' qui retourne le nombre d'élément dans une
liste.

#### Exemple {num}`ex-py2`

```{exec} python
:editor:
notes = [5, 5.5, 4, 5.5, 6]

# Cette boucle parcourt tous les index de la liste de 0 à la longueur de la liste - 1
for i in range(len(notes)):
  print(notes[i])
```

### Par élément

En Python, il est possible de parcourir directement les éléments d'une liste.

#### Exemple {num}`ex-py2`

```{exec} python
:editor:
notes = [5, 5.5, 4, 5.5, 6]

# Cette boucle parcourt les éléments les uns après les autres
for note in notes:    # La variable note change de valeur à chaque itération
  print(note)
```

### Exercice {num}`exo-py2`

Avant de les exécuter, déterminer ce que font les programmes suivants.

1.  ```{exec} python
    :editor: 62c85fe3-5435-4c6e-8c68-c88763bc0f0e
    questions = ["Quelle est ta couleur préférée?",
                 "Quel est ton animal préféré?",
                 "Où étudies-tu?"]
    reponses = []

    for question in questions:
      print(question)
      reponse = await input_line("Réponse: ")
      reponses.append(reponse)

    print("Tes réponses: ", reponses)
    if reponses[2] == "STX":
      print("Tu es dans la meilleure école ;-)")
    ```

2.  ```{exec} python
    :editor: 7f08c47a-00a7-47f8-9ce1-305e46961f22
    notes = [5.5, 3.8, 6, 6, 3.5, 4,5]
    nb_notes_insuf = 0

    for note in notes:
      if note < 4:
        nb_notes_insuf += 1

    print("Tu as fait", nb_notes_insuf, "notes insuffisantes.")
    ```

### Exercice {num}`exo-py2`

1. Écrire une programme qui génère une liste de 50 nombres entiers tirés au
hasard entre 1 et 1000.
2. Déterminer le maximum de la liste en définissant une fonction
`maximum(liste)`.
3. Déterminer le minimum de la liste en définissant une fonction
`minimum(liste)`.

```{exec} python
:editor: 51fa6ba6-954c-4728-ab9a-b264c595416f
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
from random import randint

def maximum(listes_nombres):
  max = 0
  for nombre in listes_nombres:
    if nombre > max:
      max = nombre
  return max

def minimum(listes_nombres):
  min = 1000
  for nombre in listes_nombres:
    if nombre < min:
      min = nombre
  return min


nombres = []

# Genère la liste de 50 nombres entiers
for _ in range(50):
  nombres.append(randint(1, 1000))

print("Le maximum est", maximum(nombres))
print("Le minimum est", minimum(nombres))
print(nombres)

```
````

### Exercice {num}`exo-py2`

Compléter le programme ci-dessous afin qu'il affiche correctement l'itinéraire
de la manière suivante:

```{code-block} text
Début de l'itinéraire
Vas à Bulle
Vas à Riaz
Vas à Marsens
Vas à Echarlens
Vas à Charmey
Tu es arrivé!
```

```{exec} python
:editor: dc635abe-c4ee-4beb-badd-02733dff234e
itineraire = ["Bulle", "Riaz", "Marsens", "Echarlens", "Charmey"]

# Compléter le programme
```

````{solution}
```{exec} python
:linenos:
itineraire = ["Bulle", "Riaz", "Marsens", "Echarlens", "Charmey"]
print("Début de l'itinéraire")
for ville in itineraire:
    print("Vas à", ville)
print("Tu es arrivé!")
```
````
