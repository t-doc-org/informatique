<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Langage SQL

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
attributs, ainsi que leur [type](./type-donnees.md).\
Chaque instruction doit se terminer par un point-virgule.

```{code-block} sql
CREATE TABLE stock (
    id INT,                 - nombre entier (integer)
    article VARCHAR(15),    - chaîne de caractères de maximum 15 caractères
    couleur VARCHAR(15),
    taille VARCHAR(3),
    quantite INT,
    prixUnitaire INT
);
```

## Exercice 1

Écrire la requête SQL qui permet de créer la table **produit** ci-dessous,
sachant que **no_p** et **prix** sont des entiers et que **nom** et **description** sont des chaînes
de caractères avec respectivement maximum de 20 et 100 caractères:

| no_p | nom | description | prix |
| :--: | :-: | :---------: | :--: |
| ... | ... | ... | ... |

<!-- TODO: Ajouter un éditeur pour que les élèves puissent effectuer l'ex
    directement sur la page -->
<!-- TODO: Ajouter un affichage de la table créée si c'est possible -->

````{admonition} Solution
:class: note dropdown
```{code-block} sql
CREATE TABLE produit (
    no_p INT,
    nom VARCHAR(20),
    description VARCHAR(100)
);
```
````

## Ajout d'éléments

Pour insérer une nouvelle entité dans une table, il faut utiliser l'instruction
`INSERT INTO {nom de la table} VALUES (...);`. Entre parenthèses, nous indiquons
les valeurs des attributs. L'ordre doit être le même que lors de la création de
la table.

```{code-block} sql
INSERT INTO stock VALUES(1, "T-shirt", "rouge", "M", 15, 20);
```

```{attention}
Comme en Python, les chaînes de caractères doivent être entre guillemets ou
apostrophes.
```

## Exercice 2

Écrire les instructions SQL qui permettent d'insérer dans la table produit les
éléments suivants:

| no_p | nom | description | prix |
| :--: | :-: | :---------: | :--: |
| 1 | Ektorp | canapé 2 places | 599 |
| 2 | Brimnes | structure de lit | 129 |
| 3 | Jaren | matelas à ressorts | 59 |

````{admonition} Solution
:class: note dropdown
```{code-block} sql
INSERT INTO produit VALUES(1, "Ektorp", "canapé 2 places", 599);
INSERT INTO produit VALUES(2, "Brimnes", "structure de lit", 129);
INSERT INTO produit VALUES(3, "Jaren", "matelas à ressorts", 59);
```
````

## Affichage d'éléments

L'instruction SQL suivante permet d'afficher le contenu d'une table,
c'est-à-dire les valeurs de chaque attributs.

```{code-block} sql
SELECT * FROM stock;
```

Le caractère * signifie tous les attributs, cela évite de devoir écrire toute la
liste d'attributs.
Traduite en français, cette instruction signifie: "Afficher tous les attributs
de la table stock."

Il est aussi possible d'afficher seulement un ou plusieurs des attributs.

```{code-block} sql
SELECT article FROM stock;
SELECT article, quantite FROM stock;
```

## Exercice 3

Écrire la requête qui permet d'afficher toutes les éléments de la table
**produit**.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM produit;
```
````

Écrire la requête SQL qui permet d'afficher le nom de tous les produits et
celle qui permet d'afficher le nom et le prix de tous les prduits.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT nom FROM produit;
SELECT nom, prix FROM produit;
```
````

## Affichage d'éléments avec critères

Il est souvent utile de faire des recherches par critères, par exemple on
souhaiterait afficher tous les livres parus aux Editions Gallimards.

Voici la base de données à disposition:

| id | article | couleur | taille | quantité | prixUnitaire
| :-: | :----: | :-----: | :----: | :------: | :----------: |
| 1 | T-shirt | rouge | M | 15 | 20 |
| 2 | T-shirt | blanc | XL | 17 | 25 |
| 3 | Polo | rouge | L | 12 | 35 |
| 4 | Polo | blanc | M | 10 | 40 |
| 5 | T-shirt | rouge | XL | 8 | 20 |
| 6 | T-shirt | blanc | S | 30 | 20 |
| 7 | Veste | rouge | L | 5 | 50 |

