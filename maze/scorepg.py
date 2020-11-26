import pygame
from start.button import Button
pygame.init()

class ScoreEnvironment():
    def __init__(self, score):
        pygame.font.init()
        self.h = 1000
        self.w = 1000
        self.maxxy = 20
        self.fact = self.h//self.maxxy
        self.score=score
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.lstoftext =['Game Complete!', 'Your Score: {}'.format(self.score)]
        self.txtsize =100
        self.myfont1 = pygame.font.SysFont('Impact', self.txtsize)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', self.txtsize)
        self.textsurface1=self.myfont1.render(self.lstoftext[0], True, (255,255,255))
        self.textsurface2=self.myfont2.render(self.lstoftext[1], True, (44, 50, 150))
        self.btnimg1 = "start/genbtnonclick.jpg"
        self.btnimg2 = "start/genbtn.jpg"
        self.returnb = Button(8*self.fact,16*self.fact,6*self.fact,2*self.fact,self.btnimg1, self.btnimg2,(0,0,0),self.screen,'Return to Start')
        self.running = True

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
        #self.screen.blit(self.bgimg,[0,0])
        self.returnb.draw()
        y=50
        self.screen.blit(self.textsurface1,(50, y))
        self.screen.blit(self.textsurface2,(50, y+self.txtsize))
        
        pygame.display.update()