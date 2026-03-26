import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
DINO_Y = 300
CACTUS_WIDTH = 50
CACTUS_HEIGHT = 70
GRAVITY = 0.5
JUMP_STRENGTH = 10
SCORE = 0

# Load images
cloud_image = pygame.image.load('cloud.png')
dino_image = pygame.image.load('dino.png')
cactus_image = pygame.image.load('cactus.png')
bird_image = pygame.image.load('bird.png')
font = pygame.font.SysFont('Arial', 30)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chrome-style Dino Runner')

# Game variables
class Dino:
    def __init__(self):
        self.image = dino_image
        self.rect = self.image.get_rect(center=(100, DINO_Y))
        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -JUMP_STRENGTH

    def update(self):
        if self.is_jumping:
            self.velocity_y += GRAVITY
            self.rect.y += self.velocity_y
            if self.rect.y >= DINO_Y:
                self.rect.y = DINO_Y
                self.is_jumping = False

class Cactus:
    def __init__(self):
        self.image = cactus_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH, DINO_Y))

    def update(self, speed):
        self.rect.x -= speed

def show_score(score):
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

# Game loop
clock = pygame.time.Clock()
run = True
speed = 5
cacti = []

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump()

    # Update
    screen.fill((135, 206, 250))  # Sky color
    dino.update()
    if random.randint(0, 100) < 2:
        cacti.append(Cactus())
    for cactus in cacti:
        cactus.update(speed)
        if cactus.rect.x < 0:
            cacti.remove(cactus)
            SCORE += 1
        if dino.rect.colliderect(cactus.rect):
            run = False  # Game Over

    # Draw
    screen.blit(dino.image, dino.rect)
    for cactus in cacti:
        screen.blit(cactus.image, cactus.rect)
    show_score(SCORE)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
