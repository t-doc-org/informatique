% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Architecture de l'ordinateur et numérique et société

```{metadata}
subject: "Mathématiques 1re année"
print-styles: tdoc/print-exam.css
page-break-force: 1
page-break-avoid: 2
```

```{include} /_include/entete-examen.export.md
```
```{class} align-center
**Détails des calculs obligatoires. Attention au soin.**
```
---

## Question {nump}`question`{points}`4`

Cochez la bonne réponse.

```{list-grid}
:style: |
: grid-template-columns: 5fr 1fr 1fr;

- Si j'augmente la mémoire de mon disque dur, mon ordinateur sera plus rapide.
- &#9744; Vrai
- &#9744; Faux
- Un fichier peut contenir des répertoires ou des fichiers.
- &#9744; Vrai
- &#9744; Faux
- Une extension définit l'application qui peut ouvrir ce fichier.
- &#9744; Vrai
- &#9744; Faux
- Le système d'exploitation offre une interface homme-machine simplifiée.
- &#9744; Vrai
- &#9744; Faux
- C'est le processeur qui démarre le système d'exploitation.
- &#9744; Vrai
- &#9744; Faux
- L'utilisateur peut interagir directement avec le système d'exploitation.
- &#9744; Vrai
- &#9744; Faux
- Une imprimante est un périphérique d'entrée.
- &#9744; Vrai
- &#9744; Faux
- Android est un système de fichiers.
- &#9744; Vrai
- &#9744; Faux
```

```{solution}
Faux, Faux, Vrai, Vrai, Faux, Vrai, Faux, Faux
```

## Question {nump}`question`{points}`2`

Complétez ce schéma vu en cours et donnez un exemple pour chaque niveau.

```{figure} images/os.png
:width: 40%
:align: left
```

```{solution}
1.  Utilisateurs: un élève
2.  Application: word, chrome,
3.  Système d'exploitation: Android, iOS
4.  Matériel informatique: processeur, disque dur, ram
```

<style>
.os td {
    border: 1px solid black;
    border-collapse: collapse;
    padding: 10px;
    text-align: left;
    width: 50%;
}
</style>

## Question {nump}`question`{points}`2.5`

Pour chaque description, indiquez le rôle du système d'exploitation (ce que le
système d'exploitation gère):

```{flex-table}
:class: os
|   |  Le système d'exploitation gère qui peut accéder à quel répertoire ou fichier.
|   |  Le système d'exploitation détecte un nouveau matériel qui est branché à l'ordinateur.
|   |  Le système d'exploitation partage la RAM entre les différentes applications qui en ont besoin.
|   |  Le système d'exploitation gère le démarrage des applications.
|   |  Le système d'exploitation permet d'avoir une structure hiérarchique dans nos documents sauvegardés.
```
````{solution}
```{flex-table}
:class: os
| Les droits et accès |  Le système d'exploitation gère qui peut accéder à quel répertoire ou fichier.
| Les périphériques   |  Le système d'exploitation détecte un nouveau matériel qui est branché à l'ordinateur.
| Les ressources      |  Le système d'exploitation partage la RAM entre les différentes applications qui en ont besoin.
| L'exécution des programmes  |  Le système d'exploitation gère le démarrage des applications.
| Le système de fichiers      |  Le système d'exploitation permet d'avoir une structure hiérarchique dans nos documents sauvegardés.
```
````

## Question {nump}`question`{points}`3`

{.lower-alpha-paren}
1.   Complétez le schéma de von Neumann.
     ```{figure} images/vonneumann.png
     :width: 80%
     :align: center
     ```
2.   Citez deux différences entre la mémoire vive et la mémoire de masse.
3.   Quel est le rôle de l'unité de contrôle?


````{solution}
{.lower-alpha-paren}
1.   (1) Mémoire (2) Unité arithmétique et logique
2.   La mémoire vive s'efface lorsqu'on éteint l'ordinateur, alors que la
     mémoire de masse ne s'efface pas.<br>
     La mémoire vive est plus rapide que la mémoire de masse.
     La mémoire vive a moins de capacité (espace de stockage) que la mémoire de
     masse.
