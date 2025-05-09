% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# JavaScript

```{metadata}
solutions: show
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

### Exemple {num}`ex-js:exemple`

Voici une page web qui permet de calculer les solutions d'une équation
du deuxième degré.

```{exec} html
:when: load
:editor: 7f6e9026-6aaf-452b-a60c-88c8a86b8a32
:style: height: 30rem
:output-style: height: 30rem
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Équations du deuxième degré</title>
<style>
table {
    margin-top: 1em;
    margin-left: auto;
    margin-right: auto;
    table-layout: fixed;
    border-collapse: collapse;
}
table, th, td {
    border: 1px solid black;
    width: 100%;
    text-align: center;
}
td {
    height: 1.2em;
}
#erreur {
    margin-top: 1em;
    text-align: center;
    font-weight: bold;
    color: #ff0000;
}
</style>
</head>

<body>
<h1>Résolution d'équations du deuxième degré</h1>

<h2>Demande les coefficients a, b et c à l'utilisateur</h2>

<p>Les coefficients a, b et c sont demandés à l'utilisateur au moyen de
    l'élément HTML <b><code>&lt;input&gt;</code></b>.</p>

<p>
a: <input type="number" id="coeffA" value="0">
b: <input type="number" id="coeffB" value="0">
c: <input type="number" id="coeffC" value="0">
<p/>

<h2>Calcule des solutions</h2>

<p>Pour déterminer le nombre de solutions, il faut calculer le discriminant
    (&Delta;).</p>

<ul>
    <li>Si &Delta; &lt; 0, l'équation n'a pas de solution réelle.</li>
    <li>Si &Delta; = 0, l'équation a une solution: x = -b / 2a.</li>
    <li>Si &Delta; &gt; 0, l'équation a deux solutions:
        x1 = (-b + &radic;<span style="border-top: 1px solid black">&Delta;</span>) / 2a et
        x2 = (-b - &radic;<span style="border-top: 1px solid black">&Delta;</span>) / 2a.</li>
</ul>

<button id="calculer">Calculer les solutions</button>
<button id="effacer">Effacer</button>

<table class="solutions">
    <tr>
        <th>Équation</th><th>Nombre de solutions</th><th>Solutions</th>
    </tr>
    <tr>
        <td></td><td></td><td></td>
    </tr>
</table>

<div id="erreur"></div>

<script>
/* Créé des références pour les éléments que l'on veut modifier */
const calculer = document.querySelector("#calculer");
const effacer = document.querySelector("#effacer");
const erreur = document.querySelector("#erreur");

/* Stocke les cellules du tableau dans une liste */
const cellules = [...document.querySelectorAll(".solutions td")];

function clear() {
    for (const c of cellules) {
      c.textContent = "";
    }
    erreur.textContent = "";
}

effacer.addEventListener("click", clear);

function calculeSol() {
    clear();
    const a = Number(document.getElementById("coeffA").value);
    const b = Number(document.getElementById("coeffB").value);
    const c = Number(document.getElementById("coeffC").value);
    cellules[0].textContent = a + "x² + " + b + "x + " + c + " = 0";
    if (a === 0) {
        erreur.textContent = "Erreur: Ce n'est pas une équation du second degré.";
        return;
    }
    const delta = b ** 2 - 4 * a * c;
    if (delta < 0) {
        cellules[1].textContent = "L'équation n'a pas de solution réelle.";
        cellules[2].textContent = "/";
    } else if (delta === 0) {
        cellules[1].textContent = "L'équation a une solution.";
        const x = (-b) / (2 * a);
        cellules[2].textContent = "x = " + x;
    } else {
        cellules[1].textContent = "L'équation a deux solutions";
        const x1 = (-b + Math.sqrt(delta)) / (2 * a);
        const x2 = (-b - Math.sqrt(delta)) / (2 * a);
        cellules[2].textContent = "x1 = " + x1 + " et x2 = " + x2;
    }
}

