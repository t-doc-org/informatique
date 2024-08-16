<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Langage SQL - Notions avancées

## Clé primaire

Reprenons l'exemple du client. Lors de la création de la table client en SQL,
nous voulons spécifier que `no_c` est une clé primaire. Pour cela, nous ajoutons
l'attribut `primary key` en plus de `not null`. Ainsi, il sera impossible
d'insérer une ligne dans la table si la valeur de `no_c` existe déjà dans
celle-ci ou si elle est null.

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
      <tr> <td> <b>client</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="0" >
          <tr> <td align="left"><u>no_c </u> (clé primaire)</td> </tr>
          <tr> <td align="left" >nom</td> </tr>
          <tr> <td align="left" >prenom</td> </tr>
          <tr> <td align="left" >adresse</td> </tr>
          <tr> <td align="left" >telephone</td> </tr>
          <tr> <td align="left" >mail</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

}
```

</td><td style="width:70%" valign="top">


```{code-block} sql
create table client (
  no_c int not null primary key,    -- Ajouter aussi not null
  nom text not null,
  prenom text not null,
  adresse text,
  telephone text,
  mail text
);
```

</td></tr></table>


<!-- TOTO: Ajouter une numérotation automatique des exercices par chapitre. -->

## Exercice 10

Écrire la requête SQL qui permet de créer la table `client` ci-dessous,
sachant que `no_c` est un entier et la clé primaire, `titre`, `prenom` et `nom`
sont des chaînes de caractères:

| no_c | titre | prenom | nom |
| :--: | :---: | :----: | :-: |
| 1 | M | Albert | Einstein |
| 2 | Mme | Ada | Lovelace |
| 3 | M | Alan | Turing |
| 4 | M | Stephen | Kleene |

Contrôler le résultat en affichant tous les éléments de la table.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
create table client (
  no_c int primary key not null,
  titre text,
  prenom text,
  nom text
);

insert into client values
  (1, 'M', 'Albert', 'Einstein'),    -- Evite d'écrire insert into à chaque ligne
  (2, 'Mme', 'Ada', 'Lovelace'),     -- Ne pas oublier la virgule à chaque ligne
  (3, 'M', 'Alan', 'Turing'),
  (4, 'M', 'Stephen', 'Kleene');     -- Ne pas oublier le point-virgule à la fin
```
````

## Exercice 11

Écrire les requêtes SQL qui permet de créer la table `achat` et d'y
enregistrer les achats effectués par les clients:

1. Alan Turing a acheté le canapé 2 places Ektrop.
2. Ada Lovelace a également acheté le canapé Ektrop.
3. Albert Einstein a acheté la structure de lit et le canapé.
4. Stephen Kleene n'a rien acheté.

| no_c | no_p |
| :--: | :---: |
| ... | ... |
| ... | ... |
| ... | ... |

Contrôler le résultat en affichant tous les éléments de la table.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
create table achat (
  no_c int,
  no_p int
);

insert into achat values (3, 1);
insert into achat values (2, 1);
insert into achat values (1, 2);
insert into achat values (1, 1);
```
````

## Requête sur plusieurs tables

En SQL, il est souvent utile de fusionner toute ou une partie de deux ou
plusieurs tables. Par exemple, la table de l'exercice précédent n'est pas très
lisible pour un humain:

| no_c | no_p |
| :--: | :--: |
| 3 | 1 |
| 2 | 1 |
| 1 | 2 |
| 1 | 1 |

Il serait préférable que la table contienne aussi le prénom et le nom du client,
ainsi que le nom du produit acheté./
Cela se fait au moyen d'une jointure. Celle-ci va créer une nouvelle table avec
les informations souhaitées.

| no_c | prenom | nom | no_p | nom |
| :--: | :----: | :-: | :--: | :-: |
| 3 | Alan | Turing | 1 | Ektorp |
| 2 | Ada | Lovelace | 1 | Ektorp |
| 1 | Albert | Einstein | 2 | Brimnes |
| 1 | Albert | Einstein | 1 | Ektorp |

Pour joindre deux tables, il faut utiliser l'instruction
`join ... on ... where`.

La requête suivante permet d'afficher le(s) nom(s) du (des) produits acheté(s)
par le client n°3.

```{code-block} sql
select nom from produit        -- sélectionne la colonne nom de la table produit

join achat                     -- joint la table précédente avec la table achat
on produit.no_p=achat.no_p     -- condition de jointure

where no_c=3;                  -- critère de sélection
```

## Exercice 12

Écrire la requête SQL qui permet d'afficher le(s) nom(s) du (des) produits
acheté(s) par le client n°1.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
select nom from produit

join achat on produit.no_p=achat.no_p

where no_c=1;
```
````

## Exercice 13

Écrire la requête SQL qui permet d'afficher le titre, le prénom et le nom des
clients ayant acheté le produit Ektorp.\
Trier les valeurs dans l'ordre alphabétique des prénoms.

````{admonition} Solution
:class: note dropdown
```{code-block} sql
select client.titre, client.prenom, client.nom from client

join achat on client.no_c = achat.no_c

where achat.no_p = 1
order by prenom ASC;
```
````

## Exercice 14

Écrire la requête SQL qui permet d'afficher la table ci-dessous (triée selon
les prénoms):
| no_c | prenom | nom | no_p | nom | prix |
| :--: | :----: | :-: | :--: | :-: | :-: |
| 2 | Ada | Lovelace | 1 | Ektorp | 599 |
| 3 | Alan | Turing | 1 | Ektorp | 599 |
| 1 | Albert | Einstein | 1 | Ektorp | 599 |
| 1 | Albert | Einstein | 2 | Brimnes | 129 |


````{admonition} Solution
:class: note dropdown
```{code-block} sql
select client.no_c, client.prenom, client.nom, produit.no_p, produit.nom, prix
  from client

join achat on client.no_c = achat.no_c      -- joint les tables client et achat
join produit on achat.no_p=produit.no_p     -- joint les tables achat et produit

order by prenom asc;
```
````

