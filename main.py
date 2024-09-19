import pygame

pygame.init()

W = 500
H = 500
FPS = 60
x = W // 2
y = H // 2
r = 20
root = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption('Tronix')
root.fill((255, 255, 255))
pygame.display.update()

while True:
    root.fill((255, 255, 255))
    pygame.draw.circle(root, (0, 70, 225), (x, y), r)
    if x == 500 and y == 500:
        x += 1
        y += 1
    elif x != 0 and y != 0:
        x -= 1
        y -= 1
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            pygame.quit()


clock.tick(FPS)
