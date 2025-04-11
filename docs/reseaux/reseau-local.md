% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
solutions: hide
scripts:
  - src: quizz-helpers.js
```

# Réseau local

Un réseau local, en anglais Local Area Network (LAN), est un réseau informatique
au sein d'une zone géographique restreinte, généralement à l'intérieur d'un
même bâtiment (une école, un appartement, une entrepise, etc).

Il permet notamment:

- la communication entre tous les équipements du réseau.
- l'échange d'information
- l'accès à internet
- l'utilisation d'une imprimante distante connectée au réseau
- la protection du réseaux (de LAN vers internet et vice-versa)

## Matériel

Voici un schéma qui représente l'infrastructure d'un réseau local.

```{figure} images/reseau-local.jpg
:alt: Réseau local
:width: 80 %
:align: center
Source: [https://technopartage.jimdofree.com](https://technopartage.jimdofree.com/r%C3%A9seaux-informatiques/)
```

### Exercice {num}`exo-reseaux`

Sur le schéma, ci-dessus sont nommés différents équipements. Complétez-le
[tableau](reseau-local.docx) en expliquant le rôle dans le réseau local de chaque
élément.


```{solution}

| Nom                 | Rôle |
| :------------------ | :--- |
| Client (PC, laptop) | Un client est un utilisateur du réseau. Il accède, partage et utilise les ressources disponibles. |
| Serveur             | Le serveur fournit des services et des ressources aux clients. Il gère les utilisateurs et les accès et sécurise les données.|
| Modem               | Un modem (acronyme de modulateur-démodulateur) relie un réseau local à internet. Il convertit les données numériques en signal modulé analogique (et vice-versa) qui pourra être transmis sur les lignes téléphoniques (DSL), les réseaux câblés (câble TV ou fibre optique), le réseau mobile, etc. |
| Routeur             |  Un routeur est un appareil électronique qui sert d'intermédiaire entre deux réseaux: le réseau local et internet. Il gère la transmission de l'information (paquets) jusqu'au destinataire selon des règles définies. |
| Passerelle          | Chaque réseau a sa manière de fonctionner (ses protocoles). Une passerelle permet à deux réseaux qui fonctionnent différemment de se comprendre. Elle permet aussi de contôler le trafic et de protéger des intrusions (pare-feu et antivirus). |
| Switch              | Un switch permet d'interconnecter plusieurs appareils sur un même réseau. Il gère le transfert de l'information jusqu'au destinataire en évitant les collisions.     |
| Borne Wi-Fi         | Une borne Wi-Fi, aussi appelée point d'accès, est un appareil qui permet de se connecter à un réseau sans fil. C'est un pont entre le réseau filaire et le réseau sans fil. La borne diffuse le signal du réseau filaire sur les ondes radio. |
| Imprimante réseau   |  Une imprimante réseau est une imprimante connectée au réseau local via un câble ou le Wi-Fi. Elle permet à plusieurs utilisateurs d'un même réseau d'imprimer des documents sans avoir de connexion directe (câble USB). |

Le modem, le routeur, la passerelle, le switch et la borne Wi-Fi sont souvent
intégrés à la box internet fournie par le fournisseur d'accès internet.

```

### Exercice {num}`exo-reseaux`

1.  Qu'est-ce qu'un fournisseur d'accès internet (FAI)s?
2.  Citez quelques exemples de fournisseur d'accès internet en Suisse.

```{solution}
1.  Un fournisseur d'accès internet est une entreprise qui offre une connexion
    au réseau internet. Il possède (ou loue) l'infrastructure, comme les câbles
    et les serveurs, nécessaires à la connection.

    Il s'occupe aussi d'acheminer correctement les données, fournit des services
    de sécurité et peut aussi fournir des adresses électroniques.

    Il peut voir toutes les données qui transitent, ainsi que les sites visités.

2. Swisscom, Salt, Sunrise UPC, Wingo (Réseau Swisscom), M-Budget internet (réseau Swisscom)
```


```{youtube} HPhUNJ2L8mk
```

## Envoi de message à l'intérieur d'un sous-réseau

Dans un sous-réseau, chaque machine est reliée à un switch qui gère
l'acheminement des paquets de l'expéditeur au destinaire:

1.  L'expéditeur découpe ses données en paquet de bits auquels il ajoute son
    adresse et l'adresse du destinataire.
2.  Si le destinataire est dans le sous-réseau, l'expéditeur envoie le paquet
    directement au destinataire via le switch.
3.  Si le destinataire n'est pas dans le sous-réseau, l'expéditeur envoie le
    paquet au routeur via le switch.
4.  Le destinaire rassemble les différents paquets pour former l'ensemble des
    données.


```{youtube} g_C2QPCyLNY
```




