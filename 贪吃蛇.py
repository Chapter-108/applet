import pygame
import time
import random

pygame.init()

window_x = 1200
window_y = 800

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
purple = pygame.Color(128, 0, 128)
cyan = pygame.Color(0, 255, 255)

colors = [green, red, blue, yellow, purple, cyan]

pygame.display.set_caption('贪吃蛇')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_colors = [random.choice(colors) for _ in range(len(snake_body))]

fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('zhe,shi,fen,shu : ' + str(score), True, color, black)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50, bold=True)
    game_over_surface = my_font.render('If youre a vegetable,prsctice more', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    if change_to == 'UP':
        direction = 'UP'
    if change_to == 'DOWN':
        direction = 'DOWN'
    if change_to == 'LEFT':
        direction = 'LEFT'
    if change_to == 'RIGHT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    snake_colors.insert(0, random.choice(colors))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
        snake_colors.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    game_window.fill(black)

    for i, pos in enumerate(snake_body):
        pygame.draw.rect(game_window, snake_colors[i], pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10 or snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(20)
