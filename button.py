import pygame
pygame.font.init()
pygame.init()

class Button():
    def __init__(self, x,y,w,h,btncol,txtcol,screen,txt):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.txtcol =txtcol
        self.txt=txt
        self.btncol = btncol
        self.screen = screen
        self.myfont = pygame.font.SysFont('Impact', 50)
    def draw(self):
        pygame.draw.rect(self.screen, self.btncol, (self.x, self.y, self.w, self.h))   
        textsurface = self.myfont.render(self.txt, False, (0, 0, 0))
        self.screen.blit(textsurface,(self.x,self.y))
    def intersect(self,coord):
        x,y=coord
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            return True




