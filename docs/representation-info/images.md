% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Images

Nous avons vu comment représenter des nombres et des caractères. Maintenant nous
allons nous intéresser aux images.

## Format

Il existe deux types de format d'image:

- le format matriciel ou bitmap (bmp, jpg, gif, png, ...)\
  L'image est composée de points appelés **pixels**[^sn1]. Ceux-ci sont
  tellement petits que nous ne les voyons pas à l'oeil nu, mais si nous
  agrandissons l'image, les pixels deviennent visibles et l'image devient floue.
- le format vectoriel (svg, eps, pdf)\
  L'image est composée d'objets géométriques (segments, cercles, polygones,
  etc.) définis par des attributs (forme, position, couleur, etc.). De ce fait,
  une image vectorielle peut être agrandie sans perte de qualité.
[^sn1]: picture element

| image originale | image matricielle zoomée | image vectorielle zoomée |
|:---------------:|:------------------------:|:------------------------:|
| <img src="images/birds.png" width="80%">| <img src="images/image-matricielle.png" width="80%">|<img src="images/image-vectorielle.png" width="55%">|

## Images en noir et blanc

Pour représenter une image en noir et blanc, nous définissons qu'un bit
représente un pixel. S'il est blanc, il prendra la valeur 0, s'il est noir,
la valeur 1.

```{figure} images/image-noir-blanc.png
:alt: Image en noir et blanc
:width: 50%
:align: center
```

Cette image a donc besoin de 8 octets (64 bits) pour être sauvegardée en
mémoire, car nous avons 64 cases qui ont besoin chacune d'un bit pour définir
le noir ou le blanc. Cette image a un poids de 8 octets.

## Exercice {num}`exo-info`

1.  Quel est le poids de l'image ci-dessous?

2.  Quel est le code binaire de la lettre S représentée ci-dessous.

```{figure} images/s-pixels.png
:alt: Image S en noir et blanc
:width: 30%
:align: center
```

````{solution}
1.  Le poids de cette image est $1 \cdot 8 \cdot 8 = 64\, \text{bits} = 8$ octets.
2.  ```{code-block}
    0000 0000
    0111 1110
    1000 0001
    1000 0000
    0111 1110
    0000 0001
    1000 0001
    0111 1110
    ```
````

## Exercice {num}`exo-info`

Représenter l'image en noir et blanc donnée par le code suivant:
```{figure} images/vide-noir-blanc-pixels.png
:alt: Image vide en noir et blanc
:width: 50%
:align: center
```

````{solution}
```{figure} images/image-noir-blanc-alien.png
:alt: Image noir blanc alien
:width: 30%
:align: center
```
````

## Images en niveaux de gris

Dans le cas d'une image en niveau de gris, nous n'utiliserons pas 1 mais
plusieurs bits par pixel.
Dans cet exemple, nous utilisons 2 bits, nous aurons donc 4 niveaux de gris à
disposition.

```{figure} images/niveaux-gris.png
:alt: Image des niveaux de gris
:width: 70%
:align: center
```

```{figure} images/image-gris.png
:alt: Image en niveaux de gris
:width: 50%
:align: center
```
Cette image a un poids de $2 * 8 * 8 = 128$ bits qui est équivalent à 16 octets,
car nous avons 64 cases qui ont besoin chacune de 2 bits pour définir le gris.


## Exercice {num}`exo-info`

1. Quel est le poids de l'image ci-dessous?

2. Quel est le code binaire de cette image en 4 niveaux de gris.

```{figure} images/koala-pixels.png
:alt: Image d'un koala en gris
:width: 70%
:align: center
```

````{solution}
1.  Le poids de cette image est $2 \cdot 8 \cdot 8 = 128\, \text{bits} = 16$
    octets.
2.  ```{code-block}
    0101 0000 0000 0101
    0101 0101 0101 0101
    0001 1101 0111 0100
    0001 1101 0111 0100
    0101 0101 0101 0101
    0101 0100 0001 0101
    0101 0100 0001 0101
    0001 1010 1010 0100
    ```
