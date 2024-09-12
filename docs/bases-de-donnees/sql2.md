<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Langage SQL - Notions avancées

## Clé primaire

Reprenons l'exemple du client. Lors de la création de la table client en SQL,
nous voulons spécifier que `no_c` est une clé primaire. Pour cela, nous ajoutons
l'attribut `primary key` en plus de `not null`. Ainsi, il sera impossible
d'insérer une ligne dans la table si la valeur de `no_c` existe déjà dans
celle-ci ou si elle est `null`.

<table><tr><td valign="top">

```{graphviz}
:align: center
digraph UML_Class_diagram {
  graph [
    labelloc="t"
    fontname="Helvetica,Arial,sans-serif"
    fontsize="20pt"
    layout="circo"
  ]
  node [
    fontname="Helvetica,Arial,sans-serif"
    shape=record
    style=filled
    fillcolor=gray95
  ]

  Class1 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr><td><b>client</b></td></tr>
      <tr><td>
        <table border="0" cellborder="0" cellspacing="7">
          <tr><td align="left"><u>no_c</u> (clé primaire)</td></tr>
          <tr><td align="left" >nom</td></tr>
          <tr><td align="left" >prenom</td></tr>
          <tr><td align="left" >adresse</td></tr>
          <tr><td align="left" >telephone</td></tr>
          <tr><td align="left" >mail</td></tr>
        </table>
      </td></tr>
    </table>>
  ]

}
```

</td><td style="width:70%" valign="top">

```{exec} sql
:name: sql-client1
:when: never
create table client (
  no_c int not null primary key,    -- Ajouter aussi not null
  nom text not null,
  prenom text not null,
  adresse text,
  telephone text,
  mail text
);
```

```{exec} sql
:after: sql-client1
select * from client;
```

</td></tr></table>

Si une clé primaire est définie au moyen de deux colonnes (par exemple, le nom
et le mail), nous utilisons la notation suivante:

```{exec} sql
:name: sql-client2
:when: never
create table client (
  nom text not null,                -- Ajouter not null, car clé primaire
  prenom text not null,
  adresse text,
  telephone text,
  mail text not null,               -- Ajouter not null, car clé primaire
  primary key (nom, mail)           -- Défini la clé primaire
);
```

```{exec} sql
:after: sql-client2
select * from client;
```

<!-- TODO: Ajouter une numérotation automatique des exercices par chapitre. -->

## Exercice 10

Recréer la table `produit` de l'exercice 1 en y ajoutant la clé primaire.

```{exec} sql
:name: sql-produit-resp
:when: never
:editable:
```

```{exec} sql
:after: sql-produit-resp
select * from produit;
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:name: sql-produit
:when: never
create table produit (
    no_p int primary key not null,
    nom text not null,
    description text,
    prix int
);
```
````

## Exercice 11

Que se passe-t-il si on ajoute une ligne qui ne contient pas de valeur pour la
clé primaire? Tester avec l'exemple ci-dessous.

```{exec} sql
:after: sql-produit
insert into produit (nom, description, prix) values ('Fado', 'Lampe de table', 20);
select * from produit;
```

## Exercice 12

Créer et compléter la table `client` ci-dessous, sachant que `no_c` est un
entier et la clé primaire, `titre`, `prenom` et `nom` sont des chaînes de
caractères.

```{exec} sql
:after: sql-client
:when: load
:class: hidden
select * from client;
```

```{exec} sql
:name: sql-client-resp
:when: never
:editable:
```

```{exec} sql
:after: sql-client-resp
select * from client;
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:name: sql-client
:when: never
create table client (
  no_c int primary key not null,
  titre text,
  prenom text not null,
  nom text not null
);

insert into client values
  (1, 'M', 'Albert', 'Einstein'),    -- Evite d'écrire insert into à chaque ligne
  (2, 'Mme', 'Ada', 'Lovelace'),     -- Ne pas oublier la virgule à chaque ligne
  (3, 'M', 'Alan', 'Turing'),
  (4, 'M', 'Stephen', 'Kleene');     -- Ne pas oublier le point-virgule à la fin
```
````

## Exercice 13

