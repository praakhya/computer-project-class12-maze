import pygame


class Ball():
    def __init__(self, x, y, radius, color, env, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.env = env
        self.speed = speed
        
    def moveLeft(self):
        self.x = self.x-self.speed
    def moveRight(self):
        self.x = self.x+self.speed
    def moveUp(self):
        self.y = self.y-self.speed
    def moveDown(self):
        self.y = self.y+self.speed 
    def draw(self):
        pygame.draw.circle(self.env.screen, self.color, (self.x, self.y), self.radius) 

            
            
        
