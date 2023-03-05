import pygame
import random

pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Coin Collector")

# Set up the character
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50
character = pygame.Rect(50, WINDOW_HEIGHT - CHARACTER_HEIGHT - 50, CHARACTER_WIDTH, CHARACTER_HEIGHT)

# Set up the obstacles and coins
obstacles = []
coins = []
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
COIN_WIDTH = 20
COIN_HEIGHT = 20
OBSTACLE_GAP = 200
OBSTACLE_SPEED = 5
COIN_SPEED = 3
COIN_RATE = 25

# Load the images
CHARACTER_IMAGE = pygame.image.load("character.png")
OBSTACLE_IMAGE = pygame.image.load("obstacle.png")
COIN_IMAGE = pygame.image.load("coin.png")

# Set up the score
score = 0
font = pygame.font.SysFont(None, 30)

# Set up the game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character.x > 0:
        character.x -= 5
    if keys[pygame.K_RIGHT] and character.x < WINDOW_WIDTH - CHARACTER_WIDTH:
        character.x += 5

    # Spawn obstacles and coins
    if len(obstacles) == 0 or obstacles[-1].x < WINDOW_WIDTH - OBSTACLE_GAP:
        obstacle_rect = pygame.Rect(WINDOW_WIDTH, WINDOW_HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        obstacles.append(obstacle_rect)
    if random.randint(0, COIN_RATE) == 0:
        coin_rect = pygame.Rect(random.randint(0, WINDOW_WIDTH - COIN_WIDTH), 0, COIN_WIDTH, COIN_HEIGHT)
        coins.append(coin_rect)

    # Move obstacles and coins
    for obstacle in obstacles:
        obstacle.x -= OBSTACLE_SPEED
        if obstacle.colliderect(character):
            running = False
    for coin in coins:
        coin.y += COIN_SPEED
        if coin.colliderect(character):
            coins.remove(coin)
            score += 1

    # Remove obstacles and coins that have gone offscreen
    if obstacles and obstacles[0].x < -OBSTACLE_WIDTH:
        obstacles.pop(0)
    if coins and coins[0].y > WINDOW_HEIGHT:
        coins.pop(0)

    # Draw the screen
    window.fill((255, 255, 255))
    window.blit(CHARACTER_IMAGE, character)
    for obstacle in obstacles:
        window.blit(OBSTACLE_IMAGE, obstacle)
    for coin in coins:
        window.blit(COIN_IMAGE, coin)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    window.blit(score_text, (10, 10))
    pygame.display.update()

    # Set the game clock
    clock.tick(60)

pygame.quit()
