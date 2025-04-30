% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Labo - Jeu

```{metadata}
solutions: remove
```

## Introduction

Pendant ce labo, vous allez développer la version "Lights In", du jeu
["Light Out"](https://fr.wikipedia.org/wiki/Lights_Out_(jeu)) dont le but
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
Utiliser un tableau sans entête.
````

`````
`````{tab-item} Étape 2
:sync: etape2

Ajouter du style à votre page pour que:

1. le tableau ait des bordures,
2. la hauteur et la largeur des cellules soient de 100px,
3. la couleur de fond des cellules soient d'une autre couleur,
4. le tableau soit centré.

````{tip}
:class: dropdown
Utilisez des sélecteurs de type.

Pour que le tableau soit centré, il faut que les marges à droite et à gauche
soient automatiques.

Les différents propriétés nécessaires sont:\
`border`, `border-collapse`, `width`, `height`, `margin-left`, `margin-right`
````

`````
`````{tab-item} Étape 3
:sync: etape3

Dans la partie script, ajoutez la fonctionnalité suivante en définissant la
fonction `changeEtat(event)`:

Lorsqu'on clique sur une cellule du tableau, affichez dans la cellule le texte
"clic". Cela permettra de vérifier que les clics dans les cellules sont
correctement détectés.

````{tip}
:class: dropdown
1.  Pour que les clics sur les cellules soient détectés, il faut utiliser
    `addEventListener` sur chaque cellule. Pour éviter les répétitions, il faut
    stocker toutes les cellules dans une liste et faire une boucle
    sur chaque élément (cf {numref}`exemple %s<ex-js:exemple>`).
2.  La fonction `changeEtat(event)` a un paramètre `event` qui est déclenché par
    le clic de la souris (ou du touchpad).
    ```{exec} html
    :when: never
    function changeEtat(event) {
        const c = event.target;    // récupère l'élément html cible
        ...
    ```
````

`````
`````{tab-item} Étape 4
:sync: etape4

Modifiez la fonction `changeEtat(event)` pour que lorsqu'on clique sur une
cellule, celle-ci change d'état. Si elle est allumée (colorée), elle s'éteint
(sans couleur de fond) et vice-versa.

````{tip}
:class: dropdown
1.  Trouvez la propriété qui permet de changer la couleur de fond d'une cellule.
2.  Pour changer la couleur d'une cellule, il faut pouvoir les différencier.
    Cela se fait au moyen d'un sélecteur de classe.
    -   dans la partie style: définir la couleur des cellules allumées
        ```{exec} html
        :when: never
        .allume {
        /* compléter par la propriété et la valeur désirée */
        }
        ```
    -   en ajoutant la classe "allume" à la cellule pour l'allumer et en la
        supprimant pour l'éteindre. Cela se fait au moyen de:
        ```{exec} html
        :when: never
        c.classList.toggle("allume");  // ajoute la classe "allume" à l'élément ou l'efface
        ```
        Ce code doit remplacer `c.innerHTML = "clic"`.
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
1.  Dans la fonction `gagne`, il faut parcourir la liste de cellules et dès
    qu'on rencontre une cellule qui n'est pas allumée, on renvoie `False`, car
    le but n'est pas atteint. À la fin de la fonction, on renvoie `True`, car si
    on arrive à la fin de la fonction, cela signifie que toutes les cellules
    sont allumées.
2.  Pour afficher du texte sur la page, voir comment se fait l'affichage des
    erreurs dans l'{numref}`exemple %s<ex-js:exemple>`.
````

`````
`````{tab-item} Étape 7
:sync: etape7

Modifiez la fonction `changeEtat(event)` pour qu'elle suive la règle du jeu,
c'est-à-dire qu'elle modifie aussi les 4 cellules voisines (au nord, sud, est et
ouest).

````{tip}
:class: dropdown
On peut convertir l'index d'une cellule en coordonnée (x, y), cela facilite
grandement les tests pour déterminer les cases à modifier.
```{exec} html
const c = event.target;             // retourne l'élément ciblé
const index = cellules.indexOf(c);  // retourne l'index de l'élément ciblé
const x = index % larg;             // calcule la coordonnée x en fonction de la largeur
const y = Math.trunc(index / larg); // calcule la coordonnée y en fonction de la largeur
```
La fonction suivant permet de passer des coordonnées x et y à l'index:
```{exec} html
function changeCoorEnIndex(x, y) {
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
/* Ajout des éléments HTML */

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
/* Ajout des styles css */
td {
    border: 1px solid black;
    border-collapse: collapse;
    width: 100px;
    height: 100px;
}

table, tr {
    border: 1px solid black;
    border-collapse: collapse;
    margin-left:auto;
    margin-right:auto;
}

.allume {
    background: yellow;
}

#gagne {
    text-align: center;
    font-size: 6em;
    color: #C71585;
}
</style>
</head>
<body>
<h1>Création d'un jeu</h1>

<h2>Règles du jeu</h2>
<p>Lorsqu'on clique sur une case, celle-ci change d'état ainsi que ses quatre
voisines (au sud, à l'est, au nord et à l'ouest), si elles existent.</p>

<h2>But</h2>
<p>Allumer toutes les cellules.<p/>

<br><br><br>

<table class="cellules">
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td></tr>
</table>

<div id="gagne"></div>

<script>
/* Ajout du JavaScript */

const larg = 3;
const haut = 3;
const cellules = [...document.querySelectorAll(".cellules td")];

function changeCoorEnIndex(x, y) {
    return y * larg + x;
}

function gagne(liste) {
    for (const c of liste) {
        if (!(c.className == "allume")) {
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
    /* Vérifie qu'on est pas sur la première ligne */
    if (y > 0) {
        cellules[changeCoorEnIndex(x, y-1)].classList.toggle("allume");
    }
    /* Vérifie qu'on est pas sur la dernière ligne */
    if (y < haut - 1) {
        cellules[changeCoorEnIndex(x, y+1)].classList.toggle("allume");
    }
    if (x > 0) {
        cellules[changeCoorEnIndex(x-1, y)].classList.toggle("allume");
    }
    cellules[changeCoorEnIndex(x, y)].classList.toggle("allume");
    if (x < larg - 1) {
        cellules[changeCoorEnIndex(x + 1, y)].classList.toggle("allume");
    }
    if (gagne(cellules)) {
        document.getElementById("gagne").innerHTML = "Bravo, tu as gagné!"
    }
}
/* boucle sur toutes les cellules pour les initaliser */
for (const c of cellules) {
    c.addEventListener("click", changeEtat);
    const n = Math.random();
    if (n < 0.5) {
        c.classList.add("allume");
    }

}

</script>
</body>
</html>
```

````
