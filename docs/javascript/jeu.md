% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Labo - Jeu

```{metadata}
solutions: dynamic
```

## Introduction

Pendant ce labo, vous allez développer la version "Lights In", du jeu
["Lights Out"](https://fr.wikipedia.org/wiki/Lights_Out_(jeu)), dont le but
est d'allumer toutes les cellules.

Règle du jeu:\
Lorsqu'on clique sur une cellule, celle-ci change d'état ainsi que ses quatre
voisines (au sud, à l'est, au nord et à l'ouest), si elles existent.

## Programmation

En vous aidant de l'{numref}`exemple %s<ex-js:exemple>`, programmez les étapes
ci-dessous dans l'ordre.

``````{tab-set}
:sync-group: etape
`````{tab-item} Étape 1
:sync: etape1
En utilisant les éléments HTML appropriés, commencez par créer la page statique
de votre jeu avec un titre, les règles du jeu, ainsi que le but. Ajoutez un
tableau de dimension 3x3.

````{tip}
:class: dropdown
Utilisez un tableau sans entête.
````

`````
`````{tab-item} Étape 2
:sync: etape2
Ajoutez du style à votre page pour que:

1. le tableau ait des bordures,
2. la hauteur et la largeur des cellules soient de 50px,
3. la couleur de fond des cellules soit d'une autre couleur,
4. le tableau soit centré.

````{tip}
:class: dropdown
Utilisez des sélecteurs de type.

Pour que le tableau soit centré, les marges à droite et à gauche doivent être
automatiques.

Les différents propriétés nécessaires sont:\
`border`, `border-collapse`, `width`, `height`, `margin-left`, `margin-right`,
`margin-top`
````

`````
`````{tab-item} Étape 3
:sync: etape3
Dans la partie script, ajoutez la fonctionnalité suivante en définissant la
fonction `changeEtat(event)`:

Lorsque vous cliquez sur une cellule du tableau, le texte "clic" doit s'afficher
dans celle-ci. Cela permettra de vérifier que les clics dans les cellules sont
correctement détectés.

````{tip}
:class: dropdown
Programmez les éléments suivants en javascript (dans la partie `<script>`):

1.  Créez une liste des cellules.
2.  Effectuez une boucle sur toutes les cellules pour ajouter `addEventListener`.
3.  Définissez la fonction `changeEtat(event)` qui a un paramètre `event` qui est
    déclenché par le clic de la souris (ou du touchpad).
    ```{exec} html
    :when: never
    function changeEtat(event) {
        const c = event.target;    // récupère l'élément html ciblé par le clic
        ...                        // écrit "clic" dans la cellule
    }
    ```
````

`````
`````{tab-item} Étape 4
:sync: etape4
Modifiez la fonction `changeEtat(event)` pour que lorsque vous cliquez sur une
cellule, celle-ci change d'état. Si elle est allumée (colorée), elle s'éteint
(sans couleur de fond) et vice-versa.

````{tip}
:class: dropdown
1.  Trouvez la propriété qui permet de changer la couleur de fond d'une cellule.
2.  Pour changer la couleur d'une cellule, utiliser une classe "allume".
    -   dans la partie style, définissez le style de la classe "allume"
        (choisissez une couleur de fond).
        ```{exec} html
        :when: never
        .allume {
        /* complétez par la propriété et la valeur désirée */
        }
        ```
    -   ajoutez la classe "allume" au `<td>` de la cellule pour l'allumer et en
        la supprimant pour l'éteindre. Cela se fait au moyen de:
        ```{exec} html
        :when: never
        c.classList.toggle("allume");  // ajoute la classe "allume" à l'élément ou l'efface
        ```
        Ce code doit remplacer `c.textContent = "clic"`.
````

`````
`````{tab-item} Étape 5
:sync: etape5
Ajoutez la fonctionnalité suivante:

Au début du jeu, l'état des cellules doit être déterminé de manière aléatoire.

````{tip}
:class: dropdown
La fonction `Math.random()` renvoie un nombre à virgule pseudo-aléatoire compris
dans l'intervalle [0, 1[.

Parcourez toutes les cellules (ce que vous avez déjà programmé à l'étape 3) et
colorez-en certaines en utilisant la fonction `Math.random()` et en leur
ajoutant la classe "allume".
```{exec} html
:when: never
c.classList.add("allume");  // ajoute la classe entre parenthèse à l'élément c
```
````

`````
`````{tab-item} Étape 6
:sync: etape6
Programmez la fin de la partie, c'est-à-dire le moment où toutes les cellules
sont allumées:

1.  Définissez une fonction `gagne(liste)` qui teste si toutes les cellules sont
    allumées.
2.  Après avoir changé l'état des cellules, vérifiez si la partie est gagnée.
3.  Si c'est le cas, affichez le message de victoire.

````{tip}
:class: dropdown
1.  Dans la fonction `gagne`, parcourez la liste des cellules et dès qu'une
    cellule n'est pas allumée, renvoyez `False` (le but n'est pas atteint). À la
    fin de la fonction, renvoyez `True` (toutes les cellules sont allumées).
2.  Pour afficher du texte sur la page, regardez l'affichage de l'erreur dans
    l'{numref}`exemple %s<ex-js:exemple>`.
````

`````
`````{tab-item} Étape 7
:sync: etape7
Modifiez la fonction `changeEtat(event)` pour qu'elle suive la règle du jeu,
c'est-à-dire qu'elle modifie aussi les 4 cellules voisines (au nord, sud, est et
ouest).

````{tip}
:class: dropdown
Il est plus facile de travailler avec des coordonnées x et y pour le tableau
plutôt que d'utiliser l'index. Voici le code qui permet de convertir l'index
en coodonnées x et y:
```{exec} html
const c = event.target;             // retourne l'élément ciblé
const index = cellules.indexOf(c);  // retourne l'index de l'élément ciblé
const x = index % larg;             // calcule la coordonnée x en fonction de l'index
const y = Math.trunc(index / larg); // calcule la coordonnée y en fonction de l'index
```
Et celui pour convertir les coordonnées x et y en index:
```{exec} html
function changeCoordEnIndex(x, y) {
    return y * larg + x;
}
```
````
`````
``````

```{exec} html
:when: load
:editor: 74030d10-6a1c-40a9-8e43-5818b63085cf
:style: height: 30rem
:output-style: height: 30rem
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Création d'un jeu</title>
<style>
/* Ajout des styles CSS */

</style>
</head>
<body>
<!-- Ajout des éléments HTML -->

<script>
/* Ajout du JavaScript */

</script>
</body>
</html>
```

````{Solution}
```{exec} html
:when: load
:style: height: 30rem
:output-style: height: 30rem
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Création d'un jeu</title>
<style>
table {
    margin-top: 1em;
    border: 1px solid black;
    border-collapse: collapse;
    margin-left:auto;
    margin-right:auto;
}
td {
    border: 1px solid black;
    width: 50px;
    height: 50px;
}
.allume {
    background: yellow;
}
#gagne {
    margin-top: 1em;
    text-align: center;
    font-weight: bold;
    color: #c71585;
}
</style>
</head>
<body>
<h1>Création d'un jeu</h1>

<h2>Règles du jeu</h2>
<p>Lorsqu'on clique sur une case, celle-ci change d'état ainsi que ses quatre
    voisines (au sud, à l'est, au nord et à l'ouest), si elles existent.</p>

<h2>But</h2>
<p>Allumer toutes les cellules.</p>

<table class="cellules">
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
</table>
<div id="gagne"></div>

<script>
const larg = 3, haut = 3;
const cellules = [...document.querySelectorAll(".cellules td")];

function changeCoordEnIndex(x, y) {
    return y * larg + x;
}

function gagne(liste) {
    for (const c of liste) {
        if (!c.classList.contains("allume")) {
            return false;
        }
    }
    return true;
}

/* change l'état de la case cliquée */
function changeEtat(event) {
    const c = event.target;
    const index = cellules.indexOf(c);
    const x = index % larg;
    const y = Math.trunc(index / larg);
    cellules[changeCoordEnIndex(x, y)].classList.toggle("allume");
    /* Vérifie qu'on n'est pas sur la première ligne */
    if (y > 0) {
        cellules[changeCoordEnIndex(x, y - 1)].classList.toggle("allume");
    }
    /* Vérifie qu'on n'est pas sur la dernière ligne */
    if (y < haut - 1) {
        cellules[changeCoordEnIndex(x, y + 1)].classList.toggle("allume");
    }
    if (x > 0) {
        cellules[changeCoordEnIndex(x - 1, y)].classList.toggle("allume");
    }
    if (x < larg - 1) {
        cellules[changeCoordEnIndex(x + 1, y)].classList.toggle("allume");
    }
    if (gagne(cellules)) {
        document.getElementById("gagne").textContent = "Bravo, tu as gagné!"
    }
}
/* boucle sur toutes les cellules pour les initaliser */
for (const c of cellules) {
    c.addEventListener("click", changeEtat);
    if (Math.random() < 0.5) {
        c.classList.add("allume");
    }
}
</script>
</body>
</html>
```

````