Créer la table `achat` et la compléter avec les achats effectués par les
clients.

1. Alan Turing a acheté le canapé 2 places Ektrop.
2. Ada Lovelace a également acheté le canapé Ektrop.
3. Albert Einstein a acheté la structure de lit et le canapé.
4. Stephen Kleene n'a rien acheté.

```{exec} sql
:after: sql-achat
:when: load
:class: hidden
select * from achat where false;
```

```{exec} sql
:name: sql-achat-resp
:when: never
:editable:
```

```{exec} sql
:after: sql-achat-resp
select * from achat;
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:name: sql-achat
:when: never
create table achat (
  no_c int not null,
  no_p int not null,
  primary key(no_c, no_p)
);

insert into achat values (3, 1), (2, 1), (1, 2), (1, 1);
```
````

## Requête sur plusieurs tables

En SQL, il est souvent utile de fusionner toute ou une partie de deux ou
plusieurs tables. Par exemple, la table de l'exercice précédent n'est pas très
lisible pour un humain:

```{exec} sql
:after: sql-achat
:when: load
:class: hidden
select * from achat;
```

```{exec} sql
:name: sql-tables
:after: sql-produit sql-client sql-achat
:when: never
:class: hidden
insert into produit values
  (1, 'Ektorp', 'canapé 2 places', 599),
  (2, 'Brimnes', 'structure de lit', 129),
  (3, 'Jaren', 'matelas à ressorts', 59);
```

Il serait préférable que la table contienne aussi le prénom et le nom du client,
ainsi que le nom du produit acheté.\
Cela se fait au moyen d'une jointure. Celle-ci va créer une nouvelle table avec
les informations souhaitées.

```{exec} sql
:after: sql-tables
:when: load
:class: hidden
select client.no_c, client.prenom, client.nom, produit.no_p, produit.nom
  from client
  join achat on client.no_c = achat.no_c
  join produit on achat.no_p=produit.no_p
```

Pour joindre deux tables, il faut utiliser l'instruction
`join ... on ... where`.

La requête suivante permet d'afficher le(s) nom(s) du (des) produits acheté(s)
par le client n°3.

```{exec} sql
:after: sql-tables
select nom from produit        -- sélectionne la colonne nom de la table produit

  join achat                   -- joint la table précédente avec la table achat
  on produit.no_p=achat.no_p   -- condition de jointure

  where no_c=3;                -- critère de sélection
```

## Exercice 14

Écrire la requête SQL qui permet d'afficher le(s) nom(s) du (des) produits
acheté(s) par le client n°1.

```{exec} sql
:after: sql-tables
:editable:
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-tables
select nom from produit
  join achat on produit.no_p=achat.no_p
  where no_c=1;
```
````

## Exercice 15

Écrire la requête SQL qui permet d'afficher le titre, le prénom et le nom des
clients ayant acheté le produit Ektorp.\
Trier les valeurs dans l'ordre alphabétique des prénoms.

```{exec} sql
:after: sql-tables
:editable:
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-tables
select client.titre, client.prenom, client.nom from client
  join achat on client.no_c = achat.no_c
  where achat.no_p = 1
  order by prenom ASC;
```
````

<!-- TODO: éviter la duplication de code avec les joints, lorsque j'affiche le
          résultat dans l'énoncé de l'exercice. -->

## Exercice 16

Utiliser des jointures pour afficher la table ci-dessous (triée selon les
prénoms):
```{exec} sql
:after: sql-tables
:when: load
:class: hidden
select client.no_c, client.prenom, client.nom, produit.no_p, produit.nom, produit.prix
  from client
  join achat on client.no_c = achat.no_c
  join produit on achat.no_p=produit.no_p
  order by prenom asc;
```

```{exec} sql
:after: sql-tables
:editable:
```

````{admonition} Solution
:class: note dropdown
```{exec} sql
:after: sql-tables
select client.no_c, client.prenom, client.nom, produit.no_p, produit.nom, prix
  from client

  join achat on client.no_c = achat.no_c    -- joint les tables client et achat
  join produit on achat.no_p=produit.no_p   -- joint les tables achat et produit

  order by prenom asc;
```
````
