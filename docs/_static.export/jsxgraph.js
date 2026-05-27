/* Copyright 2026 Caroline Blank <caro@c-space.org> */
/* SPDX-License-Identifier: CC-BY-NC-SA-4.0 */

export const [{
    attrs, gcd, initBoard, JXG, merge, templates, withAxesLabels,
}] = await tdoc.imports('tdoc/jsxgraph.js');

// Defaults for use on screen media.
attrs.screen = [{
  axis: true, grid: true,
  defaultAxes: {
    x: {ticks: {minorTicks: 1}},
    y: {ticks: {minorTicks: 1}},
  },
  defaults: {
    arrow: {
      strokeWidth: 2, strokeColor: JXG.palette.black,
    },
    circle: {
      strokeWidth: 2, strokeColor: JXG.palette.blue,
      label: {strokeColor: JXG.palette.blue},
    },
    curve: {
      strokeWidth: 2, strokeColor: JXG.palette.blue,
      label: {strokeColor: JXG.palette.blue},
    },
    functiongraph: {
      label: {strokeColor: JXG.palette.blue},
    },
    line: {
      strokeWidth: 1, strokeColor: JXG.palette.black,
    },
    point: {
      size: 1.5,
      strokeWidth: 1, strokeColor: JXG.palette.black,
      fillColor: JXG.palette.black,
    },
  },
}];

// Defaults for use on print media.
attrs.print = [attrs.nonInteractive, {
  axis: true, grid: true,
  defaultAxes: {
    x: {ticks: {insertTicks: false, ticksDistance: 1, minorTicks: 0}},
    y: {ticks: {insertTicks: false, ticksDistance: 1, minorTicks: 0}},
  },
  defaults: {
    curve: {strokeWidth: 2, strokeColor: JXG.palette.black},
    point: {
      name: '', size: 2,
      strokeWidth: 1, strokeColor: JXG.palette.black,
      fillColor: JXG.palette.black,
    },
  },
}];

templates['discrete-cumulative-distribution'] = (el, {
  samples, classes, frequency = true, board = {},
}) => {
  if (samples === undefined) {
    samples = [];
    for (const [v, count] of classes) {
      for (let i = 0; i < count; ++i) samples.push(v);
    }
  }
  samples.sort();
  let min = Infinity, max = -Infinity;
  const data = [[-Infinity, 0]];
  for (const [i, v] of samples.entries()) {
    if (v < min) min = v;
    if (v > max) max = v;
    const last = data[data.length - 1];
    if (v === last[0]) {
      ++last[1];
    } else {
      data.push([v, last[1] + 1]);
    }
  }
  const bounds = [min - 0.16 * (max - min), 1.2,
                  max + 0.05 * (max - min), -0.2];
  if (frequency) {
    for (let i = 1; i < data.length; ++i) data[i][1] /= samples.length;
  } else {
    const maxCnt = data[data.length - 1][1];
    bounds[1] *= maxCnt;
    bounds[3] *= maxCnt;
  }

  function f(x) {
    for (let i = 1; i < data.length; ++i) {
      if (x < data[i][0]) return data[i - 1][1];
    }
    return data[data.length - 1][1];
  }

  return initBoard(el, [
    board.defaults ?? {},
    {
      boundingBox: bounds, keepAspectRatio: false, axis: true,
      zoom: {factorY: 1},
      defaultAxes: {
        x: {
          ticks: {
            insertTicks: true, majorHeight: -1, minorHeight: 10,
            strokeOpacity: 0.25, drawZero: true,
          },
        },
        y: {
          name: '\\[f\\]',
          position: 'fixed', anchor: 'left', anchorDist: '0.08fr',
          ticks: {
            insertTicks: true, majorHeight: -1, minorHeight: 10,
            strokeOpacity: 0.25,
          },
        },
      },
      defaults: {
        functiongraph: {strokeWidth: 3},
        point: {strokeWidth: 1, fixed: true, withLabel: false},
      },
    },
    board.overrides ?? {},
  ], board => {
    board.create('functiongraph',
      [f, min - 0.5 * (max - min), max + 0.5 * (max - min)]);
    for (let i = 1; i < data.length; ++i) {
      const v = data[i][0];
      board.create('point', [v, data[i - 1][1]],
                   {fillColor: JXG.palette.white});
      board.create('point', [v, data[i][1]]);
    }
    board.on('boundingbox', () => {
      const box = board.getBoundingBox(), nbox = [...box];
      nbox[1] = bounds[1];
      nbox[3] = bounds[3];
      if (nbox.some((v, i) => v !== box[i])) board.setBoundingBox(nbox);
    });
  });
};
