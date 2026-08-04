import numpy as np
import pygame
import time
import math

pygame.init()
windowSize = 20 #blocks
blockSize = 30 #pixels
window = pygame.display.set_mode((windowSize * blockSize, windowSize * blockSize))
pygame.display.set_caption("Tool")
window.fill((127, 127, 127))
events = pygame.event.get()

field = np.zeros((windowSize, windowSize), dtype= np.bool_)

#colors
c0 = (255, 255, 255)
c1 = (0, 0, 255)
c2 = (0, 255, 0)
c3 = (255, 0, 0)
c4 = (0, 0, 150)
c5 = (150, 50, 0)
c6 = (0, 150, 150)
c7 = (255, 0, 255)
c8 = (0, 0, 0)
colors = [c0, c1, c2, c3, c4, c5, c6, c7, c8]

def addGrid():
    for y in range(0, windowSize):
        for x in range(0, windowSize):
            pygame.draw.rect(window, (0, 0, 0), (y * blockSize, x * blockSize, 1, blockSize))
            pygame.draw.rect(window, (0, 0, 0), (y * blockSize, x * blockSize, blockSize, 1))
            pygame.draw.rect(window, (0, 0, 0), ((y + 1) * blockSize - 1, x * blockSize, 1, blockSize))
            pygame.draw.rect(window, (0, 0, 0), (y * blockSize, (x + 1) * blockSize - 1, blockSize, 1))

def getKey():
    pos = -1, -1
    events = pygame.event.get()
    update = False
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                field.fill(False)
    return pos

def getNeighbors(x, y):
    neighbors = -1
    for ly in range(-1, 2):
        for lx in range(-1, 2):
            if field[y + ly, x + lx]:
                neighbors += 1
    return neighbors

def renderField():
    for y in range(0, windowSize):
        for x in range(0, windowSize):
            if field[y, x]:
                pygame.draw.rect(window, colors[getNeighbors(x, y)], (x * blockSize, y * blockSize, blockSize, blockSize))

def checkIfInGroup():
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for y in range(0, windowSize):
        for x in range(0, windowSize):
            if field[y, x]:
                counts[getNeighbors(x, y)] += 1
    val = 0
    for i in counts:
        if i != 0:
            if val == 0:
                val = i
            elif val != i:
                return
    window.fill((50, 150, 50))

while True:
    window.fill((127, 127, 127))
    checkIfInGroup()
    renderField()
    addGrid()
    pygame.display.flip()
    x, y = getKey()
    if x >= 0:
        field[int(y / blockSize), int(x / blockSize)] = not field[int(y / blockSize), int(x / blockSize)]