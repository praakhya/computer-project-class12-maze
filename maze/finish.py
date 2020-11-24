import pygame
class Finish():
    def __init__(self, x,y,w,h,env):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.col = (200,50,30)
        self.env = env
    def draw(self):
        pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))   
