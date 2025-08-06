% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: dynamic
```

# Internet

Internet est un réseau informatique mondiale et publique. Il regroupe des
millions de réseaux interconnectés, qu'ils soient publics, privés,
universitaires, commerciaux ou gouvernementaux. Ces réseaux sont organisés en
entités autonomes.

Les informations circulent grâce à des câbles terrestres ou sous-marins, des
satellites, des ondes Wi-Fi et des réseaux-mobiles.

```{important}
**Internet** est le réseau physique (filaire ou par ondes) qui relie les
ordinateurs entre eux et qui permet aux ordinateurs de communiquer entre eux.

Le **World Wide Web** qui signifie la toile d'araignée mondiale (abrégé Web) est
un ensemble de pages, de documents et de ressources publiques, tous reliés les
uns aux autres par des liens hypertextes.
```

## Adressage

Pour que chaque machine puisse envoyer et recevoir des paquets, elle doit avoir
une adresse unique, appelée adresse IP.

Il en existe deux types:

1.  Les adresses IP publiques:
    Ce sont des adresses uniques attribuées aux appareils connectés directement
    à Internet
2.  Les adresses IP privées:
    Ce sont des adresses utilisées au sein d'un réseau local (LAN) pour
    permettre aux appareils de communiquer entre eux sans être directement
    accessibles depuis internet. Elles sont définies par des normes et ne sont
    pas routables sur le réseau public.

## IP (internet Protocol)

Les données circulant sur internet sont découpées en paquets de bits. On ajoute
à chaque paquet l'adresse de l'expéditeur et celle du destinataire. Les routeurs
répartis sur le réseau utilisent l'adresse du destinataire pour assurer
l'acheminement correct des paquets en suivant les règles du protocole IP.

Ce protocole permet d'identifier et de nommer de manière uniforme et unique tous
les appareils connectés à internet (ordinateurs, téléphones, objets connectés, etc.)
grâce à son adresse IP.

### IPv4

IPv4 est la première version du protocole. Les adresses sont représentées sous
la forme de quatre nombres entiers compris entre 0 et 255 (8 bits) séparés par
des points. Voici une adresse IPv4 publique d'un des routeurs du collège:

$$\texttt{156.25.4.249}$$

Il y a $2^{32}$ adresses possibles soit plus de 4 milliards. Depuis 2011,
ce n'est plus suffisant pour connecter tous les appareils à internet.

Une solution est d'utiliser des adresses IP privés (non accessibles directement
depuis internet) pour les machines qui se trouvent dans un sous-réseau. Exemple,
les adresses commençant par **10.x.x.x** ou par **192.168.x.x**.

Une autre solution est de changer le système d'adressage de IPv4 en IPv6.

### IPv6

Pour pallier le manque d'adresses disponibles avec IPv4, IPv6 a été développé
dès la fin des années 90. Il offre beaucoup plus d'adresses disponibles, mais a
aussi d'autres avantages techniques tels que la simplification de l'attribution
des adresses et un routage plus rapide des paquets.

Les adresses IPv6 sont représentées par huit groupes de quatre chiffres
hexadécimaux chacun, séparés par deux points.

$$\texttt{0:0:0:0:0:ffff:9c19:04fb}$$

IPv6 n'est pas compatible avec IPv4, ce qui a ralenti son déploiement.
Actuellement les deux systèmes sont encore utilisés.

```{youtube} kR9mCvMHWjk
```

## Adresses privées versus adresses publiques

Dans un réseau local, des adresses IP privées sont attribuées (en général sous
la forme de 10.x.x.x) à chaque équipement (ordinateurs, tablettes, téléphones,
imprimantes, etc.), ainsi qu'au routeur du réseau. Ce routeur, pour être aussi
atteignable depuis internet, a également une adresse publique.

Le routeur fonctionne comme le secrétariat d'une école en assurant la
transmission du courrier entre l'intérieur et l'extérieur de l'établissement. De
la même manière, le secrétariat dispose généralement de deux boîtes aux lettres:
l'une pour les documents déposés par les élèves et le personnel enseignant, et
l'autre réservée au facteur qui apporte le courrier provenant de l'extérieur du
collège.

```{figure} images/ip.svg
:alt: Réseau local
:width: 100 %
:align: center
Source: [https://apprendre.modulo-info.ch](https://apprendre.modulo-info.ch/resx/adressage.html)
```

### Exercice {num2}`exercice`

À l'aide d'un navigateur web, allez sur le site [https://test-ipv6.com/index.html.fr_FR](https://test-ipv6.com/index.html.fr_FR) et déterminez votre propre adresse IP.

Dans un terminal, tapez la commande suivante qui détermine votre adresse IP:

- sur Mac Os ou Linux: `ipconfig getifaddr en0`
- sur Windows: `ipconfig`

Obtenez-vous la même réponse? Pourquoi?

```{solution}
Sur le site, l'adresse IP publique du routeur de l'école est donnée, alors
qu'avec la commande ipconfig, c'est l'adresse privée du sous-réseau qui est
donnée.
```

### Exercice {num2}`exercice`

Recherchez sur le web:

1. Qu'est qu'un nom de domaine? Donnez un exemple.
2. Qu'est-ce qu'un DNS? À quoi ça sert?

```{solution}
1.  Un nom de domaine est une adresse internet d'un site web, facile à
    communiquer. Il est unique, mais peut contenir un sous-ensemble de pages.
    Le nom de domaine du collège est: [https://cscfr.ch](https://cscfr.ch).

    Il contient plusieurs pages:
    - [https://new.cscfr.ch/index.php/fr/](https://new.cscfr.ch/index.php/fr/)
    - [https://new.cscfr.ch/index.php/fr/notre-college/adresse-du-college](https://new.cscfr.ch/index.php/fr/notre-college/adresse-du-college)
    - [https://choeur.cscfr.ch/](https://cscfr.ch)

2.  Un DNS, en anglais Domain Name System, est un service qui associe les noms
    de domaine internet à leur adresse IP, difficile à retenir ou transmettre.

L'adresse IP du domaine [https://cscfr.ch](https://cscfr.ch) est 128.65.195.54
```

## Cables sous-marins

### Exercice {num2}`exercice`

Répondez aux questions en lien avec la vidéo suivante:
"[Du télégraphe à Internet: l'incroyable histoire des câbles sous-marins](https://www.nanoo.tv/link/v/2535386)"

1.  Quand et dans quel but les premiers câbles sous-marins opérationnels ont-ils
    été posés?
2.  Quelle est l'importance actuelle des câbles sous-marins pour le
    fonctionnement d'Internet?
3.  Qui sont les principaux acteurs impliqués dans le marché des câbles
    sous-marins en 2021?
4.  Quels sont les différents types de risques et de menaces auxquels les câbles
    sous-marins sont confrontés?
5.  Quelle est la durée de vie moyenne d'un câble sous-marin?

```{solution}
1.  Le premier câble télégraphique sous-marin opérationnel a été posé en 1851.
    Il reliait la ville de Calais, en France, à celle de Douvres, au
    Royaume-Uni. Le but était de permettre un échange rapide de messages entre
    les deux côtés de la Manche.
2.  Sans les câbles sous-marins, Internet ne pourrait tout simplement pas
    fonctionner, car 99% du trafic circule par ceux-ci.
3.  Les principaux acteurs sont les fabriquants (Nokia, Huawei Marine Networks),
    les sociétés de pose et de maintenance, les exploitants de câbles (les
    opérateurs télécoms) et les géants du Net (GAFAM).
4.  Les risques sont les suivants:
    - l'espionnage
    - le sabotage
    - des attaques par des requins (attirés par les ondes électriques)
    - les chalutiers (filets de pêche)
    - les événements naturels sous-marins (avalanche de boue)
5.  La durée de vie moyenne est de 25 à 30 ans. Que se passe-t-il après?
```
