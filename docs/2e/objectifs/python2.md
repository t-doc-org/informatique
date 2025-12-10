% Copyright 2025 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

```{metadata}
subject: "Informatique 2e année"
```

# Programmation en Python 2

Les objectifs de l'évaluation [](#eval-python1-2e) sont considérés comme acquis.

## Listes

-   Savoir créer une liste vide ou une liste contenant des éléments.
-   Savoir accéder à un élément au moyen de l'indexation.
-   Savoir utiliser les différents fonctions sur les listes (cf. liste
    ci-dessous).
-   Savoir déterminer si un élément appartient à une liste (if element in
    liste:).
-   Savoir utiliser une boucle `for` sur une liste (for element in liste:)
-   Savoir utiliser la fonction `randint(a, b)` et l'importer correctement.
-   Savoir lire et comprendre un programme.
-   Savoir compléter un programme.
-   Savoir écrire un programme à partir d'un énoncé.

## Fonctions sur les listes

Cette liste de fonctions sera à disposition pendant l'évaluation.

len(ma_liste)
: retourne le nombre d'éléments de `ma_liste`

ma_liste.append(mon_element)
: ajoute `mon_element` à la fin de `ma_liste`

ma_liste.insert(index, mon_element)
: ajoute `mon_element` à l'`index` spécifié de `ma_liste`

ma_liste.remove(mon_element)
: efface la première occurrence de `mon_element` dans `ma_liste`

del ma_liste[index]
: supprime l'élément de `ma_liste` qui se trouve à l'`index` spécifié

ma_liste.index(mon_element)
: retourne l'index de la première occurrence de `mon_element` dans `ma_liste`

sum(ma_liste)
: retourne la somme de tous les éléments de `ma_liste`

ma_liste.sort()
: trie `ma_liste` par ordre croissant

ma_liste.reverse()
: inverse l'ordre des éléments de `ma_liste`

ma_liste.count(mon_element)
: retourne le nombre d'apparition de `mon_element` dans `ma_liste`
