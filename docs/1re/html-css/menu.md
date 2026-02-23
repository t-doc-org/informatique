% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Menu

Un menu de navigation est un élément essentiel d'un site web qui permet aux
utilisateurs de se déplacer facilement entre les différentes pages ou sections.
Il se présente généralement sous forme de liste de liens (par exemple : Accueil,
À propos, Contact) et est souvent placé en haut, sur le côté ou en bas de la
page.

Dans cette partie, vous apprendrez à créer un menu de navigation permettant de
passer facilement d'une section à l'autre. Ce menu pourra être intégré
directement à votre projet.

## Exercice {num2}`exercice`

Créez un menu en haut d'une page qui permet de naviguer entre différentes pages.

````{tab-set}
:sync-group: etape
```{tab-item} Étape 1
:sync: etape1
Dans le fichier HTML, créez une liste non-numérotée qui contient les noms des
différentes sections de la page. Le premier élément est "Haut de page".
```
```{tab-item} Étape 2
:sync: etape2
Dans la partie CSS, le formatage du menu a déjà été défini au moyen d'un
sélecteur de classe. Pour que celui-ci s'applique au menu, ajoutez, dans le
fichier HTML, la classe `menu` à l'élément `<ul>` de la liste.
```
```{tab-item} Étape 3
:sync: etape3
Pour ajouter les références aux différentes sections, il faut, dans le fichier
HTML:

1.  Ajouter un identifiant à chaque section qui est référencée dans le menu.
2.  Ajouter une référence à la section correspondante dans le menu.

    Utilisez la balise `<a href="..."></a>` en remplaçant les `...` par le
    sélecteur d'identifiant correspondant.

    Exemple: `<li><a href="#section0">Haut de page</a></li>`
```
```{tab-item} Étape 4
:sync: etape4
Modifiez la couleur du menu, du texte, etc.
```
````

### Éditeur pour le HTML

```{exec} html
:editor: 775b3aa8-74b0-4ac9-9233-3c9779c4dac5
:reset: hide
:after: barre-navigation
:when: load
:style: height: 30rem;
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Titre de la page</title>
  </head>
  <body>
    <!-- Ajoutez le menu ici -->

    <h1>Ma page</h1>

    <h2>Section 1</h2>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <h2>Section 2</h2>
    <ul>
      <li>item 1</li>
      <li>item 2</li>
      <li>item 3</li>
      <li>item 4</li>
      <li>item 5</li>
      <li>item 6</li>
      <li>item 7</li>
      <li>item 8</li>
      <li>item 9</li>
      <li>item 10</li>
      <li>item 11</li>
      <li>item 12</li>
    </ul>

    <h2>Section 3</h2>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <h2>Section 4</h2>

    <p>Liste de toutes les références utilisées.</p>

    <ol>
      <li>item 1</li>
      <li>item 2</li>
      <li>item 3</li>
      <li>item 4</li>
      <li>item 5</li>
      <li>item 6</li>
      <li>item 7</li>
      <li>item 8</li>
      <li>item 9</li>
      <li>item 10</li>
      <li>item 11</li>
      <li>item 12</li>
    </ol>
  </body>
</html>
```

### Éditeur pour le CSS

```{exec} html
:editor: f027de1b-d4ad-442f-9c13-f3d3494c802b
:reset: hide
:name: barre-navigation
:when: never
<style>
html {
  scroll-padding-top: 3.5rem;
}

/* liste du menu */
.menu {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  background-color: #333333;
  position: sticky;
  top: 0;
  height: 3rem;
}

/* éléments de la liste */
.menu li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* élément sélectionné de la liste */
.menu li a:hover {
  background-color: #111111;
}
</style>
```

````{solution}
### Éditeur pour le HTML

```{exec} html
:editor:
:after: barre-navigation
:when: load
:style: height: 30rem;
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Titre de la page</title>
  </head>
<body>
    <ul class="menu">
      <li><a href="#home">Haut de page</a></li>
      <li><a href="#section1">Section 1</a></li>
      <li><a href="#section2">Section 2</a></li>
      <li><a href="#section3">Section 3</a></li>
      <li><a href="#section4">Section 4</a></li>
    </ul>

    <h1 id="home">Ma page</h1>

    <h2 id="section1">Section 1</h2>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <h2 id="section2">Section 2</h2>
    <ul>
      <li>item 1</li>
      <li>item 2</li>
      <li>item 3</li>
      <li>item 4</li>
      <li>item 5</li>
      <li>item 6</li>
      <li>item 7</li>
      <li>item 8</li>
      <li>item 9</li>
      <li>item 10</li>
      <li>item 11</li>
      <li>item 12</li>
    </ul>

    <h2 id="section3">Section 3</h2>

    <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
    nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
    diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
    clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit
    amet.</p>

    <h2 id="section4">Section 4</h2>

    <p>Liste de toutes les références utilisées.</p>

    <ol>
      <li>item 1</li>
      <li>item 2</li>
      <li>item 3</li>
      <li>item 4</li>
      <li>item 5</li>
      <li>item 6</li>
      <li>item 7</li>
      <li>item 8</li>
      <li>item 9</li>
      <li>item 10</li>
      <li>item 11</li>
      <li>item 12</li>
    </ol>
  </body>
</html>
```
````

