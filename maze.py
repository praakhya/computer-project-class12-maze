'''
This is the main program executor for the maze project.
\@Author Praakhya Avasthi
\@Roll No 42
'''

import pygame, sys, random, winsound
from pygame.locals import *
from rectangle import Rectangle
import time
from environment import Environment
from wall import Wall
from gem import Gem
from finish import Finish

pygame.init()
cnvh = 1000
cnvw = 1000
maxx = 21
maxy=18
fact = min(cnvw//maxx, cnvh//maxy)
env = Environment(cnvw, cnvh, "winterlandscape.png","brickh.jpg", "brickv.jpg", "gems.png", fact)
fin = Finish(int(20*fact), int(15*fact), 1*fact, 2*fact, env)
walls=[]
vars1 = [
[0,0,21,1],
[0,0,1,14],
[0,17,21,1],
[0,15,1,3],
[20,0,1,15],
[2,2,11,1],
[16,1,1,3],
[0,2,1,3],
[0,4,1,4],
[0,7,2,1],
[6,2,1,10],
[15,2,2,1],
[18,2,1,4],
[12,2,1,2],
[13,3,1,3],
[13,5,6,1],
[8,4,3,1],
[8,4,1,4],
[8,7,9,1],
[10,5,2,1],
[2,7,1,9],
[2,9,3,1],
[4,11,4,1],
[4,11,1,7],
[4,15,3,1],
[10,7,1,7],
[6,13,5,1],
[8,13,1,1],
[8,15,5,1],
[12,13,1,3],
[12,13,2,1],
[16,7,1,3],
[12,9,5,1],
[12,9,1,3],
[18,7,2,1],
[18,9,1,3],
[14,11,6,1],
[15,11,1,5],
[17,13,3,1],
[17,13,1,2],
[17,16,1,2]]



##var = [
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW",
##"WWWWWWWWWWWWWWWWWWWWW"
##]



y=0
w=10
h=10
for i in vars1:
    env.addWall(Wall(i[0]*fact, i[1]*fact, i[2]*fact, i[3]*fact, env))
print('done')
env.addFinish(fin)
env.run()





##    def checkBallCollisionLeft(self,b):
##        collision = False
##        for i in self.walls:
##            min_x = i.x
##            max_x = i.x+i.w
##            min_y = i.y
##            max_y = i.y+i.h
##            bx = b.x - b.radius - b.speed
##            by = b.x + b.radius
##            print('minx: ',min_x, 'maxx: ',max_x, 'miny: ',min_y, 'maxy: ',max_y, 'bx: ', bx, 'by: ', b.y)
##            if bx>min_x and bx<max_x and by>min_y and by<max_y:
##                collision = True
##                break
##        print(collision)
##        return collision
##    
##    def checkBallCollisionRight(self,b):
##        collision = False
##        for i in self.walls:
##            min_x = i.x
##            max_x = i.x+i.w
##            min_y = i.y
##            max_y = i.y+i.h
##            bx = b.x + b.radius + b.speed
##            by = b.y + b.radius
##            print('minx: ',min_x, 'maxx: ',max_x, 'miny: ',min_y, 'maxy: ',max_y, 'bx: ', bx, 'by: ', b.y)
##            if bx>min_x and bx<max_x and by>min_y and by<max_y:
##                collision = True
##                break
##        print(collision)
##        return collision
##    
##    def checkBallCollisionUp(self,b):
##        collision = False
##        for i in self.walls:
##            min_x = i.x
##            max_x = i.x+i.w
##            min_y = i.y
##            max_y = i.y+i.h
##            by = b.y - b.radius - b.speed
##            bx = b.x + b.radius
##            print('minx: ',min_x, 'maxx: ',max_x, 'miny: ',min_y, 'maxy: ',max_y, 'bx: ', b.x, 'by: ', by)
##            if bx>min_x and bx<max_x and by>min_y and by<max_y:
##                collision = True
##                break
##        print(collision)
##        return collision
##    
##    def checkBallCollisionDown(self,b):
##        collision = False
##        for i in self.walls:
##            min_x = i.x
##            max_x = i.x+i.w
##            min_y = i.y
##            max_y = i.y+i.h
##            by = b.y + b.radius + b.speed
##            bx = b.x + b.radius
##            print('minx: ',min_x, 'maxx: ',max_x, 'miny: ',min_y, 'maxy: ',max_y, 'bx: ', b.x, 'by: ', by)
##            if bx>min_x and bx<max_x and by>min_y and by<max_y:
##                collision = True
##                break
##        print(collision)
##        return collision
            
            
        
