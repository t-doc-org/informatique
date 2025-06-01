% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
scripts:
  - src: quizz-helpers.js
```

# Routage

Internet est constitué de millions de réseaux interconnectés, formant ainsi un
réseau décentralisé, contrôlé par une multitude d'utilisateurs. Afin d'assurer
une transmission d'informations claire et efficace, chaque machine connectée
doit être accessible et identifiable de façon unique.


## Téléphone traditionnel

Le téléphone traditionnel repose sur un réseau centralisé, administré par un
opérateur unique (le standard) qui connecte l'ensemble des appareils reliés au
réseau. Pour établir une communication entre deux personnes, l'opérateur assure
la liaison entre leurs téléphones. À l'origine, cette connexion était effectuée
manuellement par une opératrice; aujourd'hui, ce processus est automatisé.

[Standard téléphonique](https://fr.wikipedia.org/wiki/Standard_téléphonique)

Lorsqu'une communication est établie entre deux personnes, elles "occupent la
ligne": cela signifie qu'elles ne peuvent pas être jointes par d'autres
interlocuteurs, comme l'indique le signal d'occupation. Cependant, cela
n'affecte pas les autres utilisateurs du réseau, sauf en cas de surcharge du
standard. Ce fonctionnement repose sur la commutation de circuits, un procédé
par lequel un circuit électrique dédié est établi entre les deux appareils en
communication.

Établir une commutation de circuits entre deux appareils monopolise les
ressources, empêchant d'autres utilisateurs de communiquer et risquant de
saturer le réseau.

```{figure} images/commutation-circuits.png
:alt: Exemple de commutation de circuits
:width: 50%
:align: center
```

Lorsqu'une connexion est établie entre Alice et Bob, Max ne peut plus échanger
avec Zoé ou Tom.

## Internet

Internet repose sur l'interconnexion de multiples réseaux, c'est pourquoi il
utilise la commutation par paquets: les données sont découpées en petits paquets,
qui sont ensuite envoyés indépendamment à travers le réseau. Ce mode de
transmission permet de faire circuler plusieurs communications simultanément,
sans bloquer les autres utilisateurs.

```{figure} images/commutation-paquets.png
:alt: Exemple de commutation par paquets
:width: 70%
:align: center
```

Le routage désigne le processus par lequel un chemin est choisi pour faire
circuler des données à travers un ou plusieurs réseaux. Cette tâche est assurée
les routeurs, qui prennent les décisions nécessaires pour acheminer les
paquets vers leur destination.

### Exercice {num}`exo-reseaux`

Le réseau de routeurs suivant est donné.

```{figure} images/routage.png
:alt: Exercice de routage
:width: 50%
:align: center
```

Complétez les tables de routages suivantes.

Routeur B:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | A | 1 |
|C | D | 2 |
|D | | |
|E | | |
|F | | |
|G | | |
|H | | |

Routeur F:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | | |
|B | | |
|C | | |
|D | | |
|E | | |
|G | | |
|H | | |

Routeur C:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | | |
|B | | |
|D | | |
|E | | |
|F | | |
|G | | |
|H | | |

### Exercice {num}`exo-reseaux`

Proposez un réseau de routeurs qui corresponde aux tables de routages données
ci-dessous.

Routeur A:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|B | B | 1 |
|C | C | 1 |
|D | B | 2 |
|E | B | 2 |

Routeur B:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | A | 1 |
|C | A | 2 |
|D | D | 1 |
|E | E | 1 |

Routeur C:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | A | 1 |
|B | A | 2 |
|D | A | 3 |
|E | A | 3 |

Routeur D:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | B | 2 |
|B | B | 1 |
|C | B | 3 |
|E | E | 1 |

Routeur E:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | B | 2 |
|B | B | 1 |
|C | B | 3 |
|D | D | 1 |

### Exercice {num}`exo-reseaux`

Complétez le chemin (noms des routeurs) par lequel passe un message pour
atteindre sa destination depuis son point de départ en regardant seulement les
tables de routages.

| Départ | Destination | Chemin |
| :---------: | :-------------: | :------: |
|D | A |  |
|C | E |  |
|A | F |  |
|F | A |  |
|D | C |  |


Routeur A:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|B | C | 2 |
|C | C | 1 |
|D | C | 3 |
|E | C | 3 |
|F | C | 2 |

Routeur B:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | C | 2 |
|C | C | 1 |
|D | D | 1 |
|E | D | 1 |
|F | C | 2 |

Routeur C:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | A | 1 |
|B | B | 1 |
|D | B | 2 |
|E | B | 2 |
|F | F | 1 |

Routeur D:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | B | 3 |
|B | B | 1 |
|C | B | 2 |
|E | B | 2 |
|F | B | 3 |

Routeur E:

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
|A | B | 3 |
|B | B | 1 |
|C | B | 2 |
|D | B | 2 |
|E | B | 3 |
