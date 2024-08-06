<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# SQL Lab 1

Le but de cette section est d'entraîner les concepts vus dans la section
[](./sql.md).

Voici la table canton contenant certaines informations sur des cantons suisses.

| com | abr | chef_lieu | nb_communes | population | superficie |
| :----: | :--: | :-------: | :---------:  | :--------: | :--------: |
| Fribourg | FR | Fribourg | 126 | 334465 | 1670.7 |
| Genève | GE | Genève | 45 | 514114 | 282.48 |
| Berne | BE | Berne | 335 | 1051437 | 5959.44 |
| Zurich | ZH | Zurich | 160 | 1579967 | 1729 |
| Tessin | TI | Bellinzone | 106 | 354023 | 2812.2 |
| Grison | GR | Coire | 101 | 202538 | 7105.44 |
| Uri | UR | Altdorf | 19 | 37317 | 1076.57 |

## Exercice 1

Indiquer ce qu'afficheront les requêtes suivantes:

```{code-block} sql
SELECT * FROM canton WHERE nb_communes=45;
```

<!-- TODO: Cacher les solutions pour que les élèves ne puissent pas y accéder
            pendant qu'ils font les exercices. -->

````{admonition} Solution
:class: note dropdown
```{code-block} text
Genève    GE    Genève      45        514114      282.48
```
````

```{code-block} sql
SELECT * FROM canton WHERE chef_lieu=Coire;
```

````{admonition} Solution
:class: note dropdown
Cette requête produira une erreur, car il manque les guillemets simples autour
de Coire.
````

```{code-block} sql
SELECT nom, superficie FROM canton WHERE nom='Fribourg';
```

````{admonition} Solution
:class: note dropdown
```{code-block} text
Fribourg    1670.7
```
````

```{code-block} sql
SELECT * FROM canton WHERE population>500000;
```

````{admonition} Solution
:class: note dropdown
```{code-block} text
Genève    GE    Genève      45        514114      282.48
Berne     BE    Berne       335       1051437     5959.44
Zurich    ZH    Zurich      160       1579967     1729
```
````

```{code-block} sql
SELECT * FROM canton WHERE abr<'GR';
```

````{admonition} Solution
:class: note dropdown
Les opérateurs de comparaison pour du texte utilisent l'ordre alphabétique.\
Exemples: 'a' < 'b' ou 'p' > 'd'

```{code-block} text
Fribourg  FR    Fribourg    126       334465      1670.7
Genève    GE    Genève      45        514114      282.48
Berne     BE    Berne       335       1051437     5959.44
```
````

```{code-block} sql
SELECT * FROM canton ORDER BY superficie;
```
````{admonition} Solution
:class: note dropdown
```{code-block} text
Genève    GE    Genève      45        514114      282.48
Uri       UR    Altdorf     19        37317       1076.57
Fribourg  FR    Fribourg    126       334465      1670.7
Zurich    ZH    Zurich      160       1579967     1729
Tessin    TI    Bellinzone  106       354023      2812.2
Berne     BE    Berne       335       1051437     5959.44
Grison    GR    Coire       101       202538      7105.44

```
````

## Exercice 2

Créer et compléter la table canton avec des requêtes SQL. La table ne doit pas
accepter les valeurs NULL.\
Contrôler les réponses de l'exercice précédent.

```{code-block} sql
SELECT * FROM canton ORDER BY superficie;
```

````{admonition} Solution
:class: note dropdown
```{code-block} sql
CREATE TABLE canton (
  nom VARCHAR(30) NOT NULL,
  abr CHAR(2) NOT NULL,
  chef_lieu VARCHAR(30) NOT NULL,
  nb_communes SMALLINT NOT NULL,
  population INT NOT NULL,
  superficie DECIMAL(6,2) NOT NULL
);

INSERT INTO canton VALUES ('Fribourg', 'FR', 'Fribourg', 126, 334465, 1670.7);
INSERT INTO canton VALUES ('Genève', 'GE', 'Genève', 45, 514114, 282.48);
INSERT INTO canton VALUES ('Berne', 'BE', 'Berne', 335, 1051437, 5959.44);
INSERT INTO canton VALUES ('Zurich', 'ZH', 'Zurich', 160, 1579967, 1729);
INSERT INTO canton VALUES ('Tessin', 'TI', 'Bellinzone', 106, 354023, 2812.2);
INSERT INTO canton VALUES ('Grison', 'GR', 'Coire', 101, 202538, 7105.44);
INSERT INTO canton VALUES ('URI', 'UR', 'Altdorf', 19, 37317, 1076.57);
```
````

## Exercice 3

1. Écrire une requête SQL qui permet d'afficher toutes les informations du canton
dont le chef-lieu est Bellinzone.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM canton WHERE chef_lieu='Bellinzone';
```
````

2. Écrire une requête SQL qui permet d'afficher toutes les informations des
cantons dont la population est inférieure à 300'000 habitants.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM canton WHERE population<300000;
```
````

