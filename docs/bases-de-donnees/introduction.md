<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Introduction

## Gestion des données

Losque l'on utilise un ordinateur, beaucoup de données sont générées: des
documents, des images, des vidéos, de la musique, des mails, etc.
Ces différents **fichiers** sont accessibles sur votre ordinteur grâce aux
**système de fichiers**. Chaque fichier a une **extension** propre dépendante du
type de données qu'il contient (.txt, .docx, .pdf, .png, .jpg, .mp3, .py)

```{tip}
Pour retrouver facilement ses documents:

1. Utiliser une hiérachie de dossiers adéquate.\
Exemples: 1ère année, 2e année, maths, informatique, programmation, bases de
données
2. Choisir des noms de fichier qui permettent de savoir ce qu'ils contiennent.\
Exemples: ex1, théorie, exercices
```

Il existe 3 manières d'enregistrer des données:

1. Le **stockage** est l'enregistrement des fichiers sous forme de données
binaires sur un support physique (disque dur, clé USB, carte SSD, etc).
2. La **sauvegarde** (backup en anglais) est une copie des données pertinentes à
garder sous la main pour une restauration (restore en anglais) rapide en cas de
besoin.
3. L'**archivage** est l'enregistrement de fichiers pour des rétentions longues
à conserver, en général, pour des raisons légales.

Les sauvegardes sont importantes, car les pertes de données complètes ou
patielles peuvent arriver à tout moment. En voici quelques exemples:

1. Perte ou vol de matériel (ordinateur, téléphone, disque dur externe, etc.)
2. Défaut matériel ou logiciel (ordinateur qui ne démarre plus)
3. Erreur de manipulation (effacement de données)
4. Piratage, virus, rançongiciel

```{tip}
En sauvegardant vos données sur OneDrive, vous aurez toujours une copie
accessible de vos données en cas de problème avec votre ordinateur.
```

## Structure des données

### Formats non-structurés

Beaucoup de données sont partagées de manière **non-structurées**: mail,
conversation, message, texte, image, etc. On y trouve des données
**explicites**, mais aussi des données **implicites**, appelées **métadonnées**.

### Formats semi-structurés

Les **données semi-structurées** sont des données organisées de façon à
faciliter leur analyse. Une donnée est représentée par une paire
**propriété: valeur**:
- La propriété caractérise le type de la donnée.
- La valeur représente ce qu'elle vaut.

> Nom: Dupont\
> Prénom: Bob\
> Date de naissance: 15.09.2007\
> Classe: 2F8

#### Tableaux

Un **tableau** est une structure permettant de représenter un ensemble de
données sous forme de **lignes** et **colonnes**:
- un tableau (ou table) regroupe les données d'un ensemble **d'entités** de
même nature qui partage le même ensemble de **propriétés**.\
Exemples: des utilisateurs, des jeux, des élèves, des livres.
- une colonne du tableau correspond à **une et une seule propriété** commune aux
entités. Une colonne est caractérisée par son nom qui désigne la propriété
concernée.
- Une ligne du tableau correspond à **une et une seule entité** et est formée
de la liste des valeurs asssociées à chacune des propriétés pour l'entité
concernée.

```{image} images/tableau.png
:alt: Exemple de tableau
:align: center
```

#### Différents formats

Pour enregistrer le contenu d'une table de données, il faut pouvoir sauvegarder
sa structure et son contenu. Il existe différents types de fichiers texte qui
permettent cela, notamment les formats **CVS**, **XML** et **JSON**.

**CVS** est l'abréviation pour valeurs séparées par des virgules (Coma
Separated Values).\
Chaque ligne du fichier CVS correspond à une ligne de la
table.\
La première ligne du fichier énumère les noms des attributs des entités. Chaque
ligne suivante correpond à une entité.

```{code-block} text
:caption: eleves.cvs
nom, prenom, date de naissance, classe
Dupont, Bob, 15.09.2007, 2F8
Martin, Amandine, 01.01.2008, 2F7
Müller, Max, 29.02.2008, 2F7
Perroud, Marie, 01.11.2007, 2F8
```

**XML** est un langage de description de données appartenant à la même famille
que le HTML.\
La structure est définie par des balises dont les noms peuvent être librement
choisis.

```{code-block} xml
:caption: eleves.xml
<?xml version="1.0" encoding="UTF-8"?>
<eleves>
    <eleve id="0">
        <nom>Dupont</nom>
        <prenom>Bob</prenom>
        <naissance>15.09.2007</naissance>
        <classe>2F8</classe>
    <eleve>
    <eleve id="1">
        <nom>Marin</nom>
        <prenom>Amandine</prenom>
        <naissance>01.01.2008</naissance>
        <classe>2F7</classe>
    <eleve>
    <eleve id="2">
        <nom>Müller</nom>
        <prenom>Max</prenom>
        <naissance>29.02.2008</naissance>
        <classe>2F7</classe>
    <eleve>
    <eleve id="3">
        <nom>Perroud</nom>
        <prenom>Marie</prenom>
        <naissance>01.11.2007</naissance>
        <classe>2F8</classe>
    <eleve>
<eleves>
```

**JSON** (Javascript Object Notation) utilise la même syntaxe que le langage
de programmation Javascript.

```{code-block} javascript
:caption: eleves.json
[
    {
        "nom": "Dupont",
        "prenom": "Bob",
        "naissance": "15.09.2007",
        "classe": "2F8"
    },
    {
        "nom": "Marin",
        "prenom": "Amandine",
        "naissance": "01.01.2008",
        "classe": "2F7"
    },
    {
        "nom": "Müller",
        "prenom": "Max",
        "naissance": "29.02.2008",
        "classe": "2F7"
    },
    {
        "nom": "Perroud",
        "prenom": "Marie",
        "naissance": "01.11.2007",
        "classe": "2F8"
    }
]
```




