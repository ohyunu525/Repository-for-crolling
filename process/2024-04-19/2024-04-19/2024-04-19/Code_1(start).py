import pygame
from pygame.locals import Rect
import sys
import sys,os
import pygame as pg
pygame.init()

def makeGrid():
    for i in range(0, 451):
        pygame.draw.line(SURFACE, (0, 0, 0), (i*20, 0), (i*20, 1080))
    for i in range(0, 504):
        pygame.draw.line(SURFACE, (0, 0, 0), (0, i*20), (1920, i*20))
        
def setDestination():
    x = msPos[0]
    y = msPos[1]
    x /= 20
    x = int(x)
    x *= 20
    y /= 20
    y = int(y)
    y *= 20
    des = Rect(x, y, 20, 20)
    desCol = (0, 255, 0)
    pygame.draw.rect(SURFACE, desCol, des)
    global Des
    Des = (x, y)

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    
    return abs(x1-x2) + abs(y1-y2)

def astar(m):
    start = (Des[0], Des[1])
    
SURFACE = pygame.display.set_mode((1920, 1080))
UIImage = pygame.image.load("UI.png")
UI = UIImage.get_rect()
lR = Rect(275, 0, 127, 1080)
lRcolor = (0, 0, 0)
rR = Rect(1516, 0, 127, 1080)
rRcolor = (0, 0, 0)
marine = Rect(960, 540, 20, 20)
mrCol = (255, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    SURFACE.fill((255, 255, 255))
    makeGrid()
    SURFACE.blit(UIImage, UI)
    pygame.draw.rect(SURFACE, lRcolor, lR)
    pygame.draw.rect(SURFACE, rRcolor, rR)
    pygame.draw.rect(SURFACE, mrCol, marine)
    UI.centerx = 960
    UI.bottom = 924
    msClicked = pygame.mouse.get_pressed()
    if(msClicked == (0, 0, 1)):
        global msPos
        msPos = pygame.mouse.get_pos()
        setDestination()
    pygame.display.update()

if __name__ == "__main__":
    main()