# Copyright 2024 Caroline Blank <caro@c-space.org>
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

import asyncio
import enum
import math

from tdoc import core, svg


class White(enum.StrEnum):
    king = '\u2654'
    queen = '\u2655'
    rook = '\u2656'
    bishop = '\u2657'
    knight = '\u2658'
    pawn = '\u2659'


class Black(enum.StrEnum):
    king = '\u265a'
    queen = '\u265b'
    rook = '\u265c'
    bishop = '\u265d'
    knight = '\u265e'
    pawn = '\u265f'


def color(piece):
    return (White if piece.icon.text in White
            else Black if piece.icon.text in Black else None)


class Icon:
    def __init__(self, board, container, x, y, icon):
        self.board, self.container, self.icon = board, container, icon
        board.children.append(self)
        self.container.add(icon)
        self.move(x, y)

    def move(self, x, y):
        self.x, self.y = x, y
        self.icon.x, self.icon.y = self.board.center(x, y)

    def remove(self):
        self.board.children.remove(self)
        self.container.children.remove(self.icon)


class Board:
    def __init__(self, width, height, cell=50):
        self.width, self.height, self.cell = width, height, cell
        self.children = []
        # The "Segoe UI Emoji" font that is present in the font-family inherited
        # from <body> causes the pawn to look weird. So we have to replace the
        # whole list.
        self.image = svg.Image(self.cell * width, self.cell * height, style="""
            display: block;
            margin: 0 auto;
            overflow: visible;
            box-sizing: content-box;
            border: 4px solid var(--pst-color-text-base);
            user-select: none;
            -webkit-user-select: none;
            stroke: transparent;
            fill: var(--pst-color-text-base);
            text-anchor: middle;
            dominant-baseline: central;
            font-family: -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                "Noto Sans", "Liberation Sans", Arial, sans-serif;
        """)
        board = self.image.group()
        for x in range(width):
            for y in range(height):
                cx, cy = self.cell * x, self.cell * (height - 1 - y)
                board.rect(cx, cy, self.cell, self.cell,
                           style=f'opacity: {0.2 if (x + y) % 2 == 0 else 0}')
        self.spots = self.image.group(style=f"""
            font-size: {0.5 * self.cell}px;
            fill: var(--pst-color-danger);
        """)
        self.pieces = self.image.group(style=f'font-size: {self.cell}px;')

    def center(self, x, y):
        return (x * self.cell + self.cell // 2,
                (self.height - 1 - y) * self.cell + self.cell // 2)

    def piece(self, piece, x, y):
        return Icon(self, self.pieces, x, y, svg.Text(0, 0, piece))

    def spot(self, text, x, y, scale=1):
        return Icon(self, self.spots, x, y,
                    svg.Text(0, 0, text,
                             style=f'font-size: {0.5 * scale * self.cell}px;'
                             if scale != 1 else None))

    def success(self, text, angle=0):
        x, y = self.image.width / 2, self.image.height / 2
        return self.image.text(x, y, text,
                               style=f"""
            font-size: {2 * self.cell}px;
            fill: var(--pst-color-success);
            transform: rotate({angle}deg);
            transform-origin: {x}px {y}px;
        """)

    def lost(self, text, angle=0):
        x, y = self.image.width / 2, self.image.height / 2
        return self.image.text(x, y, text,
                               style=f"""
            font-size: {2 * self.cell}px;
            fill: var(--pst-color-danger);
            transform: rotate({angle}deg);
            transform-origin: {x}px {y}px;
        """)

    def __iter__(self):
        return iter(self.image)


def add_spots(piece, moves):
    x, y = piece.x, piece.y
    for i, (dx, dy) in enumerate(moves, 1):
        x, y = x + dx, y + dy
        piece.board.spot(str(i), x, y)


_loop = asyncio.get_running_loop()


async def animate(piece, moves, pause=0.1, **kwargs):
    for dx, dy in moves:
        await animate_move(piece, dx, dy, **kwargs)
        if (piece.x < 0 or piece.x > piece.board.width - 1 or piece.y < 0
                or piece.y > piece.board.height - 1):
            return False
        piece_color = color(piece)
        for p in piece.board.children:
            p_color = color(p)
            if (piece_color is not None and p_color is not None
                    and p is not piece and piece.x == p.x and piece.y == p.y):
                if p_color != piece_color:
                    p.remove()
                    await core.render(piece.board)
                    break
                else:
                    return False
        await asyncio.sleep(pause)
    return True


async def animate_move(piece, dx, dy, velocity=2.0, framerate=60):
    start = _loop.time()
    ox, oy = piece.x, piece.y
    dist = math.sqrt(dx * dx + dy * dy)
    while True:
        await asyncio.sleep(1 / framerate)
        t = _loop.time() - start
        a = velocity * t / dist
        if a >= 1: break
        piece.move(ox + a * dx, oy + a * dy)
        await core.render(piece.board)
    piece.move(ox + dx, oy + dy)
    await core.render(piece.board)


async def render_and_check(piece, moves, solution):
    add_spots(piece, solution)
    await core.render(piece.board)
    await animate(piece, moves)
    if moves == solution:
        piece.board.success("Bravo!", -10)
        await core.render(piece.board)

async def render_check_and_take(piece, moves):
    await core.render(piece.board)
    correct_move = await animate(piece, moves)
    if not(correct_move):
        piece.board.lost("Perdu!", -10)
    else:
        is_white = piece.icon.text in White
        all_pieces = True
        for p in piece.board.children:
            if  (p.icon.text in White) != is_white:
                all_pieces = False
        if all_pieces:
            piece.board.success("Bravo!", -10)
    await core.render(piece.board)
