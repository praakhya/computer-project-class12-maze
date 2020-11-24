'''
This is the main program executor for the maze project.
\@Author Praakhya Avasthi
\@Roll No 42
'''

import pygame, sys, random
from pygame.locals import *
from rectangle import Rectangle
import time
from environment import Environment
from wall import Wall
from gem import Gem
from finish import Finish
from gamemap import GameMap

pygame.init()
map1=[
    "WWWWWWWWWWWWWWWWWWWWW",
    "WEEEEEEEEEEEEEEEEEEEW",
    "WEWWWWWWWWWWWEEWWEWEW",
    "WEEEEEWEEEEEWWEEWEWEW",
    "WEEEEEWEWWWEEWEEEEWEW",
    "WEEEEEWEWEWWEWWWWWWEW",
    "WEEEEEWEWEEEEEEEEEEEW",
    "WWWEEEWEWWWWWWWWWEWWW",
    "WEWEEEWEEEWEEEEEWEEEW",
    "WEWWWEWEEEWEWWWWWEWEW",
    "WEWEEEWEEEWEWEEEEEWEW",
    "WEWEWWWWEEWEWEWWWWWWW",
    "WEWEWEEEEEWEEEEWEEEEW",
    "WEWEWEWWWWWEWWEWEWWWW",
    "EEWEWEEEEEEEWEEWEWEEW",
    "WEWEWWWEWWWWWEEWEEEEE",
    "WEEEWEWEEEEEEEEEEWEEE",
    "WWWWWWWWWWWWWWWWWWWWW"
    ]

map2=[
    'W'*21,
    'WEEEEEEEEEWEEEEEEEEEW',
    'WEWWWWWWWEWEWWWEWWWWW',
    'WEWWEEEEWEWEWEWEEEEEW',
    'WEWWEEEEWEWEWEWWWEEEW',
    'WEWWWWWEWEEEWEEEEEEEW',
    'WEWEEEWEWWWWWWWWWWEEW',
    'WEWWWEWEWEEEWEEEEEEEW',
    'WEEEWEWEEEWEWEWWWWWWW',
    'WEWWWEWEWWWEWEWEEEEEW',
    'WEEEEEEEWEEEWEWEWEWWW',
    'WWWWWEWWWWWWWEWEWEEEW',
    'WEEEEEWEEEEEEEWEWWEEW',
    'WEWEWWWEWWWWWWWEWEEEW',
    'EEWEWEEEWEEEWEEEWEEEW',
    'WEWWWEWWWEWEWEWEWEEEE',
    'WEWEEEEEEEWEEEWEWEEEE',
    'W'*21
]

gm1 = GameMap(map1,"nightbg.jpg","neontile.png", "neongem.png",(255, 110, 199))
gm1.run()

pygame.init()
gm2 = GameMap(map2,"winterlandscape.png","brick1x1.jpg", "gems.png", (20,20,20), gm1.env.score)
gm2.run()
chosenmap=random.choice([gm1, gm2])





"""

cnvh = 1000
cnvw = 1000
maxx = 21
maxy=18
fact = min(cnvw//maxx, cnvh//maxy)
env = Environment(cnvw, cnvh, "winterlandscape.png","brick1x1.jpg", "brick1x1.jpg", "gems.png", fact)
fin = Finish(int(20*fact), int(15*fact), 1*fact, 2*fact, env)
walls=[]
'''
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
'''


vars1 = [
"WWWWWWWWWWWWWWWWWWWWW",
"WEEEEEEEEEEEEEEEEEEEW",
"WEWWWWWWWWWWWEEWWEWEW",
"WEEEEEWEEEEEWWEEWEWEW",
"WEEEEEWEWWWEEWEEEEWEW",
"WEEEEEWEWEWWEWWWWWWEW",
"WEEEEEWEWEEEEEEEEEEEW",
"WWWEEEWEWWWWWWWWWEWWW",
"WEWEEEWEEEWEEEEEWEEEW",
"WEWWWEWEEEWEWWWWWEWEW",
"WEWEEEWEEEWEWEEEEEWEW",
"WEWEWWWWEEWEWEWWWWWWW",
"WEWEWEEEEEWEEEEWEEEEW",
"WEWEWEWWWWWEWWEWEWWWW",
"EEWEWEEEEEEEWEEWEWEEW",
"WEWEWWWEWWWWWEEWEEEEE",
"WEEEWEWEEEEEEEEEEWEEE",
"WWWWWWWWWWWWWWWWWWWWW"
]



y=0
w=10
h=10
for i in range(len(vars1)):
    for j in range(len(vars1[i])):
        if vars1[i][j]=='W':
            env.addWall(Wall(j*fact, i*fact, 1*fact, 1*fact, env))
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
            
            
"""       
