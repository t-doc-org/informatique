% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Couleurs

Avant de voir la représenter des images, il est nécessaire de s'intéresser à la
représentation des couleurs.

## Codage RGB

Il existe plusieurs façons de décrire les couleurs en informatique. Dans ce
cours, nous nous intéresserons au système de codage RGB (pour Red Green Blue)
noté parfois RVB en français (pour Rouge Vert Bleu). Le principe consiste à
mélanger ou plus précisément à additionner une certaine quantité des trois
couleurs primaires (rouge, vert et bleu) pour obtenir la couleur finale. Ce
procédé s'appelle la synthèse additive.

### Code RGB décimal

Chacune des trois couleurs primaires est représentée par un nombre compris entre
0 et 255 (c'est-à-dire 256 valeurs). Il faut donc 3 octets pour coder un pixel
avec le code RGB décimal, ce qui prend rapidement beaucoup de place.

Exemple: Le rouge est représenté par (255, 0, 0).

```{figure} images/rgb-color.png
:alt: Image des couleurs RGB
:width: 30%
:align: center
```

## Exercice {num2}`exercice`

De quelle couleur s'agit-il ?

```{role} select(quiz-select)
:right:
:options: |
: noir
: blanc
: rouge
: vert
: bleu
: jaune
: magenta
: cyan
: gris foncé
: gris clair
```

```{quiz}
:style: max-width: 30rem;
1.  {select}`rouge` `(255, 0, 0)`
2.  {select}`noir` `(0, 0, 0)`
3.  {select}`bleu` `(0, 0, 255)`
4.  {select}`gris foncé` `(64, 64, 64)`
5.  {select}`jaune` `(255, 255, 0)`
6.  {select}`vert` `(0, 255, 0)`
7.  {select}`blanc` `(255, 255, 255)`
8.  {select}`gris clair` `(204, 204, 204)`
9.  {select}`magenta` `(255, 0, 255)`
10.  {select}`cyan` `(0, 255, 255)`
```



### Code RGB hexadécimal

Une autre manière de représenter les couleurs est d'utiliser l'hexadécimal.
Cette représentation est plus compacte, car il suffit de 2 chiffres hexadécimaux
pour représenter 256 valeurs (de $00_{16}$ à $FF_{16}$). Le code RGB hexadécimal
débute toujours par \#.

Exemple: Le rouge est représenté par #FF0000.


### Tableau des couleurs principales

<style>
.table-couleur {
  border-collapse: collapse;
  width: 100%;
  margin: 1rem auto;
}
.table-couleur th, .table-couleur td {
  border: 1px solid black;
  text-align: center;
  padding: 8px;
}
.table-couleur th {
  background-color: #f2f2f2;
}
</style>

<table class="table-couleur">
  <tr>
    <th>Couleur</th>
    <th>Nom</th><th>Code hexadécimal</th><th>Code décimal (R,G,B)</th>
  </tr>
  <tr>
    <td style="background-color: #000000;"></td>
    <td>black</td><td>#000000</td><td>(0, 0, 0)</td>
  </tr>
  <tr>
    <td style="background-color: #ffffff;"></td>
    <td>white</td><td>#FFFFFF</td><td>(255, 255, 255)</td>
  </tr>
  <tr>
    <td style="background-color: #ff0000;"></td>
    <td>red</td><td>#FF0000</td><td>(255, 0, 0)</td>
  </tr>
  <tr>
    <td style="background-color: #00ff00;"></td>
    <td>lime</td><td>#00FF00</td><td>(0, 255, 0)</td>
  </tr>
  <tr>
    <td style="background-color: #0000ff;"></td>
    <td>blue</td><td>#0000FF</td><td>(0, 0, 255)</td>
  </tr>
  <tr>
    <td style="background-color: #ffff00;"></td>
    <td>yellow</td><td>#FFFF00</td><td>(255, 255, 0)</td>
  </tr>
  <tr>
    <td style="background-color: #00ffff;"></td>
    <td>cyan</td><td>#00FFFF</td><td>(0, 255, 255)</td>
  </tr>
  <tr>
    <td style="background-color: #ff00ff;"></td>
    <td>magenta</td><td>#FF00FF</td><td>(255, 0, 255)</td>
  </tr>
  <tr>
    <td style="background-color: #c0c0c0;"></td>
    <td>silver</td><td>#C0C0C0</td><td>(192, 192, 192)</td>
  </tr>
  <tr>
    <td style="background-color: #808080;"></td>
    <td>gray</td><td>#808080</td><td>(128, 128, 128)</td>
  </tr>
</table>

Si les trois valeurs sont identiques, nous obtiendrons du gris. Avec une valeur
petite, le gris sera foncé et avec une valeur élevée, le gris sera clair.

Sur le site
"[Liste des couleurs](https://www.rapidtables.com/web/color/RGB_Color.html)", il
y a les références de toutes les couleurs possibles.

### Nombre de couleurs possibles

Avec 3 octets (24 bits), il est possible de représenter:

$$2^{24} = 16\,777\,216 \text{ couleurs différentes}$$

Sachant qu l'oeil humain peut différencier jusqu'à 10 millions de couleurs,
cette représentation est largement suffisante.

## Exercice {num2}`exercice`

De quelle couleur s'agit-il ?

```{role} select(quiz-select)
:right:
:options: |
: noir
: blanc
: rouge
: vert
: bleu
: jaune
: magenta
: cyan
: gris foncé
: gris clair
```

```{quiz}
:style: max-width: 30rem;
1.  {select}`blanc` `#FFFFFF`
2.  {select}`vert` `#00FF00`
3.  {select}`cyan` `#00FFFF`
4.  {select}`rouge` `#FF0000`
5.  {select}`gris foncé` `#404040`
6.  {select}`noir` `#000000`
7.  {select}`jaune` `#FFFF00`
8.  {select}`bleu` `#0000FF`
9.  {select}`magenta` `#FF00FF`
10.  {select}`gris clair` `#CCCCCC`
```


## Exercice {num2}`exercice`

Combien d'octets faut-il pour représenter une image de 1920 × 1080 pixels en
couleur?

```{solution}
Chaque pixel nécessite 3 octets (un pour R, un pour G, un pour B).

Nombre de pixels: $1920 \cdot 1080 = 2\,073\,600$ pixels

Nombre d'octets: $3 \cdot 2\,073\,600 = 6\,220\,800$ octets

Cela correspond à environ $6.2$ Mo (mégaoctets).
````
