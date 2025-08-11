% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Langage SQL - Notions de base

Une **base de données** est un ensemble structuré d'informations représentées
par des tables et des relations entre ces tables. **SQL**[^sn1] est un langage
qui permet de créer des bases de données et/ou de récupérer les données
répondant à des critères particuliers.
[^sn1]: Structured Query Language (langage de requête structuré)

## Création de tables

Le langage SQL permet de créer des tables en spécifiant leur nom et le nom des
différentes colonnes.

Pour créer une table, il faut utiliser l'instruction `create table {nom de la
table} (...)` suivi du nom de la table. Entre parenthèses, nous indiquons la
liste des nom des colonnes, ainsi que leur [type](type-donnees.md).\
Chaque instruction doit se terminer par un point-virgule.

```{exec} sql
:name: sql-stock
:then: sql-stock-select
create table stock (
  id int,                 -- nombre entier (integer)
  article text,           -- chaîne de caractères
  couleur text,
  taille text,
  quantite int,
  prix_unitaire int
);
```

```{exec} sql
:name: sql-stock-select
:when: never
:class: hidden
select * from stock;
```

## Exercice {num2}`exercice:produit-create`

Écrire la requête SQL qui permet de créer la table `produit` ci-dessous,
sachant que `no_p` et `prix` sont des entiers et que `nom` et
`description` sont des chaînes de caractères:

```{exec} sql
:after: sql-produit
:then: sql-produit-select
:when: load
:class: hidden
```

```{exec} sql
:name: sql-produit-select
:when: never
:class: hidden
select * from produit;
```

```{exec} sql
:then: sql-produit-select
:editor: 4d2d44a5-b672-450b-bdf5-353c4c6da340
```

````{solution}
```{exec} sql
:name: sql-produit
:then: sql-produit-select
create table produit (
  no_p int,
  nom text,
  description text,
  prix int
);
```
````

## Insertion de lignes

Pour insérer une ligne dans une table, il faut utiliser l'instruction
`insert into {nom de la table} values (...);`. Entre parenthèses, nous indiquons
les valeurs des colonnes. L'ordre doit être le même que lors de la création de
la table.

```{exec} sql
:after: sql-stock
:name: sql-stock-insert1
:then: sql-stock-select
insert into stock values (1, 'T-shirt', 'rouge', 'M', 15, 20);
```

```{attention}
Les chaînes de caractères doivent être entourées d'apostrophes
(guillemets simples).
```

## Exercice {num2}`exercice:produit-insert`

Écrire les requêtes SQL qui permettent d'insérer dans la table `produit` les
lignes suivantes:

```{exec} sql
:after: sql-produit-insert
:then: sql-produit-select
:when: load
:class: hidden
```

```{exec} sql
:after: sql-produit
:then: sql-produit-select
:editor: 75970863-78ba-4cad-8724-641257d018f3
```

````{solution}
```{exec} sql
:name: sql-produit-insert
:after: sql-produit
:then: sql-produit-select
insert into produit values (1, 'Ektorp', 'canapé 2 places', 599);
insert into produit values (2, 'Brimnes', 'structure de lit', 129);
insert into produit values (3, 'Jaren', 'matelas à ressorts', 59);
```
````

## Affichage de lignes

La requête SQL suivante permet d'afficher le contenu d'une table,
c'est-à-dire les valeurs de chaque colonne.

```{exec} sql
:after: sql-stock-insert1
select * from stock;
```

Le caractère `*` signifie toutes les colonnes, cela évite de devoir écrire la
liste des noms des colonnes.
Traduite en français, cette instruction signifie: "Afficher toutes les colonnes
de la table stock."

Il est aussi possible d'afficher seulement une ou plusieurs colonnes.

```{exec} sql
:after: sql-stock-insert1
select article from stock;
```

```{exec} sql
:after: sql-stock-insert1
select article, quantite from stock;
```

## Exercice {num2}`exercice`

Écrire la requête SQL qui permet d'afficher toutes les lignes de la table
`produit`.

```{exec} sql
:after: sql-produit-insert
:editor: a2da982e-cff2-425a-8ed1-f1ae1229ad74
```

````{solution}
```{exec} sql
:after: sql-produit-insert
select * from produit;
```
````

Écrire la requête SQL qui permet d'afficher le `nom` de tous les produits.

```{exec} sql
:after: sql-produit-insert
:editor: 56820e63-edbf-48bd-b631-ae39461d77f0
```

````{solution}
```{exec} sql
:after: sql-produit-insert
select nom from produit;
```
````

Écrire la requête SQL qui permet d'afficher le `nom` et le `prix` de tous les
produits.

```{exec} sql
:after: sql-produit-insert
:editor: 02363fe1-0838-4df0-b05f-87a7e97bd4f0
```


````{solution}
```{exec} sql
:after: sql-produit-insert
select nom, prix from produit;
```
````

## Affichage de lignes avec critères

Il est souvent utile d'effectuer des recherches par critères, par exemple, nous
souhaiterions afficher tous les articles en taille M.

Voici la base de données à disposition:

```{exec} sql
:name: sql-stock-insert2
:after: sql-stock-insert1
:then: sql-stock-select
:when: load
:class: hidden
insert into stock values
  (2, 'T-shirt', 'blanc', 'XL', 17, 25),
  (3, 'Polo', 'rouge', 'L', 12, 35),
  (4, 'Polo', 'blanc', 'M', 10, 40),
  (5, 'T-shirt', 'rouge', 'XL', 8, 20),
  (6, 'T-shirt', 'blanc', 'S', 30, 20),
  (7, 'Veste', 'rouge', 'L', 5, 50);
