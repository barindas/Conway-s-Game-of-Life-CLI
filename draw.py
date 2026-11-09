import pygame
import config
import coords
import engine
import time
import random

pygame.init()


node_side = 10
size = [x * node_side for x in config.aspect]
screen = pygame.display.set_mode(size)


def get_random(num1: int, num2: int) -> int:
    return random.randint(num1, num2)


board = coords.make_empty_board(config.aspect)
for x, y in config.alive_at_start:
    coords.Node(
        board, x + config.offset_at_start, y + config.offset_at_start
    ).set_alive(True)


def render(board):
    screen.fill(config.background_color)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == config.alive_icon:
                pygame.draw.rect(
                    screen,
                    (get_random(165, 255), 0, get_random(165, 255)),
                    [col * node_side, row * node_side, node_side, node_side],
                )


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("leaving")
            is_running = False

    render(board)
    engine.apply(board, engine.calculate(board))
    pygame.display.flip()
    time.sleep(1 / config.fps)
pygame.quit()
