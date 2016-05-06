# -*- coding:utf-8 -*-
import pygame
import time
import random
import sys


size=(800, 600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
clock=pygame.time.Clock()

white=(255, 255, 255)
green=(0, 255, 0)
black=(0, 0, 0)
red=(255, 0, 0)
blue=(0, 0, 255)


def draw_setka():
    x = 0
    x_x = 800
    y = 0
    y_y = 800
    for i in range(22):
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y_y), 2)
        x += 40
    x = 0
    for i2 in range(22):
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x_x, y), 2)
        y += 40


done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True


    screen.fill((0, 0, 0))
    draw_setka()
    pygame.display.flip()

pygame.quit()