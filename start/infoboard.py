import pygame
from start.button import Button

pygame.init()

class InfoEnvironment(): 
    def __init__(self):
        pygame.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        f=open("start/about.txt", 'r')
        self.textlines = f.readlines()
        self.textsurfaces=[]
        f.close()
        self.txtsize = 20
        self.myfont = pygame.font.SysFont('Comic Sans MS', self.txtsize)
        for i in self.textlines:
            self.textsurfaces.append(self.myfont.render(i.rstrip('\n'), True, (44, 0, 105)))
        self.headsize = 80
        self.h = 700
        self.w = 700
        self.maxxy = 20
        self.fact = self.h//self.maxxy
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.btnimg1 = "start/genbtnonclick.jpg"
        self.btnimg2 = "start/genbtn.jpg"
        self.returnb = Button(6*self.fact,16*self.fact,10*self.fact,2*self.fact,self.btnimg1, self.btnimg2,(0,0,0),self.screen,'Return to Start')
        self.running = True
        self.bgimg = pygame.image.load("start/leaderbg.jfif")
        self.bgimg = pygame.transform.scale(self.bgimg,(self.w,self.h))

    def run(self):
        running=True
        self.draw()
        flag=None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                coord = pygame.mouse.get_pos()
                if self.returnb.intersect(coord):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('True')
                        running=False
                        flag='end'
            if flag!= 'end':
                self.draw()
            
    
    def draw(self):
        #self.screen.fill((0, 200, 150))
        self.screen.blit(self.bgimg,[0,0])
        self.returnb.draw()
        y=10
        for i in self.textsurfaces:
            self.screen.blit(i,(10, y))
            y+=self.txtsize
        pygame.display.update()


#pygame.time.delay(200000)
        
