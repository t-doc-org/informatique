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
    id INT,                 -- nombre entier (integer)
    article VARCHAR(15),    -- chaîne de caractères de maximum 15 caractères
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
INSERT INTO stock VALUES(1, 'T-shirt', 'rouge', 'M', 15, 20);
```

```{attention}
Les chaînes de caractères doivent être entre apostrophes (guillemets simples).
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
INSERT INTO produit VALUES(1, 'Ektorp', 'canapé 2 places', 599);
INSERT INTO produit VALUES(2, 'Brimnes', 'structure de lit', 129);
INSERT INTO produit VALUES(3, 'Jaren', 'matelas à ressorts', 59);
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

| id | article | couleur | taille | quantité | prixUnitaire |
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
SELECT * FROM stock WHERE stock='M';
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
SELECT * FROM produit WHERE nom='Brimnes';
```
````

Écrire la requête SQL qui permet d'afficher uniquement la description du produit
Ektorp.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
SELECT description FROM poduit WHERE nom='Ektorp';
```
````

## Modification de données

Pour modifier la couleur de l'article dont l'id est 3, la requête sera la
suivante:

```{code-block} sql
UPDATE stock SET couleur='bleu' WHERE id=3;
```

La base de donnée sera modifiée ainsi:

| id | article | couleur | taille | quantité | prixUnitaire |
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
UPDATE stock SET prix=499 WHERE description='canapé 2 places';

SELECT * FROM stock;                                                -- Pour tester le résultat
```
````

## Suppression d'éléments

Il est aussi possible de supprimer un élément, c'est-à-dire une ligne complète
d'une table.

```{code-block} sql
DELETE FROM stock WHERE article='Polo';
```

La nouvelle base de donnée sera la suivante:

| id | article | couleur | taille | quantité | prixUnitaire |
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

SELECT * FROM produit;                  -- Pour tester le résultat
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
INSERT INTO stock (no_p, article, prixUnitaire) VALUES (8, 'pantalon' , 20);
```
Une colonne sans valeur contient la [](#null).

Certaines colonnes ne doivent pas être vide sinon cela poserait problème, comme
id qui est un numéro unique qui permet de différencier les différents articles
ou la colonne article qui permet de savoir quel est le type d'article.
Il est possible d'obliger l'utilisateur à fournir ces informations lorsqu'il
ajoute un élément dans la table. Pour cela, il faut utiliser les mots
**NOT NULL** lors de la création de la table.

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

## Exercice 7

Créer une table eleve qui contient les informations des élèves: nom , prenom,
sexe, classe, naissance, email, adresse, code postal, ville, telephone.\
Quels sont les attributs obligatoires?\
Écrire la requête qui permet de créer cette table en choisissant le type
adapté.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
CREATE TABLE eleve (
    nom VARCHAR(30) NOT NULL,
    prenom VARCHAR(30) NOT NULL,
    sexe CHAR(1),
    naissance DATE NOT NULL,
    classe VARCHAR(4) NOT NULL,
    email VARCHAR(50) NOT NULL,
    adresse VARCHAR(200),
    code_postal CHAR(4),
    ville VARCHAR(30),
    telephone CHAR(12)
);
```
````

## Valeurs par défaut

Lorsqu'une colonne a généralement une même valeur, nous pouvons lui attribuer
une valeur par défaut, en anglais **DEFAULT**.

La valeur qui suit le mot réservé DEFAULT est automatiquement inséré dnas la
table si aucune valeur pour cet attribut n'est spécifiée.

La valeur par défaut doit être du même type de celui de la colonne.

| nom | description | prix |
| :-: | :---------: | :--: |
| Miel Amande | fourrée | 7.50 |
| Suzette | flambée | 5.00 |
| Citron | sirop | 5.00 |
| Sirop d'érable | sirop | 5.00 |
| Créme de marron | fourrée | 8.00 |

```{code-block} sql
CREATE TABLE crepe (
    nom VARCHAR(15) NOT NULL,
    description VARCHAR(7) NOT NULL,
    prix DEC(3,2) NOT NULL DEFAULT 5.00        -- la plupart des crêpes coûtent 5.00 CHF
);
```

## Exercice 8

Créer une table boisson qui contient la liste des prix des boissons de la
cafétéria.\
Écrire la requête qui permet de créer la table ci-dessous en utilisant une
valeur par défaut.\
Insérer les données du tableau ci-dessous.

| nom | prix |
| :-: | :--: |
| Espresso | 2.00 |
| Café | 2.00 |
| Café au lait | 2.50 |
| Cappuccino | 2.50 |
| Latte Macchiatto | 2.50 |
| Chocolat chaud | 2.50 |
| Chocolat froid | 2.50 |
| Thé | 2.00 |

````{admonition} Solution
:class: note dropdown
```{code-block} sql
CREATE TABLE boisson (
  nom VARCHAR(30) NOT NULL,
  prix DEC(3,2) NOT NULL DEFAULT 2.50
);

INSERT INTO boisson VALUES ('Espresso', 2.00);
INSERT INTO boisson VALUES ('Café', 2.00);
INSERT INTO boisson (nom) VALUES ('Café au lait');
INSERT INTO boisson (nom) VALUES ('Cappuccino');
INSERT INTO boisson (nom) VALUES ('Latte Macchiato');
INSERT INTO boisson (nom) VALUES ('Chocolat chaud');
INSERT INTO boisson (nom) VALUES ('Chocolat froid');
INSERT INTO boisson VALUES ('Thé', 2.00);

SELECT * FROM boisson;                                  -- Pour tester le résultat
```
````













