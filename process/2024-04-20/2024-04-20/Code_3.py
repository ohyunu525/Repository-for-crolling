import pygame
from pygame.locals import Rect
import sys
import sys,os
import pygame as pg
import heapq 
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

def astar(m, start, goal):
    open_list = []
    closed_list = set()
    came_from = {}
    
    heapq.heappush(open_list, (0, start))
    
    g_score = {start: 0}
    f_score = {start: h(start, goal)}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path
        
        closed_list.add(current)
        
        for neighbor in get_neighbors(current):
            if neighbor in closed_list:
                continue
                
            tentative_g_score = g_score[current] + 1
            if neighbor not in [i[1] for i in open_list]:
                heapq.heappush(open_list, (f_score.get(neighbor, float('inf')), neighbor))
            elif tentative_g_score >= g_score.get(neighbor, 0):
                continue
                
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + h(neighbor, goal)

def get_neighbors(cell):
    x, y = cell
    neighbors = [(x+dx, y+dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < 451 and 0 <= neighbor[1] < 504]

SURFACE = pygame.display.set_mode((1920, 1080))
UIImage = pygame.image.load("UI.png")
UI = UIImage.get_rect()
lR = Rect(275, 0, 127, 1080)
lRcolor = (0, 0, 0)
rR = Rect(1516, 0, 127, 1080)
rRcolor = (0, 0, 0)
marine = Rect(960, 540, 20, 20)
mrCol = (255, 0, 0)

start = (marine.x, marine.y)
goal = (0, 0)  # Placeholder, you should set this to the destination cell.

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
        msPos = pygame.mouse.get_pos()
        setDestination()
        goal = Des  # Update goal to the clicked position
        path = astar(SURFACE, start, goal)
        if path:
            for cell in path:
                pygame.draw.rect(SURFACE, (0, 0, 255), Rect(cell[0], cell[1], 20, 20))
    pygame.display.update()