import pygame
from start.button import Button
from start.CompProjMySQL import fetchscore as fs 
from maze import mainrun
from start.CompProjMySQL import scoreboard as sb
import getpass
from maze.scorepg import ScoreEnvironment
pygame.init()

class ChoiceEnvironment(): 
    def __init__(self):
        pygame.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        self.headtxt = 'Free Play: Choose a level'
        self.headtxtsize = 60
        self.headfont = pygame.font.SysFont('Impact', self.headtxtsize)
        self.scores= fs()
        self.headsurface = self.headfont.render(self.headtxt, True, (0, 0, 0))
        self.headsize = 90
        self.h = 700
        self.w = 700
        self.maxxy = 20
        self.fact = self.h//self.maxxy
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.btnimg1 = "start/genbtnonclick.jpg"
        self.btnimg2 = "start/genbtn.jpg"
        self.maze1img = "start/maze1.png"
        self.maze2img = "start/maze2.png"
        self.flappyimg = "start/flappy.png"
        self.maze1b = Button(1*self.fact,5*self.fact,5*self.fact,5*self.fact,self.maze1img, self.maze1img,(0,0,0),self.screen,'1')
        self.maze2b = Button(7*self.fact,5*self.fact,5*self.fact,5*self.fact,self.maze2img, self.maze2img,(0,0,0),self.screen,'2')
        self.flappybirdb = Button(13*self.fact,5*self.fact,5*self.fact,5*self.fact,self.flappyimg, self.flappyimg,(0,0,0),self.screen,'3')
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
                if self.maze1b.intersect(coord):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            #running=False
                            self.score = mainrun.runMaze1()
                            if self.score == None:
                                self.score=0
                            sb(getpass.getuser(), self.score)
                            self.scoreenv = ScoreEnvironment(self.score,'Return')
                            self.scoreenv.run()
                            self.screen = pygame.display.set_mode((self.w, self.h))
                if self.maze2b.intersect(coord):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            #running=False
                            self.score = mainrun.runMaze2()
                            if self.score == None:
                                self.score=0
                            sb(getpass.getuser(), self.score)
                            self.scoreenv = ScoreEnvironment(self.score, 'Return')
                            self.scoreenv.run()
                            self.screen = pygame.display.set_mode((self.w, self.h))
                if self.flappybirdb.intersect(coord):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            #running=False
                            self.score = mainrun.runFlappy()
                            if self.score == None:
                                self.score=0
                            sb(getpass.getuser(), self.score)
                            self.scoreenv = ScoreEnvironment(self.score,'Return')
                            self.scoreenv.run()
                            self.screen = pygame.display.set_mode((self.w, self.h))
            if flag!= 'end':
                self.draw()
            
    
    def draw(self):
        #self.screen.fill((0, 200, 150))
        self.screen.blit(self.bgimg,[0,0])
        self.returnb.draw()
        self.maze1b.draw()
        self.maze2b.draw()
        self.flappybirdb.draw()
        self.screen.blit(self.headsurface, (10, 10))
        pygame.display.update()


#pygame.time.delay(200000)
        
