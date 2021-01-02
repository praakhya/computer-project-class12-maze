import pygame   
class Gem():
    def __init__(self, x, y, env):
        self.x = x
        self.y = y
        self.env = env
        self.w = env.gemw
        self.h = env.gemh
        self.score = 5
    def draw(self):
        self.env.screen.blit(self.env.gemimg, (self.x, self.y))