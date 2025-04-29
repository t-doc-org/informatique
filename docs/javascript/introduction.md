% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# JavaScript

```{metadata}
solutions: remove
```

## Introduction

En première année, vous avez appris le langage HTML, utilisé pour décrire le
contenu d'une page web, ainsi que le langage CSS, employé pour définir son
style. Les sites créés uniquement avec ces deux langages sont dits statiques,
car leur contenu reste toujours identique et ne permet pas à l'utilisateur
d'interagir avec eux.

Pour aller plus loin et rendre vos pages web interactives, nous allons
maintenant découvrir JavaScript. Ce langage de programmation permet d'agir sur
le contenu d'une page une fois qu'elle est affichée dans le navigateur. Vous
pourrez, par exemple, réagir aux clics des utilisateurs, modifier du texte sans
avoir besoin de recharger la page, afficher des messages, ou encore faire
apparaître ou disparaître des éléments.

Les concepts de base (variables, entrées-sorties, instructions conditionnelles,
boucles) sont les mêmes qu'en Python, seule la manière de les écrire change.

### Exercice {num}`exo-js:exemple`

Voici une page web qui permet de calculer les solutions d'une équation
du deuxième degré. Testez la page avec quelques valeurs différentes pour a, b et
c.

```{exec} html
:when: load
:editor: 7f6e9026-6aaf-452b-a60c-88c8a86b8a32
:style: height: 30rem
:output-style: height: 30rem
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Équations du deuxième degré</title>
<style>
table, td, tr, th {
    border: 1px solid black;
    border-collapse: collapse;
    margin-left:auto;
    margin-right:auto;
    table-layout: fixed;
    width: 100%;
    text-align: center;

}

td {
    height: 1.2em;
}

#erreur {
    text-align: center;
    font-size: 2em;
    color: #FF0000;
}
</style>
</head>

<body>
<h1>Résolution d'équations du deuxième degré</h1>

<h2>Demande les coefficients a, b et c à l'utilisateur</h2>

<p>Les coefficients a, b et c sont demandés à l'utilisateur au moyen de
    l'élément HTML <b>input</b>.</p>

<p>
a: <input type="number" id="coeffA" value="0"/>
b: <input type="number" id="coeffB" value="0"/>
c: <input type="number" id="coeffC" value="0"/>
<p/>

<h2>Calcule des solutions</h2>

<p> Pour déterminer le nombre de solutions, il faut calculer le discriminant
    (&Delta;).</p>

<ul>
    <li> Si &Delta; &lt; 0, l'équation n'a pas de solution réelle.</li>
    <li> Si &Delta; = 0, l'équation a une solution: x = -b / 2a.</li>
    <li> Si &Delta; &gt; 0, l'équation a deux solutions: x1 = (-b + &radic; &Delta;) / 2a et x2 = (-b - &radic; &Delta;) / 2a.</li>
</ul>

<button id="bouton1">Calculer les solutions</button> <button id="bouton2">Effacer</button>

<br><br>

<div id="erreur"></div>

<table class="solutions">
    <tr>
        <th>Équation</th>
        <th>Nombre de solutions</th>
        <th>Solutions</th>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>

<script>
/* Stocke les cellules du tableau dans une liste */
const cellules = [...document.querySelectorAll(".solutions td")];

bouton1.addEventListener("click", calculeSol);
bouton2.addEventListener("click", clear);

function clear() {
    for (const c of cellules) {
      c.innerHTML = "";
    }
    erreur.innerHTML = "";
}

function calculeSol() {
    clear();
    const a = Number(document.getElementById("coeffA").value);
    const b = Number(document.getElementById("coeffB").value);
    const c = Number(document.getElementById("coeffC").value);
    cellules[0].innerHTML = a + "x&#178; + " + b + "x + " + c + " = 0";
    if (a === 0) {
        erreur.innerHTML = "Erreur: Ce n'est pas une équation du second degré.";
    } else {
        const delta = b ** 2 - 4 * a * c;
        if (delta < 0) {
            cellules[1].innerHTML = "L'équation n'a pas de solution réelle.";
            cellules[2].innerHTML = "/";
        } else if (delta === 0) {
            cellules[1].innerHTML = "L'équation a une solution.";
            const x = (-b) / (2 * a);
            cellules[2].innerHTML = "x = " + x;
        } else {
            cellules[1].innerHTML = "L'équation a deux solutions";
            const x1 = (-b + Math.sqrt(delta)) / (2 * a);
            const x2 = (-b - Math.sqrt(delta)) / (2 * a);
            cellules[2].innerHTML = "x1 = " + x1 + " et x2 = " + x2;
        }
    }
}

</script>
</body>
</html>
```

