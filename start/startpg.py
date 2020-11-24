from button import Button
import pygame, sys, random, winsound
from pygame.locals import *
from rectangle import Rectangle
import time
from ball import Ball
from gem import Gem
from finish import Finish
from wall import Wall
pygame.init()

class Environment(): 
    def __init__(self, w, h, background, fact, ):
        pygame.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        self.myfont = pygame.font.SysFont('Impact', 100)
        self.w = w
        self.h = h
        self.fact = fact
        self.ballcol = ballcol
        self.b = Ball(int(0.5*self.fact), int(14.5*self.fact), 0.25*self.fact, self.ballcol,self, 5)
        self.running = True
        self.score=score
        #self.clock = pygame.time.Clock()
        self.walls = []
        self.gems=[]
        self.fin = None
        self.gemw = 50
        self.gemh = 50
        self.wintext=None
        self.losetext=None
        self.maxGems=5
        self.bgimg = pygame.image.load(background)
        self.bgimg = pygame.transform.scale(self.bgimg,(self.w,self.h))
        self.tilehimg = pygame.image.load(tileh)
        self.tilevimg = pygame.image.load(tilev)
        self.gemimg = pygame.image.load(gemimg)
        self.gemimg = pygame.transform.scale(self.gemimg,(self.gemw,self.gemh))
        self.startTime = time.process_time()







screen = pygame.display.set_mode((500, 500))
screen.fill((0, 200, 150))
b = Button(0,0,200,50,(255,255,255),(0,0,0),screen,'Alive')
b.draw()
pygame.display.update()
coord = pygame.mouse.get_pos()
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        coord = pygame.mouse.get_pos()
        if b.intersect(coord) and event.type == pygame.MOUSEBUTTONDOWN:
            print('True')
            running=False
        else:
            print('False')

#pygame.time.delay(200000)
pygame.quit()