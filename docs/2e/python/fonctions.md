% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Fonctions

## Fonctions simples

En programmation, une **fonction** est un bloc de code (suite d'instructions)
permettant de réaliser une tâche donnée et auquel nous donnons un nom. Cela
permet de découper un programme en plusieurs petites tâches plus faciles à
résoudre. Ainsi le code est plus lisible et plus facile à comprendre. Pour cela,
il est essentiel de choisir un nom de fonction qui explique ce qu'elle fait.

```{tip}
Une fonction doit toujours être définie avant d'être appelée, c'est pourquoi il
est préférable de placer toutes les définitions de fonctions au début du
programme (après les imports et les définitions de variables globales).
```

### Exemple {num2}`exemple`

Fonction qui affiche un conseil météo:

```{exec} python
:editor:
# définition des fonctions
def conseil_meteo():
  print("Mets tes lunettes de soleil et profite!")

# programme principal
print("=== Conseil météo ===")
# appel de la fonction
conseil_meteo()
```

Cette fonction affiche toujours le même conseil météo ce qui n'est pas très
intéressant, le conseil devrait s'adapter au temps qu'il fait.

## Fonctions avec paramètres

Un **paramètre d'une fonction** est une variable définie dans la fonction qui
recevra une valeur lors de chaque appel de la fonction. Ainsi le comportement
d'une fonction varie suivant les valeurs de ses paramètres.

### Exemple {num2}`exemple`

Fonction qui affiche un conseil météo en fonction de celle-ci

```{exec} python
:editor:
# définition des fonctions
def conseil_meteo(meteo):
  if meteo == "soleil":
    print("Mets tes lunettes de soleil et profite!")
  elif meteo == "pluie":
    print("Prends ton parapluie ou tu seras trempé(e)!")
  elif meteo == "neige":
    print("Enfile tes gants et va faire un bonhomme de neige!")
  else:
    print("Hmm... je ne sais pas quoi te conseiller pour cette météo!")


# programme principal
print("=== Conseil météo ===")

# demande la météo du jour à l'utilisateur
meteo_du_jour = input("Quel temps fait-il aujourd'hui? (soleil/pluie/neige/autre): ")

# appel de la fonction en fonction de la réponse de l'utilisateur
conseil_meteo(meteo_du_jour)
```

### Exercice {num2}`exercice`

Créez une fonction `compteur()`...
1.  qui compte de 0 à un nombre donné appelé `stop`:

    ```{exec} python
    :editor: b5114e99-47c4-40d8-93e4-7bac649c10f2
    def compteur(stop):
      # à compléter

    compteur(11)
    ```

    ````{solution}
    Version avec une boucle while
      ```{exec} python
      :linenos:
      def compteur(stop):
        i = 0
        while i <= stop:
          print(i)
          i += 1

      compteur(11)
      ```

     Version avec une boucle for
      ```{exec} python
      :linenos:
      def compteur(stop):
        for i in range(stop + 1):
          print(i)

      compteur(11)
      ```
    ````

2.  qui compte de `start` à `stop` avec `start` < `stop`:

    ```{exec} python
    :editor: 4b3ebd3f-e3a6-4041-a51a-3362a1b299c3
    def compteur(start, stop):
      # à compléter

    compteur(4, 11)
    ```

    ````{solution}
    Version avec une boucle while
      ```{exec} python
      :linenos:
      def compteur(start, stop):
        i = start
        while i <= stop:
          print(i)
          i += 1

      compteur(4, 11)
      ```

     Version avec une boucle for
      ```{exec} python
      :linenos:
      def compteur(start, stop):
        for i in range(start, stop + 1):
          print(i)

      compteur(4, 11)
      ```
    ````

3.  qui compte de `start` à `stop` avec un pas donné `step` (de 2 en 2 ou
    de 3 en 3):

    ```{exec} python
    :editor: fd8b8f40-1de2-41ca-8868-6a29af56c20d
    def compteur(start, stop, step):
      # à compléter

    compteur(4, 11, 3)
    ```

    ````{solution}
    Version avec une boucle while
      ```{exec} python
      :linenos:
      def compteur(start, stop, step):
        i = start
        while i <= stop:
          print(i)
          i += step

      compteur(4, 11, 3)
      ```

     Version avec une boucle for
      ```{exec} python
      :linenos:
      def compteur(start, stop, step):
        for i in range(start, stop + 1, step):
          print(i)

      compteur(4, 11, 3)
      ```
    ````

### Exercice {num2}`exercice`

Définissez un fonction `affiche_max` qui prend 2 paramètres numériques. Cette
fonction doit comparer les deux paramètres et afficher le maximum.


```{exec} python
:editor: 085391cb-a478-4b38-b2f3-0acc4fb65c10
# Complétez la fonction
def affiche_max(a, b):
  ...

affiche_max(4, 12)
affiche_max(14, 5)
affiche_max(3, -7)
affiche_max(2, 2)
```

````{solution}
```{exec} python
:linenos:
def affiche_max(a, b):
  if a >= b:
    print(a)
  else:
    print(b)

affiche_max(4, 12)
affiche_max(14, 5)
affiche_max(3, -7)
affiche_max(2, 2)
```
````

### Exercice {num2}`exercice`

Au-dessus du code donné, définissez une fonction nommée `affiche_prix_billet`
prenant en paramètre l'âge de l'utilisateur et affichant le prix du billet de
cinéma en fonction de cet âge.

Le prix du billet est de 10 CHF pour les moins de 12 ans, de 14 CHF pour les
65 ans et plus et de 16 CHF pour les autres. La fonction affiche uniquement le
prix.

Le code donné doit ensuite pouvoir s'exécuter sans erreur et afficher exactement
les prix des billets pour tous les âges de 1 à 70 ans.

```{exec} python
:editor: 64d9c4cf-247a-4879-b4a4-d9b923bee5b8
# Définissez la fonction affiche_prix_billet
...

for a in range(1, 71):
  affiche_prix_billet(a)
```

````{solution}
```{exec} python
:linenos:
def affiche_prix_billet(age):
  if a < 12:
    print(10)
  elif a >= 65:
    print(14)
  else:
    print(16)

# affiche le prix des billets de 1 à 70 ans
for a in range(1, 71):
  affiche_prix_billet(a)
```
````


### Exercice {num2}`exercice`

Il est souvent difficile de débugger un code qui ne fonctionne pas. En s'aidant
des messages d'erreurs affichés, corrigez le programme ci-dessous qui calcule
l'aire et le périmètre d'un triangle isocèle et rectangle dont la base
(hypoténuse) est connue.

```{image} images/triangle_iso_rect.png
:alt: Triangle isocèle rectangle
:width: 50%
:align: center
```

```{exec} python
:editor: 36bcae3e-b90a-40b1-bac0-33bea021bc99
from math import sqrt

def affiche_aire(base, hauteur)
  aire_triangle = base * hauteur
  print("L'aire vaut", aire_triangle)

def affiche_perimetre(cote1, cote2, cote3):
  perimetre = cote1 + cote2 + cote3
  print("Le périmètre vaut" perimetre)

base = 500
cathete = base / 2
cote = sqrt(cathete**2 + cathete**2)
aire = affiche_aire(base, hauteur)
perimetre = affiche_perimetre(base, cote, cote)
```

```{solution}
Erreurs de syntaxe:
1.  Ligne 3: `SyntaxError: expected ':'` &rarr; il manque les 2 points à la fin
    de la ligne.
2.  Ligne 9: `SyntaxError: invalid syntax. Perhaps you forgot a comma?` &rarr;
    il manque une virgule entre la chaîne de caractère et le variable `perimetre`.

Erreur d'exécution:
1.  Ligne 14: `NameError: name 'hauteur' is not defined` &rarr; la variable
`hauteur` n'est pas définie, elle correspond à la variable `cathete`.

Erreur de logique:
1.  Le calcul d'aire n'est pas correct, pour un rectangle la formule est
    $\dfrac{base \cdot hauteur}{2}$.

Résultat correct:\
L'aire vaut 62500.0\
Le périmètre vaut 1207.1067811865476
```


### Exemple {num2}`exemple`

Nous avons défini une fonction `discriminant` qui calcule et affiche le
discriminant d'une équation du 2<sup></sup> degré. L'équation est de la forme:

$$ax^2 + bx + c = 0$$

```{exec} python
:editor:
# definition des fonctions
def discriminant(a, b, c):
  print(b ** 2 - 4 * a * c)

# progamme principal
discriminant(1, 2, 1)
```

Pour afficher le nombre de solution ou les solutions de cette équation, j'ai
besoin du résultat du discriminant. Malheureusement la fonction `print` ne permet
pas de récupérer cette valeur.

## Fonctions avec valeur de retour

La commande `return` permet de retourner le résultat d'une fonction et ainsi de
pouvoir le réutiliser dans la suite du programme. Pour cela, il est nécessaire
de sauvegarder la valeur retournée dans une variable.

### Exemple {num2}`exemple:py2-delta2`

```{exec} python
:editor:
# définition des fonctions
def discriminant(a, b, c):
  return(b ** 2 - 4 * a * c)

# programme principal

# afficher le nombre de solution
delta = discriminant(1, 2, 1)
if delta > 0:
  print("L'équation a deux solutions.")
elif delta == 0:
  print("L'équation a une solution.")
else:
  print("L'équation n'a pas de solution.")
```
Améliorations possibles de l'exemple:

1.  Demandez les valeurs des coefficients `a`, `b` et `c` à l'utilisateur.
2.  Affichez les solutions quand elles existent.

### Exercice {num2}`exercice`

Déterminez ce que font les programmes suivants et corrigez les erreurs.

1.  ```{exec} python
    :editor:
    def convertit_min_sec(min):
      return min * 60

    convertit_min_sec(145)
    print("145 minutes donnent", nb_secondes, "secondes.")
    ```

2.  ```{exec} python
    :editor:
    def convertit_sec_min(sec):
      min = sec / 60

    nb_minutes = convertit_sec_min(38700)
    print("38700 secondes donnent", nb_minutes, "minutes.")
    ```

3.  ```{exec} python
    :editor:
    def calcule_double_moins_trois(x):
      x = 2 * x
      return x
      x = x - 3

    print(calcule_double_moins_trois(4))
    ```

````{solution}

 1. Il faut sauvegarder la valeur de retour dans la variable nb_secondes
    ```{exec} python
    :linenos:
    def convertit_min_sec(min):
      return min * 60

    nb_secondes = convertit_min_sec(145)
    print("145 minutes donnent", nb_secondes, "secondes.")
    ```

2.  Il manque le `return` dans la fonction. Dans ce cas, la valeur retournée est
    `None`.
    ```{exec} python
    :linenos:
    def convertit_sec_min(sec):
      return sec / 60

    nb_minutes = convertit_sec_min(38700)
    print("38700 secondes donnent", nb_minutes, "minutes.")
    ```

3.  Le `return` n'est pas à la bonne place.
    ```{exec} python
    :linenos:
    def calcule_double_moins_trois(x):
      x = 2 * x
      x = x - 3
      return x

    print(calcule_double_moins_trois(4))
    ```
````

````{important}
`return` interrompt la fonction. Tout ce qui se trouve dans la fonction, mais
après le `return` sera ignoré.

```{exec} python
:linenos:
def double(x):
  return 2*x
  print("Ce texte ne s'affichera pas.")

print(double(5))
print("Fin du programme")
```
````

### Exercice {num2}`exercice`

Sans l'exécuter, déterminez ce que va afficher le programme suivant. Ensuite,
exécutez-le pour vérifier votre réponse.

```{exec} python
:editor:
def mystery_1(z):
  z *= 2
  return z

def mystery_2(x):
  x -= 7
  if x < 0:
    return x
  else:
    return x % 2

y = 5
print(mystery_1(y))
print(mystery_2(y))
print(mystery_2(2 * y))
print(y // 2)
```

### Exercice {num2}`exercice`

Complétez le programme ci-dessous. Nous avons défini une fonction `majeur` pour
tester si une personne est majeure ou pas.

```{exec} python
:editor: d62933bb-5602-48e8-b92e-302c5857b135
def majeur(age):
  if ... :
    return True
  else:
    return False

# Demandez son âge à l'utilisateur
age = ...

if majeur(age):
  print("Tu as le droit de vote")
else:
  print("Tu pourras voter dans", ..., "ans.")
```

````{solution}
```{exec} python
def majeur(age):
  if age >= 18 :
    return True
  else:
    return False

# Demandez son âge à l'utilisateur
age = int(input("Quel âge as-tu?"))

if majeur(age):
  print("Tu as le droit de vote")
else:
  print("Tu pourras voter dans", 18 - age, "ans.")
```
````

(string)=
## Les fonctions sur les chaînes de caractères

En Python, il existe beaucoup de fonctions prédéfinies qui permettent de
manipuler les chaînes de caractères. La plupart
sont des fonctions avec valeurs de retour.

`txt`: représente le texte analysé.<br>
`s`: représente un caractère ou une chaine de caractères

len(txt)
: retourne le nombre de caractères du texte (espaces compris)

txt.count(s)
: retourne le nombre de fois que `s` apparaît dans `txt`.

txt.find(s)
: retourne l'index de l'emplacement de la première apparition de `s` dans `txt`.<br>
 Si `s` n'apparaît pas dans `txt` la fonction retourne `-1`.

txt.replace(s, t)
: retourne une nouvelle chaîne de caractère dans laquelle tous les `s` de `txt`
  ont été remplacé par `t`.

txt.lower()
: retourne une nouvelle chaîne de caractère écrite en minuscules.

txt.upper()
: retourne une nouvelle chaîne de caractère écrite en majuscules.


### Exercice {num2}`exercice`

Sans les exécuter, que vont afficher ces programmes?<br>
Exécutez-les ensuite pour vérifier votre réponse.

1.  ```{exec} python
    :linenos:
    txt = "J'aime les pommes, les pommes sont mon fruit favori!"
    n = len(txt)
    print(n)
    ```

2.  ```{exec} python
    :linenos:
    txt = "J'aime les pommes, les pommes sont mon fruit favori!"
    n = txt.count("pommes")
    print(n)
    ```

3.  ```{exec} python
    :linenos:
    txt = "J'aime les pommes, les pommes sont mon fruit favori!"
    n = txt.find("pommes")
    m = txt.find("poires")
    print(n)
    print(m)
    ```

4.  ```{exec} python
    :linenos:
    txt = "J'aime les pommes, les pommes sont mon fruit favori!"
    new_txt = txt.replace("pommes", "poires")
    print(new_txt)
    print(txt)
    ```

5.  ```{exec} python
    :linenos:
    txt = "J'aime les POMMES!"
    minu = txt.lower()
    maju = txt.upper()
    print(minu)
    print(maju)
    print(txt)
    ```

### Exercice {num2}`exercice`

```{exec} python
:name: texte
:class: hidden
texte = "L'école moderne, c'est l'art d'enseigner le théorème de Pythagore à des ados capables de scroller sur TikTok à la vitesse de la lumière tout en ouvrant discrètement trois onglets de jeux en ligne pendant le cours d'histoire. Aujourd'hui, le stylo plume a pris sa retraite, remplacé par des tablettes où les notes de cours cohabitent joyeusement avec des mèmes et des vidéos en tendance. Les profs ne se battent plus contre les avions en papier, mais contre le correcteur automatique et les copier-coller un peu trop magiques de ChatGPT. Au fond, c'est une génération ultra-connectée et pleine de ressources, capable de faire un montage vidéo digne d'Hollywood en deux minutes sur leur téléphone, mais qui cherche encore la formule magique pour faire ses devoirs sans procrastiner."
```

Un texte, généré par Gemini, a été sauvegardé dans la variable `texte`.

1.  Affichez le texte.
2.  Calculez et affichez le nombre de caractères de ce texte.
3.  Calculez et affichez la fréquence de la lettre "e", de la lettre "a", de la
    lettre "d" et de la lettre "x".<br>
    Les valeurs correspondent-elles à celles attendues
    (voir [](../crypto/frequences.md))? Pourquoi?
4.  Définissez une fonction qui teste si le texte contient une certaine lettre
    et affiche:

      - "Oui, ce texte contient la lettre ..."
      - "Non, ce texte ne contient pas la lettre ..."

    La fonction prend deux paramètres: la lettre à tester et le texte.<br>
    Testez la fonction avec les lettres "y" et "z".

```{exec} python
:after: texte
:editor: e43729d7-c4e9-491d-8874-9c7e21038966
```

````{solution}
```{exec} python
:after: texte
# 1
print(texte)
# 2
total = len(texte)
print(total)
# 3
n = texte.count("e")
print(n/total)
n = texte.count("a")
print(n/total)
n = texte.count("d")
print(n/total)
n = texte.count("x")
print(n/total)
# 4
def contenu(lettre, texte):
  if texte.find(lettre) != -1:
    print("Oui, ce texte contient la lettre", lettre)
  else:
    print("Non, ce texte ne contient pas la lettre", lettre)
contenu("y", texte)
contenu("z", texte)
```

Les valeurs pour le "d" et le "x" sont proches, mais pas pour le "e" et le "a".

Les fréquences d'apparition des lettres en français des
[](../crypto/frequences.md) ne tiennent pas compte des différences entre une
lettre majuscule ou minuscule, ni celles des lettres accentuées. Pour faire une
analyse de fréquence, il faudrait tout d'abord modifier le texte (supprimer les
majuscules, les accents, ...).
````

