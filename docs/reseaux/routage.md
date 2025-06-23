% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
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
par les routeurs, qui prennent les décisions nécessaires pour acheminer les
paquets vers leur destination.

```{youtube} 88JeRflty4s
```

### Exercice {num}`exo-reseaux`

Le réseau de routeurs suivant est donné.

```{figure} images/routage.png
:alt: Exercice de routage
:width: 50%
:align: center
```

Complétez les tables de routages suivantes.

```{role} input(quiz-input)
:style: width: 3rem; text-align: center;
:check: split trim uppercase
```

**Routeur B:**

```{quiz}
| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | A | 1 |
| C | D | 2 |
| D | {input}`D` | {input}`1` |
| E | {input}`A` | {input}`2` |
| F | {input}`D` | {input}`3` |
| G | {input}`A,D` | {input}`3` |
| H | {input}`A,D` | {input}`4` |
```

**Routeur F:**

```{quiz}
| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | {input}`C,H` | {input}`4` |
| B | {input}`C` | {input}`3` |
| C | {input}`C` | {input}`1` |
| D | {input}`C` | {input}`2` |
| E | {input}`C,H` | {input}`3` |
| G | {input}`C,H` | {input}`2` |
| H | {input}`H` | {input}`1` |
```

**Routeur C:**

```{quiz}
| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | {input}`D,G` | {input}`3` |
| B | {input}`D` | {input}`2` |
| D | {input}`D` | {input}`1` |
| E | {input}`G` | {input}`2` |
| F | {input}`F` | {input}`1` |
| G | {input}`G` | {input}`1` |
| H | {input}`F,G` | {input}`2` |
```

### Exercice {num}`exo-reseaux`

Proposez un réseau de routeurs qui corresponde aux tables de routages données
ci-dessous.

**Routeur A:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| B | B | 1 |
| C | C | 1 |
| D | B | 2 |
| E | B | 2 |

**Routeur B:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | A | 1 |
| C | A | 2 |
| D | D | 1 |
| E | E | 1 |

**Routeur C:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | A | 1 |
| B | A | 2 |
| D | A | 3 |
| E | A | 3 |

**Routeur D:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | B | 2 |
| B | B | 1 |
| C | B | 3 |
| E | E | 1 |

**Routeur E:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | B | 2 |
| B | B | 1 |
| C | B | 3 |
| D | D | 1 |

````{solution}
```{figure} images/routage-sol.png
:alt: Solution de routage possible
:width: 50%
:align: center
```
````

### Exercice {num}`exo-reseaux`

Complétez le chemin (noms des routeurs) par lequel passe un message pour
atteindre sa destination depuis son point de départ en regardant seulement les
tables de routages.

```{role} input(quiz-input)
:style: width: 5rem; text-align: center;
```

```{quiz}
| Départ | Destination | Chemin |
| :----: | :---------: | :----: |
| D | A | {input}`DBCA` |
| C | E | {input}`CBE` |
| A | F | {input}`ACF` |
| F | A | {input}`FCA` |
| D | C | {input}`DBC` |
```

**Routeur A:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| B | C | 2 |
| C | C | 1 |
| D | C | 3 |
| E | C | 3 |
| F | C | 2 |

**Routeur B:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | C | 2 |
| C | C | 1 |
| D | D | 1 |
| E | E | 1 |
| F | C | 2 |

**Routeur C:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | A | 1 |
| B | B | 1 |
| D | B | 2 |
| E | B | 2 |
| F | F | 1 |

**Routeur D:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | B | 3 |
| B | B | 1 |
| C | B | 2 |
| E | B | 2 |
| F | B | 3 |

**Routeur E:**

| Destination | Routeur suivant | Distance |
| :---------: | :-------------: | :------: |
| A | B | 3 |
| B | B | 1 |
| C | B | 2 |
| D | B | 2 |
| E | B | 3 |


```{youtube} -2TDDyjClBI
```
