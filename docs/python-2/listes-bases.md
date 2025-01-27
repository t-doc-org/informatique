% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Listes - Bases

```{metadata}
hide-solutions: true
scripts:
  - src: quizz-helpers.js
```

En Python, une liste est une variable dans laquelle il est possible de stocker
plusieurs valeurs (de types différents).

```{code-block} text
matieres = ["français", "informatique", "allemand"]
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
matieres = ["français", "informatique", "allemand"]
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

1.  Créez les listes suivantes en Python :
    - Les salles de classe dans lesquelles tu as des cours
    - Les années de naissance des membres de ta famille
    - La taille en mètres de tes amis

2.  Affichez les trois listes.

```{exec} python
:editor: bda26e73-b3dc-4d27-807c-e90f97d2ea25
# Écrivez le programme ici
```

````{solution}
```{exec} python
:linenos:
# Créations des listes
salles = ["P207", "G107", "P214", "P-107"]
annees_naissance = [1941, 1966, 1974, 1975, 1978, 2006]
tailles = [1.8, 1.9, 1.96]

# Affichage des listes
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
Dans une liste de n éléments, le dernier élément sera à l'**index n-1**.
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

Complétez le programme suivant en utilisant l'indexation de manière à ce que le
programme affiche le texte suivant:

```{code-block} text
rouge
noir
brun
bleu
```

```{exec} python
:editor: 5487e3b6-2af5-48fc-82d6-29ccd2600828
couleurs = ["noir", "blanc", "brun", "gris", "rouge", "jaune", "bleu"]

# complétez les index corrects
print(couleurs[...])
print(couleurs[...])
print(couleurs[...])
print(couleurs[...])
```

````{solution}
```{exec} python
:linenos:
couleurs = ["noir", "blanc", "brun", "gris", "rouge", "jaune", "bleu"]
print(couleurs[4])
print(couleurs[0])
print(couleurs[2])
print(couleurs[6])
```
````

### Exercice {num}`exo-py2`

Ajoutez les instructions nécessaires pour que l'affichage de la liste soit le
suivant:

```{code-block} text
['B', 'B', 'W', 'D', 'E', 'X']
```

```{exec} python
:editor: b0091579-35b5-41d7-9316-81f642ff24c0
lettres = ["A", "B", "C", "D", "E", "F"]
# ajoutez le code ici
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

### Exercice {num}`exo-py2`

Complétez le programme ci-dessous en utilisant l'indexation de manière à ce que
le print affiche la liste suivante:

```{code-block} text
['Fribourg', 'Lausanne', 'Berne', 'Zurich', 'Genève']
```

Il vous faudra pour cela modifier les éléments de la liste villes.

```{exec} python
:editor: e0da4c93-4aed-4db0-8b9e-6155b829ad46
villes = ["Fribourg", "Zug", "Berne", "Lugano", "Soleure"]

# à modifier
villes
villes
villes

print(villes)
```

````{solution}
```{exec} python
:linenos:
villes = ["Fribourg", "Zug", "Berne", "Lugano", "Soleure"]

villes[1] = "Lausanne"
villes[3] = "Zurich"
villes[4] = "Genève"

print(villes)
```
````

### Exercice {num}`exo-py2`

La fonction `controle_position` prend en paramètre une liste à 2 éléments
correspondant à la position d'un personnage. Cette fonction doit afficher
"Position correcte" si les 2 coordonnées sont strictement positives.

```{exec} python
:editor: 61333d65-5221-4b00-867b-736bbee822a6
def controle_position(position):
  # modifiez le programme ici
  print("Position correcte")
  print("Position incorrecte")

controle_position([100, 200])
controle_position([-100, 200])
controle_position([100, -200])
controle_position([0, 200])
```

````{solution}
```{exec} python
:linenos:
def controle_position(position):
  if position[0]>0 and position[1]>0:
    print("Position correcte")
  else:
    print("Position incorrecte")

controle_position([100, 200])
controle_position([-100, 200])
controle_position([100, -200])
controle_position([0, 200])
```
````

## Fonctions sur les listes

En Python, il existe beaucoup de fonctions prédéfinies qui permettent de
manipuler les listes. Nous en avons vu déjà rencontrées certaines dans
[](listes-lab2.md).

len(ma_liste)
: retourne le nombre d'éléments de  la liste

ma_liste.append(mon_element)
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

<script>
function question(...args) {
  tdoc.question("Que va afficher ce programme?", ...args);
}
</script>

1.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    print(liste[4])
    ```

    <script>
    question({'7': true}, "Le premier élément se trouve à l'index 0.");
    </script>

2.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste[5] = 6
    print(liste)
    ```

    <script>
    question({'[1,5,4,12,7,6,10,2]': true},
             "Le premier élément se trouve à l'index 0.");
    </script>

3.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste.remove(5)
    print(liste)
    ```

    <script>
    question({'[1,4,12,7,9,10,2]': true},
             "La fonction remove(element) efface la première occurrence de " +
             "l'élément donné entre parenthèses.");
    </script>

4.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste.sort()
    print(liste)
    ```

    <script>
    question({'[1,2,4,5,7,9,10,12]': true},
             "La fonction sort() trie les éléments par ordre croissant.");
    </script>

5.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    del liste[2]
    print(liste)
    ```

    <script>
    question({'[1,5,12,7,9,10,2]': true}, "del efface l'élément donné.");
    </script>

