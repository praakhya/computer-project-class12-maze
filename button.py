import pygame

class Button():
    def __init__(self, x, y, w, h,env):
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Impact', 100)
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.col = (0,0,0)
        self.env = env
    def draw(self):
        pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))
        textsurface3 = self.myfont.render('Quit', False, (200, 200, 200))
        self.env.screen.blit(textsurface3 , (self.x,self.y-20))