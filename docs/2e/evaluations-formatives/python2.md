% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Python 2

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Détails des calculs obligatoires. Attention au soin. Calculatrice autorisée.**
```
---

## Question {nump}`question`{points}`6`

Déterminez ce que va afficher le programme suivant:

```{exec} python
:name: nombres
:when:
:linenos:
nombres = [7, 3, -1, 0, 7, 4, -5, 8, 2, 6]
print(nombres[4])
nombres.remove(7)
print(nombres)
nombres.insert(1, 6)
print(nombres)
nombres[2] = 8
print(nombres)
nombres.reverse()
print(nombres)
print(nombres.index(8))
```

````{solution}
Le programme va afficher:
```{exec} python
:after: nombres
:when: load
:class: hidden
```
````

## Question {nump}`question`{points}`5`

Complétez le programme suivant:

```{exec} python
:when:
:linenos:
# Ce programme calcule le nombre de bonnes notes dans une liste de notes donnée
# Une note est considérée comme bonne à partir de 5
notes = [5.4, 4.7, 5, 4.3, 3.7, 3.1, 6, 4.5]

nb_bonnes_notes = __________________

for _____________________________________________

  if note >= 5:

    nb_bonnes_notes _____________________________

print("Il y a" _________________________________ "bonnes notes.")
```

````{solution}
```{exec} python
:linenos:
# Ce programme calcule le nombre de bonnes notes dans une liste de notes
# Une note est considérée comme bonne à partir de 5
notes = [5.4, 4.7, 5, 4.3, 3.7, 3.1, 6, 4.5]

nb_bonnes_notes = 0

for note in notes:

  if note >= 5:

    nb_bonnes_notes += 1

print("Il y a", nb_bonnes_notes, "bonnes notes.")
```
````

## Question {nump}`question`{points}`5`

Complétez le programme suivant:

```{exec} python
:when:
:linenos:
classique = ["chien", "chat", "poissons"]
petits_compagnons = ["lapin", "hamster", "cochon d'inde", "gerbille"]
sang_froid = ["serpent", "lézard"]

# demandez son animal de compagnie à l'utilisateur
animal = _____________"Quel animal de compagnie as-tu?"__


# en fonction de la réponse afficher la phrase qui correspond

if ___________________________________________ in ____________________
  print("Tu préfères les petits compagnons!")

_____________________________________________ in ____________________
  print("Un animal à sang froid, tu es audacieux!")

_____________________________________________ in ____________________
  print("Un grand classique, fidèle et affectueux!")

_____________________________________________  "aucun":
  print("Dommage, c'est chouette d'avoir un animal!")

______________________________
  print("Je ne connais pas cet animal.")
```

````{solution}
```{exec} python
:linenos:
classique = ["chien", "chat", "poissons"]
petits_compagnons = ["lapin", "hamster", "cochon d'inde", "gerbille"]
sang_froid = ["serpent", "lézard"]

# demandez son animal de compagnie à l'utilisateur
animal = input("Quel animal de compagnie as-tu?")


# en fonction de la réponse afficher la phrase qui correspond

if animal in petits_compagnons:
  print("Tu préfères les petits compagnons!")

elif animal in sang_froid:
  print("Un animal à sang froid, tu es audacieux!")

elif animal in classique:
  print("Un grand classique, fidèle et affectueux!")

elif animal ==  "aucun":
  print("Dommage, c'est chouette d'avoir un animal!")

else:
  print("Je ne connais pas cet animal.")
```
````


## Question {nump}`question`{points}`10`

Écrivez un programme qui respecte les instructions suivantes:

{.lower-alpha-paren}
1.  Générez une liste **nombres** de 10 nombres entiers aléatoires entre 15 et
    25 et affichez la liste.<br>
    Conseil: Si vous n'arrivez pas faire le point 1, choisissez-vous même une
    liste de 10 nombres pour faire la suite de l'exercice et tester votre code.
2.  Affichez le maximum de la liste **nombres**.
3.  Créez une nouvelle liste vide qui s'appelle **paires**.
4.  En parcourant les éléments de la liste **nombres**, stockez les nombres
    paires dans la liste **paires**.
5.  Affichez la liste **paires**.
6.  Définissez une fonction **calcule_moyenne(liste)** qui calcule et retourne
    la moyenne de la liste passée en paramètres. Attention: la liste peut avoir
    un nombre d'éléments qui change.
7.  Calculez et affichez la moyenne des nombres de la liste **nombres** en
    utilisant la fonction définie au point précédent.
8.  Au lieu de générer une liste de 10 nombres, demandez à l'utilisateur combien
    de nombres doivent être générés.

Exemple d'exécution:

```{code} text
Combien de nombres doivent être générés? 10
[15, 15, 21, 22, 23, 17, 24, 20, 20, 15]
Le maximum est 24
[20, 20, 22, 24]
La moyenne vaut 21.5
```

````{solution}
```{exec} python
:when: click
from random import randint

def calcule_moyenne(liste):
  return sum(liste)/len(liste)

nombres = []
nb_elements = int(input("Combien de nombres doivent être générés?"))
for _ in range(nb_elements):
  nombre = randint(15, 25)
  nombres.append(nombre)
print(nombres)

nombres.sort()
print("Le maximum est", nombres[-1])

paires = []
for nombre in nombres:
  if nombre % 2 == 0:
    paires.append(nombre)
print(paires)

print("La moyenne vaut", calcule_moyenne(paires))
```
````
