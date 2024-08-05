import pygame
import sys
from ball import Ball
from enum import Enum

# 1 meter = 100 units

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Pygame Program')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up a clock to control the frame rate
clock = pygame.time.Clock()

# Initialize Object
ball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 15, white)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(black)

    # Main Content
    ball.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Draw a white rectangle
    ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
