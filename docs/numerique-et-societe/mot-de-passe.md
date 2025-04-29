% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Mot de passe
```{metadata}
solutions: remove
scripts:
  - src: quizz-helpers.js
```

## Introduction

De nombreux services, y compris des services sensibles comme la banque en ligne,
sont désormais accessibles via Internet. Pour s'y connecter, l'utilisateur doit
généralement fournir un identifiant — souvent attribué par le service et public
— ainsi qu'un authentifiant, comme un mot de passe, qu'il choisit lui-même et
qui reste confidentiel.

Identification:
: Donner son identité (par exemple montrer son passeport)\
  Nom d'utilisateur

Authentification:
: Prouver son identité (prouver que le passeport est authentique)\
  Mot de passe, sms, empreinte digitale, …



## Force d'un mot de passe

Attaque par force brute
: Méthode qui consiste à tester, l'une après l'autre, chaque combinaison
  possible d'un mot de passe.

Force d'un mot de passe
: Capacité à résister à une attaque par force brute.

### Exercice {num}`exo-num`

De quoi dépend la force d'un mot de passe?

```{solution}
La force d'un mot de passe dépend de la longueur du mot de passe et du nombre de
caractères possibles (minuscules, majuscules, chiffres, etc.).
```

### Exercice {num}`exo-num`

Les 3 symboles suivants sont à disposition pour faire un mot de passe:
&#9733; &#9728; et &#9729;

Combien y a-t-il de mots de passe possibles,

1. <script>tdoc.question("si la longueur du mot de passe est de 1?", {'3': true});</script>
2. <script>tdoc.question("si la longueur du mot de passe est de 2?", {'9': true});</script>
3. <script>tdoc.question("si la longueur du mot de passe est de 3?", {'27': true});</script>
4. <script>tdoc.question("si la longueur du mot de passe est de 4?", {'81': true});</script>


### Nombre de mots de passe possibles

| Symboles à disposition | Nombre de symboles | Longueur du mot de passe | Nombre de possibilités |
| :--------------------: | :----------------: | :----------------------: | :--------------------: |
| lettres minuscules     | 26                 | 8                        | $26^8 \cong 2 \cdot 10^{11}$ |
| lettres minuscules <br> et majuscules | 52  | 8                        | $52^8 \cong 5 \cdot 10^{13}$ |
| lettres et chiffres | 62                    | 8                        | $62^8 \cong 2 \cdot 10^{14}$ |
| lettres, chiffres et <br> caractères spéciaux | 93  | 8                | $93^8 \cong 6 \cdot 10^{15}$ |

Pour renforcer la sécurité d'un mot de passe, il est nécessaire d'en augmenter
sa longueur et la variété des caractères utilisés.

## Choix d'un mot de passe

### Mauvaises pratiques

Beaucoup trop d'utilisateurs ne mettent pas d'importance au choix d'un mot de passe:

1. Laisser le mot de passe d'origine
2. Utiliser des mots de passe communs tels que 123456, admin, password, azerty, loulou.
3. Utiliser les mêmes mots de passe pour plusieurs services.

### Bonnes pratiques

L'idéal est d'utiliser un mot de passe long, facile à retenir:

1.  Utiliser une phrase:\
    "J'aime passer mes vacances à la mer en automne"
    "J'AimePasserMesVacancesALaMerEnAutomne"

2.  Utiliser une suite de mots aléatoires:\
    Aimer Champignon Vacances Dehors Pantalon

3.  Utiliser les initiales d'une phrase:\
    **J**'aime **l**es **f**raises **et** **l**a **g**lace **à** **l**a **v**anille **r**ecouvertes **d**e **c**rème **c**hantilly =>  Jalf&lgàlvrdcc

## Récupération du mot de passe

