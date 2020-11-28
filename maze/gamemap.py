
import pygame, sys, random
from pygame.locals import *
from maze.rectangle import Rectangle
import time
from maze.environment import Environment
from maze.wall import Wall
from maze.gem import Gem
from maze.finish import Finish, Finishwall
pygame.init()

class GameMap():
    def __init__(self, map, bgimg, obstacleimg, pointimg, ballcol, score=0):
        self.cnvh = 700
        self.cnvw = 700
        self.maxx = 21
        self.maxy=18
        self.bgimg = bgimg
        self.obstacleimg = obstacleimg
        self.pointimg = pointimg
        self.ballcol = ballcol
        self.fact = min(self.cnvw//self.maxx, self.cnvh//self.maxy)
        self.env = Environment(self.cnvw, self.cnvh, self.bgimg, self.obstacleimg, self.obstacleimg, self.pointimg, self.fact, self.ballcol, score)
        self.fin = Finish(int(20*self.fact), int(15*self.fact), 1*self.fact, 2*self.fact, self.env)
        self.finwall = Finishwall(int(20*self.fact), int(15*self.fact), 2*self.fact, self.obstacleimg, self.env)
        #walls=[]
        self.map = map

    def run(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j]=='W':
                    self.env.addWall(Wall(j*self.fact, i*self.fact, 1*self.fact, 1*self.fact, self.env))
        print('done')
        self.env.addFinish(self.fin)
        self.env.addFinishwall(self.finwall)
        self.env.run()
