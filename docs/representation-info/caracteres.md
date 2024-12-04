% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Caractères


Pour pouvoir écrire, afficher ou stocker un texte sur un ordinateur, il faut
définir une représentation des caractères compréhensibles pour celui-ci. L'idée
la plus simple est de faire correspondre à chaque caractère un numéro unique.

Il existe plusieurs codes utilisés, ASCII, Unicode et UTF qui sont les plus
courants.

## Code ASCII

Dans les années 50, ils existaient beaucoup d'encodages différents pour les
caractères, ce qui posait des problèmes de compatibilité et rendait les échanges
compliqués. Au début des années 60, l'ANSI (American National Standards
Institute) propose la norme de codage pour les caractères appelée ASCII
(American Standard Code for Information Interchange). Cette norme définit 128
caractères sur 7 bits.

```{figure} images/ascii.png
:alt: Tableau code ASCII
:width: 100%
:align: center
```

Le tableau ci-dessus semble désordonné, mais si on écrit le code hexadécimal, il
y a une certaine logique:
- Les codes 0 à 31 ne sont pas des caractère, on les appelle les caractères de
contrôle (ex: retour à la ligne, bip sonore);
- Le code 32 est l'espace;
- Les codes 48 à 57 sont les chiffres;
- Les codes 65 à 90 représentent les majuscules;
- Les codes 97 à 122 représentent les minuscules.

Dans ce tableau, il n'y a aucun caractère accentué, car cette norme a été
développée pour l'anglais. Ce code a été ensuite étendu à 8 bits pour pouvoir
coder plus de caractères. Le problème est que le code ASCII étendu n'est pas
identique dans tous les pays.

## Exercice {num}`exo-info`

Convertir les chaînes de caractères en utilisant le code ASCII hexadécimal.
1. INFO

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "494E464F": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

2. hello

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "68656C6C6F": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

3. Bonjour

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "426F6E6A6F7572": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

4. ;-)

    ```{exec} python
    :when: load
    :class: hidden
    while True:
      resp = await input_line("Réponse:")
      if resp.replace(" ", "") == "3B2D29": break
      print("\x0cEssaie encore")
    print("\x0cBravo")
    ```

## Exercice {num}`exo-info`

Convertir le texte suivant écrit en code ASCII hexadécimal.

4A 27 61 69 6D 65 20 6C 27 69 6E 66 6F 72 6D 61 74 69 71 75 65 21

```{exec} python
:when: load
:class: hidden
while True:
  resp = await input_line("Réponse:")
  if resp == "J'aime l'informatique!": break
  print("\x0cEssaie encore")
print("\x0cBravo")
```

## Exercice {num}`exo-info`

Comment peut-on transformer un lettre majuscule en lettre minuscule et
vice-versa en utilisant le code ASCII?

```{solution}
Le code de A majuscule en décimale est 65, pour a minuscule c'est 97. Il faut
donc ajouter 32 (97-65) pour passer d'une lettre majuscule à l'équivalent en
minuscule.
```


## Unicode

Une solution au problème des caractères accentués est l'Unicode, car il permet
de représenter tous les caractères spécifiques à chaque langue. Mais pour cela,
nous avons besoin de 2 octets pour coder un caractère, ce qui est le double par
rapport au ASCII. Il faut donc le double de place pour stocker un texte, alors
qu'en français, par exemple, nous n'avons besoin que de quelques caractères en
plus par rapport au ASCII. Ce n'est donc pas optimal.

## UTF-8

L'UTF-8[^sn1] est une combinaison du code ASCII et de l'Unicode. Il est donc
universel et efficace.
[^sn1]: Universal Character Set Transformation Format

Nous utilisons le code ASCII pour coder le texte, mais lorsqu'un caractère
spéciale doit être codé, nous utilisons pour ce caractère le Unicode.

Encodage du mot **Début** avec les différents encodages:
- ASCII\
 Le mot Début contient 5 caractères qui sont codés sur 7 bits. Nous auront donc
 besoin de $5 \cdot 7 = 35$ bits. Comme le code ASCII n'a pas d'accent,
 résultat sera **Debut**.
- Unicode\
 Le mot Début contient 5 caractères qui sont codés sur 2 octets (16 bits). Nous
 auront donc besoin de $5 \cdot 16 = 80$ bits. Le résultat sera **Début**.
- UTF-8\
 Le mot Début contient 5 caractères. Les caractères sans accents sont codés sur
 8 bits (7 bits du code ASCII et un bit pour indiquer si c'est l'ASCII qui est
 utilisé ou le Unicode) et ceux avec accents sur 16 bits. nous auront donc
 besoin de $4 \cdot 8 + 1 \cdot 16 = 48$ bits. Le résultat sera **Début**.

Encodage mot **Début** avec l'UTF-8 en binaire:\
L'Unicode du caractère é est U+00E9 qui en binaire donne **1110 1001**

| D    | é    | b    | u    | t    |
|:----:|:----:|:----:|:----:|:----:|
|<span style="color:red">0</span>1000100| <span style="color:red">11</span>0000**11** <span style="color:red">1</span>0**101001**| <span style="color:red">0</span>1100010| <span style="color:red">0</span>1110101| <span style="color:red">0</span>1110100|


## Exercice {num}`exo-info`

Pourquoi n'utilise-t-on pas toujours l'unicode étant donné que nous pouvons
coder tous les caractères pour chaque langue?

```{solution}
Nous n'utilisons pas toujours le unicdoe, parce qu'il prend beaucoup de place de
stockage : 2 octets par caractère. C'est le double par rapport au code ASCII.
```

## Exercice {num}`exo-info`

Quels sont les avantages et les inconvénients des différents encodages?

```{solution}
| encodage | avantages | inconvénients |
|:--------:|:---------:|:-------------:|
| ASCII | Prend peu de place (7 bits par lettre) | Ne permet pas d'encoder les caractères avec accents |
| ASCII étendu | Prend peu de place (8 bits par lettre) et permet d'encoder certains accents | Pas standardisé donc différent suivant les pays |
| Unicode | Permet d'encoder tous les caractères possibles (accents, caractères chinois, ...) | Prend beaucoup de place: 2 octets (16 bits) |
| UTF-8 | Universel et efficace: utilise 2 octets seulement quand c'est nécessaire |  |
```
