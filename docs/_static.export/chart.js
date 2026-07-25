// Copyright 2026 Caroline Blank <caro@c-space.org>
// SPDX-License-Identifier: CC-BY-NC-SA-4.0

const [core, {chart, render}] =
  await tdoc.import('tdoc/core.js', 'tdoc/chart.js');

const sets = new Map([
  [1, [0b0, 0b1]],
  [2, [0b00, 0b10, 0b01, 0b11]],
  [3, [0b000, 0b100, 0b010, 0b001, 0b110, 0b101, 0b011, 0b111]],
  [4, [0b0000,
       0b1000, 0b0100, 0b0010, 0b0001,
       0b1100, 0b1010, 0b1001, 0b0110, 0b0101, 0b0011,
       0b1110, 0b1101, 0b1011, 0b0111,
       0b1111]],
  [5, [0b00000,
       0b10000, 0b01000, 0b00100, 0b00010, 0b00001,
       0b11000, 0b10100, 0b10010, 0b10001, 0b01100, 0b01010, 0b01001,
       0b00110, 0b00101, 0b00011,
       0b11100, 0b11010, 0b11001, 0b10110, 0b10101, 0b10011, 0b01110,
       0b01101, 0b01011, 0b00111,
       0b11110, 0b11101, 0b11011, 0b10111, 0b01111,
       0b11111]]
]);

render.vennOperations = async (el, {labels, areas, options}) => {
  const indexes = sets.get(labels.length);
  areas = areas.map(a => new RegExp(a.replaceAll('x', '[01]')));
  const colors = []
  for (const v of indexes) {
    let color = '#fff';
    for (const area of areas) {
      if (area.test(core.toRadix(v, 2, labels.length))) {
        color = '#ddd';
        break;
      }
    }
    colors.push(color);
  }
  const venn = await render.venn;
  return await venn(el, [{
    data: {
      labels,
      datasets: [{data: new Array(2 ** labels.length - 1).fill({})}],
    },
    options: {
      borderWidth: 1, borderColor: '#888',
      backgroundColor: colors.slice(1),
      layout: {padding: 30},
      hover: {mode: ''},
      scales: {
        x: {ticks: {font: {size: 12}}},
        y: {ticks: {font: {size: 16}}},
      },
      plugins: {
        background: {color: colors[0]},
        tooltip: false,
        legend: {display: false},
      },
    },
  }, {options}]);
};