```

L'instruction `where` permet de ne sélectionner que les lignes qui répondent à
ce(s) critère(s).

```{exec} sql
:after: sql-stock-insert2
select * from stock where taille = 'M';
```

```{exec} sql
:after: sql-stock-insert2
select * from stock where prix_unitaire = 35;
```

## Exercice {num2}`exercice`

Écrire la requête SQL qui permet d'afficher toutes les colonnes du produit
Brimnes.

```{exec} sql
:after: sql-produit-insert
:editor: bf813c8f-71a0-4aea-97d1-7e3bb5fab62a
```

````{solution}
```{exec} sql
:after: sql-produit-insert
select * from produit where nom = 'Brimnes';
```
````

Écrire la requête SQL qui permet d'afficher uniquement la description du produit
Ektorp.

```{exec} sql
:after: sql-produit-insert
:editor: 72ca4a83-6c72-4e56-a617-ed6181e7a980
```

````{solution}
```{exec} sql
:after: sql-produit-insert
select description from produit where nom = 'Ektorp';
```
````

## Modification de cellules

Pour modifier la couleur de l'article dont l'`id` est 3, la requête sera la
suivante:

```{exec} sql
:name: sql-stock-update
:after: sql-stock-insert2
:then: sql-stock-select
update stock set couleur = 'bleu' where id = 3;
```

## Exercice {num2}`exercice`

Mettre à jour le prix du **canapé 2 places** qui ne coûte plus que 499 CHF.

```{exec} sql
:after: sql-produit-insert
:then: sql-produit-select
:editor: d296c57b-c340-4d2c-9712-99dd651665fc
```

````{solution}
```{exec} sql
:name: sql-produit-update
:after: sql-produit-insert
:then: sql-produit-select
update produit set prix = 499 where description = 'canapé 2 places';
```
````

## Suppression de lignes

Il est aussi possible de supprimer une ligne complète d'une table.

```{exec} sql
:name: sql-stock-delete
:after: sql-stock-update
:then: sql-stock-select
delete from stock where article = 'Polo';
```

## Exercice {num2}`exercice`

Supprimer le produit dont le `no_p` est 3.\
Contrôler le résultat en affichant tous les éléments de la table produit.

```{exec} sql
:after: sql-produit-update
:then: sql-produit-select
:editor: 81de2da2-d302-4554-b87e-cf04d1cafd3c
```

````{solution}
```{exec} sql
:name: sql-produit-delete
:after: sql-produit-update
:then: sql-produit-select
delete from produit where no_p = 3;
```
````

## Colonnes sans valeur

Nous souhaitons compléter notre table stock avec l'article Pantalon dont le
numéro de produit est 8 et le prix unitaire 45 CHF. Nous ne connaissons pas
(encore) la couleur, la taille et la quantité.

Nous ne pouvons pas utiliser la requête utilisée précédemment (liste de toutes
les colonnes dans l'ordre), car nous n'avons pas toutes les informations, mais
nous pouvons spécifier que certaines colonnes.

```{exec} sql
:name: sql-stock-null
:after: sql-stock-delete
:then: sql-stock-select
insert into stock (id, article, prix_unitaire) values (8, 'Pantalon', 20);
```

Une colonne sans valeur contient la valeur [`null`](#null).

Certaines colonnes ne doivent pas être vides sinon cela poserait un problème,
comme id qui est un numéro unique qui permet de différencier les différents
articles ou la colonne article qui permet de savoir quel est le type d'article.
Il est possible d'obliger l'utilisateur à fournir ces informations lorsqu'il
ajoute un élément dans la table. Pour cela, il faut utiliser les mots réservés
`not null` lors de la création de la table.

```{exec} sql
:name: sql-stock2
:then: sql-stock-select
create table stock (
  id int not null,
  article text not null,
  couleur text,
  taille text,
  quantite int,
  prix_unitaire int
);
```

## Exercice {num2}`exercice`

Créer une table `eleve` qui contient les informations des élèves: nom, prénom,
sexe, classe, date de naissance, email, adresse, code postal, ville, téléphone.\
Quelles sont les colonnes obligatoires?\
Écrire la requête qui permet de créer cette table en choisissant le type
adapté pour chaque colonne.\
Ajouter une ligne avec vos propres informations sauf le numéro de téléphone.

```{exec} sql
:then: sql-eleve-select
:editor: db13712e-c734-47bf-af0e-3460cb6a2c9a
```

```{exec} sql
:name: sql-eleve-select
:when: never
:class: hidden
select * from eleve;
```

````{solution}
```{exec} sql
:then: sql-eleve-select
create table eleve (
  nom text not null,
  prenom text not null,
  sexe text,
  naissance date not null,
  classe text not null,
  email text not null,
  adresse text,
  code_postal text,
  ville text,
  telephone text
);