En général, il est possible de réinitialiser un mot de passe avec
1.  des questions secrètes:
    -   Ne pas utiliser des questions secrètes trop simples à deviner ou qu'on
        peut trouver sur le web (date d'anniversaire, lieu de naissance, etc.)
    -   Éviter de publier des informations personnelles sur le web

2.  un mail de récupération:\
    Avoir un mot de passe fort pour sa messagerie, car si quelqu'un a accès à
    votre messagerie, il peut réinitialiser tous vos mots de passe…


## Second facteur d'authentification

La double authentification, aussi appelée authentification à deux facteurs (2FA),
est une méthode de sécurité renforcée qui permet à un utilisateur d'accéder à
une ressource informatique (ordinateur, smartphone, site web, etc.) en
fournissant deux preuves d'identité différentes. Ces deux étapes permettent de
vérifier que la personne est bien autorisée à accéder au service.

Si un pirate réussit à voler ou deviner votre mot de passe, cela ne suffit pas
pour accéder à votre compte, car il lui manque le deuxième facteur
d'identification, qui peut être par exemple :

- un code par SMS
- un code via une application d'authentification
- un clé de sécurité USB
- un code par appel à un numéro
- une notification sur un appareil de confiance qui demande la validation de la connexion

Ainsi, le mot de passe seul ne donne plus automatiquement accès au compte, ce
qui réduit fortement les risques de piratage.

## Quelques conseils

-   Utiliser un mot de passe long et compliqué (minimum 12 caractères de toutes
    sortes), mais facile à retenir comme une phrase.
-   Utiliser des mots de passe différents pour chaque compte surtout pour les
    services sensibles.
-   Utiliser la double authentification lorsque c'est possible.
-   Ne jamais transmettre son mot de passe.


### Exercice {num}`exo-num`

Hubert possède un compte sur le site marchand boulatique.com. La base de données
du site a été piratée. Les données concernant Hubert qui ont fuité sont:
- son identité, à savoir Hubert Dupont,
- son adresse mail,
- son mot de passe.

1.  Quelles pourraient être les conséquences?
2.  Que se passerait-il si Hubert utilise le même mot de passe pour son compte
    Microsoft 365 que celui utilisé pour le site boulatique.com?


```{solution}
1.  On utilise souvent le même identifiant, comme une adresse e-mail, pour se
    connecter à différents services. Si le même mot de passe est réutilisé
    partout, un attaquant qui réussit à l'obtenir pourra facilement accéder à
    tous les autres comptes.\
    Si Hubert utilise le même mot de passe pour sa messagerie, le pirate aura
    aussi accès à sa messagerie, il pourra donc réinitialiser les mots de passe
    d'autres services liés à cette adresse.
2.  Comme les adresses professionnelles sont faciles à déterminer, l'attaquant
    pourrait accéder à ses documents, ses e-mails professionnels, et
    potentiellement à toutes les données de son entreprise.
```

## Cassage de mot de passe

### Attaque par force brute

Le pirate essaie toutes les combinaisons possibles jusqu'à trouver le mot de
passe:

-   Cela prend beaucoup de temps.
-   Les services limitent le nombre de tentatives et ensuite se bloquent pendant
    un certain temps.

### Attaque par dictionnaire

Le pirate utilise une liste de mots de passe fréquemment utilisés, comme des
mots simples, des prénoms ou des mots déjà compromis lors de fuites de données.
Cette technique est souvent combinée à une attaque par force brute pour tester
automatiquement des variantes de ces mots, par exemple: bonjour, Bonjour,
Bonjour1, etc.

### Utilisation de bases de données compromises

Les pirates utilisent des mots de passe récupérés lors de fuites de données.
Dans les systèmes, les mots de passe ne sont généralement pas stocké en clair,
mais sous forme de hash, c'est-à-dire une empreinte numérique qui en représente
la version chiffrée.

Pour retrouver un mot de passe à partir de son empreinte (hash), un pirate peut
utiliser un logiciel spécialisé appelé casseur de mots de passe. Ce logiciel
exploite des tables de correspondance (dictionnaires) empreinte-mot de passe
disponibles sur le web, notamment sur le darknet. Si cela ne suffit pas, le
pirate devra:

1.  Identifier la fonction de hachage utilisée.
2.  Créer son propre dictionnaire mot de passe-empreinte pour la fonction de
    hachage trouvée en:
    -   Testant, d'abord, les mots de passe courants.
    -   Testant tous les mots de passe possibles (ce qui demande du temps et des
        ressources, mais n'est pas limité comme lors de tentatives de connexion
        à un service).

## Conclusion

Nous ne pouvons pas empêcher le vol de données, mais avec des mots de passe
robustes et différents pour chaque service, il est possible de limiter les
dégâts.





