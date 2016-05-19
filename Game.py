#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, os, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
f = open('Snake.txt', 'r')

print(f.read())



clock = pygame.time.Clock()
center = 300
SIZE = [center*2, center*2]
cell_size = 20
screen = pygame.display.set_mode(SIZE)

cell = pygame.Surface((cell_size, cell_size))

zmei_pos = []
for i in range(5):
    zmei_pos.append([center, center-cell_size*i])

zmei_cell = pygame.Surface((cell_size, cell_size))
zmei_cell.fill(BLACK)

apple_cell = pygame.Surface((cell_size, cell_size))
apple_cell.fill(GREEN)
apple_pos = [random.randrange(0, center*2, cell_size), random.randrange(0, center*2, cell_size)]
dirs = 0
done = False
move = False
while not done:
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            zmei_cell.fill(BLACK)
            if event.key == pygame.K_UP:
                dirs = 1
            elif event.key == pygame.K_RIGHT:
                dirs = 2
            elif event.key == pygame.K_DOWN:
                dirs = 3
            elif event.key == pygame.K_LEFT:
                dirs = 4

    screen.fill(WHITE)
    if dirs > 0:
        last = zmei_pos[len(zmei_pos)-1].copy()
        for i in range(len(zmei_pos)-1, 0, -1):
            zmei_pos[i] = zmei_pos[i-1].copy()

        if dirs == 1:
            zmei_pos[0][1] -= cell_size
        elif dirs == 2:
            zmei_pos[0][0] += cell_size
        elif dirs == 3:
            zmei_pos[0][1] += cell_size
        elif dirs == 4:
            zmei_pos[0][0] -= cell_size
        # dirs = 0
        for i in range(len(zmei_pos)-1, 0, -1):
            if zmei_pos[0][0] == zmei_pos[i][0] and zmei_pos[0][1] == zmei_pos[i][1]:
                dirs = 0
                zmei_cell.fill(RED)

        if zmei_pos[0][0] == apple_pos[0] and zmei_pos[0][1] == apple_pos[1]:
            apple_pos = [random.randrange(0, center*2, cell_size), random.randrange(0, center*2, cell_size)]
            zmei_pos.append(last)


    for zmei_i in zmei_pos:
        screen.blit(zmei_cell, zmei_i)
    screen.blit(apple_cell, apple_pos)
    pygame.display.flip()

    dt = clock.tick(5)

pygame.quit()