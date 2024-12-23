% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Listes Lab - Mini projet

```{metadata}
hide-solutions: true
```

Les exercices suivants vous mèneront petit à petit à simuler la création d'un
compte et l'identification sur un site ou une application.

Pour cet exercice, travaillez avec Visual Studio Code.

Pour débuter, vous avez le code suivant:

```{exec} python
:when: never
utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mpd3"]
```

## Exercice {num}`py2-lab3`

Complétez le programme ci-dessus qui a pour but d'enregistrer de nouveaux
utilisateurs sur un site ou une application.

Le programme doit:
- demander à l'utilisateur de choisir un nom d'utilisateur et un mot de passe.
- créer un fonction `utilisateur_existe(utilisateur)` qui retourne `True` si
  l'utilisateur passé en paramètre existe dans la liste `utilisateurs`.
- si le nom d'utilisateur n'existe pas encore, ajouter le nom d'utilisateur dans
  la liste `utilisateurs` et le mot de passe dans celle `mots_de_passe`.

Voici un exemple d'exécution du programme:

```{code-block} text
Choisissez un nom d'utilisateur: user1
Choisissez un mot de passe: hfhf
Cet utilisateur existe déjà.

Choisissez un nom d'utilisateur: user4
Choisissez un mot de passe: mdp4
L'utilisateur user4 a été ajouté.
```

```{tip}
:class: dropdown
Utilisez la syntaxe `if a in b` pour vérifier si a se trouve dans la liste b.
```

<!-- ````{solution}
```{exec} python
:when: never
:linenos:
def utilisateur_existe(utilisateur):
  if utilisateur in utilisateurs:
    return True
  else:
    return False

utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mpd3"]

login = input("Choisissez un nom d'utilisateur: ")
mdp = input("Choisissez un mot de passe: ")

if utilisateur_existe(login):
  print("Cet utilisateur existe déjà.")
else:
  utilisateurs.append(login)
  mots_de_passe.append(mdp)
  print("L'utilisateur", login, "a été ajouté.")
```
```` -->

## Exercice {num}`py2-lab3`

Sauvegardez cette fonctionnalité dans la fonction `cree_utilisateur()` qui va se
charger d'ajouter un nouvel utilisateur avec son mot de passe.

<!-- ````{solution}
```{exec} python
:when: never
:linenos:
def utilisateur_existe(utilisateur):
  if utilisateur in utilisateurs:
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

utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mpd3"]

cree_utilisateur()

```
```` -->

## Exercice {num}`py2-lab3`

Complétez le programme précédent qui a pour but de vérifier l'accès à un site
ou à une application vis l'utilisation d'un nom d'utilisateur et d'un mot de
passe.

Le programme doit:
- demander à l'utilisateur d'entrer son nom d'utilisateur et son mot de passe.
- vérifier si les identifiants entrés sont corrects. Pour cela,
        1. utiliser la fonction `utilisateur_existe(utilisateur)` pour savoir si
           le nom d'utilisateur existe.
        2. créer une fonction `mot_de_passe_correct(utilisateur, mdp)` qui
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

<!-- ````{solution}
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

utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mpd3"]

login = input("Entrez votre nom d'utilisateur: ")
mdp = input("Entrez votre mot de passe: ")

if utilisateur_existe(login):
  if mot_de_passe_correct(login, mdp):
    print("Bienvenu(e) sur le site.")
  else:
    print("Le mot de passe est incorrect.")
else:
  print("L'utilisateur", login, "n'existe pas.")
```
```` -->

## Exercice {num}`py2-lab3`

Sauvegardez cette fonctionnalité dans la fonction `identification()` qui va
simuler l'identification d'un utilisateur.

<!-- ````{solution}
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

utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mpd3"]

cree_utilisateur()
identification()

```
```` -->

## Exercice {num}`py2-lab3`

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


<!-- ````{solution}
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

utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mpd3"]

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
```` -->


## Exercice {num}`py2-lab3`

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

<!-- ````{solution}
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

utilisateurs = ["user1", "user2", "user3"]
mots_de_passe = ["mdp1", "mdp2", "mpd3"]

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
```` -->

