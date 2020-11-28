import pygame
from start.button import Button
from start.CompProjMySQL import fetchscore as fs 
pygame.init()

class LeadEnvironment(): 
    def __init__(self):
        pygame.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        self.headtxt = 'Top 10 On the Leaderboard'
        self.headrow = "{:10s}     {:4s}".format('User Name', 'Score')
        self.headtxtsize = 80
        self.headrowtxtsize = 50
        self.txtsize =40
        self.headfont = pygame.font.SysFont('Impact', self.headtxtsize)
        self.headrowfont = pygame.font.SysFont('Impact', self.headrowtxtsize) 
        self.myfont = pygame.font.SysFont('Comic Sans MS', self.txtsize)
        self.scores= fs()
        self.headsurface = self.headfont.render(self.headtxt, True, (0, 0, 0))
        self.headrowsurface = self.headrowfont.render(self.headrow, True, (44, 0, 105))
        self.textsurfaces=[]
        if self.scores!=None:
            for i in self.scores:
                self.textsurfaces.append(self.myfont.render("{:10s}".format(i[0]), True, (44, 0, 105)))
                self.textsurfaces.append(self.myfont.render("{:>4d}".format(i[1]), True, (44, 0, 105)))
        self.headsize = 100
        self.h = 1000
        self.w = 1000
        self.maxxy = 20
        self.fact = self.h//self.maxxy
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.btnimg1 = "start/genbtnonclick.jpg"
        self.btnimg2 = "start/genbtn.jpg"
        self.returnb = Button(8*self.fact,16*self.fact,6*self.fact,2*self.fact,self.btnimg1, self.btnimg2,(0,0,0),self.screen,'Return to Start')
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
        self.screen.blit(self.headsurface, (10, y))
        y+=self.headtxtsize+50
        self.screen.blit(self.headrowsurface, (10, y))
        y+=self.headrowtxtsize+10
        xleft =10; xright= 300
        cnt=0
        for i in self.textsurfaces:
            if cnt%2==0:
                self.screen.blit(i,(xleft, y))
            else:
                self.screen.blit(i,(xright, y))
                y+=self.txtsize
            cnt+=1
        pygame.display.update()


#pygame.time.delay(200000)
        
