import pygame
pygame.font.init()
pygame.init()

class Button():
    def __init__(self, x,y,w,h,btnimg1, btnimg2,txtcol,screen,txt, txtsize=50):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.txtcol =txtcol
        self.txt=txt
        self.textx = self.x; self.texty = self.y
        self.btnimg1 = pygame.image.load(btnimg1)
        self.btnimg1 = pygame.transform.scale(self.btnimg1,(self.w,self.h))
        self.btnimg2 = pygame.image.load(btnimg2)
        self.btnimg2 = pygame.transform.scale(self.btnimg2,(self.w,self.h))
        self.btnimg = self.btnimg2
        self.screen = screen
        self.txtsize = txtsize
        self.myfont = pygame.font.SysFont('Impact', self.txtsize)
        self.adjusted = False
        self.textsurface = self.myfont.render(self.txt, True, self.txtcol)
        
    def draw(self):
        self.rect = list(self.textsurface.get_rect())
        self.wgap = (self.w - self.rect[2])/2
        self.hgap = (self.h - self.rect[3])/2
        if self.adjusted==False:
            if self.wgap>0:
                self.textx += self.wgap
            elif self.wgap==0:
                self.w +=2
                self.textx+=1
            else:
                self.x -=self.wgap
                self.w+=(self.wgap)*2

            if self.wgap>0:
                self.texty += self.hgap
            elif self.wgap==0:
                self.y -=1
                self.h +=2
            else:
                self.y -= self.hgap
                self.h += (self.hgap)*2
            self.adjusted=True
        #self.screen.draw.text(self.txt, (self.x, self.y), owidth=1.5, ocolor=self.btncol, color=self.txtcol)  
        
        #pygame.draw.rect(self.screen, self.btncol, (self.x, self.y, self.w, self.h)) 
        self.screen.blit(self.btnimg,[self.x,self.y])
        self.screen.blit(self.textsurface,(self.textx, self.texty))

        '''
        text = font.render("You win!", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
        '''

    def intersect(self,coord):
        x,y=coord
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            self.btnimg =self.btnimg1
            return True
        else:
            self.btnimg = self.btnimg2
            return False





