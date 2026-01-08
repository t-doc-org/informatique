% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
exec:
  python:
    files:
      music.sql:
    packages: [sqlite3]
```

# Python et bases de données 1

Dans cette partie, vous allez apprendre à utiliser Python pour accéder à une
base de données et faire des requêtes SQL.

La base de données à disposition est représentée par le schéma relationnel
suivant:

```{image} images/music-sql-diagram.png
:alt: Schéma relationnel de la base de données music
:width: 80%
:align: center
```

## Recherche de données dans la base de données

La recherche de données se fait en trois étapes:

- Connexion à la base de données (à effectuer une fois au début du programme):

  ```{exec} python
  :when: never
  base_donnees = sqlite3.connect("nom_de_la_base")
  ```

- Exécution de la requête de sélection

  ```{exec} python
  :when: never
  requete = base_donnees.execute("requete_selection")
  ```

- Demande des données obtenues grâce à la requête

  ```{exec} python
  :when: never
  resultats = requete.fetchall()
  ```

Par exemple:

```{exec} python
:when: never
base_donnees = sqlite3.connect("music.sqlite")
requete = base_donnees.execute("select * from artist;")
resultats = requete.fetchall()
```



## Affichage des résultats

Le résultat est une liste dans laquelle il y a des tuples (qui fonctionnent
comme des listes mais sont entourées de parenthèses au lieu des crochets) avec
les résultats:

```{code-block} text
[('Taylor Swift', 'United States', 'Big Machine Records'),
('The Beatles', 'United States', NULL),
('Galantis', 'Sweden','Big Beat Records'),
('Rihanna', 'Barbados', 'Def Jam Recordings'),
('Alessia Cara', 'Canada', 'Def Jam Recordings'),
('Khalid', 'United States', 'RCA Records'),
('Coldplay', 'United Kingdom', 'Parlophone')]
```

Il est ensuite possible d'afficher chaque résultat à l'aide d'une boucle:

```{exec} python
:when: never
for resultat in resultats:
  print(resultat)
```

Le code ci-dessus affichera:

```{code-block} text
('Taylor Swift', 'United States', 'Big Machine Records')
('The Beatles', 'United States', NULL)
...
('Khalid', 'United States', 'RCA Records')
('Coldplay', 'United Kingdom', 'Parlophone')
```


Comme le résultat est une liste, il est tout à fait possible d'accéder
directement à chaque élément grace à son index:

```{exec} python
:when: never
for resultat in resultats:
  print("Nom:", resultats[0], "Pays:", resultats[1], "Label:", resultats[2])
```

Le code ci-dessus affichera:
```{code-block} text
Nom: Taylor Swift Pays: United States Label: Big Machine Records
...
```

### Exercice {nump}`exemple`

La base de données est disponible dans la fichier `music.sqlite`.

Le programme ci-dessous:

- se connecte à la base de donnée (la connexion est plus complexe que dans
  l'exemple donné afin de pouvoir travailler directement sur le site),
- exécute la requête `select * from artist;`,
- récupère le résultat de la requête;
- affiche le résultat ligne par ligne.

1.  Exécutez le code. Comment le résultat est-il affiché?
2.  Pour améliorer l'affichage du résultat, complétez le programme pour qu'il
    affiche les informations des artistes précédées du nom des colonnes (nom,
    pays et label). Exécutez votre code pour vérifier votre réponse.

```{exec} python
:editor: d9f78b36-a803-440f-908d-0d5c423a4734
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Exécution de la requête
requete = base_donnees.execute("select * from artist;")

# Récupération du résultat de la requête
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne :
for resultat in resultats:
  print(resultat)
```

````{solution}
```{exec} python
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Exécution de la requête
requete = base_donnees.execute("select * from artist;")

# Récupération du résultat de la requête
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne avec nom de colonnes
for resultat in resultats:
  print("Nom:", resultat[0], "Pays:", resultat[1], "Label:", resultat[2])
```
````

### Exercice {nump}`exemple`

Complétez le programme pour qu'il affiche la liste de tous les albums précédés
du nom des colonnes (nom et année).


```{exec} python
:editor: 4fa0601b-a67e-4b1e-aa3a-52397de74db1
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Complétez le code ici
```

````{solution}
```{exec} python
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Exécution de la requête de sélection
requete = base_donnees.execute("select * from album;")

# Récupération du résultat de la requête
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne avec nom de colonnes
for resultat in resultats:
  print("Nom:", resultat[0], "Année:", resultat[1])
```
````

### Exercice {nump}`exemple`

Complétez le programme pour qu'il affiche la liste de toutes les chansons
chantées par Taylor Swift.


```{exec} python
:editor: 26cccff1-1b74-4199-96cb-d56aca348aad
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Complétez le code ici
```

````{solution}
```{exec} python
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Exécution de la requête de sélection
requete = base_donnees.execute("select sings_song from sings where sings_artist = 'Taylor Swift';")

# Récupération du résultat de la requête
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne:
for resultat in resultats:
  print(resultat[0])
```
````

### Exercice {nump}`exemple`

Complétez le programme pour qu'il affiche la liste de toutes les chansons, de
leur interpète et le nom de l'album qui sont du genre hip-hop.


```{exec} python
:editor: c5540bd0-a667-4158-a291-b67af30b4e8f
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Complétez le code ici
```

````{solution}
```{exec} python
import pathlib
import sqlite3

