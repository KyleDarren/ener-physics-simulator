# 1 meter = 1 units

'''
Problem
    1. Circle Collision Bounce Back Direction
'''
import pygame
import math

class Ball:
    def __init__(self, x, y, radius, color):
        # Set attributes
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = -1
        self.velocity_y = 0
        self.acceleration_y = 9.8
        self.acceleration_x = 1
        self.e = .9

        # This is use for time interal
        self.last_time = pygame.time.get_ticks() # Return a few milliseconds that is negligible
        
    def update(self, screen_width, screen_height):
        self.y += self.velocity_y
        self.x += self.velocity_x
        # self.x += self.velocity_x
        self.border_collision_detection(screen_width, screen_height)
        #self.circle_collision(circle)
        self.allow_gravity()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def allow_gravity(self):
        self.current_time = pygame.time.get_ticks()

        # Check if the current time is a millisecond greater than the last time
        if self.current_time - self.last_time >= 1:
            # Increase the value of velocity based from acceleration
            self.velocity_y += self.acceleration_y / 100
        
            # Update the last_time
            self.last_time = self.current_time

    def border_collision_detection(self, screen_width, screen_height):
        if self.x + self.radius > screen_width:
            self.velocity_x = -self.velocity_x
        elif self.x - self.radius < 0:
            self.velocity_x = -self.velocity_x
        elif self.y + self.radius > screen_height:
            self.velocity_y = -self.velocity_y
        elif self.y - self.radius < 0:
            self.velocity_y = -self.velocity_y

    def circle_collision(self, circle):
        # Calculate the live tdistance
        # This values are dynamic because this is inside a loop
        live_distance = abs(math.sqrt(((circle.x - self.x)**2) + ((circle.y - self.y)**2)))

        # The reference distance is the minimum distance the balls must exceed to be considered uncollided.
        reference_distance = self.radius + circle.radius

        if live_distance < reference_distance:
            # Execute this if the live distance is below the minimum distance
            self.color = (189, 222, 12)
            self.velocity_y = -self.velocity_y
            self.velocity_x = -self.velocity_x
        else:
            self.color = (81, 211, 211)

    def ground_collision(self, ground):
        if self.y + self.radius > ground.y:
            self.y = ground.y - self.radius

            velocity_final = -(self.velocity_y * self.e)

            self.velocity_y = velocity_final
            # My created treshold formula is purely based from data given by testing the balls at different values of coefficient of restitution
            if abs(self.velocity_y) < (10.5714 * ((self.e)**2)) - (12.06 * (self.e)) + 3.7386:  # Approximated Small threshold formula
                self.velocity_y = 0

    def check_overlap(self, circle):
        live_distance = abs(math.sqrt(((circle.x - self.x)**2) + ((circle.y - self.y)**2)))
        reference_distance = self.radius + circle.radius
        return live_distance < reference_distance

    # For Debugging purposes only
    def progress_bar(self, screen, y):
        pygame.draw.rect(screen, self.color, (10, y-150-abs(self.velocity_y*10), 50, abs(self.velocity_y*10)))
        

            
    
        
