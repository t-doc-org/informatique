% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Bases de données relationnelles

Nous avons vu précédemment qu'il est pratique de stocker des données
semi-structurées dans des tables (ou tableaux). Grâce au langage SQL, il est
facile de les créer et de les manipuler.

Une **base de données** est un ensemble d'informations organisées pour être
facilement accessibles, gérées et mises à jour par ses utilisateurs. Par exemple,
dans une entreprise, toutes les données relatives aux clients sont stockées dans
une base de données.

## Tableur[^sn1]

Une approche simple serait d'utiliser un tableur pour stocker les informations.
[^sn1]: Logiciel pour la création et la manipulation de tableaux, par exemple
Excel.

Voici un exemple de tableau qui représente les achats effectués par des clients.
Les informations concernant le client sont son nom, son prénom et son adresse et
celles concernant le produit acheté sont le nom, la description et le prix.

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

L'utilisation d'un tableur n'est donc pas adaptée pour les grandes bases de
données.

## Modèle relationnel

Une autre approche est d'utiliser plusieurs tables reliées entre elles. Nous
parlons alors de **base de données relationnelle**.

Pour pouvoir relier des tables entre elles, il est nécessaire d'introduire
quelques concepts.

### Clé primaire

Une **clé primaire** est une colonne (ou une combinaison de colonnes) qui permet
d'identifier chaque enregistrement (ligne) d'une table de manière unique. Elle
doit donc être:
- unique (deux lignes distinctes ne peuvent pas avoir la même valeur pour la
colonne qui est clé primaire)
- stable (la valeur de la colonne qui est clé primaire ne doit pas changer au
cours du temps)

Si aucune colonne ne remplit ces critères, nous pouvons en créer une nouvelle
avec un compteur (la valeur augmentera toujours de 1).

#### Exemple - Cantons

````{list-grid}
:style: grid-template-columns: 3fr 7fr;
- ```{graphviz}
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
        <tr> <td> <b>canton</b> </td> </tr>
        <tr> <td>
          <table border="0" cellborder="0" cellspacing="7" >
            <tr> <td align="left"><u>nom </u> (clé primaire)</td> </tr>
            <tr> <td align="left" >abr</td> </tr>
            <tr> <td align="left" >chef_lieu</td> </tr>
            <tr> <td align="left" >nb_communes</td> </tr>
            <tr> <td align="left" >population</td> </tr>
            <tr> <td align="left" >superficie</td> </tr>
          </table>
        </td> </tr>
      </table>>
    ]
  }
  ```
- - Chaque canton a un nom différent et ne change pas.
  - Chaque abréviation est différente et ne change pas.
  - Les chefs-lieux sont en principe différents, mais pourrait changer.
  - Le nombre de communes peut être le même, voir même changer.
  - La population peut être la même et change.
  - La superficie peut être la même, voir même changer.
````

Dans cet exemple, nous pouvons donc choisir la colonne `nom` ou `abr` comme clé
primaire. Nous avons choisi `nom`.

#### Exemple - Clients

````{list-grid}
:style: grid-template-columns: 3fr 7fr;
- ```{graphviz}
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
          <table border="0" cellborder="0" cellspacing="7" >
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
- - Deux clients peuvent avoir le même nom.
  - Deux clients peuvent avoir le même prénom.
  - Deux clients peuvent avoir la même adresse et elle peut changer.
  - Le téléphone peut changer.
  - Le mail peut changer.
````

Dans cet exemple, aucune colonne ne correspond aux critères de clé primaire
(unique et stable). Par conséquent, il faut créer une nouvelle colonne en
ajoutant, par exemple, un numéro de client `no_c`.

### Clé étrangère

Une **clé étrangère** est une colonne qui contient une information qui est une
clé primaire d'une autre table.


### Schéma relationnel

Nous pouvons représenter une base de données relationnelles à l'aide d'un
schéma. Pour ce faire, il existe quelques règles à respecter:
1. Chaque table a un nom, suivi de la liste de ses colonnes.
2. Chaque table a une clé primaire indiquée grâce au soulignement.
3. Les flèches représentent les références entre les tables et pointent
toujours d'une clé étrangère vers une clé primaire.

```{tip}
Lorsque nous construisons une base de données relationnelles, il est essentiel
de s'assurer qu'il n'y a pas de duplication d'informations. S'il y a de la
redondance, il est souvent nécessaire d'ajouter une nouvelle table pour
normaliser les données.
```

Reprenons l'exemple du tableur avec le tableau d'achats. Un **achat** est une
relation entre un **client** et un **produit**. Pour construire une base de
données relationnelle, nous aurons donc besoin de trois tables distinctes:
client, produit et achat. La table achat contiendra deux informations: le numéro
de client et le numéro de produit. Ces deux éléments sont des clés étrangères,
notées `# no_c` et le `# no_p`. Comme un client peut acheter plusieurs produits
ou un produit peut être acheté par plusieurs clients, aucune des deux colonnes
ne peut être une clé primaire à elle seule. Dans ce cas, nous utilisons la
combinaison des deux colonnes comme clé primaire. Alternativement, nous aurions
pu créer une nouvelle colonne pour servir de clé primaire.


% TODO: Améliorer le rendu des diagrammes (titre, couleur).

```{graphviz}
:align: center
digraph UML_Class_diagram {
  graph [
    label="Schéma relationnel"
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
      <tr> <td> <b>produit</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
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
      <tr> <td> <b>client</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
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
      <tr> <td> <b>achat</b> </td> </tr>
      <tr> <td>
        <table border="0" cellborder="0" cellspacing="7" >
          <tr> <td align="left" port="a1"><u># no_p</u></td> </tr>
          <tr> <td port="a2" align="left" ><u># no_c</u></td> </tr>
          <tr> <td port="a2" align="left" ><u>date</u></td> </tr>
          <tr> <td port="a2" align="left" >quantite</td> </tr>
        </table>
      </td> </tr>
    </table>>
  ]
}
```

### Exercice {num1}`exercice`

Dessiner le schéma de la base de données relationnelle qui représente un système
de location de trottinettes électriques.
1. Quelles sont les différentes tables?
2. Quelles sont les colonnes de ces tables?
3. Existe-t-il déjà une clé primaire?
4. Y a-t-il des clés étrangères?
