% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Langage SQL - Notions avancées

## Clé primaire

Reprenons l'exemple du client. Lors de la création de la table client en SQL,
nous voulons spécifier que `no_c` est une clé primaire. Pour cela, nous ajoutons
l'attribut `primary key` en plus de `not null`. Ainsi, il sera impossible
d'insérer une ligne dans la table si la valeur de `no_c` existe déjà dans
celle-ci ou si elle est `null`.

<table><tr style="vertical-align: top"><td>

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

</td><td style="width: 70%">

```{exec} sql
:then: sql-client-select
create table client (
  no_c int not null primary key,  -- Ajouter aussi not null
  nom text not null,
  prenom text not null,
  adresse text,
  telephone text,
  mail text
);
```

```{exec} sql
:name: sql-client-select
:when: never
:class: hidden
select * from client;
```

</td></tr></table>

Si une clé primaire est définie au moyen de deux colonnes (par exemple, le nom
et le mail), nous utilisons la notation suivante:

```{exec} sql
:then: sql-client-select
create table client (
  nom text not null,                -- Ajouter not null, car clé primaire
  prenom text not null,
  adresse text,
  telephone text,
  mail text not null,               -- Ajouter not null, car clé primaire
  primary key (nom, mail)           -- Définit la clé primaire
);
```

## Exercice {num1}`exercice`

Recréer la table `produit` des exercices {numref}`exercice:produit-create` et
{numref}`exercice:produit-insert` en y ajoutant la clé primaire.

```{exec} sql
:then: sql-produit-select
:editor: 3abf3878-b6c5-4e8c-83f2-6109321d980d
```

```{exec} sql
:name: sql-produit-select
:when: never
:class: hidden
select * from produit;
```

````{solution}
```{exec} sql
:name: sql-produit
:then: sql-produit-select
create table produit (
    no_p int primary key not null,
    nom text not null,
    description text,
    prix int
);

insert into produit values
  (1, 'Ektorp', 'canapé 2 places', 599),
  (2, 'Brimnes', 'structure de lit', 129),
  (3, 'Jaren', 'matelas à ressorts', 59);
```
````

## Exercice {num1}`exercice`

Que se passe-t-il si on ajoute une ligne qui ne contient pas de valeur pour la
clé primaire? Tester avec l'exemple ci-dessous.

```{exec} sql
:after: sql-produit
insert into produit (nom, description, prix) values ('Fado', 'Lampe de table', 20);
```

## Exercice {num1}`exercice`

Créer et compléter la table `client` ci-dessous, sachant que `no_c` est un
entier et la clé primaire, `titre`, `prenom` et `nom` sont des chaînes de
caractères.

```{exec} sql
:after: sql-client
:then: sql-client-select
:when: load
:class: hidden
```

```{exec} sql
:then: sql-client-select
:editor: 21f2f19d-9502-44bc-a2d5-8cb9da24f4da
```

````{solution}
```{exec} sql
:name: sql-client
:then: sql-client-select
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

## Exercice {num1}`exercice`

Créer la table `achat` et la compléter avec les achats effectués par les
clients. La clé primaire est composée des deux colonnes `no_p` et `no_c`.

1. Alan Turing a acheté le canapé 2 places Ektrop.
2. Ada Lovelace a également acheté le canapé Ektrop.
3. Albert Einstein a acheté la structure de lit et le canapé.
4. Stephen Kleene n'a rien acheté.

```{exec} sql
:after: sql-achat
:then: sql-achat-select
:when: load
:class: hidden
```

```{exec} sql
:name: sql-achat-select
:when: never
:class: hidden
select * from achat;
```

```{exec} sql
:then: sql-achat-select
:editor: 13c2d3de-26a2-4d2b-81d3-851fd1868e60
```

````{solution}
```{exec} sql
:name: sql-achat
:then: sql-achat-select
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
:then: sql-achat-select
:when: load
:class: hidden
```

```{exec} sql
:name: sql-tables
:after: sql-produit sql-client sql-achat
:when: never
:class: hidden
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
`join ... on ...`.

La requête suivante retourne le(s) nom(s) du (des) produits acheté(s) par le
client n°3.

```{exec} sql
:after: sql-tables
select nom from produit        -- sélectionne la colonne nom de la table produit

  join achat                   -- joint la table précédente avec la table achat
  on produit.no_p=achat.no_p   -- condition de jointure

  where no_c=3;                -- critère de sélection
```

## Exercice {num1}`exercice`

Écrire la requête SQL qui retourne le(s) nom(s) du (des) produits acheté(s) par
le client n°1.

```{exec} sql
:after: sql-tables
:editor: 7682c01c-f46a-4800-b3e1-810f7308b7e9
```

````{solution}
```{exec} sql
:after: sql-tables
select nom from produit
  join achat on produit.no_p=achat.no_p
  where no_c=1;
```
````

## Exercice {num1}`exercice`

Écrire la requête SQL qui retourne le titre, le prénom et le nom des clients
ayant acheté le produit Ektorp.\
Trier les valeurs dans l'ordre alphabétique des prénoms.

```{exec} sql
:after: sql-tables
:editor: aec5da39-5a2a-4e0a-9805-1d1b8e3ff681
```

````{solution}
```{exec} sql
:after: sql-tables
select client.titre, client.prenom, client.nom from client
  join achat on client.no_c = achat.no_c
  where achat.no_p = 1
  order by prenom asc;
```
````

## Exercice {num1}`exercice`

Utiliser des jointures pour retourner la table ci-dessous (triée selon les
prénoms):

```{exec} sql
:after: sql-tables
:then: sql-ex-16-sol
:when: load
:class: hidden
```

```{exec} sql
:after: sql-tables
:editor: 8e0be548-feef-4705-84ea-b4c916db9c8b
```

````{solution}
```{exec} sql
:name: sql-ex-16-sol
:after: sql-tables
select client.no_c, client.prenom, client.nom, produit.no_p, produit.nom, prix
  from client

  join achat on client.no_c = achat.no_c    -- joint les tables client et achat
  join produit on achat.no_p=produit.no_p   -- joint les tables achat et produit

  order by prenom asc;
```
````
