from typing import NamedTuple
import config


class Changes(NamedTuple):
    to_kill: set[tuple[int, int]]
    to_birth: set[tuple[int, int]]


def count_neighbors(board: list[list[str]], x: int, y: int) -> int:
    rows, cols = len(board), len(board[0])
    n = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r, c = y + dr, x + dc
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == config.alive_icon:
                n += 1
    return n


def calculate(board: list[list[str]]) -> Changes:
    to_kill: set[tuple[int, int]] = set()
    to_birth: set[tuple[int, int]] = set()

    for y in range(len(board)):
        for x in range(len(board[0])):
            n = count_neighbors(board, x, y)
            alive = board[y][x] == config.alive_icon
            if alive and n in (2, 3):
                continue
            if alive:
                to_kill.add((x, y))
            elif n == 3:
                to_birth.add((x, y))

    return Changes(to_kill, to_birth)


def apply(board: list[list[str]], changes: Changes) -> None:
    for x, y in changes.to_kill:
        board[y][x] = config.none_icon
    for x, y in changes.to_birth:
        board[y][x] = config.alive_icon


def render(board: list[list[str]]) -> None:
    for row in board:
        print("".join(row))
