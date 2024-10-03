<!-- Copyright 2024 Caroline Blank <caro@c-space.org> -->
<!-- SPDX-License-Identifier: CC-BY-NC-SA-4.0 -->

# Architecture de von Neumann

Les techniques utilisées pour fabriquer des ordinateurs ont beaucoup évolué,
mais la plupart se basent sur les concepts définis par John von Neumann dans les
années 1940.

Ce modèle comporte quatre types de composants:

1. L'unité arithmétique et logique (UAL)
2. L'unité de contrôle (UC)
3. La mémoire
4. Les périphériques d'entrées-sorties

```{image} images/von-neumann.png
:alt: Architecture de von Neumann
:width: 80%
:align: center
```

## Unité arithmétique et logique

L'unité arithmétique et logique (ou UAL) est l'élément qui réalise tous les
calculs de l'ordinateur:

- Les opérations élémentaires (additions, soustractions, etc.)
- Les opérations logiques (ET, OU, NI, etc.)
- Les opérations de comparaison (vérifie si deux valeurs sont égales)

## Unité de contrôle

L'unité de contrôle (ou UC) joue le rôle de chef d'orchestre de l'ordinateur en
facilitant la communication entre l'UAL, la mémoire et les périphériques. Elle
se charge de récupérer en mémoire la prochaine instruction à exécuter, ainsi que
les données nécessaires, puis les envoie à l'unité arithmétique et logique.


## Mémoire

La mémoire peut être décrite comme une suite de cellules numérotées contenant
chacune une petite quantité d'information. Cette information peut servir à
indiquer à l'ordinateur ce qu'il doit faire (instructions ou programme) ou
contenir des données.

On distingue habituellement trois types de mémoires:

1. La **mémoire vive** (RAM) ou la mémoire centrale permet de stocker
temporairement les données lors de l'exécution de programme. Les données
stockées dans la mémoire vive peuvent être lues, effacées ou déplacées comme
nous le souhaitons. La mémoire vive perd son contenu dès que nous éteignons
l'ordinateur.
Le principal avantage de cette mémoire est la rapidité d'accès aux données
qu'elle contient.

2. La **mémoire de masse** conserve ses données quand nous arrêtons
l'ordinateur. Il en existe différents types:
   - Le **disque dur** qui se trouvent dans l'ordinateur.
   - Tous les **supports externes** qui permettent de stocker des données tels
   que disques durs externes, mémoire flash (SSD), clés USB, carte SD, CD, DVD,
   Blu-ray.

3. La **mémoire morte** ou ROM est une mémoire en lecture seule. C'est-à-dire
qu'elle est prévue pour être lues souvent, mais pas modifiée.

## Périphériques d'entrées-sorties

Les périphériques d'entrées/sorties permettent à l'ordinateur de communiquer
avec l'extérieur (clavier, écran, etc.).

Les périphériques d'entrées convertissent l'information qu'ils récupèrent de
l'extérieur (appui d'une touche) en données compréhensibles par l'ordinateur
(en binaire).

Les périphériques de sorties décodent l'information fournie par l'ordinateur (en
binaire) afin de la rendre compréhensible par l'utilisateur (une image qui
s'affiche sur l'écran).

<!-- TODO: À Ajouter lorsque la section sera créée.
Nous verrons cela plus en détail dans la section [](./encodage-information.md).
-->

## Vidéo

<iframe credentialless style="width: 100%; aspect-ratio: 16/9;"
  src="https://www.youtube.com/embed/85XUJXHbjBo?si=JRyirLX78uKkRVnE"
  title="Vidéo sur l'architecture de l'ordinateur" frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;
    picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