insert into eleve values
  ('Bob', 'Dubois', 'M', '2007-03-14', '2F9', 'bob.dubois@example.com',
   'Boulevard de Pérolle 11', '1700', 'Fribourg', null);
```
````

## Valeurs par défaut

Lorsqu'une colonne contient souvent la même valeur, il est possible de lui
attribuer une valeur par défaut, en anglais default.

La valeur qui suit le mot réservé `default` est automatiquement insérée dans la
table, si aucune valeur pour cette colonne n'est spécifiée.

La valeur par défaut doit être du même type que celui de la colonne.

```{exec} sql
:name: sql-crepe
:then: sql-crepe-select
create table crepe (
  nom text not null,
  description text not null,
  prix dec(3,2) not null default 5.00   -- souvent les crêpes coûtent 5.00 CHF
);

insert into crepe values
  ('Miel-Amande', 'fourrée', 7.5),
  ('Crème de marron', 'fourrée', 8);
insert into crepe (nom, description) values
  ('Suzette', 'flambée'),
  ('Citron', 'sirop'),
  ('Sirop d''érable', 'sirop');
```

```{exec} sql
:name: sql-crepe-select
:when: never
:class: hidden
select * from crepe;
```

## Exercice {num2}`exercice`

Créer une table boisson qui contient la liste des prix des boissons de la
cafétéria.\
Écrire la requête qui permet de créer la table ci-dessous en utilisant une
valeur par défaut.\
Insérer les données du tableau ci-dessous.

```{exec} sql
:after: sql-boisson
:then: sql-boisson-select
:when: load
:class: hidden
```

```{exec} sql
:name: sql-boisson-select
:when: never
:class: hidden
select * from boisson;
```

```{exec} sql
:editor: 336d388e-1795-475e-89e5-30e7c7cb99d2
:then: sql-boisson-select
```

````{solution}
```{exec} sql
:name: sql-boisson
:then: sql-boisson-select
create table boisson (
  nom text not null,
  prix dec(3,2) not null default 2.50
);

insert into boisson values
  ('Espresso', 2.00),
  ('Café', 2.00);
insert into boisson (nom) values
  ('Café au lait'),
  ('Cappuccino'),
  ('Latte Macchiato'),
  ('Chocolat chaud'),
  ('Chocolat froid');
insert into boisson values ('Thé', 2.00);
```
````
