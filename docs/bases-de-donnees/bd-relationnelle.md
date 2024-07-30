<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Base de données

Nous avons vu précedemment qu'il est pratique de stocker des données
semi-structurées dans des tables (ou tableaux). Grâce au langage SQL, il est
facile de les créer et de les manipuler.

Une **base de données** est un ensemble d'informations organisées pour être
facilement accessible, géré et mis à jour par ses utilisateurs. Dans une école,
toutes les données relatives aux élèves et aux enseignants sont stockées dans
une base de données.

<!-- TODO: Afficher le menu du contenu, même lorsqu'une note est dans la marge
           lorsqu'il y a la place -->

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
| Léclair | Buzz | Rue de Centre 14<br> 1752 Villars sur Glâne | Brimnes | structure de lit | 129 |
| Duck | Donald | Bd de Pérolles 7<br> 1700 Fribourg | Brimnes | structure de lit | 129 |
| Léclair | Buzz | Rue de Centre 14<br> 1752 Villars sur Glâne | Jaren | matelas à ressorts | 59 |
| Lebricoleur | Bob | Rue de Lausanne 65<br> 1700 Fribourg  | Brimnes | structure de lit | 129 |

Que se passe-t-il si un client change d'adresse?

Les inconvénients de cette réprésentation sont les suivants:
1. Les informations sont **redondantes**: l'adresse du client ou la description
du produit apparaîssent sur plusieurs lignes.
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
| 2 | Lebricoleur | Bob | Rue de Centre 14<br> 1752 Villars sur Glâne | 075 652 56 90 | bob.lebricoleur@gmail.com |
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


<!-- TODO: Améliorer le rendu des diagrammes. -->

```{graphviz}
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

Écrire une instruction SQL qui permet de créer la table **client** ci-dessous,
sachant que **no_c** est un entier et que **titre**, **prenom** et **sont** sont
des chaînes de caractères avec respectivement maximum de 3, 20 et 20 caractères:

| no_c | titre | prenom | nom |
| :--: | :---: | :----: | :-: |
| 1 | M | Albert | Einstein |
| 2 | Mme | Ada | Lovelace |
| 3 | M | Alan | Turing |
| 4 | M | Stephen | Kleene |

Contrôler le résultat en affichant tous les éléments de la table.



````{admonition} Solution
:class: hint dropdown
```{code-block} sql
CREATE TABLE client (
  no_c INT,
  titre VARCHAR(3),
  prenom VARCHAR(20),
  nom VARCHAR(20)
);

INSERT INTO client VALUES (1, 'M', 'Albert', 'Einstein');
INSERT INTO client VALUES (2, 'Mme', 'Ada', 'Lovelace');
INSERT INTO client VALUES (3, 'M', 'Alan', 'Turing');
INSERT INTO client VALUES (4, 'M', 'Stephen', 'Kleene');
);
```
````

## Exercice 7

Écrire les instructions SQL permettant de créer la table **achat** et d'y
enregistrer les achats effectués par les clients:
1. Alan Turing a acheté le canapé 2 places Ektrop.
2. Ada Lovelace a également achaté le canapé Ektrop.
3. Albert Einstein a acheté la structure de lit et le canapé.
4. Stephen Kleene n'a rien acheté.

| no_c | no_p |
| :--: | :---: |
| ... | ... |
| ... | ... |
| ... | ... |

Contrôler le résultat en affichant tous les éléments de la table.



````{admonition} Solution
:class: hint dropdown
```{code-block} sql
CREATE TABLE achat (
  no_c INT,
  no_p INT
);

INSERT INTO achat VALUES (3, 1);
INSERT INTO achat VALUES (2, 1);
INSERT INTO achat VALUES (1, 2);
INSERT INTO achat VALUES (1, 1);
```
````
