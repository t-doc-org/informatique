% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Vol de données

```{metadata}
solutions: dynamic
```

## Introduction

Pour voler vos données un attaquant a besoin de deux informations:

1.  votre identifiant:
    Donnée publique, donc facile à trouver.

2.  votre authentifiant:
    Donnée privée, il faut donc trouver un moyen de l'obtenir.

## Ingénierie sociale

L'ingénierie sociale regroupe les techniques qui consistent pour un fraudeur à
instaurer une relation de confiance avec une cible dans le but de la manipuler,
pour lui soutirer des informations confidentielles ou lui faire exécuter des
actions à des fins malveillantes.

Le cybercriminel ne vise pas une personne précise, mais cible un grand nombre de
personnes pour ensuite concentrer ses efforts avec celles qui semblent
réceptives.

### Exemple {num}`ex-num`

Un individu entre dans les locaux d'une entreprise et placarde une affiche à
l'aspect officiel affirmant que le numéro de service de dépannage informatique a
changé. Donc quand les salariés de l'entreprise auront besoin d'une assistance
technique ils appelleront cet individu, en ayant une entière confiance en lui.
Ainsi ce dernier pourra leur demander login, mot de passe ou d'autres
informations confidentielles et personnelles prétextant une intervention à
distance par exemple. De cette manière l'individu pourra avoir accès au système
d'information de l'entreprise. (source: Wikipédia)

### Exercice {num}`exo-num`

Citez d'autres exemples d'ingénierie sociale et expliquez pourquoi cela
fonctionne.

```{solution}
-   L'arnaque au faux support informatique:
    beaucoup de personnes ne maîtrisent pas les outils informatiques et ont
    peur des virus.
-   L'arnaque au faux policier:
    Les gens font confiance à la personne qui porte un uniforme.
-   L'arnaque aux sentiments:
    Les gens amoureux font beaucoup de choses sans réfléchir.
```

### Comment se protéger?

-   Ne jamais communiquer, par oral ou par écrit, des mots de passe ou des codes.
-   Ne pas divulguer d'informations personnelles à des inconnus.
-   Ne rien faire sous pression et prendre le temps de réfléchir.
-   Ne laisser personne accéder à votre ordinateur.
-   En cas de doute, discutez-en avec des camarades, vos parents, vos
    enseignants, etc.

## Hameçonnage

L'hameçonnage (ou phishing en anglais) est un type d'ingénierie sociale. La
méthode consiste pour un fraudeur à usurper l'identité d'un tiers de confiance,
comme une banque, une administration ou une entreprise, en reproduisant à
l'identique son site web. L'objectif est de tromper la victime en lui faisant
croire qu'elle se connecte à un site légitime afin de lui soutirer des
informations personnelles telles que des identifiants, mots de passe, numéros de
carte bancaire ou de passeport. Une fois ces données saisies sur le faux site,
elles sont récupérées par le fraudeur, qui peut alors se connecter au véritable
site avec les identifiants volés et accéder à des données confidentielles ou
dérober de l'argent.

### Exemple {num}`ex-num`

<table><tr><td>

```{figure} images/phishing1.png
:alt: Exemple de phishing
:width: 100%
:align: center
```

</td><td>

```{figure} images/phishing2.png
:alt: Exemple de phishing (zoom)
:width: 95%
:align: center
```

</td></tr></table>

````{admonition} Drôle de phénomène
:class: dropdown
```{figure} images/bd.png
:alt: Drôle de phénomène
:width: 100%
:align: center
```
````

### Comment se protéger?

Lorsque vous recevez un mail ou un sms, vérifiez:
1.  l'adresse de l'expéditeur
2.  la cohérence du message (langue, formule d'appel, signature, etc.)
3.  les liens:
    -   Ne pas ouvrir les documents attachés suspects
    -   Ne pas cliquer sur un lien sans vérifier l'adresse

Si vous vous êtes fait avoir, changez les mots de passe et/ou faites bloquer les
comptes au plus vite.

### Exemple {num}`ex-num`

["ABE - Hameçonnage"](https://www.nanoo.tv/link/v/LhTeiDga)

### Exercice {num}`exo-num`

Effectuez les quizz sur les pages suivantes:

1.  [Savez-vous reconnaître une tentative d'hameçonnage?](https://phishingquiz.withgoogle.com/)
2.  [Test sur le phishing](https://www.ebas.ch/fr/test-sur-le-hameconnage/)