calculer.addEventListener("click", calculeSol);
</script>
</body>
</html>
```

### Exercice {num}`exo-js`

Testez la page avec quelques valeurs différentes pour a, b et c.

### Exercice {num}`exo-js`

Le code HTML est composé de 2 parties:
- `<head>` qui est l'entête du document et contient un certain nombre
  d'informations, tels que l'encodage ou le titre de l'onglet.
- `<body>` qui contient le contenu de la page.

1.  À quelles lignes se trouve l'entête?

2.  À quelles lignes se trouve le corps du html?

3.  Dans quelle partie se trouve la balise `<style>` qui permet d'intégrer le CSS
    directement dans le document HTML?

4.  Où se trouve la balise `<script>` qui permet d'intégrer du JavaScript?

```{solution}
1. L'entête se trouve entre la ligne 3 et la ligne 30, entre les balise `<head>`et `</head>`.
2. Le corps se trouve entre la ligne 32 et la ligne 119, entre les balise `<body>`et `</body>`.
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
- Dans les instructions conditionnelles, on écrit `else if` à place de `elif`.
- Les conditions doivent être mises entre parenthèses.
- Devant les variables, on ajoute le mot-clé `const` (ou `let` si la valeur change).
- Pour comparer: === (égal) ou !== (pas égal).
```


## Comparaison Python et JavaScript

### Saisie utilisateur

En Python:

```{exec} python
:when: never
a = input("Texte qui s'affiche")
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
/* Stocke la valeur dans la variable a */
const a = document.getElementById("mon_input").value;
</script>
</body>
```

#### Exercice {num}`exo-js`

Trouvez les `<input>` contenus dans le code de l'{numref}`exemple %s<ex-js:exemple>`:

1.  De quel type sont-ils?
2.  Quels sont leur identifiant?
3.  Que signifie `value="0"`?

```{solution}
1.  Ils sont de type "number". Cela empêche l'utilisateur de saisir autre chose
    que des nombres.
2.  Les identifiants sont "coeffA", "coeffB" et "coeffC".
3.  `value="0"` est la valeur par défaut indiquée dans le champ de texte.
```

#### Exercice {num}`exo-js`

1.  À quelles lignes récupère-t-on les valeurs entrées dans les champs de texte?
2.  Pourquoi note-on: `Number` devant `document.getElementById("coeffA").value`

```{solution}
1.  Aux lignes 93 à 95.
2.  La valeur retournée par la fonction `document.getElementById("coeffA").value`
    est toujours du texte, il faut donc la convertir en nombre avec la fonction
    `Number()`.
```

### Boucle for

Comme en Python, il est possible de faire une boucle for sur tous les éléments
d'une liste.

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
const notes = [5, 5.5, 4, 5.5, 6];
for (const note of notes) {
  /* Affiche la valeur sur la console */
  console.log(note);
}
</script>
```

</td></tr></table>

#### Exercice {num}`exo-js`

1. À quelle ligne cette construction est-elle utilisée dans l'{numref}`exemple %s<ex-js:exemple>`.
2. Expliquez ce que fait cette boucle.

```{Solution}
1. Lignes 83 à 85.
2. Elle efface le contenu des cellules `<td>` du tableau l'une après l'autre.
```

### Interactions entre l'utilisateur et la page web

Les événements sont des actions qui se produisent sur la page, par exemple
lorsque l'utilisateur clique sur un bouton.

Pour définir les actions, il faut:

1.  Dans le HTML, définir un élément qui interagira avec l'utilisateur (ici un
    bouton).
2.  Créer une référence sur l'élément que l'on veut modifier.
3.  Associer l'événement (clic) à la fonction qui sera appelée (action).
```{exec} html
:when: never
<body>
...
<button id="identifiant">Texte affiché sur le bouton</button>
...
<script>
const nom = document.querySelector("#identifiant");

function action() {
    ...
}

nom.addEventListener("click", action);
</script>
</body>
```

#### Exercice {num}`exo-js`

1. À quelles lignes se trouvent les deux éléments HTML `<button>`?
2. Quels sont les identifiants de ces deux boutons?
3. Quelle fonction est utilisée pour créer la référence?
4. Quelle fonction est appelée par un clic du bouton `calculer`?
5. Quelle fonction est appelée par un clic du bouton `effacer`?

```{Solution}
1. Au lignes 59 et 60.
2. L'identifiant du premier est "calculer" et celui du second est "effacer".
3. document.querySelector("#calculer") et document.querySelector("#effacer")
4. La fonction `calculeSol()`.
5. La fonction `clear()`.
```

### Affichage dynamique de texte

Le message d'erreur s'affiche sur la page uniquement dans certaines conditions.
Pour cela, un conteneur vide, muni d'un identifiant, doit être ajouté à la page
afin de pouvoir y insérer le message si nécessaire.

```{exec} html
:when: never
<div id="message"></div>
```

Dans le partie script, il est ainsi possible de changer la valeur du conteneur
"message".

#### Exercice {num}`exo-js`

1.  À quelle ligne se trouve le conteneur pour le message d'erreur?
2.  À quelle ligne est créée la référence du conteneur?
3.  À quelles lignes la valeur du conteneur est-elle modifiée?
4.  Quelle syntaxe est utilisée pour modifier la valeur du conteneur?


```{Solution}
1.  À la ligne 71.
2.  À la ligne 77.
3.  Aux lignes 86 et 98.
4.  `erreur.textContent = "..."`
```

