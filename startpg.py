import pygame, random, time
from start.button import Button
from maze import mainrun
import pygame, sys, random
from pygame.locals import *
from maze.rectangle import Rectangle
import time
from maze.environment import Environment
from maze.wall import Wall
from maze.gem import Gem
from maze.finish import Finish, Finishwall
from maze.gamemap import GameMap
from arushi.gameworking import runcargame as rcg

pygame.init()



class StartEnvironment(): 
    def __init__(self, background):
        pygame.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        self.headsize = 100
        self.h = 1000
        self.w = 1000
        self.maxxy = 20
        self.fact = self.h//self.maxxy
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.startbimg1 = "start/startbtnonclick.jpg"
        self.startbimg2 = "start/startbtnnoclick.jpg"
        self.btnimg1 = "start/genbtnonclick.jpg"
        self.btnimg2 = "start/genbtn.jpg"
        self.headb = Button(6*self.fact,6*self.fact,10*self.fact,3*self.fact,self.btnimg1, self.btnimg2,(0,0,0),self.screen,'Maze',self.headsize)
        self.leadb = Button(8*self.fact,10*self.fact,6*self.fact,2*self.fact,self.btnimg1, self.btnimg2,(0,0,0),self.screen,'Leaderboard')
        self.startb = Button(8*self.fact,13*self.fact,6*self.fact,2*self.fact,self.startbimg1, self.startbimg2,(0,0,0),self.screen,'Start')
        self.quitb = Button(8*self.fact,16*self.fact,6*self.fact,2*self.fact,self.btnimg1, self.btnimg2,(0,0,0),self.screen,'Quit')
        self.running = True
        self.bgimg = pygame.image.load(background)
        self.bgimg = pygame.transform.scale(self.bgimg,(self.w,self.h))
        self.startTime = time.process_time()

    def run(self):
        running=True
        self.draw()
        flag=None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                coord = pygame.mouse.get_pos()
                if self.quitb.intersect(coord):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('True')
                        running=False
                        flag='end'
                elif self.startb.intersect(coord):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        running=False
                        mainrun.runGame()
                        flag='end'
            if flag!= 'end':
                self.draw()
            else:
                pygame.quit()
        pygame.quit()
    
    def draw(self):
        #self.screen.fill((0, 200, 150))
        self.screen.blit(self.bgimg,[0,0])
        self.headb.draw()
        self.leadb.draw()
        self.startb.draw()
        self.quitb.draw()
        pygame.display.update()


#pygame.time.delay(200000)
        
env = StartEnvironment("start/startbg.jpg")
env.run()