### Exercice {num2}`exercice`

Définissez une fonction qui modifie une phrase en son équivalent en **leet
speak**. La fonction prend le texte à modifier en paramètre et retourne la
phrase modifiée.

Testez avec d'autres phrases.

```{Admonition} Le saviez-vous?
:class: attention, dropdown
Le **leet speak** (ou « 1337 5p34k ») est un système d'écriture informel né dans
les années 1980. Créé à l'origine pour tromper les filtres automatiques et
sécuriser les mots de passe, le leet speak est devenu aujourd'hui un pilier
incontournable de la culture geek et de l'argot des jeux vidéo.

Il consiste à remplacer certaines lettres par des chiffres ou des caractères
spéciaux qui leur ressemblent visuellement.

{.columns-4}
- A → 4
- E → 3
- G → 6
- I / L → 1
- O → 0
- S → 5
- T → 7
- B → 8
```

```{exec} python
:editor: fa658599-28d3-44bd-a377-8d4526435362
phrase = "Mon devoir est corrompu par un virus :-/"
```

````{solution}
```{exec} python
:editor:
phrase = "Mon devoir est corrompu par un virus :-/"
def leet_speak(texte):
  txt = texte.upper()
  txt = txt.replace("A", "4")
  txt = txt.replace("E", "3")
  txt = txt.replace("G", "6")
  txt = txt.replace("I", "1")
  txt = txt.replace("L", "1")
  txt = txt.replace("O", "0")
  txt = txt.replace("S", "5")
  txt = txt.replace("T", "7")
  txt = txt.replace("B", "8")
  return txt

print(phrase ,"devient:", leet_speak(phrase))
```
````

