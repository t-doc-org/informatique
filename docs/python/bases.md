---
py-config:
  splashscreen:
    autoclose: true
  packages:
  - matplotlib
---

<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Les bases

## Introduction

En programmation, il est important de suivre certaines règles pour que le code soit lisible.
1. Il est important de ne pas se répéter. Si tu copies/colles une ou des ligne(s), il y a une autre manière de faire qui est meilleure.
2. Commenter le code pour expliquer ce qu'on fait. En Python, il faut utiliser \# suivi du commentaire.
3. Pour chaque exercice, créer un nouveau document et le nommer avec un nom qui permet de savoir ce qu'il contient (utiliser par exemple le numéro de l'exercice).
4.s Tester souvent (lors de l'exécution, le programme est sauvegardé).

## Fonction `print()`

La fonction `print()` permet d'afficher d'afficher une phrase ou la valeur d'un objet sur la console.

```{code-block} python
:caption: Exemple
print("Hello World!")
```

### Exercice 1

Écrire un programme qui affiche exactement ce texte:
> Salut\
> Je suis élève au collège Sainte-Croix\
> J'ai 16 ans\
> J'aime bien jouer au volley

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 1
:linenos:
print("Salut")
print("Je suis élève au collège Sainte-Croix")
print("J'ai 16 ans")
print("J'aime bien jouer au volley")
```

</details>

### Exercice 2

1. Écrire un programme qui affiche "Bonjour tout le monde!".
2. Écrire un programme qui affiche "Je programme! ".
3. Écrire un programme qui affiche "Je programme! Je programme!".
4. Écrire un programme qui affiche "Je programme! " 10 fois de suite sans récrire 10 fois la même chose.
5. Ajouter un commentaire qui explique ce que tu as fait au point précédent.

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 2
:linenos:
print("Bonjour tout le monde!")
print("Je programme!")
print("Je programme! Je programme!")
# Pour répéter plusieurs fois une chaine de caractère, on peut utiliser *
print("Je programme! " * 10)
```

</details>

## Opérateurs mathématiques

Les opérateurs mathématiques permettent de faire des calculs simples avec les nombres.

| Opérateur | Nom | Exemple | Résultat |
| :-------: | :-: | :-----: | :------: |
| + | Addition | 3+4 | - 7 |
| - | Soustraction | 9-12 | -3 |
| * | Mutliplication | 5*6| 30 |
| / | Division | 11/2 | 5.5 |
| ** | Puissance | 2**3 | 8 |
| // | Division entière | 26//6 | 4 |
| % | Modulo (reste de la division entière) | 26 mod 6 | 2 |

### Exercice 3

1. Effectuer mentalement les 7 opérations ci-dessus avec les nombres 13 et 2.
2. Écrire un programme qui permet d'effectuer les 7 opérations ci-dessus avec 13 et 2 et d'afficher le résulat. Les résultats sont-ils les mêmes qu'au point précédent?
3. Faire de même avec 10 et 3.
4. Faire de même avec 8 et 5.
5. Que faut-il utiliser pour éviter de modifier chaque ligne? Noter la réponse par un commentaire dans le code.

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 3
:linenos:
print(13 + 2)
print(13 - 2)
print(13 * 2)
print(13 / 2)
print(13 ** 2)
print(13 // 2)
print(13 % 2)

# Pour éviter de devoir changer les valeurs à toutes les lignes, il faut utiliser des variables.
a = 13
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)
print(a % b)
```

</details>

### Exercice 4

Écrire un programme qui permet d'afficher les calculs suivants, ainsi que la réponse:
1. 452.52 + 27.78 =
2. 5.65 \cdot 3.4 =
3. 4 569 - 8 532 =
4. 56 / 3 =
5. Calculer le quotient et le reste de la division de 345 par 37.

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 4
:linenos:
print("452.52 + 27.78 = ", 452.52 + 27.78)
print("5.65 * 3.4 = ", 5.65 * 3.4)
print("4569 - 8532 = ", 4569 - 8532)
print("56 / 3 = ", 56 / 3)
print("Le quotient de la division de 345 par 37 est ", 345 // 37)
print("Le reste de la division de 345 par 37 est ", 345 % 37)
```

</details>

### Exercice 5

Écrire un programme qui permet de résoudre l'exercice suivant (N'oublier pas les phrases d'explication):
1. Luc va faire des courses. Il achète deux livres à 9.30 CHF, un jeu vidéo à 59 CHF et trois mangas à 13.50 CHF. Calculer le montant total des dépenses de Luc.
2. Juliette achète un livre, deux jeux vidéo et deux mangas. Calculer le montant total des dépenses de Juliette.
3. En période de soldes, les jeux vidéo sont à 50 \%, les livres à 5 CHF et les mangas ont 6 CHF de rabais.
4. Calculer les économies faites par chacun pendant les soldes (Utiliser des variables pour stocker le prix avant et après réduction).
5. Arrondir les prix aux centimes.

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 5
:linenos:
prix_livre = 9.30
prix_jeu = 59
prix_manga = 13.50

print("Montant total des achats de Luc:", 2 * prix_livre + 1 * prix_jeu + 3 * prix_manga, " francs.")
print("Montant total des achats de Juliette:", 1 * prix_livre + 2 * prix_jeu + 2 * prix_manga, " francs.")

print("Après réduction")
prix_livre = 5
prix_jeu = prix_jeu * 50 / 100
prix_manga = prix_manga - 6

print("Montant total des achats de Luc:", 2 * prix_livre + 1 * prix_jeu + 3 * prix_manga, " francs.")
print("Montant total des achats de Juliette:", 1 * prix_livre + 2 * prix_jeu + 2 * prix_manga, " francs.")


# Version améliorée
print("*********************************************************")
prix_livre = 9.30
prix_jeu = 59
prix_manga = 13.50

depenses_Luc = 2 * prix_livre + 1 * prix_jeu + 3 * prix_manga
depenses_Juliette = 1 * prix_livre + 2 * prix_jeu + 2 * prix_manga
print("Montant total des achats de Luc:", depenses_Luc , " francs.")
print("Montant total des achats de Juliette:", depenses_Juliette, " francs.")

print("Après réductions")
# Utiliser les variables de prix, sinon si le prix change, ça ne fonctionne plus.
prix_livre = 5
prix_jeu = prix_jeu * 50 / 100
prix_manga = prix_manga - 6

depenses_Luc_apres = 2 * prix_livre + 1 * prix_jeu + 3 * prix_manga
depenses_Juliette_apres = 1 * prix_livre + 2 * prix_jeu + 2 * prix_manga
print("Montant total des achats de Luc:", depenses_Luc_apres, " francs.")
print("Montant total des achats de Juliette:", depenses_Juliette_apres, " francs.")

# Que constate-on par rapport à certaines valeurs?
# les nombres à virgule ne peuvent pas être tous représenté en binaire (il en existe une infinité)
economies_Luc = round(depenses_Luc - depenses_Luc_apres, 2)
economies_Juliette = round(depenses_Juliette - depenses_Juliette_apres, 2)
print("Les économies de Luc sont de ", economies_Luc, " francs.")
print("Les économies de Juliette sont de ", economies_Juliette, " francs.")
```

</details>

### Exercice 6

Écrire un programme qui demande à l'utilisateur son nom, son prénom et où il habite. Le programme affichera:
> Quel est ton nom?\
> Quel est ton prénom?\
> Où habites-tu?\
> Bonjour {afficher le prénom} {afficher le nom}, heureux de faire ta connaissance.\
> Je vois que tu habites à {afficher le lieu}.

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 6
:linenos:
nom = input("Quel est ton nom? ")
prenom = input("Quel est ton prénom? ")
lieu = input("Où habites-tu? ")
print("Bonjour", prenom, nom, ", heureux de faire ta connaissance.")
print("Je vois que tu habites à", lieu)
```

</details>

### Exercice 7

Écrire un programme qui demande à l'utilisateur l'année actuelle, ainsi que l'âge qu'il avait le 31 décembre dernier et qui calcule l'année de naissance de l'utilisateur.\
Le programme affichera:
> Quel âge avais-tu au 31 décembre?\
> En quelle année sommes-nous?\
> Tu es né en {afficher l'année de naissance}.

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 7
:linenos:
age = int(input("Quel âge avais-tu au 31 décembre? "))
annee = int(input("En quelle année sommes-nous? "))
print("Tu es né.e en", annee - age - 1)
```

</details>

### Exercice 8
Écrire un programme qui convertit des mégaoctets en bits.\
Le programme affichera:
> Combien de mégaoctets veux-tu convertir en bits?\
> {afficher le nombre de mégaoctets} Mo  donnent {afficher le nombre de bits} bits.

<details>
<summary>Solution</summary>

```{code-block} python
:caption: Exercice 8
:linenos:
nb_mo = float(input("Combien de mégaoctets veux-tu convertir en bits? "))
# 1 octet = 8 bits
nb_bits = nb_mo * 8 * 1000000
print(nb_mo, "Mo donnent", nb_bits, "bits.")
```

</details>
