# -*- coding: utf-8 -*-
import pygame
import random

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")
screen = pygame.Surface((800, 600))
done = True # для главного цикла
#рисуем сетку
def draw_setka():
    x = 0
    x_x = 800
    y = 0
    y_y = 600
    for i in range(22):
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y_y), 2)
        x += 40
    x = 0
    for i2 in range(22):
        pygame.draw.line(screen, (255, 255, 255), (x, y), (x_x, y), 2)
        y += 40
#класс героя, элемента хвоста, яблока
class Zmey():
    def __init__(self, xpos, ypos, filename):
        self.xpos = xpos
        self.ypos = ypos
        self.bitmap = pygame.image.load(filename)

    def render(self):
        screen.blit(self.bitmap, (self.xpos * 40 + 2,self.ypos * 40 + 2))
#движение хвоста
def going_hv():
    x = 2
    y = len(list)
    for i in reversed(list[1:]):
            i.xpos, i.ypos = list[y - x].xpos, list[y - x].ypos #каждый кубик (элемент хвоста) получает координаты стоящего перед ним (ближе к голове змейки)
            x += 1
counter = 0 #для будущего счёта
hvost = Zmey(4, 5, 'element.jpg')
hero = Zmey(4, 4, 'element.jpg')
going = '' # для клавиш
list = [hero, hvost] #тут хранится змейка
#движение хвоста змейки
def do_going(going):
    if going == 'left':
        going_hv()
        list[0].xpos -= 1
        if list[0].xpos < 0:
            list[0].xpos = 19
    if going == 'right':
        going_hv()
        list[0].xpos += 1
        if list[0].xpos > 19:
            list[0].xpos = 0
    if going == 'up':
        going_hv()
        list[0].ypos -= 1
        if list[0].ypos < 0:
            list[0].ypos = 15
    if going == 'down':
        going_hv()
        list[0].ypos += 1
        if list[0].ypos > 15:
            list[0].ypos = 0
apple = Zmey(10, 10, 'apple.jpg')
#генерация яблока
def apple_gen(list):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    for i in list:
        if (i.xpos, i.ypos) == (x, y):
            x, y = apple_gen(list)
        else:
            continue
    return x, y
apple.xpos, apple.ypos = apple_gen(list) #начальное положение яблока
while done:
    some_x = list[len(list) - 1].xpos #если бедет захвачено яблоко, добавленной части хвоста передаётся это значение по Х
    some_y = list[len(list) - 1].ypos # --//-- по У
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            # Выясняем какая именно кнопка была нажата
            if event.key == pygame.K_LEFT:
                going = 'left'
            if event.key == pygame.K_RIGHT:
                going = 'right'
            if event.key == pygame.K_UP:
                going = 'up'
            if event.key == pygame.K_DOWN:
                going = 'down'
    do_going(going) #передаем новые координаты змейки
    #если съедено яблоко
    if list[0].xpos == apple.xpos and list[0].ypos == apple.ypos:
        counter += 1
        list.append(Zmey( some_x, some_y, 'element.jpg'))
        apple.xpos, apple.ypos = apple_gen(list)
    screen.fill((0, 0, 0))
    draw_setka()
    #отрисовка змейки через цикл
    for i in list:
        i.render()
    apple.render()
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(300)