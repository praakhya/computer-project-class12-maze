import pygame


class Wall():
    def __init__(self, x, y, w, h,env):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.col = (150,250,230)
        self.blinkcol =(150,230,250)
        self.env = env
    def draw(self):
        pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))
        tileimg = pygame.transform.scale(self.env.tilevimg, (self.w, self.h))
        if self.w>self.h:
            tileimg = pygame.transform.scale(self.env.tilehimg, (self.w, self.h))
        self.env.screen.blit(tileimg,(self.x,self.y))
    '''            
    def blink(self):
        pygame.draw.rect(self.env.screen, self.blinkcol, (self.x, self.y, self.w, self.h))
        pygame.display.update()
        pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))
    '''
 