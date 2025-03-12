% Copyright 2024 Brice Canvel, modifié par Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Python et bases de données 1

```{metadata}
hide-solutions: true
```

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
base_donnees = sqlite3.connect("music")
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

Pour les exercices suivants, vou allez travailler dans Visual Studio Code.

### Exercice {num}`py-sql1`

Sauvegarde du fichier `main.py`:

1. Créez un dossier `music` sur OneDrive dans votre dossier `Informatique`.
2. Téléchargez le fichier [main.py](main.py) et sauvegardez-le dans le dossier
  `music`.
3. Démarrez VSCode et ouvrez le dossier `music` que vous avez créé sur OneDrive.

Création de la base de données:

1. Dans le dossier `music`, créez un nouveau fichier `music.sqlite`.
2. Ouvrir la base de données avec `Open Database` (clic droit).
3. Cliquez sur **SQLITE EXPLORER** et sélectionnez `New Query` en face de `music.sqlite`.
4. Un nouveau fichier s'est ouvert `SQLite Untitled-1`. Dans ce fichier, copiez le code ci-dessous.

````{admonition} Code à copier
    :class: dropdown

   ```{code-block} text
   CREATE TABLE genre (
    genre_name              VARCHAR(100)    PRIMARY KEY,
    genre_number_of_listeners       INT     NOT NULL
    );

    CREATE TABLE album (
        album_name          VARCHAR(100)    PRIMARY KEY,
        album_year          INT             NOT NULL
    );

    CREATE TABLE song (
        song_name           VARCHAR(100)    PRIMARY KEY,
        song_year           INT             NOT NULL,
        song_album          VARCHAR(100),
        song_genre          VARCHAR(100)    NOT NULL,
        FOREIGN KEY (song_album) REFERENCES album(album_name)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (song_genre) REFERENCES genre(genre_name)
            ON DELETE RESTRICT ON UPDATE CASCADE
    );

    CREATE TABLE record_label (
        record_label_name               VARCHAR(100)    PRIMARY KEY,
        record_label_revenue            INT             NOT NULL,
        record_label_origin_country     VARCHAR(100)    NOT NULL
    );

    CREATE TABLE artist (
        artist_name             VARCHAR(100)    PRIMARY KEY,
        artist_country          VARCHAR(100)    NOT NULL,
        artist_record_label     VARCHAR(100),
        FOREIGN KEY (artist_record_label) REFERENCES record_label(record_label_name)
            ON DELETE SET NULL ON UPDATE CASCADE
    );

    CREATE TABLE sings (
        sings_artist    VARCHAR(100)    NOT NULL,
        sings_song      VARCHAR(100)    NOT NULL,
        PRIMARY KEY (sings_artist, sings_song),
        FOREIGN KEY (sings_artist) REFERENCES artist(artist_name)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (sings_song) REFERENCES song(song_name)
            ON DELETE CASCADE ON UPDATE CASCADE
    );


    INSERT INTO genre VALUES
    ('hip-hop', 156),
    ('rock', 132),
    ('pop', 81),
    ('country', 49),
    ('latin', 38),
    ('electronic', 22),
    ('jazz', 6),
    ('classical', 6);

    INSERT INTO album VALUES
    ('DAMN.', 2017),
    ('Melodrama', 2017),
    ('Everybody', 2017),
    ('1989', 2014),
    ('Life Changes', 2017),
    ('Abbey Road', 1969),
    ('The Aviary', 2017);

    INSERT INTO song VALUES
    ('DNA.', 2017, 'DAMN.', 'hip-hop'),
    ('ELEMENT.', 2017, 'DAMN.', 'hip-hop'),
    ('FEEL.', 2017, 'DAMN.', 'hip-hop'),
    ('LOYALTY.', 2017, 'DAMN.', 'hip-hop'),
    ('HUMBLE.', 2017, 'DAMN.', 'hip-hop'),
    ('LOVE.', 2017, 'DAMN.', 'hip-hop'),
    ('Green Light', 2017, 'Melodrama', 'pop'),
    ('Sober', 2017, 'Melodrama', 'pop'),
    ('Homemade Dynamite', 2017, 'Melodrama', 'pop'),
    ('Liability', 2017, 'Melodrama', 'pop'),
    ('Hallelujah', 2017, 'Everybody', 'hip-hop'),
    ('Everybody', 2017, 'Everybody', 'hip-hop'),
    ('Mos Definitely', 2017, 'Everybody', 'hip-hop'),
    ('1-800-272-8255', 2017, 'Everybody', 'hip-hop'),
    ('Anziety', 2017, 'Everybody', 'hip-hop'),
    ('Welcome to New York', 2014, '1989', 'pop'),
    ('Blank Space', 2014, '1989', 'pop'),
    ('Shake It Off', 2014, '1989', 'pop'),
    ('Bad Blood', 2014, '1989', 'pop'),
    ('Wildest Dreams', 2014, '1989', 'pop'),
    ('How You Get The Girl', 2014, '1989', 'pop'),
    ('Craving You', 2017, 'Life Changes', 'country'),
    ('Unforgettable', 2017, 'Life Changes', 'country'),
    ('Sixteen', 2017, 'Life Changes', 'country'),
    ('Marry Me', 2017, 'Life Changes', 'country'),
    ('Come Together', 1969, 'Abbey Road', 'rock'),
    ('Something', 1969, 'Abbey Road', 'rock'),
    ('I Want You', 1969, 'Abbey Road', 'rock'),
    ('Here Comes The Sun', 1969, 'Abbey Road', 'rock'),
    ('Hey Alligator', 2017, 'The Aviary', 'electronic'),
    ('Girls On Boys', 2017, 'The Aviary', 'electronic'),
    ('Tell Me You Love Me', 2017, 'The Aviary', 'electronic'),
    ('Hunter', 2017, 'The Aviary', 'electronic'),
    ('Love On Me', 2017, 'The Aviary', 'electronic'),
    ('No Money', 2017, 'The Aviary', 'electronic'),
    ('Closer', 2016, NULL, 'pop'),
    ('Roses', 2015, NULL, 'pop'),
    ('Don''t Let Me Down', 2016, NULL, 'pop'),
    ('Something Just Like This', 2017, NULL, 'pop');


    INSERT INTO record_label VALUES
    ('Top Dawg Entertainment', 125, 'United States'),
    ('Universal Music Group', 150, 'United States'),
    ('Def Jam Recordings', 180, 'United States'),
    ('Big Machine Records', 130, 'United States'),
    ('Big Beat Records', 78, 'United States'),
    ('Sony Music Entertainment', 85, 'United States'),
    ('RCA Records', 50, 'United States'),
    ('Parlophone', 70, 'Germany');

    INSERT INTO artist VALUES
    ('Kendrick Lamar', 'United States', 'Top Dawg Entertainment'),
    ('Lorde', 'New Zealand', 'Universal Music Group'),
    ('Logic', 'United States', 'Def Jam Recordings'),
    ('Taylor Swift', 'United States', 'Big Machine Records'),
    ('Thomas Rhett', 'United States', 'Big Machine Records'),
    ('The Beatles', 'United States', NULL),
    ('Galantis', 'Sweden', 'Big Beat Records'),
    ('The Chainsmokers', 'United States', 'Sony Music Entertainment'),
    ('Rihanna', 'Barbados', 'Def Jam Recordings'),
    ('Alessia Cara', 'Canada', 'Def Jam Recordings'),
    ('Khalid', 'United States', 'RCA Records'),
    ('Coldplay', 'United Kingdom', 'Parlophone');

    INSERT INTO sings VALUES
    ('Kendrick Lamar', 'DNA.'),
    ('Kendrick Lamar', 'ELEMENT.'),
    ('Kendrick Lamar', 'FEEL.'),
    ('Kendrick Lamar', 'LOYALTY.'),
    ('Rihanna', 'LOYALTY.'),
    ('Kendrick Lamar', 'HUMBLE.'),
    ('Kendrick Lamar', 'LOVE.'),
    ('Lorde', 'Green Light'),
    ('Lorde', 'Sober'),
    ('Lorde', 'Homemade Dynamite'),
    ('Lorde', 'Liability'),
    ('Lorde', 'Hallelujah'),
    ('Logic', 'Everybody'),
    ('Lorde', 'Mos Definitely'),
    ('Logic', '1-800-272-8255'),
    ('Alessia Cara', '1-800-272-8255'),
    ('Khalid', '1-800-272-8255'),
    ('Logic', 'Anziety'),
    ('Taylor Swift', 'Welcome to New York'),
    ('Taylor Swift', 'Blank Space'),
    ('Taylor Swift', 'Shake It Off'),
    ('Taylor Swift', 'Bad Blood'),
    ('Kendrick Lamar', 'Bad Blood'),
    ('Taylor Swift', 'Wildest Dreams'),
    ('Taylor Swift', 'How You Get The Girl'),
    ('Thomas Rhett', 'Craving You'),
    ('Thomas Rhett', 'Unforgettable'),
    ('Thomas Rhett', 'Sixteen'),
    ('Thomas Rhett', 'Marry Me'),
    ('The Beatles', 'Come Together'),
    ('The Beatles', 'Something'),
    ('The Beatles', 'I Want You'),
    ('The Beatles', 'Here Comes The Sun'),
    ('Galantis', 'Hey Alligator'),
    ('Galantis', 'Girls On Boys'),
    ('Galantis', 'Tell Me You Love Me'),
    ('Galantis', 'Hunter'),
    ('Galantis', 'Love On Me'),
    ('Galantis', 'No Money'),
    ('The Chainsmokers', 'Closer'),
    ('The Chainsmokers', 'Roses'),
    ('The Chainsmokers', 'Don''t Let Me Down'),
    ('The Chainsmokers', 'Something Just Like This'),
    ('Coldplay', 'Something Just Like This');

```
````
5. Sélectionnez `Run Query` (clic droit).


