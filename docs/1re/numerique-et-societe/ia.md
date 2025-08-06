% Copyright 2025 Caroline Blank <caro@c-space.org>
% Copyright 2025 Brice Canvel
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Intelligence artificielle

```{metadata}
solutions: dynamic
```

```{poll} 424dffac-9cd1-4d5c-9007-0bd2facce7f3
:number: none
À quelle fréquence utilisez-vous l'intelligence artificielle? Par exemple
ChatGPT.

- Jamais
- Rarement
- Au moins une fois par mois
- Une fois par semaine
- Plusieurs fois par semaine
- Tous les jours d'école
- Tous les jours
```

## Introduction

L'intelligence artificielle est un ensemble de technologies du traitement
automatique de l'information ayant pour but de simuler le raisonnement humain.

Le terme anglais machine learning [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) est plus adapté.

L'IA vise à imiter certaines capacités propres à l'être humain:
- l'apprentissage de règles
- le raisonnement logique
- le langage
- la planification
- la reconnaissance d'images et de son

```{poll} 0e6b485a-1184-4289-aafd-016ce448da05
:mode: multi
:number: none
Quels services utilisent l'intelligence artificielle?

- Les moteurs de recherche
- Les messageries électroniques
- Wikipédia
- Spotify
- Les sites marchands
- Les caisses automatiques
- Les réseaux sociaux
- Les assistants vocaux
- Les voitures autonomes
- Les traducteurs
- Les applications de navigation
```

Singularité technologique
: Correspond au moment hypothétique où l'IA dépassera l'intelligence humaine et
  donc que les machines seront elles-mêmes capables de programmer des machines.

```{poll} bf3dfff8-c0df-47ca-a66b-27ad70aa2f9e
:number: none
Pensez-vous que ce moment arrivera?

- Oui
- Non
```

## Fonctionnement

L'IA repose sur des méthodes permettant aux machines d'apprendre à partir de
données (modèles prédictifs). Pour créer de bons modèles prédictifs, les
réseaux de neurones de l'intelligence artificielle sont entraînés avec beaucoup
de données. C'est ce qu'on appelle l'apprentissage automatique: les algorithmes
apprennent à partir des données qu'on leur donne. Il existe différents types
d'apprentissage, par exemple:

-   L'apprentissage supervisé:\
    l'algorithme apprend à partir de donnée étiquetées par des humains.
-   L'apprentissage non-supervisé:\
    L'algorithme organise les données et recherche des structures cachées, des
    motifs qui se répètent, etc. pour classifier les éléments.
-   L'apprentissage par renforcement:\
    L'algorithme pend des décisions en fonction de la situation et reçoit un
    feedback positif ou négatif en fonction de ses choix. Il apprend donc par
    expérience.

### Exercice {num2}`exercice`

But: comprendre comment fonctionne l'apprentissage supervisé.

**Mise en place**

1.  Téléchargez le document [Pommes vs oranges](ia-training.docx) et répondez
    à la première question.
2.  Allez sur le site
    [Teachable Machine](https://teachablemachine.withgoogle.com/train).
3.  Choisissez **Projet Images** &rarr; **Modèle d'image standard**.
4.  Télécharger les images de pommes: [data_pommes.zip](data_pommes.zip).
5.  Importez les images de pommes:
    - Renommez "Class 1" en Pommes.
    - Cliquez sur "Importer".
    ```{image} images/import.png
    :alt: import des images
    :width: 50%
    :align: center
    ```
6.  Télécharger les images d'oranges: [data_oranges.zip](data_oranges.zip).
7.  Importez les images d'oranges:
    - Renommez "Class 1" en Oranges.
    - Cliquez sur "Importer".
8.  Cliquez sur "Entrainer le modèle".
    ```{image} images/train.png
    :alt: entrainer le modèle
    :width: 20%
    :align: center
    ```

**Test**

Pour chacun des tests, mais à faire l'un après l'autre.

1.  Téléchargez les images pour les tests:
    - Test 1: [test_1.zip](test_1.zip)
    - Test 2: [test_2.zip](test_2.zip)
    - Test 3: [test_3.zip](test_3.zip)
    - Test 4: [test_4.zip](test_4.zip)
2.  Choisissez ensuite chaque image et regardez ce qu'identifie l'IA (Est-ce une
    pomme ou une orange?)
    ```{image} images/test.png
    :alt: tester le modèle
    :width: 30%
    :align: center
    ```
3.  Répondez aux questions.

## Modèle de langage

Les modèles de langage, comme ChatGPT, utilisent des techniques d'apprentissage
automatique pour étudier de grandes quantités de textes et repérer les
régularités et les habitudes d'usage de la langue. Ils apprennent comment les
mots s'associent fréquemment les uns avec les autres.

En se basant sur le contexte des mots déjà présents dans une phrase, le modèle
va déterminer le mot suivant le plus plausible.

### Points forts

-   Générations de textes (rédactions, poèmes, chansons, discours, etc.)
-   Générations d'images
-   Résumés (textes ou vidéos)
-   Traduction
-   Amélioration d'un texte (grammaire, orthographe, tournures de phrases, etc.)

### Limites

-   Sources manquantes ou pas vérifiées
-   Pas de compréhension réelle
-   Génération de réponses incorrectes (hallucinations)
-   Dépendance aux données d'entrainement &rarr; biais (stéréotypes, préjugés)
-   Confidentialité et données personnelles
-   Création de contenus offensants ou dangereux
-   Réglementation

## Discussions

```{poll} fd94ae7e-41e2-425c-893c-bc490b98499d
:number: none
Est-ce qu'un texte écrit par ChatGPT est du plagiat?

**Définition:** Le plagiat est le fait de présenter le travail de quelqu'un
d'autre comme étant le sien.

- Oui
- Non
```

```{poll} f5533270-83b6-40ce-9052-94eb554bdce5
:number: none
Est-ce acceptable d'utiliser ChatGPT pour faire ses devoirs?

- Oui
- Non
```

```{poll} c1bcbbd3-32ce-4f30-9c58-2116980c7e5f
:number: none
Faut-il poser des limites à l'utilisation de l'IA à l'école?

- Oui
- Non
```

- Comment les IA comme ChatGPT pourraient-elles changer les métiers de demain?
- Quel est l'impact écologique de l'entraînement et de l'utilisation de ces
  modèles?
