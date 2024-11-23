% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Listes Lab

```{metadata}
hide-solutions: true
```

## Exercice {num}`py2-lab2`

Écrire un programme pour calculer et afficher la moyenne de 5 notes qui seront
demandées à l'utilisateur.

```{exec} python
:linenos:
:editable:
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
# Définition des variables
somme_notes = 0

# Demande des notes à l'utilisateur
for _ in range(5):
  somme_notes += float(await input_line("Note: "))

# Calcule de la moyenne
moyenne = somme_notes / 5

# Affiche la moyenne
print(moyenne)
```
````

## Exercice {num}`py2-lab2:exemple-liste`

Répondre aux questions suivantes en lien avec le programme suivant:
1. Que fait `apprend(5.5)`?
2. Qu'affiche `print(notes[2])`?
3. Quelle différence y a-t-il entre `remove()` et `del`?

```{exec} python
:linenos:
:when: never
notes = [6, 5, 4.5, 5, 3.5]
print(notes)
notes.append(5.5)
print(notes)
print(notes[2])
notes.remove(5)
print(notes)
del notes[3]
print(notes)
```

## Exercice {num}`py2-lab2`

1. Exécuter le code et vérifier les réponses de l'{numref}`exercice %s<py2-lab2:exemple-liste>`.

  ```{exec} python
  :linenos:
  :editable:
  notes = [6, 5, 4.5, 5, 3.5]
  print(notes)
  notes.append(5.5)
  print(notes)
  print(notes[2])
  notes.remove(5)
  print(notes)
  del notes[3]
  print(notes)
  ```

2. Répondre aux questions suivantes en testant dans le code ci-dessus,
si nécessaire:

    1. À quel endroit de la variable notes la fonction `append()` ajoute-t-elle
    une valeur?
    2. Qu'est-ce qui s'affiche en remplaçant `print(notes[2])` par
    `print(notes[0])`?
    3. Qu'est-ce qui s'affiche en remplaçant `print(notes[2])` par
    `print(notes[5])`?
    4. Qu'est-ce qui s'affiche en remplaçant `print(notes[2])` par
    `print(notes[6])`?
    5. Quelle hypothèse peut être faite sur l'utilisation de la notation
    `notes[i]` où `i` est un nombre entier?
    6. `notes` est une variable de type "list" (une liste). Comment créer une
    liste vide?



```{solution}
1.  1. `apprend(5.5)` ajoute la note 5.5 à la fin de la liste des notes.
    2. `print(notes[2])` affiche le 3{sup}`e` élément de la liste.
    3. `remove()` est une fonction qui efface la première occurence de l'élément
        spécifié entre parenthèse.\
       `del` est un mot clé qui supprime l'élément à l'emplacement spécifié.
2.  1. La fonction `append()` ajoute l'élément à la fin de la liste.
    2. `print(notes[0])` affiche le premier élément de la liste, c'est-à-dire 6.
    3. `print(notes[5])` affiche le 6{sup}`e` élément, c'est-à-dire 5.5.
    4. `print(notes[6])` produit une erreur `IndexError: list index out of
        range` qui est une erreur lors de l'exécution, car `notes[6]` appelle
        le 7{sup}`e` élément de la liste, mais il n'y a que 6 éléments dans
        celle-ci.
    5. `notes[i]` où `i` est un nombre entier retourne l'élément en position
        `i+1`.
    6. Pour créer une liste vide: `notes = []`
```

## Exercice {num}`py2-lab2`

Écrire un programme qui demande à l'utilisateur d'entrer 10 notes qui seront
stockées dans une liste.

Le programme doit être facilement modifiable pour changer le nombre de notes à
saisir.


```{exec} python
:linenos:
:editable:
# Écrire le programme ici
```

````{solution}
```{exec} python
:linenos:
# Définition des variables
notes = []

# Demande des notes à l'utiliateur
for _ in range(10):
  notes.append(float(await input_line("Note: ")))

# Afficher la liste de notes
print(notes)
```
````

## Exercice {num}`py2-lab2:exemple-for`

Que va afficher ce programme?


```{exec} python
:linenos:
:when: never
notes = [6, 5, 4.5, 5, 3.5]
for i in notes:
  print(i)
```

## Exercice {num}`py2-lab2`

1. Exécuter le code et vérifier les réponses de l'{numref}`exercice %s<py2-lab2:exemple-for>`.