### Exercice {num}`py-sql1`

Maintenant que la base de données a été créée, vous allez pouvoir faire des
requêtes.

Complétez le programme pour qu'il affiche les informations des artistes
précédées du nom des colonnes (nom, pays et label).

Exécutez votre code pour vérifier votre réponse.

````{solution}
```{exec} python
:when: never
import sqlite3

# Connexion à la base de données nommée music
base_donnees = sqlite3.connect("music.sqlite")

# Exécution de la requête de sélection
requete = base_donnees.execute("select * from artist;")

# Lecture des données
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne avec nom de colonnes
for resultat in resultats:
  print("Nom:", resultat[0], "Pays:", resultat[1], "label:", resultat[2])
```
````

### Exercice {num}`py-sql1`

Complétez le programme pour qu'il affiche la liste de tous les albums précédés
du nom des colonnes (nom et année).

````{solution}
```{exec} python
:when: never
import sqlite3

# Connexion à la base de données nommée music
base_donnees = sqlite3.connect("music.sqlite")

# Exécution de la requête de sélection
requete = base_donnees.execute("select * from album;")

# Lecture des données
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne avec nom de colonnes
for resultat in resultats:
  print("Nom:", resultat[0], "Année:", resultat[1])
```
````

### Exercice {num}`py-sql1`

