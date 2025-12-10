% Copyright 2024 Brice Canvel
% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Listes Lab - Mini projet

Le but de cet exercice est de créer étape par étape une simulation de la
création d'un compte et l'identification sur un site ou une application.

``````{tab-set}
:sync-group: etape
`````{tab-item} Étape 1
:sync: etape1
**Enregistrement d'un nouvel utilisateur**

Complétez le programme ci-dessous:

1.  demandez à l'utilisateur de choisir un nom d'utilisateur et un mot de passe.
2.  créez un fonction `utilisateur_existe(utilisateur)` qui retourne `True` si
    l'utilisateur passé en paramètre existe dans la liste `utilisateurs`.
3.  si le nom d'utilisateur n'existe pas encore, ajoutez le nom d'utilisateur
    dans la liste `utilisateurs` et le mot de passe dans celle `mots_de_passe`.

Voici un exemple d'exécution du programme:

````{code-block} text
Choisissez un nom d'utilisateur: user1
Choisissez un mot de passe: hfhf
Cet utilisateur existe déjà.

Choisissez un nom d'utilisateur: user4
Choisissez un mot de passe: mdp4
L'utilisateur user4 a été ajouté.
````

````{tip}
:class: dropdown
Utilisez la syntaxe `if a in b` pour vérifier si a se trouve dans la liste b.
````

````{solution}
```{exec} python
:when: never
:linenos:
def utilisateur_existe(utilisateur):
  if utilisateur in utilisateurs:
    return True
  else:
    return False

...

if utilisateur_existe(login):
  print("Cet utilisateur existe déjà.")
else:
  utilisateurs.append(login)
  mots_de_passe.append(mdp)
  print("L'utilisateur", login, "a été ajouté.")
```
````
`````
`````{tab-item} Étape 2
:sync: etape2
**Fonction pour créer un utilisateur**

Sauvegardez cette fonctionnalité dans la fonction `cree_utilisateur()` qui va se
charger d'ajouter un nouvel utilisateur avec son mot de passe.

````{solution}
```{exec} python
:when: never
:linenos:
def utilisateur_existe(utilisateur):
  ...

def cree_utilisateur():
  login = input("Choisissez un nom d'utilisateur: ")
  mdp = input("Choisissez un mot de passe: ")

  if utilisateur_existe(login):
    print("Cet utilisateur existe déjà.")
  else:
    utilisateurs.append(login)
    mots_de_passe.append(mdp)
    print("L'utilisateur", login, "a été ajouté.")

...

cree_utilisateur()
```
````
`````
`````{tab-item} Étape 3
:sync: etape3
**Identification d'un utilisateur**

Complétez le programme ci-dessous:

1.  demandez à l'utilisateur d'entrer son nom d'utilisateur et son mot de passe.
2.  vérifiez si les identifiants entrés sont corrects. Pour cela,
    -   utiliser la fonction `utilisateur_existe(utilisateur)` pour savoir si
        le nom d'utilisateur existe.
    -   créer une fonction `mot_de_passe_correct(utilisateur, mdp)` qui
        retourne `True` si le mot de passe passé en paramètre correspond au
        mot de passe de l'utilisateur.

Voici un exemple d'exécution du programme:

```{code-block} text
Entrez votre nom d'utilisateur: user5
Entrez votre mot de passe: hfhf
L'utilisateur user5 n'existe pas.

Entrez votre nom d'utilisateur: user2
Entrez votre mot de passe: mdp4
Le mot de passe est incorrect.

Entrez votre nom d'utilisateur: user2
Entrez votre mot de passe: mdp2
Bienvenu(e) sur le site.
```

```{tip}
:class: dropdown
Utilisez `ma_liste.index(mon_element)` pour récupérer l'index d'un élément.

`utilisateurs.index("user1")` retourne l'index de l'élément `user1`,
c'est-à-dire 0.

Pensez à stocker la valeur pour pouvoir la réutiliser.
```

````{solution}
```{exec} python
:when: never
:linenos:
def utilisateur_existe(utilisateur):
  ...

def mot_de_passe_correct(utilisateur, mdp):
  index = utilisateurs.index(utilisateur)
  if mdp == mots_de_passe[index]:
    return True
  else:
    return False

def cree_utilisateur():
  ...

...

if utilisateur_existe(login):
  if mot_de_passe_correct(login, mdp):
    print("Bienvenu(e) sur le site.")
  else:
    print("Le mot de passe est incorrect.")
else:
  print("L'utilisateur", login, "n'existe pas.")
