import pygame
import sys
from ball import Ball
from ground import Ground
from enum import Enum
import random

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
ball1 = Ball(SCREEN_WIDTH-100, 100, 20, white)
ball2 = Ball(SCREEN_WIDTH-200, 100, 20, white)
ball3 = Ball(SCREEN_WIDTH-300, 100, 20, white)

ball_array = []

for i in range(0, 50):
    ball_array.append(Ball(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT-100), 20, white))
#ball2 = Ball(SCREEN_WIDTH/4, 0, 100, (42, 67, 29))
ground = Ground(0, SCREEN_HEIGHT-100, SCREEN_WIDTH, 20, (145, 35, 76))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(black)


    for i in ball_array:
        i.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        i.ground_collision(ground)
        i.draw(screen)
        for j in ball_array:
            if i != j:
                i.circle_collision(j)

    # # Main Content
    # ball1.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    # #ball2.update(SCREEN_WIDTH, SCREEN_HEIGHT, ball1)
    # ball1.ground_collision(ground)

    # ball2.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    # #ball2.update(SCREEN_WIDTH, SCREEN_HEIGHT, ball1)
    # ball2.ground_collision(ground)

    # ball3.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    # #ball2.update(SCREEN_WIDTH, SCREEN_HEIGHT, ball1)
    # ball3.ground_collision(ground)
    # #ball2.ground_collision(ground)
    # #ball1.progress_bar(screen, SCREEN_HEIGHT)

    # # Draw objects
    # ball1.draw(screen)
    # ball2.draw(screen)
    # ball3.draw(screen)

    # ball1.circle_collision(ball2)
    # ball1.circle_collision(ball3)
    # ball2.circle_collision(ball1)
    # ball2.circle_collision(ball3)
    # ball3.circle_collision(ball1)
    # ball3.circle_collision(ball2)
    #ball2.draw(screen)
    ground.draw(screen)
    #ground.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
