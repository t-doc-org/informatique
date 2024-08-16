<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# HTML

Le format **HTML** (HyperText Markup Language) est un format qui permet de
décrire le contenu et la structure d'une page Web. HTML n'est pas un langage de
programmation, il ne contient ni fonction, ni boucle, ni instruction
conditionnelle, mais c'est un ensemble de balises qui permettent de mettre un
document en page, afin que le navigateur puisse l'afficher correctement.

Les balises ont la forme suivante:

```{code} html
<h1>Bienvenue sur notre site Web</h1>
```

`<h1>` est une balise ouvrante et `</h1>` est une balise fermante. À chaque
balise ouvrante correspond une balise fermante à l'exception des balises qui
n'ont pas de contenu.

## Balise `<!DOCTYPE html>`

Tous documents qui décrivent une page Web doivent débuter par:

```{code} html
<!DOCTYPE html>
```

Ce n'est pas une balise HTML, mais une information qui permet au navigateur de
savoir le type de document.

## Balise `<html>`

Tout le code HTML doit être inséré dans une balise nommée html:
`<html> … </html>`.
La balise html contient en général deux autres balises:
- `<head> … </head>`: entête du document, elle contient différentes informations
concernant le document (titre de la page, type d'encodage, lien vers le fichier
CSS, etc.).
  Ces informations ne seront pas affichées à l'écran à l'exception du titre
  affiché sur l'onglet de la page.
- `<body> … </body>`: contient le contenu (corps) de la page. Tout ce qui sera
dans cette partie sera affiché.

<!-- TODO: Améliorer le styling du code, notamment la numérotation. -->

````{sidebar}
```{figure} images/balise-html.png
:alt: Balise HTML
:align: center
```
````

```{code} html
:number-lines:
<!DOCTYPE html>
<html>
  <head>
    ...
  </head>
  <body>
    ...
  </body>
</html>
```

## Balise `<body>`

Dans la balise `<body>`, nous allons structurer le contenu de la page. Nous
  allons voir les balises les plus simples qui permettent de définir des titres,
  sous-titres et paragraphes:
- `<h1> ... </h1>`: permet de définir un titre principal
- `<h2> ... </h2>`: permet de définir un sous-titre
- `<h3> ... </h3>`: permet de définir un sous-sous-titre
- `<h...> ... </h...>`: permet de définir un sous-...-sous-titre
- `<p> ... </p>`: permet de définir un paragraphe

<table><tr><td>

```{code} html
:number-lines:
<!DOCTYPE html>
<html>
  <head> ... </head>
  <body>
    <h1>Titre principal</h1>
    <p>
      Vous êtes dans le corps de la page de test HTML.
    </p>
  </body>
</html>
```

</td><td>

![balise body](images/balise-body.png)

</td></tr></table>

## Balise `<head>`

La balise `<head>` contient différentes informations sur le document, notamment
  le titre de la page et le type d'encodage.

## Balise `<title>`

La balise `<title>` permet de définir le titre de la page qui s'affichera sur
  l'onglet du navigateur web.

```{code} html
<title>Ma page</title>
```

![titre](images/titre.png)

## Balise `<meta>`

La balise `<meta>` permet d'indiquer le type d'encodage (ASCII, Unicode, UTF-8).
Nous souhaitons que les accents s'écrire correctement sur notre page, nous
allons donc utiliser de l'utf-8 que nous allons indiquer dans l'attribut
charset:

```{code} html
<meta charset="utf-8">
```

Comme cette balise ne contient pas de contenu, c'est une balise unique (pas de
balise ouvrante et fermante).

(hyperliens)=
## Hyperliens

La balise `<a>` permet de créer un  hyperlien, c'est-à-dire un texte sur lequel
  il faut cliquer pour accéder à une autre page. Il faut indiquer le lien dans
  l'attribut href: `<a href='lien'>Texte</a>`

```{code} html
:number-lines:
<p>
  Pour accéder au site du collège,
  cliquez <a href="https://www.cscfr.ch/index.php/fr/">ici</a>
</p>
```

Pour ouvrir la nouvelle page dans un nouvel onglet, il faut ajouter l'attribut
`target` avec la valeur `_blank`:

```{code} html
<a href="lien" target="_blank">Texte</a>
```

