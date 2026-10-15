% Copyright 2026 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Listes - Escape game

But: Créer un escape game en Python.

## Exemple

Afin de comprendre la structure que vous deverez utiliser, voici un exemple d'un
programme qui représente une partie d'"Un conte à votre façon" de Raymond Queneau.

<style>
.frame {
height: 30rem;
overflow-y: scroll;
}
</style>

{.frame}
```{container} frame
# "Un conte à votre façon" de Raymond Queneau

1.  Désirez-vous connaître l'histoire des trois alertes petits pois?
    - Si oui,  passez à 4.
    - Si non, passez à 2.

2.  Préférez-vous celle des trois minces grands échalas?
    - Si oui, passez à 16.
    - Si non, passez à 3.

3.  Préférez-vous celle des trois moyens médiocres arbustes?
    - Si oui, passez à 17.
    - Si non, passez à 21.

4.  Il y avait une fois trois petits pois vêtus de vert qui dormaient gentiment
    dans leur cosse. Leur visage bien rond respirait par les trous de leurs
    narines et l'on entendait leur ronflement doux et harmonieux.
    - Si vous préférez une autre description, passez à 9.
    - Si celle-ci vous convient, passez à 5.

5.  Ils ne rêvaient pas. Ces petits êtres en effet ne rêvent jamais.
    - Si vous préférez qu'ils rêvent passez à 6.
    - Si non, passez à 7.

6.  Ils rêvaient. Ces petits être en effet rêvent toujours et leurs nuits
    sécrètent des songes charmants.
    - Si vous désirez connaître ces songes, passez à 11.
    - Si vous n'y tenez pas, vous passez à 7.

7.  Leurs pieds mignons trempaient dans de chaudes chaussettes et ils portaient
    au lit des gants de velours noir.
    - Si vous préférez des gants d'une autre couleur, passez à 8.
    - Si cette couleur vous convient, passez à 10.

8.  Ils portaient au lit des gants de velours bleu.
    - Si vous préférez des gants d'une autre couleur, passez à 7.
    - Si cette couleur vous convient, passez à 10.

9.  Il y avait une fois trois petits pois qui roulaient leur bosse sur les
    grands chemins. Le soir venu, fatigués et las, ils s'endormirent très
    rapidement.
    - Si vous désirez connaître la suite, passez à 5.
    - Si non, passez à 21.

10. Tous les trois faisaient le même rêve, ils s'aimaient en effet tendrement
    et, en bons fiers trumeaux, songeaient toujours semblablement.
    - Si vous désirez connaître leur rêve, passez à 11.
    - Si non, passez à 12.

11. Ils rêvaient qu'ils allaient chercher leur soupe à la cantine populaire et
    qu'en ouvrant leur gamelle, ils découvraient que c'était de la soupe d'ers.
    D'horreur, ils s'éveillent.
    - Si vous voulez savoir pourquoi ils s'éveillent d'horreur, consulter le
      Larousse au mot « ers » et n'en parlons plus.
    - Si vous jugez inutile d'approfondir la question, passez à 12.

12. Opopoï! S'écrient-ils en ouvrant les yeux. Opopoï! Quel songe avons-nous
    enfanté là? Mauvais présage dit le premier. Oui-da dit le second, c'est bien
    vrai, me voilà triste. Ne vous troublez pas ainsi, dit le troisième qui
    était le plus futé, il ne s'agit pas de s'émouvoir, mais de comprendre,
    bref, je m'en vais vous analyser ça.
    - Si vous désirez connaître tout de suite l'interprétation de ce songe,
      passez à 15.
    - Si vous souhaitez au contraire connaître les réactions des deux autres,
      passez à 13.

13. Tu nous la bailles belle, dit le premier. Depuis quand sais-tu analyser les
    songes? Oui, depuis quand, ajouta le second?
    - Si vous désirez aussi savoir depuis quand, passez à 14.
    - Si non, passez à 14 tout de même car vous ne le saurez pas plus.

14. Depuis quand? s'écria le troisième. Est-ce que je sais moi! Le fait est que
    je pratique la chose. Vous allez voir!
    - Si vous voulez aussi voir, passez à 15.
    - Si non, passez également à 15, car vous ne verrez rien.

15. Eh bien! voyons, dirent ses frères. Votre ironie ne me plaît pas, répliqua
    l'autre, et vous ne saurez rien. D'ailleurs au cours de cette conversation
    d'un ton assez vif, votre sentiment d'horreur ne s'est-il pas estompé?
    effacé même? Alors à quoi bon remuer le bourbier de votre inconscient de
    papilionacées? Allons plutôt nous laver à la fontaine et saluer ce gai matin
    dans l'hygiène et la sainte euphorie! Aussitôt dit, aussitôt fait: les voilà
    qui se glissent hors de leur cosse, se laissent doucement rouler sur le sol
    et puis au petit trot gagnent joyeusement le théâtre de leurs ablutions.
    - Si vous désirez savoir ce qui se passe sur le théâtre de leurs ablutions,
      passez à 16.
    - Si vous ne le désirez pas, vous passez à 21.

16. Trois grands échalas les regardaient faire.
    - Si les trois grands échalas vous déplaisent, passez à 21.
    - S'ils vous conviennent, passez à 18.

17. Trois moyens médiocres arbustes les regardaient faire.
    - Si les trois moyens médiocres arbustes vous déplaisent, passez à 21.
    - S'ils vous conviennent, passez à 18.

18. Se voyant ainsi zyeutés, les trois alertes petits pois qui étaient fort
    pudiques s'ensauvèrent.
    - Si vous désirez savoir ce qu'ils firent ensuite, passez à 19.
    - Si vous ne le désirez pas, vous passez à 21.

19. Ils coururent bien fort pour regagner leur cosse et, refermant celle-ci
    derrière eux, s'y endormirent de nouveau.
    - Si vous désirez connaître la suite, passez à 20.
    - Si vous ne le désirez pas, vous passez à 21.

20. Il n'y a pas de suite, le conte est terminé.

21. Dans ce cas, le conte est également terminé.
```