Complétez le programme pour qu'il affiche la liste de toutes les chansons
chantées par Taylor Swift.

````{solution}
```{exec} python
:when: never
import sqlite3

# Connexion à la base de données nommée music
base_donnees = sqlite3.connect("music.sqlite")

# Exécution de la requête de sélection
requete = base_donnees.execute("select sings_song from sings where sings_artist = 'Taylor Swift';")

# Lecture des données
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne:
for resultat in resultats:
  print(resultat[0])
```
````

### Exercice {num}`py-sql1`

Complétez le programme pour qu'il affiche la liste de toutes les chansons, de
leur interpète et le nom de l'album qui sont du genre hip-hop.

````{solution}
```{exec} python
:when: never
import sqlite3

# Connexion à la base de données nommée music
base_donnees = sqlite3.connect("music.sqlite")

# Exécution de la requête de sélection
requete = base_donnees.execute("select sings_song, sings_artist, song_album from sings join song on sings_song = song_name where song_genre = 'hip-hop';")

# Lecture des données
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
  base_donnees = sqlite3.connect("music")
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

### Exercice {num}`py-sql1`

1. Ajoutez dans la table `song`, la chanson **Leave Right Now** sortie en
**2017** de l'album **Life Changes** de genre **country**.
2. Ajoutez dans la table `sings` que la chanson **Leave Right Now** est chantée
par **Thomas Rhett**.
3. Affichez toutes les chansons chantées par Thomas Rhett pour vérifier que
votre ajout a bien fonctionné.

````{solution}
```{exec} python
:when: never
import sqlite3

# Connexion à la base de données nommée music
base_donnees = sqlite3.connect("music.sqlite")

# Exécution de la requête d'ajout
base_donnees.execute("insert into song values ('Leave Right Now', 2017, 'Life Changes', 'country');")

# Exécution de la requête d'ajout
base_donnees.execute("insert into sings values ('Thomas Rhett', 'Leave Right Now');")

# Écriture dans la base de données
base_donnees.commit()

# Exécution de la requête de sélection
requete = base_donnees.execute("select sings_song from sings where sings_artist = 'Thomas Rhett';")

# Lecture des données
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne
for resultat in resultats:
  print(resultat[0])
```
````

### Exercice {num}`py-sql1`

Quand on recherche quelque chose qui n'existe pas dans la base de données,
celle-ci retourne comme résultat une liste vide [].

Avant d'ajouter des informations dans une table, il est préférable de vérifier
que ces informations n'y sont pas déjà.

```{exec} python
:when: never
if resultats == []:
  # Ajout des informations
else:
  print("Ces informations existent déjà.")
```

1. Ajoutez dans la table `song`, la chanson **Blood** sortie en **2017** de
l'album **DAMN.** de genre **hip-hop**.
2. Ajoutez dans la table `sings` que la chanson **Blood** est chantée par
**Kendrick Lamar**.
3. Affichez toutes les chansons chantées par Kendrick Lamar pour vérifier que
votre ajout a bien fonctionné.

````{solution}
```{exec} python
:when: never
import sqlite3

# Connexion à la base de données nommée music
base_donnees = sqlite3.connect("music.sqlite")

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

# Lecture des données
resultats = requete.fetchall()

# Affichage des résultats ligne par ligne:
for resultat in resultats:
  print(resultat[0])
```
````

### Exercice {num}`py-sql1`

Essayez d'ajouter **Kendrick Lamar** des **United States** et du label **Top
Dawg Entertainment** dans la table. Vous devriez recevoir comme message que "ces
informations existent déjà".

````{solution}
```{exec} python
:when: never
import sqlite3

# Connexion à la base de données nommée music
base_donnees = sqlite3.connect("music.sqlite")

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

