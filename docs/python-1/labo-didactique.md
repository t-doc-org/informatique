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
</style>

<script type="module">
import {domLoaded, text} from '../_static/tdoc/core.js';
import {decryptSecret, pageKey} from '../_static/tdoc/crypto.js';
import {findEditor} from '../_static/tdoc/editor.js';

// Décrypte les informations d'identification de l'API.
const token = await decryptSecret(await pageKey('key', 'nMHqoWnA0tvA'), {
    iv: 'WhVOIKndPgFcQp8x',
    data: 'cB2+NNx58sdf5faBu+65lYUit6U2HDWA9Tt110nr+NsHxCc/T9Ael+FrE1qmylZQfB' +
          'isbrRRQg46vAZL76Rk0cGAdWM43A82YImq59xOk5el2EMsRi2VIyVXOswoJbNQ',
});

// Exécute une requête JSON sur une API.
async function request(method, url, headers, body) {
    const resp = await fetch(url, {
        method, headers,
        body: body !== undefined ? JSON.stringify(body) : undefined,
        cache: 'no-cache', referrer: '',
    });
    if (resp.status !== 200) {
        throw Error(`Request failed: ${resp.status} ${resp.statusText}`);
    }
    return await resp.json();
}

const completionsURL =
    "https://im-api.proxy.c-space.net/1/ai/782/openai/chat/completions";
const conversation = {
    'model': 'llama3',
    'messages': [],
};

// Ajoute une question à la conversation.
async function ask(prompt) {
    conversation['messages'].push({'content': prompt, 'role': 'user'});
    const resp = await request('POST', completionsURL, {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
    }, conversation);
    const msg = resp['choices'][0]['message'];
    conversation['messages'].push(msg);
    return msg['content'];
}

let level = 0;
const examples = [
    [`\ Écrire le programme python qui correspond à l'algorithme suivant:
La longueur vaut 10. La largeur vaut 5. Calculer et afficher l'aire du
rectangle
`,`Utiliser des variables et la fonction print.`],
    [`\
Écrire le programme python qui correspond à l'algorithme suivant:
Demander l'âge à l'utilisateur.
S'il a plus de 18 ans, afficher qu'il est majeur, sinon afficher qu'il est
mineur.
`, `Il ne doit contenir qu'un if et un else.`],
    [`\
Écrire le programme python qui correspond à l'algorithme suivant:
Demander l'âge à l'utilisateur.
S'il a moins de 16, afficher qu'il n'a pas le droit de boire d'alcool.
S'il a 16 ans et moins de 18 ans, afficher qu'il a le droit de boire du vin et
de la bière.
Sinon afficher qu'il a le droit de boire de l'alcool.
`, `Il doit contenir un elif.`],
    [`\
Écrire le programme python qui correspond à l'algorithme suivant:
Initialiser une variable compte_a_rebours à 10.
Tant que compte_a_rebours est plus grand que 0, afficher la valeur de
compte_a_rebours.
Soustraire 1 à compte_a_rebours.
Afficher 'BOOM'.
`, `Utiliser une boucle while.`],
        [`\
Écrire le programme python qui correspond à l'algorithme suivant:
Afficher les nombres de 1 à 50.
`, `Utiliser for i in range(n) avec un seul paramètre. Ne pas demander \
d'afficher des lettres.`]
];

await domLoaded;

const question = document.querySelector('#question pre');
const feedback = document.querySelector('#feedback');

const correct = document.querySelector('#correct');
const newQuestion = document.querySelector('#newQuestion');
const help = document.querySelector('#help');

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
    question.replaceChildren(text("Génération d'une nouvelle question..."));
    const [ex, constraint] = examples[level];
    const q = await ask(`\
Génère un autre exercice du même genre que l'exemple suivant sans mentionner \
la condition dans l'énoncé, mais sois créatif ou pas.

${ex}

Cet exercice doit suivre la condition suivante: ${constraint}
Ne pas résoudre l'exemple et transmettre juste l'énoncé de l'exercice sans autre
commentaire.`);
    feedback.classList.add('hidden');
    question.replaceChildren(text(q));
}

correct.addEventListener('click', async () => {
    await blocking(async () => {
        // Obtient le code de l'utilisateur à partir de l'éditeur.
        const [editor, _] = findEditor(document.querySelector('#editor'));
        const code = editor.state.doc.toString();

        // Demande la correction de la réponse.
        const fb = await ask(`\
Si le code est vide, répondre "Tu n'as pas donné de réponse." \
Sans s'occuper de la gestion des erreurs et des fautes d'orthographe, le code \
contient-il des erreurs de syntaxe, d'exécution ou de logique?

${code}

Si un cas a été traité dans le if ou un elif précédent, il n'a pas besoin \
d'être répété, ce n'est donc pas une erreur.
Dans la boucle for i in range(n), la boucle s'effectue de 0 à (n-1).
S'il y a des erreurs, explique-les, mais ne donne pas la solution, sinon\
renvoie seulement ok et rien d'autre.\
`);
        if (fb === "ok") {
            feedback.querySelector('pre').replaceChildren("Correct!");
            feedback.classList.remove('hidden');
            if (!mistakeMade) {
                level += 1;
                conversation['messages'] = [];
            }
            if (level >= examples.length) {
                question.replaceChildren(text("Bravo, tu as terminé!"));
                newQuestion.disabled = correct.disabled = help.disabled = true;
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
        const helpResp = await ask(`\
Donne la solution de l'exercice en expliquant comment faire sans mentionner la \
condition.
`);

        feedback.querySelector('pre').replaceChildren(text(helpResp));
        feedback.classList.remove('hidden');

    });
    correct.disabled = true;
});

let mistakeMade = false;

await generateQuestion();
correct.disabled = newQuestion.disabled = help.disabled = false;
</script>

Site d'entrainement d'écriture de programme en Python.

```{code-block} text
:name: question
```

```{code-block} text
:name: feedback
:class: hidden
```

<button id="correct" class="tdoc-button" disabled>Corriger</button>
<button id="newQuestion" class="tdoc-button" disabled>Nouvelle question</button>
<button id="help" class="tdoc-button" disabled>Aide</button>

```{exec} python
:name: editor
:editable:
:style: max-height: 25rem
# Écrire le code ici...
```

