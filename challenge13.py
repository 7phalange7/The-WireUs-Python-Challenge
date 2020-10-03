# challenge 13

import pygame
pygame.init()

win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("challenge 13")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            run = False

pygame.quit()
