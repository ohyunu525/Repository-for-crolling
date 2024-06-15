import pygame
import sys

pygame.init()

SURFACE = pygame.display.set_mode((1920, 1080))
UI = pygame.image.load("UI_1.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    SURFACE.fill((255, 255, 255))
    pygame.display.update()