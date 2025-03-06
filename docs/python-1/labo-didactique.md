% Copyright 2024 Caroline Blank <caro@c-space.org>
% SPDX-License-Identifier: CC-BY-NC-SA-4.0

# Labo didactique

```{metadata}
orphan:
```

<style>
#question pre,
#feedback pre {
    white-space: pre-wrap;
}
#level {
    margin-left: 1rem;
}
</style>

<script type="module">
import {bearerAuthorization, domLoaded, fetchJson, text, toBase64} from '../_static/tdoc/core.js';
import {decryptSecret, pageKey, random} from '../_static/tdoc/crypto.js';
import {findEditor} from '../_static/tdoc/editor.js';

// Créé la clé des secrets pour les APIs.
const key = await pageKey('key', 'nMHqoWnA0tvA');

// Décrypte les informations d'identification pour l'API de logging.
const storeUrl = tdoc.store_url || `${location.origin}/*store`;
const storeToken = await decryptSecret(key, {
    iv: 'vgVd4UDZlHfcA99C',
    data: 'iZm48UGgU0I/H3tP4W4ytR1SGZQ0RDGv+mNdPCAAqZGRc2mK8/DEVttoAZ9f3mEo',
});
const session = await toBase64(await random(18));

// Décrypte les informations d'identification pour l'API de chat.
const completionsURL =
    "https://im-api.t-doc.org/1/ai/782/openai/chat/completions";
const compToken = await decryptSecret(key, {
    iv: 'WhVOIKndPgFcQp8x',
    data: 'cB2+NNx58sdf5faBu+65lYUit6U2HDWA9Tt110nr+NsHxCc/T9Ael+FrE1qmylZQfB' +
          'isbrRRQg46vAZL76Rk0cGAdWM43A82YImq59xOk5el2EMsRi2VIyVXOswoJbNQ',
});

let conversationId = 0;
const conversation = {
    'model': 'llama3',
    // 'model': 'mixtral8x22b',
    'messages': [],
};

function logConversation(data) {
    return fetchJson(`${storeUrl}/log`, {
        headers: bearerAuthorization(storeToken),
        body: {
            'time': Date.now(),
            'location': location.origin + location.pathname,
            'session': session,
            'data': {
                'id': conversationId,
                'name': name.value,
                'conversation': structuredClone(conversation),
                ...data,
            },
        },
    });
}

// Ajoute une question à la conversation.
async function ask(action, attrs, prompt) {
    conversation['messages'].push({'content': prompt, 'role': 'user'});
    try {
        const resp = await fetchJson(completionsURL, {
            headers: bearerAuthorization(compToken),
            body: conversation,
        });
        const msg = resp['choices'][0]['message'];
        conversation['messages'].push(msg);
        logConversation({
            'type': 'response', 'action': action, ...attrs,
            'level': level, 'score': score,
        });
        return msg['content'];
    } catch (e) {
        logConversation({
            'type': 'error', 'action': action, ...attrs,
            'level': level, 'score': score,
            'error': e.toString(),
        });
        throw e;
    }
}

let level = 0;
let score = 0;
let mistakeMade = false;
const examples = [[`\
Écrivez le programme Python qui correspond à l'algorithme suivant:
Demandez à l'utilisateur la longueur d'un rectangle. Sa largeur mesure 14.5.
Calculez et affichez l'aire du rectangle.
`, `\
Demandez à l'utilisateur une valeur.
Pas de calcul avec des cercles. Pas d'exercice avec des notes.
Un énoncé simple avec un seul calcul à effectuer.
Il ne doit pas y avoir de if, seulement un calcul simple.`,
    ], [`\
Écrivez le programme Python qui correspond à l'algorithme suivant:
Demandez l'âge à l'utilisateur.
S'il a 18 ans et plus, affichez qu'il est majeur, sinon affichez qu'il est \
mineur.
`, `\
Il ne doit contenir qu'un if et un else. La valeur utile pour le if doit être \
indiquée. Considérer que la valeur entrée par l'utilisateur est valide.`,
    ], [`\
Écrivez le programme Python qui correspond à l'algorithme suivant:
Demandez l'âge à l'utilisateur.
S'il a moins de 16, affichez qu'il n'a pas le droit de boire d'alcool.
S'il a 16 ans ou plus et moins de 18 ans, affichez qu'il a le droit de boire du \
vin et de la bière.
Sinon affichez qu'il a le droit de boire de l'alcool.
`, `\
Il doit contenir un elif. Les valeurs utiles pour les if, elif et else, \
doivent être indiquée en précisant si c'est strictement ou inclu. Considérer \
que la valeur entrée par l'utilisateur est valide. \ Utiliser la valeur précédente \
pour indiquer le prochain cas. Exemple: si a est plus petit que 7. Si \
a est plus grand ou égal à 7 et a plus petit (ou égal à 12). \
Les phrases à afficher doivent être courtes. \
Pas de calcul à faire, juste afficher du texte.`,
    ], [`\
Écrivez le programme Python qui correspond à l'un des algorithmes suivants:
Affichez les nombres de 0 à 50 (inclus).
`, `\
Utiliser for i in range(n) avec un seul paramètre. Ne pas demander d'afficher \
des lettres. Doit générer une suite des nombres entiers qui se suivent. Les \
valeurs de début et fin ne doivent pas être les mêmes.`,
], [`\
Écrivez le programme Python qui correspond à l'algorithme suivant:
Initialisez une variable compte_a_rebours à 10.
Tant que compte_a_rebours est plus grand que 0, affichez la valeur de \
compte_a_rebours.
Soustraire 1 à compte_a_rebours.
Affichez 'BOOM'.
`, `\
Utilisez une boucle while. Pas de demande à l'utilisateur. Pas de listes. Pas \
de calcul aléatoire avec le module random. Ne pas utiliser d'exemple avec des \
notes.`,
]];

