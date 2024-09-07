<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Langage SQL - Notions de base

Une **base de données** est un ensemble structuré d'informations représentées
par des tables et des relations entre ces tables. **SQL**[^sn1] est un langage
qui permet de créer des bases de données et/ou de récupérer les données
répondant à des critères particuliers.
[^sn1]: Structured Query Language (langage de requête structuré)

## Création de tables

Le langage SQL permet de créer des tables en spécifiant leur nom et le nom des
différentes colonnes.

Pour créer une table, il faut utiliser l'instruction `create table {nom de la table} (...)`
suivi du nom de la table. Entre parenthèses, nous indiquons la liste des nom des
colonnes, ainsi que leur [type](./type-donnees.md).\
Chaque instruction doit se terminer par un point-virgule.

```{exec} sql
:name: sql-stock
:when: never
create table stock (
    id int,                 -- nombre entier (integer)
    article text,           -- chaîne de caractères
    couleur text,
    taille text,
    quantite int,
    prix_unitaire int
);
```

## Exercice 1

Écrire la requête SQL qui permet de créer la table `produit` ci-dessous,
sachant que `no_p` et `prix` sont des entiers et que `nom` et
`description` sont des chaînes de caractères:

```{exec} sql
:after: sql-produit
:when: load
:class: hidden
select * from produit;
```

<!-- TODO: Ajouter un éditeur pour que les élèves puissent effectuer l'ex
    directement sur la page -->

````{admonition} Solution
:class: note dropdown
```{exec} sql
:name: sql-produit
:when: never
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
:when: never
insert into stock values (1, 'T-shirt', 'rouge', 'M', 15, 20);
```

```{attention}
Les chaînes de caractères doivent être entourées d'apostrophes
(guillemets simples).
```

## Exercice 2

Écrire les requêtes SQL qui permettent d'insérer dans la table `produit` les
lignes suivantes:

```{exec} sql
:after: sql-produit-insert
:when: load
:class: hidden
select * from produit;
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-produit
:name: sql-produit-insert
:when: never
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

## Exercice 3

Écrire la requête SQL qui permet d'afficher toutes les lignes de la table
`produit`.

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-produit-insert
select * from produit;
```
````

Écrire la requête SQL qui permet d'afficher le `nom` de tous les produits et
celle qui permet d'afficher le `nom` et le `prix` de tous les produits.

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-produit-insert
select nom from produit;
```
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
:after: sql-stock-insert1
:name: sql-stock-insert2
:when: load
:class: hidden
insert into stock values
    (2, 'T-shirt', 'blanc', 'XL', 17, 25),
    (3, 'Polo', 'rouge', 'L', 12, 35),
    (4, 'Polo', 'blanc', 'M', 10, 40),
    (5, 'T-shirt', 'rouge', 'XL', 8, 20),
    (6, 'T-shirt', 'blanc', 'S', 30, 20),
    (7, 'Veste', 'rouge', 'L', 5, 50);
select * from stock;
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

## Exercice 4

Écrire la requête SQL qui permet d'afficher toutes les colonnes du produit
Brimnes.

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-produit-insert
select * from produit where nom = 'Brimnes';
```
````

Écrire la requête SQL qui permet d'afficher uniquement la description du produit
Ektorp.

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-produit-insert
select description from produit where nom = 'Ektorp';
```
````

## Modification de cellules

Pour modifier la couleur de l'article dont l'`id` est 3, la requête sera la
suivante:

```{exec} sql
:after: sql-stock-insert2
:name: sql-stock-update
update stock set couleur = 'bleu' where id = 3;
select * from stock;                                  -- pour afficher le résultat
```

## Exercice 5

Mettre à jour le prix du **canapé 2 places** qui ne coûte plus que 499 CHF.\
Contrôler le résultat en affichant tous les éléments de la table produit.

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-produit-insert
:name: sql-produit-update
update produit set prix = 499 where description = 'canapé 2 places';

select * from produit;                                 -- pour afficher le résultat
```
````

## Suppression de lignes

Il est aussi possible de supprimer une ligne complète d'une table.

```{exec} sql
:after: sql-stock-update
:name: sql-stock-delete
delete from stock where article = 'Polo';
select * from stock;                                  -- pour afficher le résultat
```

## Exercice 6

Supprimer le produit dont le `no_p` est 3.\
Contrôler le résultat en affichant tous les éléments de la table produit.

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-produit-update
delete from produit where no_p = 3;

select * from produit;                               -- pour afficher le résultat
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
:after: sql-stock-delete
:name: sql-stock-null
insert into stock (id, article, prix_unitaire) values (8, 'Pantalon' , 20);
select * from stock;                                  -- pour afficher le résultat
```
Une colonne sans valeur contient la valeur [null](#null).

Certaines colonnes ne doivent pas être vides sinon cela poserait un problème,
comme id qui est un numéro unique qui permet de différencier les différents
articles ou la colonne article qui permet de savoir quel est le type d'article.
Il est possible d'obliger l'utilisateur à fournir ces informations lorsqu'il
ajoute un élément dans la table. Pour cela, il faut utiliser les mots réservés
`not null` lors de la création de la table.

```{code-block} sql
create table stock (
    id int not null,
    article text not null,
    couleur text,
    taille text,
    quantite int,
    prix_unitaire int
);
```

## Exercice 7

Créer une table `eleve` qui contient les informations des élèves: nom, prénom,
sexe, classe, date de naissance, email, adresse, code postal, ville, téléphone.\
Quelles sont les colonnes obligatoires?\
Écrire la requête qui permet de créer cette table en choisissant le type
adapté pour chaque colonne.\
Ajouter une ligne avec vos propres informations sauf le numéro de téléphone.

````{admonition} Solution
:class: note dropdown
```{exec} sql
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

select * from eleve;
```
````

## Valeurs par défaut

Lorsqu'une colonne contient souvent la même valeur, il est possible de lui
attribuer une valeur par défaut, en anglais default.

La valeur qui suit le mot réservé `default` est automatiquement insérée dans la
table, si aucune valeur pour cette colonne n'est spécifiée.

La valeur par défaut doit être du même type que celui de la colonne.

| nom | description | prix |
| :-: | :---------: | :--: |
| Miel Amande | fourrée | 7.50 |
| Suzette | flambée | 5.00 |
| Citron | sirop | 5.00 |
| Sirop d'érable | sirop | 5.00 |
| Créme de marron | fourrée | 8.00 |

```{code-block} sql
create table crepe (
    nom text not null,
    description text not null,
    prix dec(3,2) not null default 5.00   -- souvent les crêpes coûtent 5.00 CHF
);
```

## Exercice 8

Créer une table boisson qui contient la liste des prix des boissons de la
cafétéria.\
Écrire la requête qui permet de créer la table ci-dessous en utilisant une
valeur par défaut.\
Insérer les données du tableau ci-dessous.

```{exec} sql
:after: sql-boisson
:when: load
:class: hidden
select * from boisson;
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:name: sql-boisson
create table boisson (
  nom text not null,
  prix dec(3,2) not null default 2.50
);

insert into boisson values ('Espresso', 2.00);
insert into boisson values ('Café', 2.00);
insert into boisson (nom) values ('Café au lait');
insert into boisson (nom) values ('Cappuccino');
insert into boisson (nom) values ('Latte Macchiato');
insert into boisson (nom) values ('Chocolat chaud');
insert into boisson (nom) values ('Chocolat froid');
insert into boisson values ('Thé', 2.00);

select * from boisson;                                -- pour afficher le résultat
```
````













