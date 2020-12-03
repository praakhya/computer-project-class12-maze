import pygame
pygame.font.init()
pygame.init()

class Button(): #This class is used to create buttons everywhere in the program
    def __init__(self, x,y,w,h,bimg1, bimg2,txtcol,screen,txt, txtsize=50):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.txtcol =txtcol
        self.txt=txt
        self.textx = self.x; self.texty = self.y
        self.btnimg1 = pygame.image.load(bimg1)
        self.btnimg1 = pygame.transform.scale(self.btnimg1,(self.w,self.h))
        self.btnimg2 = pygame.image.load(bimg2)
        self.btnimg2 = pygame.transform.scale(self.btnimg2,(self.w,self.h))
        self.btnimg = self.btnimg2
        self.screen = screen
        self.txtsize = txtsize
        self.myfont = pygame.font.SysFont('Impact', self.txtsize) 
        self.adjusted = False
        self.textsurface = self.myfont.render(self.txt, True, self.txtcol) #this is the text on the button
        self.rect = list(self.textsurface.get_rect())
        self.text_width, self.text_height = self.myfont.size(txt)
        self.wgap = (self.w - self.text_width)/2
        self.hgap = (self.h - self.text_height)/2
        
    def draw(self): #this will draw all the elements of the button on the screen given
        if self.adjusted==True:
            pass
        else: 
            if self.wgap>0:
                self.textx += self.wgap
            elif self.wgap==0:
                self.w +=10
                self.textx+=1

            if self.hgap>0:
                self.texty += self.hgap
            elif self.hgap==0:
                self.y -=10
                self.h +=20

            self.adjusted=True
        #self.screen.draw.text(self.txt, (self.x, self.y), owidth=1.5, ocolor=self.btncol, color=self.txtcol)  
        
        #pygame.draw.rect(self.screen, self.btncol, (self.x, self.y, self.w, self.h)) 
        self.screen.blit(self.btnimg,[self.x,self.y])
        self.screen.blit(self.textsurface,(self.textx, self.texty))

    def intersect(self,coord): #it will check if the given coordinate will come within the area of the button or not
        x,y=coord
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            self.btnimg =self.btnimg1
            return True
        else:
            self.btnimg = self.btnimg2
            return False

    



