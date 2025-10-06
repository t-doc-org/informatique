% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Fonctions Lab

## Exercice {nump}`exercice`

Écrivez un programme qui simule le fonctionnement d'un bancomat.
Vous devez créer 5 fonctions:

- `affiche_solde(solde)` qui affiche le solde qui se trouve sur le compte. Cette
fonction a un paramètre, le `solde` du compte.

- `solde_suffisant(montant, solde)` qui teste si le montant que l'utilisateur veut
retirer est suffisant sur le compte. Cette fonction a deux paramètres, le
`montant` que l'on veut débiter et le `solde` du compte. Elle doit renvoyer `True` ou
`False`.

- `retrait(solde)` qui effectue le retrait d'argent sur le compte. Cette fonction
a un paramètre, le `solde` du compte. Elle doit demander le `montant` à retirer à
l'utilisateur, tester si le solde est suffisant. Si c'est le cas, elle doit
créditer la somme sur le solde du compte. La fonction doit renvoyer le nouveau
`solde`.

- `depot(solde)` qui effectue le dépôt d'argent sur le compte. Cette fonction
a un paramètre, le `solde` du compte. Elle doit renvoyer le nouveau `solde`.

- `choix_options()` qui permet à l'utilisateur de choisir parmi les différentes
options. Cette fonction doit renvoyer un `choix` valide. Si le choix n'est pas
valide, redemandez à l'utilisateur.

Voici un exemple d'exécution:

```{code-block} text
Bancomat à votre disposition! Insérez votre carte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
1
Le solde de votre compte est de 450.60 CHF.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
2
Combien voulez-vous retirez? 500
Ce montant n'est pas disponible, vous avez 450.60 CHF sur votre compte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
2
Combien voulez-vous retirez? 100
Il vous reste 350.60 CHF sur votre compte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
3
Combien voulez-vous déposer? 50
Vous avez 400.60 CHF sur votre compte.
Choisir parmi les options suivantes:
1 - Afficher le solde du compte
2 - Retirer de l'argent
3 - Déposer de l'argent
4 - Quitter
4
Au revoir!
```

```{exec} python
:editor: 3197cc87-208c-414f-a260-2f3761c69c9e
# Écrivez le programme ici
```

````{solution}
```{exec} python
from random import randint

def affiche_solde(solde):
  print("Le solde de votre compte est de", solde, "CHF.")

def solde_suffisant(montant, solde):
  if montant <= solde:
    return True
  else:
    return False

def retrait(solde):
  montant = float(input("Combien voulez-vous retirez?"))
  if solde_suffisant(montant, solde):
    solde -= montant
    print("Il vous reste", solde, "CHF sur votre compte.")
  else:
    print("Ce montant n'est pas disponible, vous avez", solde, "CHF sur votre compte.")
  return solde

def depot(solde):
  montant = float(input("Combien voulez-vous déposer?"))
  solde += montant
  print("Vous avez", solde, "CHF sur votre compte.")
  return solde

def choix_options():
  print("Choisir parmi les options suivantes:")
  print("1 - Afficher le solde du compte")
  print("2 - Retirer de l'argent")
  print("3 - Déposer de l'argent")
  print("4 - Quitter")
  choix = int(input())
  while choix != 1 and choix != 2 and choix != 3 and choix != 4:
    choix = int(input("Le choix n'est pas valide. Choisissez entre 1, 2, 3 et 4."))
  return choix

print("Bancomat à votre disposition! Insérez votre carte.")
solde = randint(50, 600)
choix = 0
while choix != 4:
  choix = choix_options()
  if choix == 1:
    affiche_solde(solde)
  elif choix == 2:
    solde = retrait(solde)
  elif choix == 3:
    solde = depot(solde)
  print("-" * 30)
print("Au revoir!")
```
````
