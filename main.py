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

def spawn_balls(existing_balls):
    random_x = random.randint(25, SCREEN_WIDTH-25)
    random_y = random.randint(25, SCREEN_HEIGHT-100)
    new_ball = Ball(random_x, random_y, 25, white)

    if len(existing_balls) == 0:
        print("helk")
        return new_ball
    elif len(existing_balls) > 0: 
        overlap = any(new_ball.check_overlap(existing_ball) for existing_ball in existing_balls)
        if not overlap:
            return new_ball
        return None


for i in range(0, 20):
    new_ball = None
    while new_ball is None:  # Keep trying until a new ball is successfully created
        new_ball = spawn_balls(ball_array)
    ball_array.append(new_ball) 
    

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
        for j in ball_array:
            if j != i:
                i.circle_collision(j)
        i.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        i.ground_collision(ground)
        i.draw(screen)

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
