import pygame


class Wall():
    def __init__(self, x, y, w, h,env):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.env = env
    def draw(self):
        tileimg = pygame.transform.scale(self.env.tileimg, (self.w, self.h))
        self.env.screen.blit(tileimg,(self.x,self.y))