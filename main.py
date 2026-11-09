import random

import pygame

import config
import coords
import engine


NODE_SIDE = 10
WINDOW_SIZE = (config.aspect[0] * NODE_SIDE, config.aspect[1] * NODE_SIDE)


def cell_color(row: int, col: int) -> tuple[int, int, int]:
    """Deterministic color per cell — stable across frames, no flicker."""
    rng = random.Random(hash((row, col)))
    return (rng.randint(165, 255), 0, rng.randint(165, 255))


def render(screen: pygame.Surface, board: list[list[str]]) -> None:
    screen.fill(config.background_color)
    for row, cells in enumerate(board):
        for col, cell in enumerate(cells):
            if cell == config.alive_icon:
                pygame.draw.rect(
                    screen,
                    cell_color(row, col),
                    (col * NODE_SIDE, row * NODE_SIDE, NODE_SIDE, NODE_SIDE),
                )


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()

    board = coords.make_empty_board(config.aspect)
    for x, y in config.alive_at_start:
        coords.Cell(
            board,
            x + config.offset_at_start,
            y + config.offset_at_start,
        ).set_alive(True)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        render(screen, board)
        engine.apply(board, engine.calculate(board))
        pygame.display.flip()
        clock.tick(config.fps)

    pygame.quit()


if __name__ == "__main__":
    main()
