import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
orange = (244, 132, 12)
black = (23, 0, 38)
red = (213, 50, 80)
green = (0, 255, 0)

# Configure display
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock
clock = pygame.time.Clock()

# Snake parameters
block_size = 10
snake_speed = 15

# Fonts
font = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 25)

def message(msg, color):
    msg_render = font.render(msg, True, color)
    window.blit(msg_render, [width / 6, height / 3])

def game():
    game_over = False
    game_close = False

    x_snake = width / 2
    y_snake = height / 2

    x_snake_change = 0
    y_snake_change = 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_close = True
                    game_over = True
                # Arrow keys handling
                if event.key == pygame.K_LEFT and x_snake_change != block_size:
                    x_snake_change = -block_size
                    y_snake_change = 0
                elif event.key == pygame.K_RIGHT and x_snake_change != -block_size:
                    x_snake_change = block_size
                    y_snake_change = 0
                elif event.key == pygame.K_UP and y_snake_change != block_size:
                    y_snake_change = -block_size
                    x_snake_change = 0
                elif event.key == pygame.K_DOWN and y_snake_change != -block_size:
                    y_snake_change = block_size
                    x_snake_change = 0

        if x_snake >= width or x_snake < 0 or y_snake >= height or y_snake < 0:
            game_close = True

        x_snake += x_snake_change
        y_snake += y_snake_change
        window.fill(black)
        pygame.draw.rect(window, green, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(x_snake)
        snake_head.append(y_snake)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for x in snake_body[:-1]:
            if x == snake_head:
                game_close = True

        for x in snake_body:
            pygame.draw.rect(window, orange, [x[0], x[1], block_size, block_size])

        # Display score
        score = score_font.render("Score: " + str(snake_length - 1), True, orange)
        window.blit(score, [0, 0])

        pygame.display.update()

        if x_snake == food_x and y_snake == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game()