````

## Exercice {num}`exo-info`

Représenter l'image en 4 niveaux de gris donnée par le code suivant:

```{figure} images/vide-gris-pixels.png
:alt: Image vide en niveaux de gris
:width: 50%
:align: center
```

````{solution}
```{figure} images/image-gris-raton.png
:alt: Image gris raton-laveur
:width: 30%
:align: center
```
````

## Images en couleurs

Il existe plusieurs façons de décrire les couleurs en informatique. Dans ce
cours, nous nous intéresserons au système de codage RGB (pour Red Green Blue)
noté parfois RVB en français (pour Rouge Vert Bleu). Le principe consiste à
mélanger ou plus précisément à additionner une certaine quantité des trois
couleurs primaires (rouge, vert et bleu) pour obtenir la couleur finale. Ce
procédé s'appelle la synthèse additive.

Chacune des trois couleurs primaires est représentée par un nombre compris entre
0 et 255 (donc 256 valeurs). Il faut donc 3 octets pour coder un pixel, ce qui
prend rapidement beaucoup de place.

```{figure} images/rgb-color.png
:alt: Image des couleurs RGB
:width: 30%
:align: center
```

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

En général, le code RGB est noté en hexadécimal et il est précédé d'un \#.\
Si les trois valeurs sont identiques, nous obtiendrons du gris.

Sur le site
"[Liste des couleurs](https://www.rapidtables.com/web/color/RGB_Color.html)", il
y a les références de toutes les couleurs possibles.

## Exercice {num}`exo-info`

Quel est le poids d'une image de 500 sur 300 pixels (1 pixel est équivalent à
une case) codée...

```{role} input(quiz-input)
:right: width: 6rem;
:check: json trim
```

```{quiz}
:style: max-width: 30rem;
1.  {input}`{"18.75": true, "18,75": true}`
    ... en noir et blanc? (en ko)
2.  {input}`{"37.5": true, "37,5": true}`
    ... en 4 niveaux de gris? (en ko)
3.  {input}`{"150": true}`
    ... en 256 niveaux de gris? (en ko)
4.  {input}`{"450": true}`
    ... en RGB? (en ko)
```

## Exercice {num}`exo-info`

Quel est le code décimal et hexadécimal d'un pixel...
1. ... en noir?
2. ... en blanc?
3. ... en gris?
4. ... en jaune?

```{solution}
| Couleur    | Code décimal          | Code hexadécimal |
|:-----------|:---------------------:|:----------------:|
| 1. noir    | (0, 0, 0)             | #000000          |
| 2. blanc   | (255, 255, 255)       | #FFFFFF          |
| 3. gris    | p.ex. (214, 214, 214) | #D6D6D6          |
| 4. jaune   | (255, 255, 0)         | #FFFF00          |
```

## Exercice {num}`exo-info`

Quelle couleur est représentée par les codes RGB suivants?
1. (100, 50, 200)
2. (20, 200, 250)
3. (50, 220, 50)

```{solution}
<style>
.table-sol.table-sol.table-sol {
  border-collapse: collapse;
  margin: 1rem auto;
}
.table-sol td {
  border: 1px solid black;
  text-align: center;
  padding: 8px;
}
.table-sol td + td + td {
  width: 4rem;
}
</style>

<table class="table-sol">
  <tr>
    <td>(100, 50, 200)</td>
    <td>violet</td>
    <td style="background-color: rgb(100, 50, 200)"></td>
  </tr>
  <tr>
    <td>(20,200,250)</td>
    <td>bleu</td>
    <td style="background-color: rgb(20,200,250)"></td>
  </tr>
  <tr>
    <td>(50,220,50)</td>
    <td>vert</td>
    <td style="background-color: rgb(50,220,50)"></td>
  </tr>
</table>
```
