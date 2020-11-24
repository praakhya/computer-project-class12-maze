
import pygame, sys, random
from pygame.locals import *
from rectangle import Rectangle
import time
from environment import Environment
from wall import Wall
from gem import Gem
from finish import Finish
pygame.init()

class GameMap():
    def __init__(self, map, bgimg, obstacleimg, pointimg, ballcol, score=0):
        self.cnvh = 1000
        self.cnvw = 1000
        self.maxx = 21
        self.maxy=18
        self.bgimg = bgimg
        self.obstacleimg = obstacleimg
        self.pointimg = pointimg
        self.ballcol = ballcol
        self.fact = min(self.cnvw//self.maxx, self.cnvh//self.maxy)
        self.env = Environment(self.cnvw, self.cnvh, self.bgimg, self.obstacleimg, self.obstacleimg, self.pointimg, self.fact, self.ballcol, score)
        self.fin = Finish(int(20*self.fact), int(15*self.fact), 1*self.fact, 2*self.fact, self.env)
        #walls=[]
        self.map = map

    def run(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j]=='W':
                    self.env.addWall(Wall(j*self.fact, i*self.fact, 1*self.fact, 1*self.fact, self.env))
        print('done')
        self.env.addFinish(self.fin)
        self.env.run()