```
````
`````
`````{tab-item} Étape 4
:sync: etape4
**Fonction pour l'identification**

Sauvegardez cette fonctionnalité dans la fonction `identification()` qui va
simuler l'identification d'un utilisateur.

````{solution}
```{exec} python
:when: never
:linenos:
def utilisateur_existe(utilisateur):
  ...

def mot_de_passe_correct(utilisateur, mdp):
  ...

def cree_utilisateur():
  ...

def identification():
  login = input("Entrez votre nom d'utilisateur: ")
  mdp = input("Entrez votre mot de passe: ")
  if utilisateur_existe(login):
    if mot_de_passe_correct(login, mdp):
      print("Bienvenu(e) sur le site.")
    else:
      print("Le mot de passe est incorrect.")
  else:
    print("L'utilisateur", login, "n'existe pas.")

...
identification()
```
````
`````
`````{tab-item} Étape 5
:sync: etape5
**Menu à choix**

Complétez le programme précédent pour pouvoir choisir entre trois options:

```{code-block} text
Que voulez-vous faire?
1: créer un compte
2: vous identifier
3: quitter
```

```{tip}
:class: dropdown
Utilisez une boucle `while True` pour que l'utilisateur puisse faire plusieurs
choix à la suite.

Pour quitter, utiliser l'instruction `break` qui permet de sortir de la boucle
infinie et continuer le programme.
```

````{solution}
```{exec} python
:when: never
:linenos:
def utilisateur_existe(utilisateur):
  ...

def mot_de_passe_correct(utilisateur, mdp):
  ...

def cree_utilisateur():
  ...

def identification():
  ...

...

while True:
  print("Que voulez-vous faire ?")
  print("1: créer un compte")
  print("2: vous identifier")
  print("3: quitter")
  choix=int(input())
  if choix == 1:
    cree_utilisateur()
  elif choix == 2:
    identification()
  elif choix == 3:
    break
  else:
    print("Choix non valide.")
print("Au revoir!")
```
````
`````
`````{tab-item} Étape 6
:sync: etape6
**Affichage des listes**

Complétez le programme précédent pour que lorsque l'utilisateur quitte le
programme la liste de tous les utilisateurs du système avec leur mot de passe
s'affiche.

Voici comment afficher les informations:

```{code-block} text
Nom d'utilisateur: user1 Mot de passe: mdp1
Nom d'utilisateur: user2 Mot de passe: mdp2
Nom d'utilisateur: user3 Mot de passe: mdp3
```

```{tip}
:class: dropdown
Utilisez `len(ma_liste)` pour récupérer la longueur de la liste et utiliser une
boucle `for` pour parcourir tous les index.
```
`````
``````

```{exec} python
:editor: 4cb48b0f-84fd-4681-a491-6aad56663022
# Définition des fonctions

# Définition des variables
utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mdp3"]

# Programme principal
```

````{solution}
```{exec} python
:linenos:
def utilisateur_existe(utilisateur):
  if utilisateur in utilisateurs:
    return True
  else:
    return False

def mot_de_passe_correct(utilisateur, mdp):
  index = utilisateurs.index(utilisateur)
  if mdp == mots_de_passe[index]:
    return True
  else:
    return False

def cree_utilisateur():
  login = input("Choisissez un nom d'utilisateur: ")
  mdp = input("Choisissez un mot de passe: ")

  if utilisateur_existe(login):
    print("Cet utilisateur existe déjà.")
  else:
    utilisateurs.append(login)
    mots_de_passe.append(mdp)
    print("L'utilisateur", login, "a été ajouté.")

def identification():
  login = input("Entrez votre nom d'utilisateur: ")
  mdp = input("Entrez votre mot de passe: ")
  if utilisateur_existe(login):
    if mot_de_passe_correct(login, mdp):
      print("Bienvenu(e) sur le site.")
    else:
      print("Le mot de passe est incorrect.")
  else:
    print("L'utilisateur", login, "n'existe pas.")

utilisateurs = []
mots_de_passe = []

while True:
  print("Que voulez-vous faire ?")
  print("1: créer un compte")
  print("2: vous identifier")
  print("3: quitter")
  choix=int(input())
  if choix == 1:
    cree_utilisateur()
  elif choix == 2:
    identification()
  elif choix == 3:
    break
  else:
    print("Choix non valide.")
for i in range(len(utilisateurs)):
    print("Nom d'utilisateur:", utilisateurs[i], "Mot de passe:", mots_de_passe[i])
```
````