```{exec} python
:linenos:
:editable:
notes = [6, 5, 4.5, 5, 3.5]
for i in notes:
  print(i)
```

2. Répondre aux questions suivantes en testant dans le code ci-dessus,
si nécessaire:

    1. Que se passe-t-il si `i` est remplacé par `k`?
    2. Quel serait un meilleur choix de nom pour `i` dans le contexte de ce
        programme?

````{solution}
1. Le programme va afficher les éléments de la liste (les notes) les unes
après les autres. Une note par ligne.
2.
    1. En remplaçant partout le `i` par `k` (lignes 2 et 3), cela ne change
    rien.
    2. `i` représente les éléments de la liste. Comme la liste contient des
    notes, un meilleur choix serait:

    ```{exec} python
    :linenos:
    notes = [6, 5, 4.5, 5, 3.5]
    for note in notes:
      print(note)
    ```
````

## Exercice {num}`py2-lab2`

Modifier le programme suivant pour qu'il calcule et affiche la somme des notes
quel que soit le nombre de notes ajoutées.

1. Tester le code en ajoutant 2 notes avant de calculer la somme.
2. Tester le code en supprimant une note avant de calculer la somme.

```{exec} python
:linenos:
:editable:
# Compléter et/ou modifier le code
notes = [6, 5, 4.5, 5, 3.5]
somme = 0
for note in notes:
  print(note)
print(somme)
```

````{solution}
```{exec} python
:linenos:
:editable:
notes = [6, 5, 4.5, 5, 3.5]
somme = 0
# notes.append(4)
# notes.append(5.5)
# notes.remove(notes[2])
for note in notes:
  somme += note
print(somme)
```
````

## Exercice {num}`py2-lab2`

Compléter le programme précédent pour qu'il:
- demande à l'utilisateur le nombre de notes qu'il veut entrer,
- lui demande d'entrer les notes,
- calcule et affiche la moyenne des notes.

Voici un exemple d'exécution du programme:

```{code-block}
Nombre de notes : 3
Entrer note: 4
Entrer note: 5
Entrer note: 5.5
Moyenne: 4.833333333333333
```

```{exec} python
:linenos:
:editable:
# Compléter et/ou modifier le code
notes = []
somme = 0
for note in notes:
    print(note)
print("Moyenne: ", moyenne)
```

````{solution}
```{exec} python
:linenos:
# Définition des variables
notes = []
somme = 0
nb_notes = int(await input_line("Nombre de notes: "))

# Demande les notes à l'utilisateur
for _ in range(nb_notes):
  notes.append(float(await input_line("Entrer note:")))

# Calcule le somme des notes
for note in notes:
    somme += note

# Calcule la moyenne des notes
moyenne = somme / nb_notes
print("Moyenne: ", moyenne)
```
````

## Exercice {num}`py2-lab2`

Pour améliorer le programme, créer une fonction 'calcule_moyenne(notes)' qui:
- prend en paramètre la liste des notes,
- calcule la moyenne et la renvoie.

````{tip}
La fonction `len(liste)` retourne le nombre d'éléments de la liste.

```{exec} python
:linenos:
:editable:
notes = [3, 4.5, 5.5]
nombre_notes = len(notes)
print(nombre_notes)
```
````

```{exec} python
:linenos:
:editable:
# Compléter et/ou modifier le code

# Définition de la fonction calcule_moyenne(notes)

# Définition des variables
notes = []

# Demande les notes à l'utilisateur
nb_notes = int(await input_line("Nombre de notes: "))
for _ in range(nb_notes):
  notes.append(float(await input_line("Entrer note:")))

# Calcule et affiche la moyenne
moyenne =
print("Moyenne: ", moyenne)
```

````{solution}
```{exec} python
:linenos:
# Définition de la fonction calcule_moyenne(notes)
def calcule_moyenne(notes):
  somme = 0
  for note in notes:
    somme += note
  moyenne = somme / len(notes)
  return moyenne


# Définition des variables
notes = []

# Demande les notes à l'utilisateur
nb_notes = int(await input_line("Nombre de notes: "))
for _ in range(nb_notes):
  notes.append(float(await input_line("Entrer note:")))

# Calcule et affiche la moyenne
moyenne = calcule_moyenne(notes)
print("Moyenne: ", moyenne)
```
````

