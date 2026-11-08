import pygame
import coords

def draw_nodes(screen, array):
    for y in array:
        for x in y:
            if y[x] == 1:
                pygame.draw.circle(
                    screen,
                    (125,125,125),
                    (array.index(y) * 80 + 30, y.index(x) * 80 + 30),
                    30
                )