await domLoaded;

const name = document.querySelector('#name');

const nameKey = 't-doc:firstName'
const firstName = localStorage.getItem(nameKey);
if (firstName !== null) name.setAttribute('value', firstName);

const question = document.querySelector('#question pre');
const feedback = document.querySelector('#feedback');

const correct = document.querySelector('#correct');
const newQuestion = document.querySelector('#new-question');
const help = document.querySelector('#help');
const levelNum = document.querySelector('#levelNum');

// Exécute une fonction en bloquant les boutons.
async function blocking(fn) {
    correct.disabled = newQuestion.disabled = help.disabled = true;
    try {
        return await fn();
    } finally {
        correct.disabled = newQuestion.disabled = help.disabled = false;
    }
}

function resetEditor() {
    const editor = findEditor(document.querySelector('#editor'));
    editor.dispatch(editor.state.update({
        changes: {from: 0, to: editor.state.doc.length, insert: ""},
    }));
}

function focusEditor() {
    findEditor(document.querySelector('#editor')).focus();
}

// Génère une nouvelle question.
async function generateQuestion() {
    levelNum.textContent = `${level + 1}`;
    question.replaceChildren(text("Génération d'une nouvelle question..."));
    const [ex, constraint] = examples[level];
    try {
        const q = await ask('new', {}, `\
Génère un autre exercice du même genre que l'exemple donné ci-dessous sans \
mentionner la condition dans l'énoncé, mais sois créatif ou pas. L'énoncé doit \
avoir du sens. Utilise des CHF à la place des euros. Si l'exercice parle de \
note de l'élève considérer des notes entre 0 et 6 au dixième.

Cet exercice doit suivre la condition suivante: ${constraint}
Transmettre juste l'énoncé de l'exercice sans la solution et autres \
commentaires.
Ne pas résoudre l'exercice et ne pas donner d'exemple.
Ne pas donner les conditions.

Exemple:
${ex}`);
        feedback.classList.add('hidden');
        question.replaceChildren(text(q));
    } catch (e) {
        question.replaceChildren(text(`ERREUR: ${e}`));
        throw e;
    }
}

commencer.addEventListener('click', async () => {
    localStorage.setItem(nameKey, name.value);
    await generateQuestion();
    correct.disabled = newQuestion.disabled = help.disabled = false;
    commencer.disabled = name.disabled = true;
    focusEditor();
});

