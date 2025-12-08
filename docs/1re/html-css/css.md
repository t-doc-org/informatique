% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# CSS

Le langage **CSS** (**C**ascading **S**tyle **S**heet en français feuilles de
style en cascade) permet de mettre en forme les documents HTML. Il permet
notamment de modifier la police, la couleur, la taille et l'emplacement du
contenu.\
CSS est un langage basé sur des règles: il permet de définir des règles de style
pour un type d'élément donné, par exemple les titres principaux `<h1></h1>` ou
les paragraphes `<p></p>`

## Structure du code CSS

La règle commence par un sélecteur qui indique à quelles balises cette règle
doit s'appliquer. Ensuite, la liste des propriétés ainsi que leurs valeurs sont
indiquées entre accolades.

```{code-block} css
sélecteur {
  propriété1: valeur1;
  propriété2: valeur2;
}
```

Exemples:

```{code-block} css
h1 {                      /* Cette règle définit le style du titre principal. */
  color: green;           /* La couleur du texte est verte. */
  text-align: center;     /* L'alignement du texte est centré. */
}
```

```{code-block} css
p {                       /* Cette règle définit le style des paragraphes. */
  font-family: verdana;   /* La police utilisée est verdana. */
  font-size: 20px;        /* La taille de la police est 20 pixels. */
}
```

(referencement)=
## Référencement

Comme le ficher HTML (`.html`) et le fichier CSS (`.css`) sont deux fichiers
distincts, il faut ajouter au document HTML une référence au fichier CSS. Cela
se fait dans le `<head>` du document HTML avec la balise `<link>`.

La balise `<link>` a deux attributs:

