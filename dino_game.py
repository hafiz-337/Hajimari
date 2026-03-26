import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Dinosaur properties
dino_x, dino_y = 50, 300
dino_width, dino_height = 40, 40
dino_color = (0, 255, 0)

# Obstacle properties
obstacle_width, obstacle_height = 20, 40
obstacle_color = (255, 0, 0)
obstacles = []

# Game variables
score = 0
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Logic for creating and moving obstacles
    if random.randint(1, 60) == 1:
        obstacles.append([WIDTH, HEIGHT - obstacle_height])

    for obstacle in obstacles:
        obstacle[0] -= 5
        if obstacle[0] < 0:
            obstacles.remove(obstacle)
            score += 1

    # Drawing everything
    window.fill((255, 255, 255))  # Clear screen
    for obstacle in obstacles:
        pygame.draw.rect(window, obstacle_color, (obstacle[0], HEIGHT - obstacle_height, obstacle_width, obstacle_height))
    
    pygame.draw.rect(window, dino_color, (dino_x, dino_y, dino_width, dino_height))
    pygame.display.update()

pygame.quit()