3.   L'unité de contrôle (ou UC) joue le rôle de chef d'orchestre de
     l'ordinateur en facilitant la communication entre l'UAL, la mémoire et les
     périphériques. Elle se charge de récupérer en mémoire la prochaine
     instruction à exécuter, ainsi que les données nécessaires, puis les envoie
     à l'unité arithmétique et logique.
````

## Question {nump}`question`{points}`6.5`

{.lower-alpha-paren}
1.   Complétez le schéma par les noms des composants correspondants.
     ```{figure} images/carte.png
     :width: 100%
     :align: center
     ```
2.   Qu'est-ce que la carte mère? À quoi sert-elle?
3.   À quoi servent les ports PCI?
4.   Quel(s) élément(s) sont placé(s) au-dessus de processeur? À quoi
     serve(nt)-il(s)?

```{solution}
{.lower-alpha-paren}
1.   (1) Mémoire RAM (2) Batterie/pile (3) Dissipateur/radiateur (4) ventilateur
     (5) Ports PCI (6) Carte mère
2.   La carte mère est un circuit imprimé permettant l'interconnexion de tous
     les composants d'un ordinateur. On y fixe tous les éléments nécessaires au
     fonctionnement d'un ordinateur.
3.   Les ports PCI permettent d'accueillir des cartes d'extension permettant
     d'ajouter des fonctionnalités à l'ordinateur: carte son, carte graphique,
     carte réseau, ….
4.   Un ventilateur est placé au dessus d'un dissipateur pour refroidir le
     processeur.
```

## Question {nump}`question`{points}`4`

{.lower-alpha-paren}
1.  Citez 4 types de logiciels malveillants (malware)?
2.  Choisissez un logiciel malveillant:
          - Expliquez comment se propage ce logiciel malveillant.
          - Comment peut-on se protéger de ce logiciel malveillant?

```{solution}
{.lower-alpha-paren}
1.  Virus / Ver / Cheval de Troie / Logiciel espion / Rançongiciel / Logiciel
    publicitaire
2.  Sans corrigé
```

## Question {nump}`question`{points}`3`

{.lower-alpha-paren}
1.  Qu'est-ce que la force d'un mot de passe?
2.  De quoi dépend-elle?
3.  Combien existe-t-il de mots de passe différents avec 93 symboles
    (majuscules, minuscules, chiffres et caractères spéciaux), si le mot de
    passe contient 12 caractères? Notez seulement le calcul.

```{solution}
{.lower-alpha-paren}
1.  C'est la capacité à résister à une attaque par force brute.
2.  Elle dépend de la longueur du mot de passe et du nombre de caractères
    possibles (minuscules, majuscules, chiffres, etc.).
3.  Nombre de mots de passe possibles: $93^{12}$
```

## Question {nump}`question`{points}`2`

Citez 3 conseils à suivre concernant les mots de passe.

```{solution}
- Utilisez des mots de passe long (minimum 12 caractères) et facile à retenir.
- Utilisez des mots de passe différents pour chaque compte.
- Utilisez un second facteur d'authentification.
- Ne jamais transmettre son mot de passe.
```

## Question {nump}`question`{points}`3`

Qu'est-ce que l'ingénierie sociale? Donnez un exemple.

```{solution}
L'ingénierie sociale regroupe les techniques qui consistent pour un fraudeur à
instaurer une relation de confiance avec une cible dans le but de la manipuler,
pour lui soutirer des informations confidentielles ou lui faire exécuter des
actions à des fins malveillantes.
```

## Question {nump}`question`{points}`3`

Le mail suivant est un mail d'hameçonnage (phishing). Donnez deux raisons qui
permettent d'affirmer cela.

```{figure} images/phishing.png
:width: 80%
:align: center
```

```{solution}
- Le nom de l'entreprise (buoygues telecom) et celle utilisée dans le lien n'est
  pas la même (bouyquestlecom).
- Ils mettent sous pression pour un payement rapidement.
- La formule d'appel est impersonnelle: "Chère Cliente, Cher Client".
```

