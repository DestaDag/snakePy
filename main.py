from dis import dis
from email import message
from pickle import TRUE
import time
import pygame
import random

pygame.init()

white = (255,255,255)
black  = (0,0,0)
red = (255,0,0)
yellow = (255,255,102)


size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsams", 35)

def score(scr):
    value = score_font.render("Score "+ str(scr), True, yellow)
    screen.blit(value, [0, 0])

def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], 10, 10])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [int(width/3), int(height/30)])


def game_loop():
    game_over = False
    game_close = False
    
    x = width/2
    y = height/2
    
    snake_list = []
    snake_length = 1

    foodx = int(round(random.randrange(0, width - x) / 10.0) * 10.0)
    foody = int(round(random.randrange(0, height - y) / 10.0) * 10.0)

    x_change = 0
    y_change = 0

    while not game_over:
        while game_close == True:
            screen.fill(white)
            message("game, over Q-quit or C-play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 10
        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, 10, 10])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]

        for item in snake_list[:-1]:
            if item == snake_head:
                game_close = True
        
        snake(snake_list)
        score(snake_length -1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = int(round(random.randrange(0, width - x) / 10.0) * 10.0)
            foody = int(round(random.randrange(0, height - y) / 10.0) * 10.0)
            snake_length += 1
            
            clock.tick(30 + 10)

    pygame.quit()
    quit()


game_loop()