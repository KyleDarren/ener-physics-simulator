# 1 meter = 1 units
import pygame
import math

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = -1
        self.velocity_y = 0
        self.acceleration_y = 9.8
        self.acceleration_x = 1
        self.e = .9
    
        self.last_time = pygame.time.get_ticks()
        
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
        
        if self.current_time - self.last_time >= 1:
            # Execute your code here
            #print("1 millisecond has passed")
            self.velocity_y += self.acceleration_y / 100
            
            #print(self.velocity_y)
        
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
            self.velocity_y = -self.velocity_y
            self.velocity_x = -self.velocity_x
            # #self.x = circle.x + abs(self.x - circle.x)
            # if self.velocity_y < 0:
            #     self.y = circle.y + abs(self.y - circle.y)
            # elif self.velocity_y > 0:
            #     self.y = circle.y - abs(self.y - circle.y)
            # elif self.velocity_x < 0:
            #     self.x = circle.x + abs(self.x - circle.x)
            # elif self.velocity_x > 0:
            #     self.x = circle.x - abs(self.x - circle.x)


            
            
            #print("collided")
        else:
            #print("not collided")
            self.color = (211, 211, 211)

    def ground_collision(self, ground):
        if self.y + self.radius > ground.y:
            #print(f"intiial {self.velocity_y}")
            self.y = ground.y - self.radius

            velocity_final = -(self.velocity_y * self.e)
            #print(f"final {velocity_final}")

            self.velocity_y = velocity_final
            if abs(self.velocity_y) < (10.5714 * ((self.e)**2)) - (12.06 * (self.e)) + 3.7386:  # Approximated Small threshold formula
                self.velocity_y = 0

    def check_overlap(self, circle):
        live_distance = abs(math.sqrt(((circle.x - self.x)**2) + ((circle.y - self.y)**2)))
        reference_distance = self.radius + circle.radius
        return live_distance < reference_distance

    def progress_bar(self, screen, y):
        pygame.draw.rect(screen, self.color, (10, y-150-abs(self.velocity_y*10), 50, abs(self.velocity_y*10)))
        

            
    
        
