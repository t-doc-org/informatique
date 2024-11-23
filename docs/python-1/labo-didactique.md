% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Labo didactique

```{metadata}
orphan:
```

Site d'entrainement d'écrire de programme en Python.

```{code-block}
Dans cette fenêtre apparaîtront les réponses de l'AI:
1) Les questions, générées par l'IA, posées aux élèves
2) Le feed-back de l'IA par rapport au code écrit par les élèves s'il y a des
erreurs

Lorsque l'élève répond correctement à 2 questions d'un niveau, il passe au
niveau suivant.
Les types de questions par niveau sont définis au préalable et stockés dans une
listes pour pouvoir les envoyer au fur à mesure à l'AI.
Le suvi de la conversation sera effacé lors du passage au niveau supérieur.
```

`Button envoyer`

```{exec} python
:style: height: 25rem
:when: never
:linenos:
# éditeur dans lequel les élèves écriront le programme demandé.
```

`Button aide`

```{code-block}
Dans cette fenêtre apparaîtra l'aide de l'IA, c'est-à-dire la réponse du code ou
éventuellement comment faire. Lorque les élèves appuyent sur le bouton d'aide,
la réponse ne sera pas comptabilisée comme correcte.
```
