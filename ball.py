# 1 meter = 1 units
import pygame
import math

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = 10
        self.velocity_y = 0
        self.acceleration_y = 9.8
        self.acceleration_x = 1
    
        self.last_time = pygame.time.get_ticks()
        

    def update(self, screen_width, screen_height, direction, circle):
        if direction == "right":
            self.x += .5
            self.y += .5
        elif direction == "left":
            self.x -= .5
            self.y -= .5
        #self.y += self.velocity_y
        # self.border_collision_detection(screen_width, screen_height)
        self.circle_collision(circle)
        #self.allow_gravity()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def allow_gravity(self):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.last_time >= 1:
            # Execute your code here
            print("1 millisecond has passed")
            self.velocity_y += self.acceleration_y / 1000
        
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
        live_distance = abs(math.sqrt(((circle.x - self.x)**2) + ((circle.y - self.y)**2)))
        reference_distance = self.radius + circle.radius
        if live_distance < reference_distance:
            self.color = (189, 222, 12)
            print("collided")
        else:
            print("not collided")
            self.color = (211, 211, 211)
    
        
