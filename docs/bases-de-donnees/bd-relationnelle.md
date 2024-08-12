<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Base de données

Nous avons vu précédemment qu'il est pratique de stocker des données
semi-structurées dans des tables (ou tableaux). Grâce au langage SQL, il est
facile de les créer et de les manipuler.

Une **base de données** est un ensemble d'informations organisées pour être
facilement accessible, géré et mis à jour par ses utilisateurs. Dans une école,
toutes les données relatives aux élèves et aux enseignants sont stockées dans
une base de données.

## Tableur[^sn1]

Une approche simple est d'utiliser un tableur pour stocker les informations.
[^sn1]: Logiciel pour la création et la manipulation de tableaux, par exemple
Excel.

Dans une entreprise, des clients achètent des produits. Les informations
concernant le client sont le nom, le prénom et l'adresse et celles concernant le
produit sont le nom, la description et le prix. Voici une représentation des
achats avec un tableau:

| nom_client | prenom | adresse | nom_produit | description | prix |
| :--------- | :----- | :------ | :---------- | :---------- | ---: |
| Duck | Donald | Bd de Pérolles 7<br> 1700 Fribourg | Ektorp | canapé 2 places | 499 |
| Léclair | Buzz | Rue de Centre 14<br> 1752 Villars-sur-Glâne | Brimnes | structure de lit | 129 |
| Duck | Donald | Bd de Pérolles 7<br> 1700 Fribourg | Brimnes | structure de lit | 129 |
| Léclair | Buzz | Rue de Centre 14<br> 1752 Villars-sur-Glâne | Jaren | matelas à ressorts | 59 |
| Lebricoleur | Bob | Rue de Lausanne 65<br> 1700 Fribourg  | Brimnes | structure de lit | 129 |

Que se passe-t-il si un client change d'adresse?

Les inconvénients de cette représentation sont les suivants:
1. Les informations sont **redondantes**: l'adresse du client ou la description
du produit apparaissent sur plusieurs lignes.
2. S'il y a un changement, il faut le faire à plusieurs endroits, sinon les
données ne sont plus cohérentes.

L'utilisation d'un tableur n'est pas adaptée pour les grandes bases de données.

## Base de données relationnelle

Une autre approche est d'utiliser plusieurs tables reliées entre elles. On parle
alors de **base de données relationnelle**.

En reprenant l'exemple précédent, nous utiliserions 3 tables.

1. Table client:\
On ajoute un numéro de client unique qui permet de différencier les clients.

| no_c | nom | prenom | adresse | telephone | mail |
| :---:| :-- | :----- | :------ | :-------: | :--: |
| 1 | Duck | Donald | Bd de Pérolles 7<br> 1700 Fribourg | 071 324 56 71 | donald.duck@proton.ch |
| 2 | Lebricoleur | Bob | Rue de Centre 14<br> 1752 Villars-sur-Glâne | 075 652 56 90 | bob.lebricoleur@gmail.com |
| 3 | Léclair | Buzz | Rue de la Lune 7<br> 1700 Fribourg | 070 589 09 12 | buzz.leclair@infomaniak.ch |

2. Table produit:

| no_p | nom | description | prix |
| :--: | :-- | :---------- | ---: |
| 1 | Ektorp | canapé 2 places | 599 |
| 2 | Brimnes | structure de lit | 129 |
| 3 | Jaren | matelas à ressorts | 59 |

3. Table achat:

| no_p | no_c |
| :--: | :--: |
| 1 | 1 |
| 2 | 3 |
| 2 | 1 |
| 3 | 3 |
| 1 | 2 |


<!-- TODO: Améliorer le rendu des diagrammes (titre, couleur). -->

```{graphviz}
:align: center
digraph UML_Class_diagram {
  graph [
    label="Modèle logique"
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
  edge [fontname="Helvetica,Arial,sans-serif"]
  edge [style=solid]
  Class3:a1 -> Class1:p1
  Class3:a2 -> Class2:c1

  Class1 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>PRODUIT</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="0" >
          <tr> <td align="left" port="p1"><u>no_p</u></td> </tr>
          <tr> <td port="p2" align="left" >nom</td> </tr>
          <tr> <td port="p3" align="left" >description</td> </tr>
          <tr> <td port="p4" align="left" >prix</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class2 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>CLIENT</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="0" >
          <tr> <td align="left" port="c1"><u>no_c</u></td> </tr>
          <tr> <td port="c2" align="left" >nom</td> </tr>
          <tr> <td port="c3" align="left" >prenom</td> </tr>
          <tr> <td port="c4" align="left" >adresse</td> </tr>
          <tr> <td port="c5" align="left" >telephone</td> </tr>
          <tr> <td port="c6" align="left" >mail</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

  Class3 [
    shape=plain
    label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
      <tr> <td> <b>ACHAT</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="0" >
          <tr> <td align="left" port="a1"><u># no_p</u></td> </tr>
          <tr> <td port="a2" align="left" ><u># no_c</u></td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]

}
```

<!-- TOTO: Ajouter une numérotation automatique des exercices par chapitre. -->

## Exercice 7

Écrire la requête SQL qui permet de créer la table **client** ci-dessous,
sachant que **no_c** est un entier et que **titre**, **prenom** et **nom** sont
des chaînes de caractères avec respectivement maximum de 3, 20 et 20 caractères:

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
  no_c int,
  titre text,
  prenom text,
  nom text
);

insert into client values (1, 'M', 'Albert', 'Einstein');
insert into client values (2, 'Mme', 'Ada', 'Lovelace');
insert into client values (3, 'M', 'Alan', 'Turing');
insert into client values (4, 'M', 'Stephen', 'Kleene');
);
```
````

## Exercice 8

Écrire les requêtes SQL qui permet de créer la table **achat** et d'y
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
plusieurs tables. La table de l'exercice précédent n'est pas très lisible pour
un humain:

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

Cela se fait avec une jointure entre 3 tables.

Pour joindre deux tables, il faut utiliser l'instruction
`join ... on ... where`.

La requête suivante permet d'afficher le(s) nom(s) du (des) produits acheté(s)
par le client n°3.

```{code-block} sql
select nom from produit        -- sélectionne l'attribut nom de la table produit

join achat                     -- joint la table précédente avec la table achat
on produit.no_p=achat.no_p     -- condition de jointure

where no_c=3;                  -- critère de sélection
```

## Exercice 9

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

## Exercice 10

Écrire la requête SQL qui permet d'afficher le **titre**, le **prénom** et le
**nom** des clients ayant acheté le produit Ektorp.\
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

## Exercice 11

Écrire la requête SQL qui permet d'afficher le tableau ci-dessous (trié selon
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

join achat on client.no_c = achat.no_c      -- joins les tables client et achat
join produit on achat.no_p=produit.no_p     -- joins les tables achat et produit

order by prenom asc;
```
````
