import pygame
from maze.rectangle import Rectangle
class Finish():
    def __init__(self, x,y,w,h,env):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.finimg = pygame.image.load("maze/finish.jpg")
        self.finimg = pygame.transform.scale(self.finimg,(self.w,self.h))
        self.env = env
        #self.col = (200,50,30)
        self.env = env
    def draw(self):
        #pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))   
        self.env.screen.blit(self.finimg,[self.x,self.y])

class Finishwall():
    def __init__(self, finx, finy, finh, wallimg, env):
        self.x = finx-10
        self.y = finy
        self.w = 10
        self.h = finh 
        self.finwallimg = pygame.image.load(wallimg)
        self.finwallimg = pygame.transform.scale(self.finwallimg,(self.w,self.h))
        self.env =env
    def draw(self):
        #pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))   
        self.env.screen.blit(self.finwallimg,[self.x,self.y])