### Exercice {num2}`exercice`

Python peut être utilisé pour chiffrer ou déchiffrer un message utilisant le
[chiffre de César](#cesar), notamment en utilisant les deux fonctions
ci-dessous.

ord(c)
: retourne la valeur Unicode du caractère `c` passé en paramètre

chr(u)
: retourne le caractère qui correspond à la valeur Unicode `u` passée en
  paramètre

Les textes à chiffrer et déchiffrer ne contiendront que des lettres majuscules
ou minuscules. Les caractères spéciaux ne seront pas chiffrés (ni déchiffrés),
il seront simplement retranscrit.

Exemple: **La crypto est sympa!** $\implies$**OD FUBSWR HVW VBPSD!**

```{admonition} Rappel - Unicode
:class: tip, dropdown
Le Unicode est une norme internationale qui attribue à chaque caractère une
valeur unique. Pour les caractères présents dans la table ASCII (lettres sans
accents, chiffres et caractères spéciaux standards), la valeur Unicode
correspond à sa valeur ASCII
(voir [Représentation des caractères](/1re/representation-info/caracteres.md)).

```

Voici les principales étapes:

1.  Écrivez le message en majuscules.
2.  Créez une variable `code` pour le message codé.
3.  Parcourez le message un caractère après l'autre en utilisant une boule
    `for`:
    ```{code} text
    for c in text:
      ...
    ```
4.  Si le caractère est une lettre:
    - Récupérez l'index du caractère et lui appliquez le décalage de 3 lettres.
    - Ajoutez le nouveau caractère au `code`.
5.  Sinon, copiez le caractère dans le `code`.
6.  Affichez le message codé.
7.  Modifiez le code pour définir une fonction `chiffre(message)` qui chiffre un
    message au moyen du Chiffre de César. Cette fonction retourne le message
    codé.
8.  Définissez une fonction `dechiffre(code)` qui déchiffre un message codé au
    moyen du Chiffre de César. Cette fonction retourne le message décodé.
9.  Modifiez les deux fonctions `chiffre` et `dechiffre` pour pouvoir chiffrer
    et déchiffrer des messages avec un décalage quelconque.


```{exec} python
:editor: 94610dec-64eb-4084-9acd-8e4e7426aa41
message = "Codez ce message!"
```

````{solution}
```{exec} python
:editor:
message = "Codez ce message!"
msg = message.upper()
code = ""
for c in msg:
  index = ord(c) - ord("A")
  if 0 <= index < 26:
    index = (index + 3) % 26
    code += chr(ord("A") + index)
  else:
    code += c
print(code)
```
````