# Connexion à la base de données
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Exécution de la requête de sélection
requete = base_donnees.execute("select sings_song, sings_artist, song_album from sings join song on sings_song = song_name where song_genre = 'hip-hop';")

# Récupération du résultat de la requête
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne avec nom de colonnes
for resultat in resultats:
  print("Chanson:", resultat[0], "Interprète:", resultat[1], "Album:", resultat[2])
```
````

## Ajout de données dans la base de données

L'ajout de données se fait en trois étapes:

- Connexion à la base de données (à effectuer une fois au début du programme):

  ```{exec} python
  :when: never
  base_donnees = sqlite3.connect("nom_de_la_base")
  ```
  Par exemple:

  ```{exec} python
  :when: never
  base_donnees = sqlite3.connect("music.sqlite")
  ```

- Exécution de la requête d'ajout

  ```{exec} python
  :when: never
  base_donnees.execute("requete_ajout")
  ```

  Par exemple:

  ```{exec} python
  :when: never
  base_donnees.execute("insert into song values ('Leave Right Now', 2017, 'Life Changes', 'country');")
  ```

- Écriture dans la base de données (à effectuer à la fin de toutes les requêtes)

  ```{exec} python
  :when: never
  base_donnees.commit()
  ```

### Exercice {nump}`exemple`

1.  Ajoutez dans la table `song`, la chanson **Leave Right Now** sortie en
    **2017** de l'album **Life Changes** de genre **country**.
2.  Ajoutez dans la table `sings` que la chanson **Leave Right Now** est chantée
    par **Thomas Rhett**.
3.  Affichez toutes les chansons chantées par Thomas Rhett pour vérifier que
    votre ajout a bien fonctionné.

Complétez le programme pour qu'il affiche la liste de toutes les chansons, de
leur interpète et le nom de l'album qui sont du genre hip-hop.

```{exec} python
:editor: 794c2021-2659-4f11-98ce-a1b2513d32f9
```

````{solution}
```{exec} python
import pathlib
import sqlite3

# Connexion à la base de donnée
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Exécution de la requête d'ajout
base_donnees.execute("insert into song values ('Leave Right Now', 2017, 'Life Changes', 'country');")

# Exécution de la requête d'ajout
base_donnees.execute("insert into sings values ('Thomas Rhett', 'Leave Right Now');")

# Écriture dans la base de données
base_donnees.commit()

# Exécution de la requête de sélection
requete = base_donnees.execute("select sings_song from sings where sings_artist = 'Thomas Rhett';")

# Récupération du résultat de la requête
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne
for resultat in resultats:
  print(resultat[0])
```
````

### Exercice {nump}`exemple`

Quand quelque chose qui n'existe pas dans la base de données est recherché,
celle-ci retourne comme résultat une liste vide `[]`.

Avant d'ajouter des informations dans une table, il est préférable de vérifier
que ces informations n'y sont pas déjà.

```{exec} python
:when: never
if resultats == []:
  # Ajout des informations
else:
  print("Ces informations existent déjà.")
```

1.  Ajoutez dans la table `song`, la chanson **Blood** sortie en **2017** de
    l'album **DAMN.** de genre **hip-hop**.
2.  Ajoutez dans la table `sings` que la chanson **Blood** est chantée par
    **Kendrick Lamar**.
3.  Affichez toutes les chansons chantées par Kendrick Lamar pour vérifier que
    votre ajout a bien fonctionné.

```{exec} python
:editor: 1a1330c0-0290-4ccd-848d-3fbc45b35a52
```

````{solution}
```{exec} python
import pathlib
import sqlite3

# Connexion à la base de donnée
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Vérification si les informations existent déjà
requete = base_donnees.execute("select song_name from song where song_name = 'Blood';")
resultats = requete.fetchall()

if resultats == []:
  # Ajout des informations
  base_donnees.execute("insert into song values ('Blood', 2017, 'DAMN.', 'hip-hop');")
  base_donnees.execute("insert into sings values ('Kendrick Lamar', 'Blood');")
  base_donnees.commit()
else:
  print("Ces informations existent déjà.")

# Exécution de la requête de sélection
requete = base_donnees.execute("select sings_song from sings where sings_artist = 'Kendrick Lamar';")

# Récupération du résultat de la requête
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne:
for resultat in resultats:
  print(resultat[0])
```
````

### Exercice {nump}`exemple`

Essayez d'ajouter **Kendrick Lamar** des **United States** et du label **Top
Dawg Entertainment** dans la table. Vous devriez recevoir comme message que "Ces
informations existent déjà".

```{exec} python
:editor: f4889412-1130-4fe4-98e4-ddedec7b439f
```

````{solution}
```{exec} python
import pathlib
import sqlite3

# Connexion à la base de donnée
path = pathlib.Path('music.sqlite')
exists = path.exists()
base_donnees = sqlite3.connect(path)
if not exists:
  base_donnees.executescript(pathlib.Path('music.sql').read_text())

# Vérification si les informations existent déjà
requete = base_donnees.execute("select * from artist where artist_name = 'Kendrick Lamar';")
resultats = requete.fetchall()

if resultats == []:
  # Ajout des informations
  base_donnees.execute("insert into song values ('Kendrick Lamar', 'United States', 'Top Dawg Entertainment');")
  base_donnees.commit()
else:
  print("Ces informations existent déjà.")
```
````
