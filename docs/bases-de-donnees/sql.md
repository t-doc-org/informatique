<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# La langage SQL

Une **base de données** (BD) est un ensemble structuré d'informations
représentées par des tables et des relations entre ces tables. **SQL**
(Structured Query Language ou langage de requête structuré) est un langage qui
permet de créer des bases de données et/ou de récupérer les données répondant à
des critères particuliers.

## Création de tables

Le langage SQL permet de créer des tables en spécifiant leur nom et leurs
attributs.

```{note}
Par convention, nous écrirons les mots réservés du langage SQL en majuscule,
mais ce n'est pas obligatoire.
```

Pour créer une table, il faut utiliser l'instruction `CREATE TABLE {nom de la table} (...)`
suivi du nom de la table. Entre parenthèses, nous indiquons la liste des
attributs, ainsi que leur type.\
Chaque instruction doit se terminer par un point-virgule.

```{code-block} sql
CREATE TABLE livre (
    titre VARCHAR(100),     # chaîne de caractères de maximum 100 caractères
    editeur VARCHAR(20),
    annee INT,              # nombre entier (integer)
    isbn CHAR(14)           # chaîne de caractère avec exactement 14 caractères
);
```

## Exercice 1

Écrire l'instruction SQL qui permet de créer la table **auteur** ci-dessous,
sachant que **auteur_id** est un entier et que nom et prénom sont des chaînes
de caractères avec un maximum de 90 caractères:

| auteur_id | nom | prenom |
| :-------: | :-: | :----: |
| ... | ... | ... |

<!-- TODO: Ajouter un éditeur pour que les élèves puissent effectuer l'ex
    directement sur la page -->
<!-- TODO: Ajouter un affichage de la table créée si c'est possible -->

````{admonition} Solution
:class: hint dropdown
```{code-block} sql
CREATE TABLE auteur (
    auteur_id INT,
    nom VARCHAR(20),
    prenom VARCHAR(20)
);
```
````

## Ajout d'éléments

Pour insérer une nouvelle entité dans une table, il faut utiliser l'instruction
`INSERT INTO {nom de la table} VALUES (...);`. Entre parenthèses, nous indiquons
les valeurs des attributs. L'ordre doit être le même que lors de la création de
la table.

```{code-block} sql
INSERT INTO livre VALUES("Le Viel Homme et la Mer", "Editions Gallimard", 2018, "978-2072762093");
```

```{attention}
Comme en Python, les chaînes de caractères doivent être entre guillemets ou
apostrophes.
```

## Exercice 2

Écrire les instructions SQL qui permettent d'insérer dans la table auteur les
éléments ci-dessous:

| auteur_id | nom | prenom |
| :-------: | :-: | :----: |
| 1 | Hemingway | Ernest |
| 2 | Asimov | Isaac |
| 3 | Goscinny | René |

````{admonition} Solution
:class: hint dropdown
```{code-block} sql
INSERT INTO livre VALUES(1, "Hemingway", "Ernest");
INSERT INTO livre VALUES(2, "Asimov", "Isaac");
INSERT INTO livre VALUES(3, "Goscinny", "René");
```
````

## Affichage d'éléments

L'instruction SQL suivante permet d'afficher le contenu d'une table,
c'est-à-dire les valeurs de chaque attributs.

```{code-block} sql
SELECT * FROM livre;
```

Le caractère * signifie tous les attributs, cela évite de devoir écrire toute la
liste.
Traduite en français, cette instruction signifie: "Afficher tous les attributs
de la table livre."

Il est aussi possible d'afficher seulement un ou plusieurs des attributs.

```{code-block} sql
SELECT titre FROM livre;
SELECT titre, isbn FROM livre;
```

## Exercice 3

Écrire l'instruction SQL qui permet d'afficher toutes les entités de la table
**auteur**.

````{admonition} Solution
:class: hint dropdown
```{code-block} sql
SELECT * FROM auteur;
```
````

Écrire l'instruction SQL qui permet d'afficher le nom de tous les auteurs et
celle qui permet d'afficher le prénom et le nom de tous les auteurs.

````{admonition} Solution
:class: hint dropdown
```{code-block} sql
SELECT nom FROM auteur;
SELECT prenom, nom FROM auteur;
```
````

## Affichage d'éléments avec critères

Il est souvent utile de faire des recherches par critères, par exemple on
souhaiterait afficher tous les livres parus aux Editions Gallimards.

Voici la base de données à disposition:

| titre | editeur | annee | isbn |
| :---: | :-----: | :---: | :--: |
| Le Vieil Homme et la Mer | Editions Gallimard | 2018 | 978-2072762093 |
| Fondation et Empire | Editions Denoël | 1999 | 978-2207249123 |
| Ravage | Editions Gallimard | 2014 | 978-2072534911 |
| Demain les chiens | J'ai Lu | 2015 | 978-2290112168 |
| L'Homme qui rétrécit | Editions Gallimard | 2017 | 978-2072457340 |
| La Grande Traversée | Seuil Jeunesse | 2014 | 979-1023500448 |
| L'Étranger | Editions Gallimard | 2012 | 978-2072376429 |

L'instruction `WHERE` permet de ne sélectionner que les lignes qui répondent à
ce(s) critère(s).

```{code-block} sql
SELECT * FROM livre WHERE editeur = "Editions Gallimard";
```
Cette requête affichera le résultat suivant:

```{code-block} text
Le Vieil Homme et la Mer    Editions Gallimard     2018    978-2072762093
Ravage                      Editions Gallimard     2014    978-2072534911
L'Homme qui rétrécit        Editions Gallimard     2017    978-2072457340
L'Étranger                  Editions Gallimard     2012    978-2072376429
```

```{code-block} sql
SELECT * FROM livre WHERE annee = 2014;
```
Celle-ci affichera le résultat suivant:

```{code-block} text
Ravage                      Editions Gallimard     2014    978-2072534911
La Grande Traversée         Seuil Jeunesse         2014    979-1023500448
```

## Exercice 4

Écrire l'instruction SQL qui permet d'afficher tous les attributs de l'auteur
dont l'auteur_id est 3.

````{admonition} Solution
:class: hint dropdown
```{code-block} sql
SELECT * FROM auteur WHERE auteur_id = 3;
```
````

Écrire l'instruction SQL qui permet d'afficher le prénom de l'auteur dont le nom
est Asimov.

````{admonition} Solution
:class: hint dropdown
```{code-block} sql
SELECT prenom FROM auteur WHERE nom = "Asimov";
```
````