6.  ```{exec} python
    :linenos:
    :when: never
    liste = [1, 5, 4, 12, 7, 9, 10, 2]
    liste.insert(1, 6)
    print(liste)
    ```

    <script>
    question({'[1,6,5,4,12,7,9,10,2]': true},
             "La fonction insert(1, 6) insère l'élément 6 à l'index 1.");
    </script>

### Exercice {num}`exo-py2`

1.  Créez une liste, nommée `sports` avec les éléments suivants: `kayak`,
    `escrime` et `escalade`.
2.  Affichez la liste et son nombre d'éléments.
3.  Demandez cinq sports à l'utilisateur et ajoutez-les à la liste `sports`.
4.  Afficher la liste et son nombre d'éléments.
5.  Ajoutez l'élément `tennis de table` à l'index 3.
6.  Affichez la liste et son nombre d'éléments.
7.  Effacez l'élément `escalade`.
8.  Affichez la liste et son nombre d'éléments.
9.  Quel est l'index d'`escrime`? Affichez l'index d'`escrime`.
10. Effacez le cinquième élément de la liste.
11. Affichez la liste et son nombre d'éléments.

```{exec} python
:editor: f9da8abf-19a5-4eba-aafd-b21e58273901
# Écrivez le programme ici
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

1.  Demandez à l'utilisateur d'entrer 6 nombres et stockez-les dans la liste
    'nombres'.
2.  Afficher la liste.
3.  Trier la liste.
4.  Afficher la liste.
5.  Inverser l'ordre des éléments.
6.  Afficher la somme des éléments.

```{exec} python
:editor: 1d0149fa-92a5-4cd1-8984-1b83ed61054d
# Écrivez le programme ici
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

Sans exécuter le code, répondez aux questions suivantes:
1. Que va retourner `nombres.index(5)`?
2. Que va retourner `nombres.index(3)`?
2. Que va retourner `nombres.count(1)`?
3. Quelle sera la liste après l'instruction `nombres.remove(4)`?
4. Quelle sera la liste après l'instruction `nombres.reverse()`?
5. Quelle sera la liste après l'instruction `nombres.sort()?


```{exec} python
:editor: 5e39f143-2a7d-4e04-a373-81b744d6015c
# Complétez le code pour tester vos réponses
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
l'utilisateur écrit le texte "stop", ensuite tous les ingrédients sont affichés.

ATTENTION: le mot stop ne doit jamais entrer dans la liste des ingrédients!

Complétez le programme de manière que celui-ci corresponde à cette description.

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

Afin de simplifier la création de cette liste, complétez la fonction
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

1. Écrivez un programme qui génère une liste de 1000 nombres entiers tirés au
hasard entre 1 et 10.
2. Déterminez le nombre d'occurences de chaque nombre.

```{tip}
Dans le module `random`, la fonction `randint(a, b)` permet de généré des
nombres entiers aléatroires entre a (compris) et b (compris).

Ne pas oublier l'import: `from random import randint`
```

```{exec} python
:editor: b696c9ff-f357-4db6-b4e9-ff0d89d501c9
# Écrivez le programme ici
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

## Différence variable simple et variable de type liste

### Exemple {num}`ex-py2`

Exécutez le code donné. Que se passe-t-il lorsqu'on modifie la valeur de la
variable 'a'?

```{exec} python
:editor:
a = 5
b = a
print("a:", a, "b:", b)
a = 4
print("a:", a, "b:", b)
```

<table style="width: 100%"><tr style="text-align: center">
</tr><tr style="vertical-align: center"><td>

`a = 5` crée une référence de la variable `a` vers la valeur `5` en mémoire.

`b = a` crée une référence de la variable `b` vers la même valeur que celle
référencée par `a`.

</td><td style="padding-left: 1rem">

```{image} images/ref-nombre1.png
:alt: Références sur le même nombre
:width: 90%
:align: center
```

</td></tr></table>

<table style="width: 100%"><tr style="text-align: center">
</tr><tr style="vertical-align: center"><td>

`a = 4` change la référence de la variable `a` vers la valeur `4` en mémoire.

La référence de la variable `b` elle ne change pas.

</td><td style="padding-left: 1rem">

```{image} images/ref-nombre2.png
:alt: Références sur des nombres différents
:width: 80%
:align: center
```

</td></tr></table>


### Exemple {num}`ex-py2`

Exécutez le code donné. Que se passe-t-il lorsqu'on modifie la valeur de la
variable 'liste_a'?

```{exec} python
:editor:
a = [1, 2, 3]
b = a
print("a:", a, "b:", b)
a[1] = 9
print("a:", a, "b:", b)
b.append(7)
print("a:", a, "b:", b)
```

<table style="width: 100%"><tr style="text-align: center">
</tr><tr style="vertical-align: center"><td>

`a = [1, 2, 3]` crée une référence de la variable `a` vers la liste `[1, 2, 3]`
en mémoire.

`b = a` crée une référence de la variable `b` vers la même liste que celle
référencée par `a`.

</td><td style="padding-left: 1rem">

```{image} images/ref-liste.png
:alt: Références sur une liste
:width: 90%
:align: center
```

</td></tr></table>

En modifiant le deuxième élément de la variable `a` avec `a[1] = 9`, la variable
`b` est aussi modifiée, car c'est la même liste qui est référencée.

De même `b.append(7)` modifie aussi la variable `a` (elle ajoute un élément).

