import pygame
import random

pygame.init()

W = 500
H = 500
FPS = 60
x = W // 2
y = H // 2
r = 20

# Случайные скорости по осям x и y
vx = random.randint(-5, 5)
vy = random.randint(-5, 5)

root = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption('Tronix')

while True:
    root.fill((255, 255, 255))

    # Рисуем шарик
    pygame.draw.circle(root, (0, 70, 225), (x, y), r)

    # Изменяем положение шарика
    x += vx
    y += vy

    # Проверяем столкновение с границами экрана и меняем направление движения случайным образом
    if x - r <= 0 or x + r >= W:
        vx = random.randint(-5, 5)
        while vx == 0:  # Обеспечиваем, что скорость не будет равна 0
            vx = random.randint(-5, 5)

    if y - r <= 0 or y + r >= H:
        vy = random.randint(-5, 5)
        while vy == 0:  # Обеспечиваем, что скорость не будет равна 0
            vy = random.randint(-5, 5)

    # Обновляем экран
    pygame.display.update()

    # Проверяем события
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Ограничиваем FPS
    clock.tick(FPS)
