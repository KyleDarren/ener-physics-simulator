import pygame
import sys
from ball import Ball
from ground import Ground
from enum import Enum

# Initialize Pygame
pygame.init()

# Configure display
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Pygame Program')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up a clock to control the frame rate
clock = pygame.time.Clock()

# Initialize Object
ball1 = Ball(0, 0, 50, white)
ball2 = Ball(SCREEN_WIDTH, SCREEN_HEIGHT, 100, (42, 67, 29))
ground = Ground(0, SCREEN_HEIGHT-100, SCREEN_WIDTH, 20, (145, 35, 76))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(black)

    # Main Content
    ball1.update(SCREEN_WIDTH, SCREEN_HEIGHT, "right", ball2)
    ball2.update(SCREEN_WIDTH, SCREEN_HEIGHT, "left", ball1)

    # Draw objects
    ball1.draw(screen)
    ball2.draw(screen)
    #ground.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