```{exec} python
:style: max-height: 60vh
:linenos:
def etape1():
  print("Désirez-vous connaître l'histoire des trois alertes petits pois?")
  print("Si oui, passez à 4. Si non, passez à 2.")
  choix = input("oui ou non?").lower()
  while choix != "oui" and choix != "non":
    choix = input("oui ou non?").lower()
  if choix == "oui":
    return 4
  else:
    return 2

def etape2():
  print("Préférez-vous celle des trois minces grands échalas?")
  print("Si oui, passez à 16. Si non, passez à 3.")
  choix = input("oui ou non?").lower()
  while choix != "oui" and choix != "non":
    choix = input("oui ou non?").lower()
  if choix == "oui":
    return 16
  else:
    return 3

def etape3():
  print("Préférez-vous celle des trois moyens médiocres arbustes?")
  print("Si oui, passez à 17. Si non, passez à 21.")
  choix = input("oui ou non?").lower()
  while choix != "oui" and choix != "non":
    choix = input("oui ou non?").lower()
  if choix == "oui":
    return 17
  else:
    return 21

def autres_etapes():
  print("...")
  print("Si oui, passez à ... Si non, passez à ...")
  choix = input("oui ou non?").lower()
  while choix != "oui" and choix != "non":
    choix = input("oui ou non?").lower()
  if choix == "oui":
    return 4
  else:
    return 20

def etape20():
  print("Il n'y a pas de suite, le conte est terminé.")
  return 100

def etape21():
  print("Dans ce cas, le conte est également terminé.")
  return 100

# initialisation des variables pour le déroulement du jeu
etape = 1
histoire_terminee = False

# texte d'introduction
print('Bienvenu dans "Un conte à votre façon" de Raymond Queneau.')

while histoire_terminee == False:
  if etape == 1:
    etape = etape1()
  elif etape == 2:
    etape = etape2()
  elif etape == 3:
    etape = etape3()
  elif etape == 4 or etape == 16 or etape == 17:
    etape = autres_etapes()
  elif etape == 20:
    etape = etape20()
  elif etape == 21:
    etape = etape21()
  elif etape == 100:
    histoire_terminee = True
  else:
    print("Valeur non valide, il y a un problème quelque part...")

# texte final
print("J'espère que cette histoire t'a plu!")

```