1. `rel` (précise à quoi sert le fichier référencé)
2. `href` (chemin d'accès au document):

```{code-block} html
<link href="style.css" rel="stylesheet" type="text/css"/>
```

## Sélecteur

Dans ce cours, nous allons travailler sur 3 types de sélecteurs:

1. Sélecteur de type
2. Sélecteur d'identifiant
3. Sélecteur de classe

### Sélecteur de type

Le sélecteur de type permet d'appliquer un style à toutes les balises de même
type (`h1`, `h2`, `p`, ...).

Il est de la forme:

```{code-block} css
h1 {                      /* Cette règle définit le style du titre principal. */
  color: green;           /* La couleur du texte est verte. */
  text-align: center;     /* L'alignement du texte est centré. */
}
```

Ce style s'appliquera au contenu de toutes les balises `<h1>...</h1>`.

## Exercice {num2}`exercice`

Le contenu d'un page a été défini en HTML de la manière suivante.

```{exec} html
:name: selecteur-type
:when: never
:style: height: 30rem;
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Labrador</title>
</head>
<body>
    <h1>Le Labrador</h1>

    <h2>Origine et caractéristiques</h2>

    <p>Le Labrador est une race de chien originaire du Canada, plus précisément
    de Terre-Neuve. Il est connu pour son tempérament amical, son intelligence
    et sa grande capacité d'adaptation.</p>

    <h3>Caractéristiques</h3>
    <table>
      <tr>
        <th>Taille</th><th>Poids</th><th>Espérance de vie</th><th>Couleurs</td>
      </tr>
      <tr>
        <td>54 à 57 cm</td><td>25 à 36 kg</td><td>10 à 14 ans</td>
        <td>Noir, jaune, chocolat</td>
      </tr>
    </table>

    <h2>Comportement et utilisation</h2>
    <p>Très sociable, le Labrador est souvent utilisé comme chien guide pour les
    personnes malvoyantes, mais aussi comme chien de sauvetage et compagnon
    familial.</p>

    <h2>Photo</h2>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Labrador_Retriever_portrait.jpg/1024px-Labrador_Retriever_portrait.jpg">

    <p>Source: texte généré par Copilot.</p>
</body>
</html>
```

Au moyen du CSS, modifiez les éléments suivants:

1.  Le titre principal doit être en bleu et centré.
2.  Les sous-titres de niveau 2 doivent être en couleur ([choix de couleurs](https://htmlcolorcodes.com/color-names/)).
3.  La table doit avoir une bordure (attributs: `border` et `border-collapse`).
4.  La table doit prendre `100%` de la largeur de la page.
5.  L'image doit avoir une largeur de `300px`.
6.  La famille de la police `font-family` des paragraphes doit être "Goudy
    Bookletter 1911".
7.  La couleur de fond `background-color` doit être "cornsilk".

```{exec} html
:editor: 76fa6122-75cd-449c-a539-d4141d082c56
:after: selecteur-type
:when: load
:reset: hide
<style>
/*  Écrivez le CSS ici */
</style>
```

````{solution}
```{exec} html
:editor:
:after: selecteur-type
:when: load
:reset: hide
<style>
h1 {
  color: blue;
  text-align: center;
}

h2 {
  color: deepskyblue;
}

table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}

table {
  width: 100%;
}

img {
  width: 300px;
}

p {
  font-family: "Goudy Bookletter 1911";
}

html {
  background-color: cornsilk;
}
</style>
```
````

### Sélecteur d'identifiant

Le sélecteur d'identifiant permet d'appliquer un style à un élément précis. Pour
cela, il faut ajouter un nouvel attribut `id` à la balise HTML concernée.

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Fichier HTML
  ```{code-block} html
  <p id="intro">
  Dans ce paragraphe, j'écris l'introduction
  de mon texte.
  </p>
  ```
- # Fichier CSS
  ```{code-block} css
  #intro {
    text-align: justify;
    color: blue;
  }
  ```
````

Ce style ne s'appliquera qu'à un élément unique, la balise dont l'`id` est
"intro".

## Exercice {num2}`exercice`

Le contenu d'un page a été défini en HTML de la manière suivante.

```{exec} html
:name: selecteur-id
:when: never
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}

table {
  width: 100%;
  background-color: lightgrey;
}

p {
  text-align: justify;
}

#intro {
  font-weight: bold;
}

#evolution {
  background-color: orange;
}

</style>
```


Au moyen du CSS, modifiez les éléments suivants:

1.  Le premier paragraphe doit être en gras et justifié.
2.  Le dernier tableau doit avoir la couleur de fond "orange".

```{exec} html
:editor: 7abfb302-7e87-4061-85ba-7ccf0a2ad1b1
:after: selecteur-id
:when: load
:style: height: 30rem;
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Smartphone - Histoire</title>
</head>
<body>
  <h1>Histoire du smartphone</h1>

  <p>
    Le smartphone résulte de la fusion entre la téléphonie mobile,
    l'informatique et l'Internet. En quelques décennies, il est passé d'un outil
    centré sur les appels et SMS à une plateforme polyvalente pour communiquer,
    créer, apprendre et travailler partout.
  </p>

  <p>
    Dans les années 1990, les PDA (assistants personnels) popularisent l'agenda
    et la prise de notes dans la poche, mais les capacités cellulaires restent
    limitées. En 1994, l'IBM Simon réunit téléphone, écran tactile et
    applications simples — un précurseur du smartphone. Début 2000, BlackBerry
    et Nokia généralisent l'e‑mail mobile et les services de données pour les
    pros.
  </p>

  <table>
    <tr>
      <th>Année</th>
      <th>Événement</th>
      <th>Impact</th>
    </tr>
    <tr>
      <td>1994</td>
      <td>IBM Simon Personal Communicator</td>
      <td>Première convergence téléphone + écran tactile + apps simples</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>Nokia 7110 (WAP)</td>
      <td>Première navigation web mobile grand public (WAP)</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>BlackBerry 5810 / Nokia 7650</td>
      <td>E‑mail “push”, photo intégrée, convergence téléphonie‑PDA</td>
    </tr>
  </table>

  <p>
    En 2007, l'iPhone démocratise l'écran capacitif multi‑touch et une interface
    pensée pour le doigt. À partir de 2008, les boutiques d'apps (App Store,
    Android Market/Google Play) accélèrent l'innovation. Les réseaux 3G puis 4G
    rendent la vidéo, la navigation et le cloud réellement fluides.
  </p>

  <p>
    Les puces (SoC) regroupent CPU, GPU, NPU et modem, gagnant en puissance et
    en efficacité énergétique. La photographie mobile progresse: capteurs plus
    grands, multiples focales, HDR et traitement computationnel. La sécurité
    s'améliore avec chiffrement, biométrie et mises à jour OTA, favorisant
    paiements et identités numériques.
  </p>

  <table>
    <tr>
      <th>Année</th>
      <th>Événement</th>
      <th>Impact</th>
    </tr>
    <tr>
      <td>2007</td>
      <td>iPhone (multi‑touch capacitif)</td>
      <td>Nouveau paradigme d'interface et navigation web avancée</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Android (HTC Dream) + boutiques d'apps</td>
      <td>Écosystèmes ouverts et distribution massive d'applications</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Déploiements 4G LTE</td>
      <td>Haut débit mobile : streaming, cloud, visiophonie</td>
    </tr>
    <tr>
      <td>2019–2021</td>
      <td>Commercialisation large de la 5G</td>
      <td>Latence réduite, débits élevés, nouveaux usages temps réel</td>
    </tr>
  </table>

  <p>
    De L'IBM Simon aux appareils 5G d'aujourd'hui, l'histoire du smartphone
    illustre une accélération continue des usages et des technologies. L'avenir
    mêlera encore plus d'IA embarquée, d'efficacité énergétique, de connectivité
    et de services, au service d'expériences mobiles toujours plus riches.
  </p>

  <table>
  <caption>Évolutions clés par domaine</caption>
    <tr>
      <th>Domaine</th>
      <th>Début</th>
      <th>Tendance actuelle</th>
      <th>Bénéfice principal</th>
    </tr>
    <tr>
      <td>Écran</td>
      <td>Résistif, petites diagonales, 320×480</td>
      <td>OLED/AMOLED, 90–120 Hz, haute définition, HDR</td>
      <td>Confort, fluidité, meilleurs contrastes et couleurs</td>
    </tr>
    <tr>
      <td>Réseau</td>
      <td>2G (GPRS/EDGE)</td>
      <td>4G avancée et 5G (selon régions)</td>
      <td>Débits/latence pour vidéo, cloud, jeux en ligne</td>
    </tr>
    <tr>
      <td>Puissance</td>
      <td>CPU monocœur, GPU limité</td>
      <td>SoC multi‑cœurs, GPU puissants, NPU/IA</td>
      <td>Apps riches, IA embarquée, efficacité énergétique</td>
    </tr>
    <tr>
      <td>Photo</td>
      <td>VGA / 1 MP, sans HDR</td>
      <td>Capteurs plus grands, multi‑objectifs, HDR/Night Mode</td>
      <td>Qualité d'image, zoom polyvalent, basse lumière</td>
    </tr>
    <tr>
      <td>Batterie et charge</td>
      <td>Autonomie modeste, charge lente</td>
      <td>Optimisations logicielles, charge rapide/sans fil</td>
      <td>Moins d'interruptions, usage intensif soutenu</td>
    </tr>
    <tr>
      <td>Sécurité</td>
      <td>Code PIN basique</td>
      <td>Chiffrement par défaut, biométrie (empreinte/visage)</td>
      <td>Protection des données et des paiements</td>
    </tr>
    <tr>
      <td>Logiciels et écosystèmes</td>
      <td>Peu d'apps, API limitées</td>
      <td>App stores, mises à jour OTA, services cloud</td>
      <td>Fonctionnalités continues et connectées</td>
    </tr>
    <tr>
      <td>Matériaux</td>
      <td>Plastiques variés</td>
      <td>Aluminium, verre renforcé, normes IP67/IP68</td>
      <td>Durabilité, résistance à l'eau et à la poussière</td>
    </tr>
  </table>

  <p>Source: texte généré par Copilot.</p>
</body>
</html>
```

````{solution}
```{exec} html
:editor:
:after: selecteur-id
:when: load
:style: height: 30rem;
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Histoire du smartphone</title>
</head>
<body>
  <h1>Histoire du smartphone</h1>

  <p id="intro">
    Le smartphone résulte de la fusion entre la téléphonie mobile,
    l'informatique et l'Internet. En quelques décennies, il est passé d'un outil
    centré sur les appels et SMS à une plateforme polyvalente pour communiquer,
    créer, apprendre et travailler partout.
  </p>

  <p>
    Dans les années 1990, les PDA (assistants personnels) popularisent l'agenda
    et la prise de notes dans la poche, mais les capacités cellulaires restent
    limitées. En 1994, l'IBM Simon réunit téléphone, écran tactile et
    applications simples — un précurseur du smartphone. Début 2000, BlackBerry
    et Nokia généralisent l'e‑mail mobile et les services de données pour les
    pros.
  </p>

  <table>
    <tr>
      <th>Année</th>
      <th>Événement</th>
      <th>Impact</th>
    </tr>
    <tr>
      <td>1994</td>
      <td>IBM Simon Personal Communicator</td>
      <td>Première convergence téléphone + écran tactile + apps simples</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>Nokia 7110 (WAP)</td>
      <td>Première navigation web mobile grand public (WAP)</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>BlackBerry 5810 / Nokia 7650</td>
      <td>E‑mail “push”, photo intégrée, convergence téléphonie‑PDA</td>
    </tr>
  </table>

  <p>
    En 2007, l'iPhone démocratise l'écran capacitif multi‑touch et une interface
    pensée pour le doigt. À partir de 2008, les boutiques d'apps (App Store,
    Android Market/Google Play) accélèrent l'innovation. Les réseaux 3G puis 4G
    rendent la vidéo, la navigation et le cloud réellement fluides.
  </p>

  <p>
    Les puces (SoC) regroupent CPU, GPU, NPU et modem, gagnant en puissance et
    en efficacité énergétique. La photographie mobile progresse: capteurs plus
    grands, multiples focales, HDR et traitement computationnel. La sécurité
    s'améliore avec chiffrement, biométrie et mises à jour OTA, favorisant
    paiements et identités numériques.
  </p>

  <table>
    <tr>
      <th>Année</th>
      <th>Événement</th>
      <th>Impact</th>
    </tr>
    <tr>
      <td>2007</td>
      <td>iPhone (multi‑touch capacitif)</td>
      <td>Nouveau paradigme d'interface et navigation web avancée</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Android (HTC Dream) + boutiques d'apps</td>
      <td>Écosystèmes ouverts et distribution massive d'applications</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Déploiements 4G LTE</td>
      <td>Haut débit mobile : streaming, cloud, visiophonie</td>
    </tr>
    <tr>
      <td>2019–2021</td>
      <td>Commercialisation large de la 5G</td>
      <td>Latence réduite, débits élevés, nouveaux usages temps réel</td>
    </tr>
  </table>

  <p>
    De L'IBM Simon aux appareils 5G d'aujourd'hui, l'histoire du smartphone
    illustre une accélération continue des usages et des technologies. L'avenir
    mêlera encore plus d'IA embarquée, d'efficacité énergétique, de connectivité
    et de services, au service d'expériences mobiles toujours plus riches.
  </p>

  <table id="evolution">
  <caption>Évolutions clés par domaine</caption>
    <tr>
      <th>Domaine</th>
      <th>Début</th>
      <th>Tendance actuelle</th>
      <th>Bénéfice principal</th>
    </tr>
    <tr>
      <td>Écran</td>
      <td>Résistif, petites diagonales, 320×480</td>
      <td>OLED/AMOLED, 90–120 Hz, haute définition, HDR</td>
      <td>Confort, fluidité, meilleurs contrastes et couleurs</td>
    </tr>
    <tr>
      <td>Réseau</td>
      <td>2G (GPRS/EDGE)</td>
      <td>4G avancée et 5G (selon régions)</td>
      <td>Débits/latence pour vidéo, cloud, jeux en ligne</td>
    </tr>
    <tr>
      <td>Puissance</td>
      <td>CPU monocœur, GPU limité</td>
      <td>SoC multi‑cœurs, GPU puissants, NPU/IA</td>
      <td>Apps riches, IA embarquée, efficacité énergétique</td>
    </tr>
    <tr>
      <td>Photo</td>
      <td>VGA / 1 MP, sans HDR</td>
      <td>Capteurs plus grands, multi‑objectifs, HDR/Night Mode</td>
      <td>Qualité d'image, zoom polyvalent, basse lumière</td>
    </tr>
    <tr>
      <td>Batterie et charge</td>
      <td>Autonomie modeste, charge lente</td>
      <td>Optimisations logicielles, charge rapide/sans fil</td>
      <td>Moins d'interruptions, usage intensif soutenu</td>
    </tr>
    <tr>
      <td>Sécurité</td>
      <td>Code PIN basique</td>
      <td>Chiffrement par défaut, biométrie (empreinte/visage)</td>
      <td>Protection des données et des paiements</td>
    </tr>
    <tr>
      <td>Logiciels et écosystèmes</td>
      <td>Peu d'apps, API limitées</td>
      <td>App stores, mises à jour OTA, services cloud</td>
      <td>Fonctionnalités continues et connectées</td>
    </tr>
    <tr>
      <td>Matériaux</td>
      <td>Plastiques variés</td>
      <td>Aluminium, verre renforcé, normes IP67/IP68</td>
      <td>Durabilité, résistance à l'eau et à la poussière</td>
    </tr>
  </table>

  <p>Source: texte généré par Copilot.</p>
</body>
</html>
```
````


### Sélecteur par classe

Le sélecteur de classe permet d'appliquer un style à plusieurs éléments qui
appartiennent à une même classe (groupe). Pour cela, il faut ajouter un nouvel
attribut class à la balise HTML concernée.

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Fichier HTML
  ```{code-block} html
  <p class="centre">
  Le texte de ce paragraphe sera centré.
  </p>
  ```
- # Fichier CSS
  ```{code-block} css
  .centre {
    text-align: center;
  }
  ```
````

Ce style ne s'appliquera qu'aux balises dont la classe est "centre".

## Exercice {num2}`exercice`

Le contenu d'un page a été défini en HTML de la manière suivante.

```{exec} html
:name: selecteur-classe
:when: never
<style>
td {
  padding: 30px;
  vertical-align: top;
}

.centre {
  text-align: center;
}

</style>
```


Au moyen du CSS, modifiez les éléments suivants:

1.  Le titre doit être centré.
2.  Le texte à droite de l'image doit être centré.
3.  L'image doit être centrée, ainsi sa source.

```{exec} html
:editor: 4b0c4093-3e13-461a-9bdd-426319a4344e
:after: selecteur-classe
:when: load
:style: height: 30rem;
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Drapeau Suisse</title>
  </head>
  <body>
    <h1>La Suisse</h1>
    <p>
      La Suisse est un pays situé au coeur de l’Europe, connu pour ses montagnes majestueuses
      comme les Alpes et le Jura, ses lacs pittoresques et ses villes cosmopolites telles que
      Zurich, Genève et Berne (la capitale).
    </p>
    <p>
      Elle est réputée pour sa neutralité politique, son système démocratique unique,
      ses banques, son chocolat et ses montres de haute précision.
      La Suisse est composée de 26 cantons et possède quatre langues officielles :
      l’allemand, le français, l’italien et le romanche.
    </p>
    <p>
      Grâce à sa diversité culturelle et géographique, la Suisse attire des millions de visiteurs
      chaque année et reste un symbole de stabilité et de prospérité en Europe.
    </p>

    <h2>Drapeau</h2>
    <table>
      <tr>
        <td>
          <p>
            Le drapeau suisse est rouge avec une croix blanche au centre.
            Il est unique car il est de forme carrée, contrairement à la plupart des drapeaux
            nationaux. La croix blanche symbolise la neutralité, la paix et l’unité du pays.
          </p>
          <p>
            Le rouge représente le courage et la force.
            Ce drapeau est reconnu dans le monde entier et est un symbole fort de la
            Confédération suisse.
          </p>
        </td>
        <td>
          <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Switzerland.svg" width="200">
          <p>source: <a href= "https://fr.wikipedia.org/wiki/Suisse">Wikipédia</a></p>
        </td>
      </tr>
    </table>

    <p>Source: texte généré par Copilot.</p>
  </body>
</html>
```

````{solution}
```{exec} html
:editor:
:after: selecteur-classe
:when: load
:style: height: 30rem;
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Drapeau Suisse</title>
  </head>
  <body>
    <h1 class="centre">La Suisse</h1>
    <p>
      La Suisse est un pays situé au cœur de l’Europe, connu pour ses montagnes majestueuses
      comme les Alpes et le Jura, ses lacs pittoresques et ses villes cosmopolites telles que
      Zurich, Genève et Berne (la capitale).
    </p>
    <p>
      Elle est réputée pour sa neutralité politique, son système démocratique unique,
      ses banques, son chocolat et ses montres de haute précision.
      La Suisse est composée de 26 cantons et possède quatre langues officielles :
      l’allemand, le français, l’italien et le romanche.
    </p>
    <p>
      Grâce à sa diversité culturelle et géographique, la Suisse attire des millions de visiteurs
      chaque année et reste un symbole de stabilité et de prospérité en Europe.
    </p>

    <h2>Drapeau</h2>
    <table>
      <tr>
        <td>
          <div class="centre">
          <p>
            Le drapeau suisse est rouge avec une croix blanche au centre.
            Il est unique car il est de forme carrée, contrairement à la plupart des drapeaux
            nationaux. La croix blanche symbolise la neutralité, la paix et l’unité du pays.
          </p>
          <p>
            Le rouge représente le courage et la force.
            Ce drapeau est reconnu dans le monde entier et est un symbole fort de la
            Confédération suisse.
          </p>
          </div>
        </td>
        <td>
          <div class="centre">
          <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Switzerland.svg" width="200">
          <p>source: <a href= "https://fr.wikipedia.org/wiki/Suisse">Wikipédia</a></p>
          </div>
        </td>
      </tr>
    </table>

    <p>Source: texte généré par Copilot.</p>
  </body>
</html>
```
````


[Tuto](https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/CSS_basics)
bases du CSS.

## Conteneurs `<div>`

Un conteneur est un élément qui contient plusieurs éléments et qui est défini
comme un bloc. Il est défini en HTML par la balise `<div>...</div>`. Dans le
fichier CSS, il est possible de définir différentes propriétés d'un bloc, comme
la hauteur (height), la largeur (width), la marge intérieure (padding), la marge
extérieure (margin) ou la bordure (border).

```{image} images/conteneur.png
:alt: Définition des marges d'un conteneur
:align: center
```

````{list-grid}
:style: grid-template-columns: 1fr 1fr;
- # Fichier HTML
  ```{code-block} html
  <div id="mon_conteneur">
  <h2>Mon sous-titre</h2>
  <p>Lorem ipsum dolor sit amet, consectetur
  adipiscing elit. Suspendisse ut erat eu risus
  pharetra volutpat eu eget velit. Suspendisse
  ultrices felis a facilisis feugiat.</p>
  </div>
  ```
- # Fichier CSS
  ```{code-block} css
  #mon_conteneur {
    background-color: red;
    width: 100%;
    height: 400px:
    border: 2px solid;
    padding: 1em;
  }
  ```
````

## Liens utiles

- [Tuto](https://developer.mozilla.org/fr/docs/Web/HTML) pour le HTML.
- [Tuto](https://developer.mozilla.org/fr/docs/Web/CSS) pour le CSS.
- [Tuto](https://www.w3schools.com/) en anglais.