L'instruction `WHERE` permet de ne sélectionner que les lignes qui répondent à
ce(s) critère(s).

```{code-block} sql
SELECT * FROM stock WHERE stock="M";
```
Cette requête affichera le résultat suivant:

```{code-block} text
1   T-shirt     rouge   M   15  20
4   Polo        blanc   M   10  40
```

```{code-block} sql
SELECT * FROM stock WHERE prix=35;
```
Celle-ci affichera le résultat suivant:

```{code-block} text
3   Polo        rouge   L   12  35
```

## Exercice 4

Écrire la requête SQL qui permet d'afficher tous les attributs du produit
Brimnes.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT * FROM produit WHERE nom="Brimnes";
```
````

Écrire la requête SQL qui permet d'afficher uniquement la description du produit
Ektorp.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT description FROM poduit WHERE nom="Ektorp";
```
````

## Modification de données

Pour modifier la couleur de l'article dont l'id est 3, la requête sera la
suivante:

```{code-block} sql
UPDATE stock SET couleur="bleu" WHERE id=3;
```

La base de donnée sera modifiée ainsi:

| id | article | couleur | taille | quantité | prixUnitaire
| :-: | :----: | :-----: | :----: | :------: | :----------: |
| 1 | T-shirt | rouge | M | 15 | 20 |
| 2 | T-shirt | blanc | XL | 17 | 25 |
| 3 | Polo | **bleu** | L | 12 | 35 |
| 4 | Polo | blanc | M | 10 | 40 |
| 5 | T-shirt | rouge | XL | 8 | 20 |
| 6 | T-shirt | blanc | S | 30 | 20 |
| 7 | Veste | rouge | L | 5 | 50 |

## Exercice 5

Mettre à jour le prix du **canapé 2 places** qui ne coûte plus que 499 CHF.\
Contrôler le résultat en affichant tous les éléments de la table produit.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
UPDATE stock SET prix=499 WHERE description="canapé 2 places";
```
````

## Suppression d'éléments

Il est aussi possible de supprimer un élément, c'est-à-dire une ligne complète
d'une table.

```{code-block} sql
DELETE FROM stock WHERE article="Polo";
```

La nouvelle base de donnée sera la suivante:

| id | article | couleur | taille | quantité | prixUnitaire
| :-: | :----: | :-----: | :----: | :------: | :----------: |
| 1 | T-shirt | rouge | M | 15 | 20 |
| 2 | T-shirt | blanc | XL | 17 | 25 |
| 5 | T-shirt | rouge | XL | 8 | 20 |
| 6 | T-shirt | blanc | S | 30 | 20 |
| 7 | Veste | rouge | L | 5 | 50 |

## Exercice 6

Supprimer le produit dont le no_p est 3.\
Contrôler le résultat en affichant tous les éléments de la table produit.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
DELETE FROM produit WHERE no_p=3;
```
````

## Colonnes sans valeur

Nous souhaitons compléter notre table stock avec l'article Pantalon dont le
numéro de produit est 8 et le prix unitaire
45 CHF. Nous ne connaissons pas (encore) la couleur, la taille et la quantité.

Nous ne pouvons pas utiliser la requête utilisée précédemment (liste de tous les
attributs dans l'ordre), car nous n'avons pas toutes les informations, mais nous
pouvons spécifier que certains attributs.

```{code-block} sql
INSERT INTO stock (no_p, article, prixUnitaire) VALUES (8, "pantalon" , 20);
```
<!-- TODO: Faire en sorte que le lien amène au bon endroit de la page-->
Une colonne sans valeur contient la valeur [NULL](./type-donnees.md).

Certaines colonnes ne doivent pas être vide sinon cela posera problème, comme
id qui est un numéro unique qui permet de différencier les différents articles
ou la colonne article qui permet de savoir quel est le type d'article.
Il est possible d'obliger l'utilisateur à fournir ces informations lorsqu'il
ajoute un élément en utilisant les mots **NOT NULL** lors de la création de la
table.

 ```{code-block} sql
CREATE TABLE stock (
    id INT NOT NULL,
    article VARCHAR(15) NOT NULL,
    couleur VARCHAR(15),
    taille VARCHAR(3),
    quantite INT,
    prixUnitaire INT
);
```



















