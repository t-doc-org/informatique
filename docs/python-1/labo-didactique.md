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
    "https://im-api.proxy.c-space.net/1/ai/782/openai/chat/completions";
const compToken = await decryptSecret(key, {
    iv: 'WhVOIKndPgFcQp8x',
    data: 'cB2+NNx58sdf5faBu+65lYUit6U2HDWA9Tt110nr+NsHxCc/T9Ael+FrE1qmylZQfB' +
          'isbrRRQg46vAZL76Rk0cGAdWM43A82YImq59xOk5el2EMsRi2VIyVXOswoJbNQ',
});

let conversationId = 0;
const conversation = {
    'model': 'llama3',
    'messages': [],
};

function logConversation(data) {
    return fetchJson(`${storeUrl}/log`, {
        headers: bearerAuthorization(storeToken),
        body: {
            'time': Date.now(), 'location': location.href, 'session': session,
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
async function ask(action, prompt) {
    conversation['messages'].push({'content': prompt, 'role': 'user'});
    try {
        const resp = await fetchJson(completionsURL, {
            headers: bearerAuthorization(compToken),
            body: conversation,
        });
        const msg = resp['choices'][0]['message'];
        conversation['messages'].push(msg);
        logConversation({'type': 'response', 'questionCount': questionCount, 'score': score, 'action': action});
        return msg['content'];
    } catch (e) {
        logConversation({'type': 'error', 'error': e.toString()});
        throw e;
    }
}

let level = 0;
let score = 0;
let questionCount = 0;
const examples = [
    [`\
Écrivez le programme Python qui correspond à l'algorithme suivant, en \
définissant une variable pour chaque donnée:
La longueur vaut 10. La largeur vaut 5. Calculez et affichez l'aire du rectangle
`,`Utiliser des variables et la fonction print. Pas de calcul avec des cercles \
et pas de calcul de pourcentage.
Un seul calcul à effectuer qui ne peut pas être fait de tête rapidement.`],
    [`\
Écrivez le programme Python qui correspond à l'algorithme suivant:
Demandez l'âge à l'utilisateur.
S'il a 18 ans et plus, affichez qu'il est majeur, sinon affichez qu'il est \
mineur.
`, `Il ne doit contenir qu'un if et un else. La valeur utile pour le if \
doit être indiquée. Considérer que la valeur entrée par l'utilisateur est \
valide`],
    [`\
Écrivez le programme Python qui correspond à l'algorithme suivant:
Demandez l'âge à l'utilisateur.
S'il a moins de 16, affichez qu'il n'a pas le droit de boire d'alcool.
S'il a 16 ans et moins de 18 ans, affichez qu'il a le droit de boire du vin et \
de la bière.
Sinon affichez qu'il a le droit de boire de l'alcool.
`, `Il doit contenir un elif. Les valeurs utiles pour les if, elif et else, \
doivent être indiquée en précisant si c'est strictement ou inclu. Considérer que la \
valeur entrée par l'utilisateur est valide.
Pas de calcul à faire, juste afficher du texte.`],
    [`\
Écrivez le programme Python qui correspond à l'algorithme suivant:
Initialisez une variable compte_a_rebours à 10.
Tant que compte_a_rebours est plus grand que 0, affichez la valeur de \
compte_a_rebours.
Soustraire 1 à compte_a_rebours.
Affichez 'BOOM'.
`, `Utilisez une boucle while. Pas de demande à l'utilisateur. Pas de listes \
Ne pas utiliser d'exemple avec des notes.`],
        [`\
Écrivez le programme Python qui correspond à l'un des algorithmes suivants:
Soit affichez les nombres de 0 à 50 (inclus).
`, `Utiliser for i in range(n) avec un seul paramètre. Ne pas demander \
d'afficher des lettres. Doit générer une suite des nombres entiers qui se \
suivent. Les valeurs de début et fin ne doivent pas être les mêmes.`]
];

await domLoaded;

const name = document.querySelector('#name');

const nameKey = 't-doc:firstName'
let mistakeMade = false;
let firstName = localStorage.getItem(nameKey);
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

// Génère une nouvelle question.
async function generateQuestion() {
    questionCount += 1;
    levelNum.textContent = `${level + 1}`;
    question.replaceChildren(text("Génération d'une nouvelle question..."));
    const [ex, constraint] = examples[level];
    const q = await ask('new', `\
Génère un autre exercice du même genre que l'exemple suivant sans mentionner \
la condition dans l'énoncé, mais sois créatif ou pas. L'énoncé doit avoir du \
sense. Utilise des CHF à la place des euros. Si l'exercice parle de note de \
l'élève considérer des notes entre 0 et 6 au dixième.

${ex}

Cet exercice doit suivre la condition suivante: ${constraint}
Ne pas résoudre l'exemple et transmettre juste l'énoncé de l'exercice sans autre
commentaire.`);
    feedback.classList.add('hidden');
    question.replaceChildren(text(q));
}

commencer.addEventListener('click', async () => {
    await generateQuestion();
    correct.disabled = newQuestion.disabled = help.disabled = false;
    commencer.disabled = name.disabled = true;
    localStorage.setItem(nameKey, name.value);
});

correct.addEventListener('click', async () => {
    await blocking(async () => {
        // Obtient le code de l'utilisateur à partir de l'éditeur.
        const editor = findEditor(document.querySelector('#editor'));
        const code = editor.state.doc.toString();

        // Demande la correction de la réponse.
        const fb = await ask('correct', `\
Vérifie si le code suivant correspond à l'énoncé.
Si le code ne contient pas de variable, répondre "Il faut utiliser des \
variables."
Sans s'occuper de la gestion des erreurs et des fautes d'orthographe, le code \
contient-il des erreurs de syntaxe, d'exécution ou de logique?
On considère que la fonction suivante a été prédéfinie:

async def input_line(text):
    return input(text)

Suppose que le code est exécuté dans une fonction asynchrone.

Si un cas a été traité dans le if, par exemple if a < 4, il n'est pas \
nécessaire elif 4 <= a < 7, a <7 est suffisant, car le cas où 4 est plus
petit que 4 a déjà été traité dans le if. Idem pour le else, ce n'est donc pas \
une erreur.
5.0 et 5 sont le même nombre, ce n'est donc pas une erreur.
Dans la boucle for i in range(n), la boucle s'effectue de 0 à (n-1).
Dans la boucle for i in range(m, n), la boucle s'effectue de m à (n-1).
S'il y a des erreurs, explique-les, mais ne donne pas la solution, sinon \
renvoie seulement ok et rien d'autre.
Le code commence ici:

${code}
`);
        if (fb === "ok") {
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
            await generateQuestion();
        } else {
            mistakeMade = true;
            feedback.querySelector('pre').replaceChildren(text(fb));
            feedback.classList.remove('hidden');
        }
    });
    if (level >= examples.length) {
        newQuestion.disabled = correct.disabled = help.disabled = true;
    }
});

newQuestion.addEventListener('click', async () => {
    await blocking(async () => {
        feedback.classList.add('hidden');
        await generateQuestion();
    });
});

help.addEventListener('click', async () => {
    await blocking(async () => {
        // Demande la solution de l'exercice.
        const helpResp = await ask('help', `\
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