### Exercice {num}`exo-js`

Le code HTML est composé de 2 parties:
- `<head>` qui est l'entête du document et contient un certain nombre
  d'informations, tel que l'encodage, le titre de l'onglet.
- `<body>` qui contient le contenu de la page.

1.  À quelles lignes se trouve l'entête?

2.  À quelles lignes se trouve le corps du html?

3.  Dans quelle partie se trouve la balise `<style>` qui permet d'intégrer le CSS
    directement dans le document HTML?

4.  Où se trouve la balise `<script>` qui permet d'intégrer du JavaScript?

```{solution}
1. L'entête se trouve entre la ligne 3 et la ligne 28, entre les balise `<head>`et `</head>`.
2. Le corps se trouve entre la ligne 30 et la ligne 115, entre les balise `<body>`et `</body>`.
3. La balise `<style>` se trouve dans le `<head>`.
4. La balise `<script>` se trouve à la fin de la balise `<body>`.
```

### Exercice {num}`exo-js`

En lisant la partie `<script>` qui contient le JavaScript du code ci-dessus,
qu'est-ce qui est différent du Python?

```{Solution}
Différences:
- Il y a des `;` à la fin des lignes.
- Il y a des accolades à la place des `:` et de l'indentation.
- Le mot-clé `function` est utilisé à la place de `def`.
- Dans les instructions conditionnelle, on écrit `else if` à place de `elif`.
- Les conditions doivent être mises entre parenthèses.
- Devant les variables, on ajoute le mot-clé `const` (ou `let` si la valeur change).
- Pour comparer: === ou !==.
```


## Comparaison Python et JavaScript

### Saisie utilisateur

En Python:

```{exec} python
:when: never
a = input("Texte qui s'affiche"))
```

En JavaScript:

```{exec} html
:when: never
<body>
...
<!-- Ajoute une zone de saisie de texte -->
<input type="text" id="mon_input">
...
<script>
/* Récupère la valeur du champs texte dont l'identifiant est "mon_input" */
texte = document.getElementById("mon_input").value`
</script>
</body>
```

#### Exercice {num}`exo-js`

Trouvez les `<input>` contenu dans le code de l'{numref}`exercice %s<exo-js:exemple>`:

1.  De quel type sont-ils?
2.  Quelles sont leur identifiants?
3.  Que signifie `value="0"`?

```{solution}
1.  Ils sont de type "number". Cela empêche l'utilisateur de saisir autre chose
    que des nombres.
2.  Les identifiants sont "coeffA", "coeffB" et "coeffC".
3.  `value="0"` est la valeur par défaut indiquée dans le champ de texte.
```

#### Exercice {num}`exo-js`

1.  À quelles lignes récupèrent-on les valeurs entrées dans les champs de texte?
2.  Pourquoi note-on: `Number` devant `document.getElementById("coeffA").value`

```{solution}
1.  Aux lignes 90 à 92.
2.  La valeur retournée par la fonction `document.getElementById("coeffA").value`
    est toujours du texte, il faut donc la convertir en nombre avec la fonction
    `Number()`.
```

### Boucle for

Comme en Python, il est possible de faire une boucle for sur tous les éléments
d'une liste (appelée tableau en JS).

<table><tr style="text-align: center">
  <th>Python</th><th>JavaScript</th>
</tr><tr><td>

```{exec} python
:when: never
notes = [5, 5.5, 4, 5.5, 6]
for note in notes:
  print(note)
```

</td><td style="padding-left: 1rem">

```{exec} html
:when: never
<script>
const notes = [5, 5.5, 4, 5.5, 6]
for (const note of notes) {
  /* Affiche la valeur sur la console */
  console.log(note)
}
</script>
```

</td></tr></table>

#### Exercice {num}`exo-js`

1. À quelle ligne cette construction est-elle utilisée dans l'{numref}`exercice %s<exo-js:exemple>`.
2. Expliquez ce que fait cette boucle.

```{Solution}
1. Lignes 82 à 84.
2. Elle efface le contenu des cellules (td) du tableau l'une après l'autre.
```

### Interactions entre l'utilisateur et la page web

Les événements sont des actions qui se produisent sur la page, par exemple
lorsque l'utilisateur clique sur un bouton.

Pour définir les actions à faire, il faut utiliser la construction suivante:
```{exec} html
:when: never
<script>
bouton.addEventListener("click", action);
</script>
```
où l'action est la fonction qui sera appelée au moment du clic sur le bouton.

#### Exercice {num}`exo-js`

1. Quelle fonction est appelée par un clic du bouton1?
2. Quelle fonction est appelée par un clic du bouton2?

```{Solution}
1. La fonction `calculeSol()`.
2. La fonction `clear()`.
```