3. Écrire une requête SQL qui permet d'afficher toutes les informations des
cantons dans l'ordre alphabétique des abréviations.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM canton ORDER BY abr;
```
````

4. Écrire une requête SQL qui permet d'afficher le nom, l'abréviation et le
chef-lieu des cantons.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT nom, abr, chef_lieu FROM canton;
```

5. Écrire une requête SQL qui permet d'afficher le nom, l'abréviation et le
chef-lieu des cantons ordonnés selon le nombre d'habitants.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT nom, abr, chef_lieu FROM canton ORDER BY population;
```
````

6. Écrire une requête SQL qui permet d'afficher toutes les informations des
cantons qui ont plus de 100 communes et une population inférieure à 500'000
habitants.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM canton WHERE nb_communes>100 AND population<500000;
```
````

7. Écrire une requête SQL qui permet d'afficher toutes les informations des
cantons dont le chef-lieu est Altdorf ou le nombre de communes supérieur ou égal
à 150.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM canton WHERE chef_lieu='Altdorf' OR nb_communes>=150;
```
````

8. Écrire une requête SQL qui permet d'afficher le nom des cantons dont
l'abreviation n'est pas FR.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT nom FROM canton WHERE abr<>'FR';
```
````

9. Écrire une requête SQL qui permet d'afficher le nom et l'abréviation  des
cantons dont la population se trouvent entre 300'000 et 500'000 habitants.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT nom FROM canton WHERE population BETWEEN 300000 AND 500000;
```
````

## Exercice 4

Une application de rencontres demande, à l'enregistrement sur son site, les
informations suivantes: le nom, le prénom, l'adresse mail, le sexe,
la date de naissance, le statut, le lieu et les interêts principaux.\
Les champs obligatoires sont le nom, le prénom, adresse mail, le sexe et l'âge.

La table contact ressemble à cela:

| nom | prenom | email | sexe | anniversaire | statut | lieu | code_postal | interets |
| :-: | :----: | :---: | :--: | :----------: | :----: | :--: | :---------: | :------: |
| Dupont | Bob | dupont.bob@glog.com | M | 1990-09-10 | Divorcé | Villars-sur-Glânes | 1752 | Tennis, Animaux |
| Martin | Anne | amartin@fri.ch | F | 1995-06-02 | Célibataire | Lausanne | 1000 | Escape game |
| Dunant | Martine | martine.dunant@google.com | F | 1985-12-24 | Séparée | Val d'Illiez | 1873 | Lecture |
| Schmidt | Léo | leo@cine.ch | M | 2000-01-01 | Célibataire | La Roche | 1634 | Cinéma, Jeux de société |

<!-- TODO: Ajouter le lien pour le fichier contacts.sql et les instructions,
             si les élèves"travaillent sur replit.com
             [contacts.sql](./contacts.sql) -->

1. Rechercher les adresses mail de toutes les personnes célibataires.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT email FROM contact WHERE statut='Célibataire';
```
````

2. Recherche toutes les personnes qui habitent à Lausanne.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM contact WHERE lieu='Lausanne';
```
````

3. Rechercher toutes les personnes qui habitent dans la région lausannoise (le
code postal doit commencer par 10..).

````{tip}
Pour chercher des chaînes de caractères dans un mot, utiliser le mot
réservé **LIKE** et les caractères **%** pour remplacer plusieurs caractères ou
**_** qui remplace un seul caractère.

Pour trouver tous les contacts dont le prénom commence par Ma, utiliser
```{code-block} sql
SELECT * FROM contact WHERE prenom LIKE 'Ma%';
```

Pour trouver toutes les Laure ou les Laura dans la liste de contacts, utiliser
```{code-block} sql
SELECT * FROM contact WHERE prenom LIKE 'Laur_';
```
````

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM contact WHERE code_postal LIKE '10%';
```
````

4. Rechercher le nom, le prénom et la date de naissance de toutes les personnes
nées 1995.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT nom, prenom FROM contact WHERE naissance LIKE '1995-%';
```
````

5. Rechercher les contacts qui aiment le cinéma.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM contact WHERE interets LIKE '%Cinéma%';
```
````

6. Rechercher le nom, le prénom et la date de naissance de toutes les personnes
nées en juin.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT nom, prenom, naissance FROM contact WHERE naissance LIKE '%-06-%';
```
````

7. Rechercher tous les hommes qui sont célibataire et habitent dans la
région genevoise (12..).

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM contact WHERE sexe='M' AND statut='Célibataire' AND code_postal LIKE '12%';
```
````

8. Rechercher toutes les femmes qui sont divorcées et qui ont entre 30 et
40 ans.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM contact WHERE sexe='F' AND statut='Divorcée' AND naissance BETWEEN '1984-%' AND '1994-%';
```
````


