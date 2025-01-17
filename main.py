import pygame
import random


pygame.init()

W = 500
H = 500
FPS = 60
x = W // 2
y = H // 2

r = 20

lives = 3
game_over = False

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
f1 = pygame.font.Font(None, 36)
text1 = f1.render('ПОБЕДА', 1, (180, 0, 0))
text2 = f1.render('ВЫ ПРОИГРАЛИ', 1, (180, 0, 0))
clock = pygame.time.Clock()
pygame.display.set_caption('Tronix')

bonuses = []
bonus_active = False
bonus_timer = 0
bonus_effect = None

paddle_normal_width = paddle_width
ball_speed = (vx, vy)
ball_slowed = False
second_ball_active = False
second_ball_pos = [None, None]
controls_inverted = False
vertical_move_active = False

while True:
    if game_over:
        root.fill((255, 255, 255))
        root.blit(text2, (150, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        exit()

    root.fill((255, 255, 255))
    paddle_rect = pygame.draw.rect(root, (0, 0, 0), (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.draw.circle(root, (0, 70, 225), (x, y), r)

    for block in list_of_blocks:
        pygame.draw.rect(root, (0, 200, 0), block)

    for bonus in bonuses:
        pygame.draw.circle(root, (255, 0, 0), (bonus.centerx, bonus.centery), 10)

    lives_text = f1.render(f'Жизни: {lives}', 1, (0, 0, 0))
    root.blit(lives_text, (10, 10))

    pygame.display.update()

    if len(list_of_blocks) == 0:
        root.fill((255, 255, 255))
        root.blit(text1, (200, 250))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        exit()

    x += vx
    y += vy

    if x - r <= 0 or x + r >= W:
        vx = -vx

    if y - r <= 0:
        vy = -vy

    if paddle_rect.collidepoint(x, y + r):
        vy = -random.randint(1, 5)

    if y - r >= H:
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            x = W // 2
            y = H // 2
            vx = random.randint(-5, 5)
            vy = random.randint(-5, 5)

    keys = pygame.key.get_pressed()

    if not controls_inverted:
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < W - paddle_width:
            paddle_x += paddle_speed
    else:
        if keys[pygame.K_LEFT] and paddle_x < W - paddle_width:
            paddle_x += paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x > 0:
            paddle_x -= paddle_speed

    if vertical_move_active:
        if keys[pygame.K_UP] and paddle_y > 0:
            paddle_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle_y < H - paddle_height:
            paddle_y += paddle_speed

    ball_rect = pygame.Rect(x - r, y - r, r * 2, r * 2)
    for block in list_of_blocks[:]:
        if ball_rect.colliderect(block):
            list_of_blocks.remove(block)
            vy = -vy

            if random.random() < 0.3:
                bonuses.append(pygame.Rect(block.centerx, block.centery, 20, 20))

    for bonus in bonuses[:]:
        bonus.move_ip(0, 5)

        if bonus.colliderect(paddle_rect):
            bonus_effect = random.choice(["increase_paddle", "slow_ball", "vertical_move", "second_ball", "invert_controls"])
            bonuses.remove(bonus)

            bonus_active = True
            bonus_timer = pygame.time.get_ticks()

            if bonus_effect == "increase_paddle":
                paddle_width *= 1.5
            elif bonus_effect == "slow_ball":
                vx /= 2
                vy /= 2
                ball_slowed = True
            elif bonus_effect == "second_ball":
                second_ball_active = True
                second_ball_pos = [x, y]
            elif bonus_effect == "invert_controls":
                controls_inverted = True
            elif bonus_effect == "vertical_move":
                vertical_move_active = True

    if bonus_active and pygame.time.get_ticks() - bonus_timer > 1000:
        bonus_active = False
        if bonus_effect == "increase_paddle":
            paddle_width = paddle_normal_width
        elif bonus_effect == "slow_ball" and ball_slowed:
            vx, vy = ball_speed
            ball_slowed = False
        elif bonus_effect == "second_ball":
            second_ball_active = False
        elif bonus_effect == "invert_controls":
            controls_inverted = False
        elif bonus_effect == "vertical_move":
            vertical_move_active = False

    if second_ball_active:
        pygame.draw.circle(root, (0, 70, 225), (second_ball_pos[0], second_ball_pos[1]), r)
        second_ball_pos[0] += vx
        second_ball_pos[1] += vy

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

    clock.tick(FPS)
