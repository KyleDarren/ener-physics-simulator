import pygame
import sys
from ball import Ball
from ground import Ground
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

# Container array for created balls
ball_array = []

# Create ball function
def spawn_balls(existing_balls):
    # Set variables for random x and y
    random_x = random.randint(25, SCREEN_WIDTH-25)
    random_y = random.randint(25, SCREEN_HEIGHT-100)

    # Create a ball
    new_ball = Ball(random_x, random_y, 25, white)

    # Return the created ball if there still no existing balls inside the ball array
    if len(existing_balls) == 0:
        return new_ball
    elif len(existing_balls) > 0:
        # Check if the created circle overlaps an existing circle
        overlap = any(new_ball.check_overlap(existing_ball) for existing_ball in existing_balls)
        # Return the created ball if and only if it doesn't overlap any existing balls
        if not overlap:
            return new_ball
        # If it does overlap, return None
        return None


for i in range(0, 20):
    new_ball = None
    while new_ball is None:  
        # While the ball is None it continually assign the spawn_balls() function in the new_ball variable 
        # until it returns a Ball Object and terminates the while loop
        new_ball = spawn_balls(ball_array) # It continually return None as long as thers is an overlap
    # If it return a Ball object and not None, it will be appended into the ball_arrau
    ball_array.append(new_ball) 
    
# Initialize ground
ground = Ground(0, SCREEN_HEIGHT-100, SCREEN_WIDTH, 20, (145, 35, 76))

# Main game loop
running = True
while running:
    # Handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(black)

    # Draw and update each of the created balls
    for i in ball_array: # Iterate the ball array
        for j in ball_array: # By each iteration, iterate the ball array again,
            if j != i: # If the ball object is not equal on itself, call the circle_collision method
                i.circle_collision(j)
        i.update(SCREEN_WIDTH, SCREEN_HEIGHT)
        i.ground_collision(ground)
        i.draw(screen)

    # Draw the ground
    ground.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
