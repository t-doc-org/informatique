% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Cybersécurité

```{metadata}
solutions: remove
```

## Définitions

Cybersécurité
: Ensemble des moyens utilisés pour assurer la protection des réseaux, des
appareils et des données informatiques contre les attaques malveillantes.

Hacker
: Personne qui, par jeu, goût du défi ou souci de notoriété, cherche à
contourner les protections d'un logiciel, à s'introduire frauduleusement dans un
système ou un réseau informatique. (Larousse)

### Exercice {num}`exo-num`

1.  Quels types d'informations ou de données pourriez-vous vous faire voler?
2.  En quoi la cybersécurité est-elle devenue un enjeu majeur dans notre
    société actuelle?

```{solution}
1.  Il est possible de se faire voler:
    -   des données personnelles (nom, prénom, date de naissance, numéro de
        téléphone) -> usurpation d'identité.
    -   des données de connexion (mots de passe, adresse mail)
        -> accès aux comptes en ligne
    -   des informations financières (numéros de carte de crédit, identifiant,)
        -> vol d'argent
    -   des données personnelles (photos, vidéos, échange de messages, ...)
    -   des données médicales
    -   ...
2.  Nous vivons dans une société de plus en plus connectée, où l'utilisation
    d'appareils reliés à Internet — tels que les ordinateurs, smartphones,
    téléviseurs, montres connectées, réseaux Wi-Fi, ou encore certains
    équipements domestiques comme les fours — est devenue courante. Or, beaucoup
    de ces objets présentent des failles de sécurité importantes, certains étant
    même totalement vulnérables.\
    Parallèlement, le nombre de hackers augmente, car pirater est devenu un
    moyen relativement simple et lucratif de gagner de l'argent, souvent sans
    nécessiter de compétences techniques poussées.
```

## Malware - logiciel malveillant

Un malware (contraction de **Mal**icious et soft**ware**) est un programme conçu
pour porter atteinte à un système informatique sans l'accord de l'utilisateur,
par exemple, en bloquant son fonctionnement, en le modifiant ou en volant des
données.

Exemples:

1. Virus
2. Ver (worm)
3. Cheval de Troie (trojan horse)
4. Logiciel espion (spyware)
5. Rançongiciel (ransomware)
6. Logiciel publicitaire (adware)

### Exercice {num}`exo-num`

Pour l'exemple qui vous a été attribué:
- Donnez une définition du malware.
- Comment se propage-t-il?
- Quel type de dégâts peut-il provoquer?
- Comment se protéger de ce genre d'attaques?

```{solution}
1.  Virus\
    Définition: Un virus est un programme malveillant capable de s'insérer dans
    d'autres programmes ou fichiers afin de se multiplier et de perturber le
    fonctionnement normal d'un système.\
    Propagation: Il se propage lentement lorsqu'un fichier infecté est ouvert ou
    exécuté sur un autre appareil (par exemple via une clé USB, un
    téléchargement ou un email infecté).\
    Type de dégâts: Corruption ou suppression de fichiers, ralentissement ou
    blocage complet du système.\
    Protection: ne pas ouvrir de fichiers suspects, sauvegardes régulières et
    antivirus à jour.

2.  Ver\
    Définition: Un ver est un programme malveillant capable de se répliquer et
    de se propager automatiquement à d'autres appareils sans action humaine.\
    Propagation: Il est introduit par quelqu'un sur un réseau et ensuite il se
    propage rapidement tout seul sur celui-ci.\
    Type de dégâts: ralentissement ou blocage complet du système.\
    Protection: mise à jour des logiciels, utilisation de pare-feu et
    non-utilisation des réseaux wifi ouverts.

3.  Cheval de Troie\
    Définition: Un cheval de Troie est un logiciel malveillant qui se présente
    comme un programme légitime pour tromper l'utilisateur et exécuter des
    actions malveillantes en arrière-plan (virus, logiciel espion, etc.).\
    Propagation: Il est souvent téléchargé volontairement par l'utilisateur,
    pensant installer un programme utile ou inoffensif.\
    Type de dégâts: Vol d'informations sensibles (identifiants bancaires, mots
    de passe) et prise de contrôle à distance de l'ordinateur.\
    Protection: Télécharger uniquement depuis des sources fiables et prudence
    face aux programmes inconnus.

4.  Logiciel espion\
    Définition: Un logiciel espion est un programme qui collecte secrètement des
    informations sur l'utilisateur, comme les frappes clavier, les sites visités
    ou les mots de passe.\
    Propagation: Il provient en général de logiciels gratuits ou à travers des
    publicités piégées.\
    Type de dégâts: Vol d'informations privées (mots de passe, coordonnées
    bancaires), surveillance de l'activité en ligne et détournement des
    navigateurs vers des sites frauduleux.\
    Protection: Attention lors de l'installation de logiciels gratuits et mise à
    jour régulière du navigateur et des extensions.

5.  Rançongiciel\
    Définition: Un rançongiciel est un malware qui chiffre les fichiers d'une
    victime et exige une rançon pour en rendre l'accès.\
    Propagation: Il se propage principalement via des e-mails de phishing, des
    pièces jointes infectées ou des sites web compromis.\
    Type de dégâts: blocage complet de l'accès aux fichiers ou au système, perte
    définitive des données si la rançon n'est pas payée (et même parfois si elle
    est payée). Cela a un impact économique massif pour les entreprises et
    institutions publiques.\
    Protection: Sauvegardes fréquentes et externes, formation contre le phishing
    et sécurité réseau renforcée.

6.  Logiciel publicitaire\
    Définition: Un logiciel publicitaire est un programme qui affiche
    automatiquement des publicités non désirées, parfois de manière intrusive,
    pour générer des revenus pour ses créateurs.\
    Propagation: Il provient en général de logiciels gratuits.\
    Type de dégâts: Ralentissement important des appareils, affichage de
    publicités intrusives ou redirection vers des sites dangereux.\
    Protection: Télécharger les logiciels depuis des sites officiels, utiliser
    des bloqueurs de publicité et vigilance lors de l'installation de logiciels
    gratuits.
```

## Comment se protéger?

### Facteur humain

Un malware a besoin, en général, d'une action de l'utilisateur pour s'exécuter:

- Ne pas ouvrir n'importe quel fichier (en pièce jointe).
- Ne pas cliquer sur n'importe quel lien.
- Ne pas télécharger et installer n'importe quelle application, notamment celles
qui sont gratuites.

### Protéger ses données

Pour protéger ses données, il faut:
- Utiliser de bons mots de passe.
- Garder ses mots de passe pour soi (ne pas les transmettre).

### Protéger son ordinateur

Pour protéger son ordinateur, il faut faire les mises à jour régulièrement. Un
système de mises à jour automatique peut être mis en place.

## Témoignages

Dans la vidéo ["Hackers comment ils violent notre intimité"](https://www.nanoo.tv/link/v/sgfYfiQG),
vous allez voir deux témoignages, le premier de victimes et le deuxième d'un
hacker.

Téléchargez le [questionnaire](questionnaire-hackers.docx) et répondez aux questions.
