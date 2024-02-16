import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    food_head = []
    food_head.append(foodx)
    food_head.append(foody)
    food = []
    food.append(food_head)
    
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_KP6:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_KP8:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_KP2:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_KP7:
                    y1_change = -snake_block
                    x1_change = -snake_block
                    diagonalsnakespeed = 15
                elif event.key == pygame.K_KP3:
                    y1_change = snake_block
                    x1_change = snake_block
                elif event.key == pygame.K_KP1:
                    y1_change = snake_block
                    x1_change = -snake_block
                    diagonalsnakespeed = 15
                elif event.key == pygame.K_KP9:
                    y1_change = -snake_block
                    x1_change = snake_block
                    diagonalsnakespeed = 15
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(yellow)
        for t in food:
            pygame.draw.rect(dis, red, [t[0], t[1], snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
 
        pygame.display.update()
        g = 0
        for f in food:
            if x1 == f[0] and y1 == f[1]:
                
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                food1x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                food1y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foodH1 = []
                foodH2 = []
                foodH1.append(foodx)
                foodH1.append(foody)
                foodH2.append(food1x)
                foodH2.append(food1y)
                food.append(foodH1)
                food.append(foodH2)
                del food[g]
                Length_of_snake += 1
            g = g + 1 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
