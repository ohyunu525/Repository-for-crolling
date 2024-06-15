#from lib2to3.pgen2.tokenize import _Coord
from typing import List, Tuple, Callable
import pygame
from pygame.locals import Rect
import sys
import sys,os
import pygame as pg
import heapq 
import math
import time

pygame.init()

size = [744, 558]
Coord = Tuple[int, int]
d_row = (-1, 0, 1, 0)
d_col = (0, 1, 0, -1)
matrix = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
def get_euclidean_distance(pq1: Coord, pq2: Coord) -> float:
    p1, q1 = pq1
    p2, q2 = pq2

    return math.sqrt((p1 - p2) ** 2 + (q1 - q2) ** 2)

def is_vaild(vis: List[List[bool]], row: int, col: int) -> bool:
    h = len(matrix)
    w = len(matrix[0])

    if not (0 <= row < h and 0 <= col < w):
        return False
    
    if matrix[row][col] == 0 or matrix[row][col] == 2:
        return False

    if vis[row][col]:
        return False

    return True

def A_star(dest: Coord):
    global d_row
    global d_col

    h = len(matrix)
    w = len(matrix[0])
    
    heuristic_cost = [[float("inf")] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if(matrix[i][j] == 1):
                heuristic_cost[i][j] = round(get_euclidean_distance((i, j), dest))
                
    row = SCVPos[0]
    col = SCVPos[1]
    dest_y, dest_x = dest
    
    vis = [[False] * w for _ in range(h)]

    heap = []
    heapq.heappush(heap, (heuristic_cost[row][col] + 0, row, col))
    
    total_cost = 0
    
    came_from = []
    
    while heap and (row, col) != (dest_y, dest_x):
        total_cost, row, col = heapq.heappop(heap)
        
        depth = total_cost - heuristic_cost[row][col]

        for i in range(4):
            adjy = row + d_row[i]
            adjx = col + d_col[i]

            if is_vaild(vis, adjy, adjx):
                vis[adjy][adjx] = True
                total_cost = heuristic_cost[adjy][adjx] + depth + 1
                came_from.append(((row, col), (adjy, adjx)))
                heapq.heappush(heap, (total_cost, adjy, adjx))
                
    from_y, from_x = came_from[-1][0]
    paths = []

    for i in range(len(came_from) - 1, -1, -1):
        from_coord, to_coord = came_from[i]
        to_y, to_x = to_coord

        if from_y == to_y and from_x == to_x:
            from_y, from_x = from_coord
            paths.insert(0, to_coord)
    print(paths)
    return paths
    
def makeGrid():
    for i in range(0, 37):
        pygame.draw.line(SURFACE, (0, 0, 0), (i*20, 0), (i*20,558))
    for i in range(0, 27):
        pygame.draw.line(SURFACE, (0, 0, 0), (0, i*20), (744, i*20))
        
    for i in range(0, 27):
        for j in range(0, 37):
            if(matrix[i][j] == 0):
                obstacle = Rect(j * 20, i * 20, 20, 20)
                obCol = (0, 0, 0)
                pygame.draw.rect(SURFACE, obCol, obstacle)
            if(matrix[i][j] == 2):
                mineral = Rect(j*20, i*20, 20, 20)
                mineralCol = (21, 137, 166)
                pygame.draw.rect(SURFACE, mineralCol, mineral)

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
    x = int(x / 20)
    y = int(y / 20)
    Des = [y, x]
    canMove(Des)
    
def canMove(Des) -> None:
    if(matrix[Des[0]][Des[1]] == 1):
        return
    elif(matrix[Des[0]][Des[1]] == 2):
        Des[0] += 1
    else:
        Des = preDes
SURFACE = pygame.display.set_mode(size)
UIImage = pygame.image.load("UI.png")
UI = UIImage.get_rect()

UIImage = pygame.transform.scale(UIImage, (744, 148))
SCVPos = [0, 0]
SCV = Rect(0, 0, 20, 20)
SCVCol = (255, 0, 0)
preDes = [-1, 0]
mining = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock = pygame.time.Clock()
    clock.tick(60)        
    SURFACE.fill((255, 255, 255))
    makeGrid()
    SURFACE.blit(UIImage, UI)
    pygame.draw.rect(SURFACE, SCVCol, SCV)
    UI.centerx = 558
    UI.bottom = 638
    msClicked = pygame.mouse.get_pressed()
    if(msClicked == (0, 0, 1)):
        msPos = pygame.mouse.get_pos()
        setDestination()
        paths = []
        print(Des)
        print(preDes)        
        if(Des != preDes and matrix[Des[0]][Des[1]] != 0):
            paths= A_star(Des)
            preDes = Des
            for i in range(len(paths)):
                SCV = Rect((paths[i][1])*20, (paths[i][0])*20, 20, 20)
                print((paths[i][1]*20, paths[i][0]*20))
                pygame.draw.rect(SURFACE, SCVCol, SCV)
                time.sleep(0.1)
                pygame.display.update()
            SCVPos[0] = paths[len(paths)-1][0]
            SCVPos[1] = paths[len(paths)-1][1]
    moveX = [-1, 0, 0, 1]
    moveY =  [0, 1, -1, 0]
    touched = False
    mem = 0
    for i in range(4):
        if(SCVPos[1] + moveX[i] >= 0 and SCVPos[0] + moveY[i] >= 0):
            if(matrix[SCVPos[0] + moveY[i]][SCVPos[1] + moveX[i]] == 2):
                mining += 1
                mem = i
                touched = True
                break
                
    if(touched == False):
        mining = 0
    if(mining == 60):
        matrix[SCVPos[0] + moveY[mem]][SCVPos[1] + moveX[mem]] = 1
            
    pygame.display.update()
    
    