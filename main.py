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

list_of_blocks = [
    pygame.Rect(45, 100, 50, 15),
    pygame.Rect(100, 100, 50, 15),
    pygame.Rect(155, 100, 50, 15),
    pygame.Rect(210, 100, 50, 15),
    pygame.Rect(265, 100, 50, 15),
    pygame.Rect(320, 100, 50, 15),
    pygame.Rect(375, 100, 50, 15),
    pygame.Rect(430, 100, 50, 15),
    pygame.Rect(45, 120, 50, 15),
    pygame.Rect(100, 120, 50, 15),
    pygame.Rect(155, 120, 50, 15),
    pygame.Rect(210, 120, 50, 15),
    pygame.Rect(265, 120, 50, 15),
    pygame.Rect(320, 120, 50, 15),
    pygame.Rect(375, 120, 50, 15),
    pygame.Rect(430, 120, 50, 15),
    pygame.Rect(45, 140, 50, 15),
    pygame.Rect(100, 140, 50, 15),
    pygame.Rect(155, 140, 50, 15),
    pygame.Rect(210, 140, 50, 15),
    pygame.Rect(265, 140, 50, 15),
    pygame.Rect(320, 140, 50, 15),
    pygame.Rect(375, 140, 50, 15),
    pygame.Rect(430, 140, 50, 15),
    pygame.Rect(45, 160, 50, 15),
    pygame.Rect(100, 160, 50, 15),
    pygame.Rect(155, 160, 50, 15),
    pygame.Rect(210, 160, 50, 15),
    pygame.Rect(265, 160, 50, 15),
    pygame.Rect(320, 160, 50, 15),
    pygame.Rect(375, 160, 50, 15),
    pygame.Rect(430, 160, 50, 15),
]

vx = random.randint(-5, 5)
vy = random.randint(-5, 5)

root = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption('Tronix')

while True:
    root.fill((255, 255, 255))
    pygame.draw.circle(root, (0, 70, 225), (x, y), r)
    paddle_rect = pygame.draw.rect(root, (0, 0, 0), (paddle_x, paddle_y, paddle_width, paddle_height))

    for block in list_of_blocks:
        pygame.draw.rect(root, (0, 0, 0), block)

    pygame.display.update()

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

    ball_rect = pygame.Rect(x - r, y - r, r * 2, r * 2)
    for block in list_of_blocks[:]:
        if ball_rect.colliderect(block):
            list_of_blocks.remove(block)
            vy = -vy
            break

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
