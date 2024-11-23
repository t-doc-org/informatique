% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions Lab

```{metadata}
hide-solutions: true
```

## Exercice {num}`py2-lab1`

1. Lire le code suivant et expliquer ce qu'il fait sans l'exécuter.
2. Exécuter le code. Le code fait-il ce que vous pensiez?
3. Comment structurer ce code différemment pour qu'il soit plus lisible?
    - Découper le code en parties qui effectuent une tâche donnée et ajouter des
    commentaire.
    - Remplacer chaque partie par une fonction.

```{exec} python
:style: height: 25rem
:linenos:
from random import *
from time import *

print("Bienvenue sur mon application de jeux.")

while True:
  choix = await input_line("Quel jeu veux-tu essayer?\n"
  " Jeu 1 [1], Jeu 2 [2] ou Jeu 3 [3] ou Quitter [q]")
  if choix == "1":
    print("Tu dois deviner un nombre entre 1 et 100 en un minimum d'essais.")
    nb_secret = randint(1, 100)
    essais = 0
    trouve = False
    while not trouve:
      nb_propose = int(await input_line("Trouve le nombre: "))
      essais += 1
      if nb_propose < nb_secret:
        print("Le nombre est plus grand!")
      elif nb_propose > nb_secret:
        print("Le nombre est plus petit!")
      else:
        print("Bravo, tu as trouvé", nb_secret, "en", essais, "essais.")
        trouve = True
  elif choix == "2":
    print("Je vais deviner ton âge!")
    print("Effectue la suite de calculs suivante:")
    sleep(4)
    print("Choisis un nombre entre 2 et 10.")
    sleep(4)
    print("Muliplie ce nombre par 2.")
    sleep(4)
    print("Ajoute 5 au résultat précédent.")
    sleep(4)
    print("Multiplie le nombre par 50.")
    sleep(4)
    deja_fete = await input_line("As-tu déjà fêté ton anniversaire cette"
    " année? [oui/non]")
    if deja_fete == "oui":
      print("Ajoute 1774.")
    else:
      print("Ajoute 1775.")
    sleep(2)
    print("Soustrais ton année de naissance (par exemple, 2001).")
    nombre = await input_line("Donne-moi le résultat final: ")
    print("Tu as", nombre[1:3], "ans et le nombre que tu avais choisis au "
    "départ est", nombre[0], ".")
  elif choix == "3":
    print("Réponds à l'énigme suivante:")
    while True:
      reponse = await input_line("Placée sous les pieds elle prête à rire.\n"
      " Placée entre les doigts, elle a permis d'écrire.\n"
      " Elle sert d'ornement mais s'envolent au gré du vent.\n"
      " Qui est-elle? ")
      if (reponse.lower() == "la plume" or reponse.lower() == "plume"
            or reponse.lower() == "une plume"):
        print("Bravo!")
        break
      else:
        print("Essaye encore.")
  elif choix == "q":
    break
  else:
    print("Ce choix n'est pas valide.")

print("Au revoir. Merci d'avoir joué avec moi!")
```

````{solution}
```{exec} python
:linenos:
from random import *
from time import *

# Définition des différents jeux
async def trouve_un_nombre():
  print("Tu dois deviner un nombre entre 1 et 100 en un minimum d'essais.")
  nb_secret = randint(1, 100)
  essais = 0
  while True:
    nb_propose = int(await input_line("Trouve le nombre: "))
    essais += 1
    if nb_propose < nb_secret:
      print("Le nombre est plus grand!")
    elif nb_propose > nb_secret:
      print("Le nombre est plus petit!")
    else:
      print("Bravo, tu as trouvé", nb_secret, "en", essais, "essais.")
      break

async def devine_age():
  print("Je vais deviner ton âge!")
  print("Effectue la suite de calculs suivante:")
  sleep(4)
  print("Choisis un nombre entre 2 et 10.")
  sleep(4)
  print("Muliplie ce nombre par 2.")
  sleep(4)
  print("Ajoute 5 au résultat précédent.")
  sleep(4)
  print("Multiplie le nombre par 50.")
  sleep(4)
  deja_fete = await input_line("As-tu déjà fêté ton anniversaire cette année?"
  " [oui/non]")
  if deja_fete == "oui":
    print("Ajoute 1774.")
  else:
    print("Ajoute 1775.")
  sleep(2)
  print("Soustrais ton année de naissance (par exemple, 2001).")
  nombre = await input_line("Donne-moi le résultat final: ")
  print("Tu as", nombre[1:3], "ans et le nombre que tu avais choisis au "
  "départ est", nombre[0], ".")

async def resous_enigme():
  print("Réponds à l'énigme suivante:")
  while True:
    reponse = await input_line("Placée sous les pieds elle prête à rire.\n"
      " Placée entre les doigts, elle a permis d'écrire.\n"
      " Elle sert d'ornement mais s'envolent au gré du vent.\n"
      " Qui est-elle? ")
    if (reponse.lower() == "la plume" or reponse.lower() == "plume"
          or reponse.lower() == "une plume"):
      print("Bravo!")
      break
    else:
      print("Essaye encore.")


# Déroulement du jeu

# Phrase d'accueil
print("Bienvenue sur mon application de jeux.")

# Choix des jeux
while True:
  choix = await input_line("Quel jeu veux-tu essayer?\n"
  "Jeu 1 [1], Jeu 2 [2] ou Jeu 3 [3] ou Quitter [q] ")
  if choix == "1":
    await trouve_un_nombre()
  elif choix == "2":
    await devine_age()
  elif choix == "3":
    await resous_enigme()
  elif choix == "q":
    break
  else:
    print("Ce choix n'est pas valide.")

# Phrase de fin
print("Au revoir. Merci d'avoir joué avec moi!")
```
````

## Exercice {num}`py2-lab1`

Écrire un jeu d'énigmes qui a la structure suivante:
1. Créer plusieurs fonctions qui gèrent la résolution des énigmes. Celles-ci
doivent retourner l'information nécessaire pour le calcul du score.
2. Avoir une variable pour le score.
3. Gérer le déroulement du jeu.

```{exec} python
:linenos:
:editable:
# Écrire le programme ici
```