[Tuto](https://developer.mozilla.org/fr/docs/Web/HTML/Element/a) élément `<a>`.

(listes)=
## Listes

Il existe deux types de listes:

1. Listes numérotées (ordered) `<ol>`
   ```{code} html
   :number-lines:
   <ol>
      <li>Mettre 1L d'eau dans un casserole</li>
      <li>Porter à ébullition</li>
      ...
   </ol>
   ```
2. Listes à puces (unordered) `<ul>`
   ```{code} html
   :number-lines:
   <ul>
      <li>Tomates</li>
      <li>Courgettes</li>
      ...
   </ul>
   ```

[Tuto](https://developer.mozilla.org/fr/docs/Web/HTML/Element/li) listes.

(images)=
## Images

La balise `<img>` permet d'insérer une image sur une page Web. Dans l'attribut
`src`, il faut indiquer le lien vers l'image, soit une URL, soit le chemin
local.

- `<img src="mon_image.png">` (dans le même répertoire)
- `<img src="images/mon_image.png">` (dans un sous-répertoire)

Cette balise peut contenir aussi les attributs height ou width qui permettent de
déterminer la hauteur et/ou la largeur de l'image en pixels.

```{code} html
<img src= "images/mon_image.png" width="300" height="200">
```

[Tuto](https://developer.mozilla.org/fr/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML)
images.

## Sauts de ligne

La balise `<br>` permet de faire un saut de ligne (break). Comme cette balise ne
contient pas de contenu, c'est une balise unique (pas de balise ouvrante et
fermante).

```{code} html
À la fin de cette ligne, il y aura un saut de ligne. <br>
```

## Tables ou tableaux

La balise `<table>` permet de représenter des tableaux de données (tableaux en
  deux dimensions). Les tableaux peuvent aussi être utilisés pour la mise en
  page, par exemple mettre du texte à côté d'une image ou mettre plusieurs
  images l'une à côté de l'autre.

```{code} html
:number-lines:
<table>
  <tr>                        <!-- Première ligne -->
    <th>Ingrédients</th>      <!-- entête première colonne -->
    <th>Quantité</th>         <!-- entête deuxième colonne -->
  </tr>
  <tr>                        <!-- Deuxième ligne -->
    <td>Pommes de terre</td>  <!-- Première colonne -->
    <td>1 kg</td>             <!-- Deuxième colonne -->
  </tr>
  <tr>
    <td>lait</td>
    <td>0.5l</td>
  </tr>
</table>
```

[Tuto](https://developer.mozilla.org/fr/docs/Web/HTML/Element/table) tables et
tableaux

## Exercices

### Exercice 1

But: Comprendre la structure principale d'un document HTML.\
Faire [ex 1](https://moodle.fritic.ch/mod/hvp/view.php?id=112347) sur Moodle.

### Exercice 2

But: Ouvrir un document HTML sur replit.com.

1. Sur Moodle, télécharger le document `index.html`.
2. Sauvegarder ce document sur OneDrive dans le dossier informatique.
3. Se connecter sur replit.com.
4. Cliquer sur **+ Create Repl**.
5. Choisir **HTML, CSS, JS**.
6. Nommer le Repl **Exemple**.
7. Cliquer à nouveau sur **+ Create Repl**.\
   ![replit](images/replit.png)
8. Il faut remplacer le fichier `index.html` par celui que vous avez téléchargé:
   - Effacer le fichier `index.html` déjà présent.
   - Télécharger votre fichier en cliquant sur les 3 points verticaux et en
   sélectionnant **Upload file**. Choisir le fichier `index.html` que vous avez
   sauvegardé sur votre OneDrive.
9. Appuyer sur le bouton **Run**.

### Exercice 3

But: Comprendre un document HTML simple et le modifier.\
Vous voyez maintenant le code HTML et ce que la page affiche.

1. Qu'est-ce que vous comprenez de cette page?
2. Vous allez maintenant modifier cette page (pour valider une modification,
appuyer sur **Run**):
   - Modifier le titre et le premier paragraphe pour remplacer Collège du Sud
   par Collège Sainte-Croix.
   - Modifier la partie présentation pour avoir les informations qui
   correspondent au Collège Sainte-Croix. Changer aussi le lien vers le site de
   l'école. (cf. [](#hyperliens))
   - Compléter la liste de vos cours avec: Économie et droit, Biologie, ...
   - Changer la liste de vos cours par une liste numérotée. (cf. [](#listes))
   - Ajouter un sous-titre **Ma classe** et un paragraphe avec quelques
   informations.
   - Ajouter une image du Collège Sainte-Croix:
     - Télécharger l'image que vous avez choisie.
     - Importer l'image sur replit.com dans un répertoire nommé **images**.
     - Noter le code HTML nécessaire. (cf. [](#images))
     - Ne pas oublier d'indiquer la source.
   - Faire un tableau de votre horaire.
