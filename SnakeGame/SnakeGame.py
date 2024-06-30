import pygame
import random
import sys

pygame.init()

# Screen settings
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
green = (47, 145, 12)

# Load and scale images
background_image = pygame.image.load('SnakeGame/background.jpg')
apple_image = pygame.image.load('SnakeGame/apple.png')
apple_image = pygame.transform.scale(apple_image, (40, 40))  # Resize apple image to 40x40 pixels

# Fonts
font_big = pygame.font.SysFont(None, 48)
font_small = pygame.font.SysFont(None, 36)

# Constants for the game
apple_size = 40  # The size of the apple

# Initialize the snake
def init_game():
    global snake_pos, snake_direction, food_pos, food_spawn, score, game_over_flag
    snake_pos = [[100, 50], [90, 50], [80, 50]]
    snake_direction = 'RIGHT'
    food_pos = [random.randrange(0, (width - apple_size) // 10) * 10,
                random.randrange(0, (height - apple_size) // 10) * 10]
    food_spawn = True
    score = 0
    game_over_flag = False

# Drawing functions
def draw_snake(snake_pos):
    colors = [green, orange, black]  # List of colors
    for index, pos in enumerate(snake_pos):
        color = colors[index % 3]  # Cycle through the three colors
        pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], 15, 15))

def draw_food(food_pos):
    screen.blit(apple_image, (food_pos[0], food_pos[1]))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def show_start_menu():
    run_menu = True
    while run_menu:
        screen.blit(background_image, (0, 0))
        draw_text('Snake Game', font_big, black, screen, width//2, height//3)
        draw_text('Press [SPACE] to start', font_small, black, screen, width//2, height//2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_menu = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def show_game_over_menu(score):
    run_menu = True
    while run_menu:
        screen.blit(background_image, (0, 0))
        draw_text('Game Over!', font_big, black, screen, width//2, height//3)
        draw_text(f'Your score: {score}', font_small, black, screen, width//2, height//2)
        draw_text('Press [P] to play again', font_small, black, screen, width//2, 2*height//3)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    run_menu = False
                    init_game()
                    run_game()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def run_game():
    global snake_direction, food_pos, score
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'
                elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_UP and snake_direction != 'DOWN': 
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP': 
                    snake_direction = 'DOWN'
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        head_x, head_y = snake_pos[0]
        if snake_direction == 'RIGHT':
            head_x += 10
        elif snake_direction == 'LEFT':
            head_x -= 10
        elif snake_direction == 'UP':
            head_y -= 10
        elif snake_direction == 'DOWN':
            head_y += 10
        new_head = [head_x, head_y]

        if new_head[0] >= width or new_head[0] < 0 or new_head[1] >= height or new_head[1] < 0 or new_head in snake_pos:
            running = False
            show_game_over_menu(score)
        else:
            snake_pos.insert(0, new_head)
            if new_head[0] >= food_pos[0] and new_head[0] < food_pos[0] + apple_size and new_head[1] >= food_pos[1] and new_head[1] < food_pos[1] + apple_size:
                score += 10
                food_pos = [random.randrange(0, (width - apple_size) // 10) * 10,
                            random.randrange(0, (height - apple_size) // 10) * 10]
            else:
                snake_pos.pop()

        screen.blit(background_image, (0, 0))
        draw_snake(snake_pos)
        draw_food(food_pos)
        draw_score()
        pygame.display.update()
        clock.tick(15)


def draw_score():
    font = pygame.font.SysFont(None, 36)
    score_text = font.render('Score: ' + str(score), True, black)
    screen.blit(score_text, (0, 0))

# Main code
init_game()
show_start_menu()  # Start with the main menu
run_game()  # Start the game loop
