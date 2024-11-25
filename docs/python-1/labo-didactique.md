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

// Decrypt API credentials.
const token = await decryptSecret(await pageKey('key', 'nMHqoWnA0tvA'), {
    iv: 'WhVOIKndPgFcQp8x',
    data: 'cB2+NNx58sdf5faBu+65lYUit6U2HDWA9Tt110nr+NsHxCc/T9Ael+FrE1qmylZQfB' +
          'isbrRRQg46vAZL76Rk0cGAdWM43A82YImq59xOk5el2EMsRi2VIyVXOswoJbNQ',
});

// Perform a JSON request against an API.
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
`, `Il doit contenir au moins un elif.`],
    [`\
Écrire le programme python qui correspond à l'algorithme suivant:
Initialiser une variable compte_a_rebours à 10.
Tant que compte_a_rebours est plus grand que 0, afficher la valeur de
compte_a_rebours.
Soustraire 1 à compte_a_rebours.
Afficher 'BOOM'.
`, `Utiliser une boucle while.`],
];

await domLoaded;

let correctClicked;
const correct = document.querySelector('#correct');
correct.addEventListener('click', () => {
    if (correctClicked) correctClicked();
});

const question = document.querySelector('#question pre');
const feedback = document.querySelector('#feedback');
while (level < examples.length) {
    // Generate a new question.
    question.replaceChildren(text("Génération d'une nouvelle question..."));
    feedback.classList.add('hidden');
    const [ex, constraint] = examples[level];
    const q = await ask(`\
Génère un autre exercice du même genre que l'exemple suivant.

${ex}

Cet exercice doit suivre la condition suivante: ${constraint}
Ne pas résoudre l'exemple et transmettre juste l'énoncé de l'exercice sans autre
commentaire.`);
    question.replaceChildren(text(q));

    for (;;) {
        // Wait for the user to click "Corriger".
        const {promise, resolve} = Promise.withResolvers();
        correctClicked = resolve;
        correct.disabled = false;
        await promise;
        correct.disabled = true;
        correctClicked = undefined;

        // Get the user's code from the editor.
        const [editor, _] = findEditor(document.querySelector('#editor'));
        const code = editor.state.doc.toString();

        // Request correction of the answer.
        const fb = await ask(`\
Sans s'occuper de la gestion des erreurs et des fautes d'orthographe, le code \
suivant contient-il des erreurs de syntaxe ou de logique?

${code}

S'il y a des erreurs, explique-les, sinon renvoie seulement ok et rien d'autre.\
    `);
        if (fb === "ok") break;
        feedback.querySelector('pre').replaceChildren(text(fb));
        feedback.classList.remove('hidden');
    }

    level += 1;
    conversation['messages'] = [];
}

question.replaceChildren(text("Bravo, tu as terminé!"));
</script>

Site d'entrainement d'écriture de programme en Python.

```{code-block} text
:name: question
```

```{code-block} text
:name: feedback
:class: hidden
```

<!--
Dans cette fenêtre apparaîtront les réponses de l'AI:
1) Les questions, générées par l'IA, posées aux élèves
2) Le feed-back de l'IA par rapport au code écrit par les élèves s'il y a des
erreurs

Lorsque l'élève répond correctement à 2 questions d'un niveau, il passe au
niveau suivant.
Les types de questions par niveau sont définis au préalable et stockés dans une
listes pour pouvoir les envoyer au fur à mesure à l'AI.
Le suvi de la conversation sera effacé lors du passage au niveau supérieur.
-->

<button id="correct" class="tdoc-button" disabled>Corriger</button>

```{exec} python
:name: editor
:editable:
:style: max-height: 25rem
while False:
  print("Hello")
  name
```

<button id="help" class="tdoc-button">Aide</button>

```{code-block} text
Dans cette fenêtre apparaîtra l'aide de l'IA, c'est-à-dire la réponse du code ou
éventuellement comment faire. Lorque les élèves appuyent sur le bouton d'aide,
la réponse ne sera pas comptabilisée comme correcte.
```
