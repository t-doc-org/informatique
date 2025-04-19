// Copyright 2024 Caroline Blank <caro@c-space.org>
// SPDX-License-Identifier: CC-BY-NC-SA-4.0

'use strict';
(() => {
    const debug = false;
    let core = tdoc.import('tdoc/core.js').then(m => { core = m; });
    let quizz = tdoc.import('tdoc/quizz.js').then(m => { quizz = m; });

    // Add a quizz question checking responses against the keys of "results".
    // Keys whose value is true are accepted. Keys with a string value display
    // that value as a hint. If a response is not found in "results", "def" is
    // used as the result.
    tdoc.question = tdoc.when(quizz, (script, prompt, results, def) => {
        return quizz.question(script, prompt, resp => {
            return results[resp.replaceAll(' ', '').toLowerCase()] ?? def;
        });
    });

    // Get the content of the last `max` rows of the given column.
    function getPrev(table, column, max) {
        let prev = [];
        for (const td of core.qsa(table, `tbody td:nth-child(${column})`)) {
            prev.push(td.textContent);
        }
        return prev.slice(-max);
    }

    // Generate a random integer within an inclusive range.
    function randomInt(min, max) {
        return Math.floor(min + Math.random() * (max - min + 1));
    }

    // Generate a random binary message, avoiding repetitions.
    function randomBinary(bits, table, column) {
        const prev = getPrev(table, column, 1 << (bits - 1));
        let msg, msgStr;
        for (;;) {
            msg = Math.floor(Math.random() * (1 << bits));
            msgStr = core.toRadix(msg, 2, bits);
            if (!prev.includes(msgStr)) return {msg, msgStr};
        }
    }

    // Generate a random decimal message.
    function randomDecimal(digits) {
        const mag = 10 ** (digits - 1);
        return Math.floor(mag + Math.random() * 9 * mag);
    }

    function addText(row, value) {
        row.appendChild(core.elmt`<td class="text-center">${value}</td>`);
    }

    function addBinarySelect(row, zero, one) {
        return core.qs(row.appendChild(core.elmt`\
<td class="text-center"><select>\
<option></option>\
<option value="0">${zero}</option>\
<option value="1">${one}</option>\
</select></td>`), 'select');
    }

    function addInput(row, button) {
        const input = core.qs(row.appendChild(core.elmt`\
<td>\
<input type="text" autocapitalize="off" autocomplete="off" autocorrect="off"\
 spellcheck="false">\
</td>`), 'input');
        core.on(input).keydown(e => {
            if (e.key === 'Enter' && !e.altKey && !e.ctrlKey
                    && !e.metaKey) {
                e.preventDefault();
                button.click();
            }
        });
        return input;
    }

    // Compute the parity of the given message.
    function parity(msg) {
        let p = 0;
        while (msg !== 0) {
            p ^= msg & 1;
            msg >>= 1;
        }
        return p;
    }

    // Generate quizz questions about parity checking.
    tdoc.quizzParityCheck = tdoc.when(core, quizz, (script, min, max, p) => {
        quizz.genTable(script, (table, row, button) => {
            // Generate a new random message.
            const bits = randomInt(min + 1, max + 1);
            const {msg, msgStr} = randomBinary(bits, table, 1);
            const parityOk = parity(msg) === p;

            // Add the row cells.
            addText(row, msgStr);
            const sel = addBinarySelect(row, "oui", "non");

            function verify() {
                const ok = sel.value === '0' ? true :
                           sel.value === '1' ? false : null;
                const res = ok === parityOk;
                sel.classList.toggle('tdoc-bg-bad', !res);
                if (res) core.enable(false, sel);
                return res;
            }

            return {verify, focus: sel};
        });
    });

    // Generate quizz questions about parity encoding.
    tdoc.quizzParityEncode = tdoc.when(core, quizz, (script, min, max, p) => {
        quizz.genTable(script, (table, row, button) => {
            // Generate a new random message.
            const bits = randomInt(min, max);
            const {msg, msgStr} = randomBinary(bits, table, 1);
            const encoded = core.toRadix((msg << 1) | parity(msg), 2, bits + 1);

            // Add the row cells.
            addText(row, msgStr);
            const input = addInput(row, button);

            function verify() {
                const res = input.value.trim() === encoded;
                input.classList.toggle('tdoc-bg-bad', !res);
                if (res) core.enable(false, input);
                return res;
            }

            return {verify, focus: input};
        });
    });

    // Compute the sum of the digits of the given message.
    function digitSum(msg) {
        let s = 0;
        while (msg !== 0) {
            s += msg % 10;
            msg = Math.floor(msg / 10);
        }
        return s;
    }

    // Compute the Luhn sum of the given message.
    function luhnSum(msg) {
        let s = 0, double = false;
        while (msg !== 0) {
            let d = msg % 10;
            if (double) d *= 2;
            s += d % 10 + Math.floor(d / 10);
            msg = Math.floor(msg / 10);
            double = !double;
        }
        return s;
    }

    // Encode a message such that the given sum has `last` as the least
    // significant digit.
    function sumEncode(msg, fnSum, last = 0) {
        msg *= 10;
        return msg + (10 - fnSum(msg) % 10 + last) % 10;
    }

    function quizzSumCheck(fnSum) {
        return (script, min, max) => {
            quizz.genTable(script, (table, row, button) => {
                // Generate a new random message, with a 0.5 probability of
                // being correct.
                const msg = sumEncode(
                    randomDecimal(randomInt(min, max)), fnSum,
                                  Math.random() < 0.5 ? 0 : randomInt(1, 9));
                const sum = fnSum(msg);
                if (debug) console.log(`${msg} => ${sum}`);

                // Add the row cells.
                addText(row, msg);
                const input = addInput(row, button);
                const sel = addBinarySelect(row, "oui", "non");

                function verify() {
                    let res = input.value.trim() === sum.toString();
                    input.classList.toggle('tdoc-bg-bad', !res);
                    const v = sel.value === '0' ? true :
                              sel.value === '1' ? false : null;
                    const ok = v === (sum % 10 === 0);
                    sel.classList.toggle('tdoc-bg-bad', !ok);
                    res = res && ok;
                    if (res) core.enable(false, input, sel);
                    return res;
                }

                return {verify, focus: input};
            });
        };
    }

    // Generate quizz questions about digit sum checking.
    tdoc.quizzDigitSumCheck = tdoc.when(core, quizz, quizzSumCheck(digitSum));

    // Generate quizz questions about Luhn sum checking.
    tdoc.quizzLuhnSumCheck = tdoc.when(core, quizz, quizzSumCheck(luhnSum));

    function quizzSumEncode(fnSum) {
        return (script, min, max) => {
            quizz.genTable(script, (table, row, button) => {
                // Generate a new random message.
                const msg = randomDecimal(randomInt(min, max));
                const encoded = sumEncode(msg, fnSum);
                if (debug) console.log(`${msg} => ${encoded}`);

                // Add the row cells.
                addText(row, msg);
                const input = addInput(row, button);

                function verify() {
                    let res = input.value.trim() === encoded.toString();
                    input.classList.toggle('tdoc-bg-bad', !res);
                    if (res) core.enable(false, input);
                    return res;
                }

                return {verify, focus: input};
            });
        };
    }

    // Generate quizz questions about digit sum encoding.
    tdoc.quizzDigitSumEncode = tdoc.when(core, quizz, quizzSumEncode(digitSum));

    // Generate quizz questions about digit sum encoding.
    tdoc.quizzLuhnSumEncode = tdoc.when(core, quizz, quizzSumEncode(luhnSum));

    // Hamming-encode the given message.
    function hammingEncode(msg, parityBits) {
        const ebits = (1 << parityBits) - 1;
        const dataBits = ebits - parityBits;
        let parity = 0, encoded = 0, mask = 1 << (dataBits - 1);
        for (let i = 1; i <= ebits; ++i) {
            if ((i & (i - 1)) === 0) continue;
            const bit = (msg & mask) !== 0 ? 1 : 0;
            encoded |= bit << (ebits - i);
            for (let p = 0; p < parityBits; ++p) {
                if ((i & (1 << p)) !== 0) parity ^= bit << p;
            }
            mask >>= 1;
        }
        for (let p = 0; p < parityBits; ++p) {
            const bit = (parity & (1 << p)) !== 0 ? 1 : 0;
            encoded |= bit << (ebits - (1 << p));
        }
        return encoded;
    }

    // Generate quizz questions about Hamming encoding.
    tdoc.quizzHammingEncode = tdoc.when(core, quizz, (script, parityBits) => {
        const {enable, qs, qsa, toRadix} = core;
        const dataBits = (1 << parityBits) - parityBits - 1;
        quizz.genTable(script, (table, row, button) => {
            // Generate a new random message.
            const {msg, msgStr} = randomBinary(dataBits, table, 1);
            const encoded = toRadix(
                hammingEncode(msg, parityBits), 2, (1 << parityBits) - 1);
            if (debug) {
                console.log(`${toRadix(msg, 2, dataBits)} => ${encoded}`);
            }

            // Add the row cells.
            addText(row, msgStr);
            for (let i = 0; i < parityBits; ++i) addBinarySelect(row, "0", "1");
            const input = addInput(row, button);

            function verify() {
                let res = true;
                for (const [p, s] of qsa(row, 'select').entries()) {
                    const ok = encoded[(1 << p) - 1] === s.value;
                    res = res && ok;
                    s.classList.toggle('tdoc-bg-bad', !ok);
                }
                const ok = input.value.trim() === encoded;
                input.classList.toggle('tdoc-bg-bad', !ok);
                res = res && ok;
                if (res) enable(false, ...qsa(row, 'select, input'));
                return res;
            }

            return {verify, focus: qs(row, 'select')};
        });
    });

    // Hamming-decode the given encoded message.
    function hammingDecode(encoded, parityBits) {
        const ebits = (1 << parityBits) - 1;
        const dataBits = ebits - parityBits;
        let error = 0;
        for (let i = 1; i <= ebits; ++i) {
            for (let p = 0; p < parityBits; ++p) {
                const bit = (encoded & (1 << (ebits - i))) !== 0 ? 1 : 0;
                if ((i & (1 << p)) !== 0) error ^= bit << p;
            }
        }
        let corrected = encoded;
        if (error !== 0) corrected ^= 1 << (ebits - error);
        let decoded = 0;
        let shift = dataBits - 1;
        for (let i = 1; i <= ebits; ++i) {
            if ((i & (i - 1)) === 0) continue;
            if ((corrected & (1 << (ebits - i))) !== 0) decoded |= 1 << shift;
            shift -= 1;
        }
        return {error, corrected, decoded};
    }

    // Generate quizz questions about Hamming encoding.
    tdoc.quizzHammingDecode = tdoc.when(core, quizz, (script, parityBits) => {
        const {enable, qs, qsa, toRadix} = core;
        const ebits = (1 << parityBits) - 1;
        const dataBits = ebits - parityBits;
        quizz.genTable(script, (table, row, button) => {
            // Generate a new random message.
            const {msg, msgStr} = randomBinary(ebits, table, 1);
            const dec = hammingDecode(msg, parityBits);
            if (debug) {
                console.log(`\
${toRadix(msg, 2, ebits)} => ${toRadix(dec.corrected, 2, ebits)}`);
            }

            // Add the row cells.
            addText(row, msgStr);
            for (let i = 0; i < parityBits; ++i) {
                addBinarySelect(row, "correcte", "fausse");
            }
            const inputs = [];
            for (let i = 0; i < 3; ++i) inputs.push(addInput(row, button));

            function verify() {
                let res = true;
                for (const [p, s] of qsa(row, 'select').entries()) {
                    const bit = s.value === '0' ? 0 :
                                s.value === '1' ? 1 : null;
                    const ok = ((dec.error >> p) & 1) === bit;
                    res = res && ok;
                    s.classList.toggle('tdoc-bg-bad', !ok);
                }
                const want = [
                    dec.error.toString(),
                    toRadix(dec.corrected, 2, ebits),
                    toRadix(dec.decoded, 2, dataBits),
                ];
                for (const [i, input] of inputs.entries()) {
                    let v = input.value.trim();
                    if (i === 0 && v === '') v = '0';
                    const ok = v === want[i].toString();
                    input.classList.toggle('tdoc-bg-bad', !ok);
                    res = res && ok;
                }
                if (res) enable(false, ...qsa(row, 'select, input'));
                return res;
            }

            return {verify, focus: qs(row, 'select')};
        });
    });
})();
