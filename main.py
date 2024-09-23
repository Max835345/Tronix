import pygame
import random

pygame.init()

W = 500
H = 500
FPS = 60
x = W // 2
y = H // 2
r = 20

paddle_width = 100
paddle_height = 20
paddle_x = W // 2 - paddle_width // 2
paddle_y = H - paddle_height - 10
paddle_speed = 10

vx = random.randint(-5, 5)
vy = random.randint(-5, 5)

root = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption('Tronix')

while True:
    root.fill((255, 255, 255))
    pygame.draw.circle(root, (0, 70, 225), (x, y), r)
    paddle_rect = pygame.draw.rect(root, (0, 0, 0), (paddle_x, paddle_y, paddle_width, paddle_height))

    x += vx
    y += vy

    if x - r <= 0 or x + r >= W:
        vx = random.randint(-5, 5)

        while vx == 0:
            vx = random.randint(-5, 5)

    if y - r <= 0:
        vy = random.randint(-5, 5)

        while vy == 0:
            vy = random.randint(-5, 5)

    if paddle_rect.collidepoint(x, y + r):
        vy = -random.randint(1, 5)

    if y - r >= H:
        x = W // 2
        y = H // 2
        vx = random.randint(-5, 5)
        vy = random.randint(-5, 5)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed

    if keys[pygame.K_RIGHT] and paddle_x < W - paddle_width:
        paddle_x += paddle_speed
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
