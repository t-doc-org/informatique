% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Jeu - Blackjack

```{metadata}
solutions: hide
```

## Introduction

Dans cette partie, vous allez programmer un jeu de Blackjack.

### Règle du jeu simplifiée:

Le but du jeu est d'atteindre 21 ou de s'en approcher le plus possible, mais
sans le dépasser.\
Au début du jeu, vous recevez deux cartes, chaque carte a une valeur entre 1 et
11. Ensuite, vous décidez de prendre une carte supplémentaire ou de vous arrêter.\
Si vous dépassez 21, vous perdez votre mise.\
Si vous avez 21 points, vous avez un blackjack. Si le croupier n'a pas lui aussi
un blackjack, vous gagnez 1.5 fois votre mise.\
En cas d'égalité, chacun récupère sa mise.\
Si vous n'avez pas un blackjack, mais mieux que le croupier, vous gagnez une
fois votre mise.\
Le croupier, lui, continue de tirer des cartes tant qu'il est en dessous de 17.

### Programmation

Pensez à utiliser des fonctions, en voici quelques exemples:

- `affichage_regles()` qui affiche les règles du jeu.
- `calcule_gain(somme_joueur, somme_croupier, mise)` qui calcule le gain du
joueur en fonction des cartes de chacun.
- `tirer_carte(personne)` qui gère le tirage des cartes pour le joueur ou pour
le croupier.
- `tour_joueur(somme_joueur)` qui gère le tour du joueur.
- `tour_croupier(somme_croupier)` qui gère le tour du croupier.
- `nouvelle_manche(mise)` qui gère chaque manche.


```{exec} python
:editor: 08044a00-6df6-459b-894b-b735f448782db
# Écrivez le programme ici
```

````{solution}
```{exec} python
from random import randint

# cette fonction doit afficher les règles du jeu.
def affichage_regles():
  reponse = input("Voulez-vous lire les règles du jeu? [oui/non]")
  if reponse == "oui":
    print("Le but du jeu est d'atteindre 21 ou de s'en approcher le plus "
          "possible, mais sans le dépasser.\n"
          "Au début du jeu, vous recevez deux cartes, chaque carte a une valeur "
          "entre 1 et 11. Ensuite, vous décidez de prendre une carte "
          "supplémentaire ou de vous arrêter.\n"
          "Si vous dépassez 21, vous perdez votre mise.\n"
          "Si vous avez 21 points, vous avez un blackjack. Si le croupier n'a "
          "pas lui aussi un blackjack, vous gagnez 1.5 fois votre mise.\n"
          "En cas d'égalité, chacun récupère sa mise.\n"
          "Si vous n'avez pas un blackjack, mais mieux que le croupier, vous "
          "gagnez une fois votre mise.\n"
          "Le croupier, lui, continue de tirer des cartes tant qu'il est en "
          "dessous de 17.")


def calcule_gain(somme_joueur, somme_croupier, mise):
  if somme_joueur > 21:
    print("Vous avez perdu!")
    return -mise
  elif somme_joueur == somme_croupier:
    print("Égalité!")
    return 0
  elif somme_joueur == 21:
    print("Vous avez gagné avec un blackjack!")
    return mise * 1.5
  elif somme_croupier > 21 or somme_joueur > somme_croupier:
    print("Vous avez gagné!")
    return mise
  else:
    print("Vous avez perdu!")
    return -mise

def tirer_carte(personne):
  carte = randint(1, 11)
  if personne == "joueur":
    print("Vous recevez un", carte)
  else:
    print("Le croupier reçoit un", carte)
  return carte

def tour_joueur(somme_joueur):
  nouvelle_carte = ""
  while nouvelle_carte != "non" and somme_joueur < 21:
    nouvelle_carte = input("Voulez-vous une nouvelle carte? [oui/non]")
    if nouvelle_carte == "oui":
      somme_joueur += tirer_carte("joueur")
      print("Vous avez un total de", somme_joueur)
  return somme_joueur

def tour_croupier(somme_croupier):
  while  somme_croupier < 17:
    somme_croupier += tirer_carte("croupier")
    print("Le croupier a un total de", somme_croupier)
  return somme_croupier

def nouvelle_manche(mise):
  somme_joueur = 0
  somme_croupier = 0
  joueur_carte1 = randint(1, 11)
  somme_joueur =  tirer_carte("joueur") + tirer_carte("joueur")
  print("Vous avez un total de", somme_joueur)
  somme_croupier = tirer_carte("croupier") + tirer_carte("croupier")
  print("Le croupier a un total de", somme_croupier)
  somme_joueur = tour_joueur(somme_joueur)
  somme_croupier = tour_croupier(somme_croupier)
  gain = calcule_gain(somme_joueur, somme_croupier, mise)
  return gain

credit = 1000
fin_partie = False

print("Bienvenue à la table de Blackjack")
affichage_regles()

while credit > 0 and not(fin_partie):
  print("Vous avez", credit, "CHF.")
  mise = float(input("Combien voulez-vous miser?"))
  if mise > credit:
    print("Vous ne pouvez pas pariez autant. Vous n'avez que", credit, "CHF.")
  else:
    credit += nouvelle_manche(mise)
  continuer = input("Voulez-vous continuer à jouer? [oui/non]")
  if continuer == "non":
    fin_partie = True

print("vous partez avec", credit, "CHF. Au revoir et à bientôt")
```
````