correct.addEventListener('click', async () => {
    await blocking(async () => {
        // Obtient le code de l'utilisateur à partir de l'éditeur.
        const editor = findEditor(document.querySelector('#editor'));
        const code = editor.state.doc.toString();

        // Demande la correction de la réponse.
        const fb = await ask('correct', {'code': code}, `\
Vérifie si le code suivant correspond à l'énoncé.
Sans s'occuper de la gestion des erreurs et des fautes d'orthographe, vérifie \
si le code contient des erreurs de syntaxe ou d'exécution.

Si le code est vide ou ne contient qu'un commentaire, considérez cela comme une \
erreur.

S'il n'y a pas d'erreur ou que le code semble correct, renvoie seulement ok et \
rien d'autre.
S'il y a des erreurs, explique-les sans afficher de code python.

Pour les codes avec des if, elif et else, les trois codes suivants sont \
équivalents et donc corrects. Il n'est pas nécessaire d'écrire dans le elif note > 4,
car ce cas est déjà pris en compte dans le if. Dans ce cas renvoyer seulement ok.
code 1:
note = float(input("Note de l'élève : "))
if note <= 4.0 :
    print("Insuffisant")
elif note <= 5.5 :
    print("Satisfaisant")
else :
    print("Très bien")

code 2:
note = float(input("Note de l'élève : "))
if note <= 4.0 :
    print("Insuffisant")
elif note > 4.0 and note <= 5.5 :
    print("Satisfaisant")
else :
    print("Très bien")

code 3:
note = float(input("Note de l'élève : "))
if note <= 4.0 :
    print("Insuffisant")
elif 4.0 < note <= 5.5 :
    print("Satisfaisant")
else :
    print("Très bien")

La meilleure version étant le code 1, sans la répétition de note > 4.


Si une valeur est demandée à l'utilisateur et que c'est toujours un nombre \
entier comme un âge, vérifiez que la valeur a été convertie en entier par \
int() et pas en float. Si c'est un nombre à virgule comme une note ou un \
montant, la conversion doit se faire avec float().

La multiplication est commutative, donc l'ordre n'a pas d'importance, cela \
signifie que 3 * 4 donne le même résultat que 4 * 3, c'est donc correct.
Dans une suite de multiplications et de divisions, les opérations sont \
commutatives, cela signifie que nb_km * 1.2 * 7 / 100 donne le même résultat que \
nb_km / 100 * 1.2 * 7, c'est donc correct.
5.0 et 5 sont le même nombre, ce n'est donc pas une erreur.
2.5 et 2.50 sont le même nombre, ce n'est donc pas une erreur.
Dans la boucle for i in range(n), la boucle s'effectue de 0 à (n-1).
Dans la boucle for i in range(m, n), la boucle s'effectue de m à (n-1).

Le code commence ici:

${code.replace('await input_line', 'input')}
`);
        if (fb === "ok" || fb.endsWith("ok")) {
            feedback.querySelector('pre').replaceChildren("Correct!");
            feedback.classList.remove('hidden');
            if (!mistakeMade) {
                score += 1;
                level = Math.floor(score / 2);
                if (score % 2 == 0) {
                    conversation['messages'] = [];
                    conversationId += 1;
                }
            }
            if (level >= examples.length) {
                question.replaceChildren(text("Bravo, tu as terminé!"));
                return;
            }
            mistakeMade = false;
            resetEditor();
            await generateQuestion();
            focusEditor();
        } else {
            mistakeMade = true;
            feedback.querySelector('pre').replaceChildren(text(fb));
            feedback.classList.remove('hidden');
            focusEditor();
        }
    });
    if (level >= examples.length) {
        newQuestion.disabled = correct.disabled = help.disabled = true;
    }
});

newQuestion.addEventListener('click', async () => {
    await blocking(async () => {
        feedback.classList.add('hidden');
        mistakeMade = false;
        resetEditor();
        await generateQuestion();
        focusEditor();
    });
});

help.addEventListener('click', async () => {
    await blocking(async () => {
        // Obtient le code de l'utilisateur à partir de l'éditeur.
        const editor = findEditor(document.querySelector('#editor'));
        const code = editor.state.doc.toString();

        // Demande la solution de l'exercice.
        const helpResp = await ask('help', {'code': code}, `\
Donne la solution de l'exercice en expliquant comment faire sans mentionner la \
condition.
`);
        feedback.querySelector('pre').replaceChildren(text(helpResp));
        feedback.classList.remove('hidden');

    });
    correct.disabled = true;
});
</script>

Site d'entrainement d'écriture de programme en Python.

<label for="name">Prénom:</label>
<input type="text" id="name" size="20"/>
<button id="commencer" class="tdoc-button">Commencer</button>

```{code-block} text
:name: question
```

```{code-block} text
:name: feedback
:class: hidden
```

<button id="correct" class="tdoc-button" disabled>Corriger</button>
<button id="new-question" class="tdoc-button" disabled>Nouvelle question</button>
<button id="help" class="tdoc-button" disabled>Aide</button>
<span id="level">Niveau: <span id="levelNum"></span></span>

```{exec} python
:name: editor
:editor:
:style: max-height: 25rem
# Écrivez le code ici...
```
