# -*- coding:utf-8 -*-
import pygame
import time
import random
import sys

size=(800, 600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

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

    class Zmey():
        def __init__(self, xpos, ypos, filename):
            self.xpos = xpos
            self.ypos = ypos
            self.bitmap = pygame.image.load(filename)
        def render(self):
            screen.blit(self.bitmap, (self.xpos * 40 + 2,self.ypos * 40 + 2))

    screen.fill((0, 0, 0))
    draw_setka()
    pygame.display.flip()

pygame.quit()