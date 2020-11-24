import pygame, sys, random
from pygame.locals import *
from rectangle import Rectangle
import time
from pygame import mixer

class Environment():
    def __init__(self, w, h, background, tileh, tilev, gemimg):
        self.w = w
        self.h = h
        self.running = True
        self.score=0
        #self.clock = pygame.time.Clock()
        self.walls = []
        self.gems=[]
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
        mixer.init()
        mixer.music.load('beep.wav')
        mixer.music.set_volume(0.7)
        
        

    def drawTime(self):
        elapsedTime = time.process_time() - self.startTime
        print(elapsedTime)
        elapsedSeconds = int(elapsedTime % 60)
        elapsedTime = elapsedTime // 60
        elapsedMinutes = int(elapsedTime % 60)
        elapsedTime = elapsedTime // 60
        elapsedHours = int(elapsedTime)
        timeString = "{:02d}:{:02d}:{:02d}".format(elapsedHours, elapsedMinutes, elapsedSeconds)
        textsurface = myfont.render(timeString, False, (0, 0, 0))
        self.screen.blit(textsurface,(self.w - 400,self.h-100))

    def beep(self):
        mixer.music.play()
    

    def run(self):
        self.draw()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_q:
                    self.running = False
            self.spawnGems()     
            if self.expireGame():
                    self.losetext = 'Your Time is Up!'
                    self.running = False
                    self.beep()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                futureball = Rectangle.fromCircle(self.b.x+self.b.speed, self.b.y, self.b.radius)
                if self.finishGame(futureball):
                    self.wintext = 'You Win!'
                    self.running = False
                    self.beep()
                self.handleGems(futureball)
                di, w = self.doesIntersect(futureball) 
                if  not di:
                    b.moveRight()
                else:
                    self.beep()
            elif keys[pygame.K_LEFT]:
                futureball = Rectangle.fromCircle(self.b.x-self.b.speed, self.b.y, self.b.radius)
                self.handleGems(futureball)
                di, w = self.doesIntersect(futureball)
                if  not di:
                    b.moveLeft()
                else:
                    self.beep()
            elif keys[pygame.K_UP]:
                futureball = Rectangle.fromCircle(self.b.x, self.b.y-self.b.speed, self.b.radius)
                self.handleGems(futureball)
                di, w = self.doesIntersect(futureball)
                if  not di:
                    b.moveUp()
                else:
                    self.beep()                        
            elif keys[pygame.K_DOWN]:
                futureball = Rectangle.fromCircle(self.b.x, self.b.y+self.b.speed, self.b.radius)
                self.handleGems(futureball)
                di, w = self.doesIntersect(futureball)
                if  not di:
                    b.moveDown()
                else:
                    self.beep()                        

            
            self.draw()
        #self.clock.tick(60)
        pygame.quit()

    def handleGems(self,futureball):
        gi, g = self.doesIntersectWithGem(futureball)
        if gi:
            self.score+=g.score
            self.removeGem(g)


    def draw(self):
        self.screen = pygame.display.set_mode((self.w,self.h))
        self.screen.blit(self.bgimg,[0,0])
        self.b.draw()
        self.fin.draw()
        for i in self.walls:
            i.draw()
        for j in self.gems:
            j.draw()
        textsurface = myfont.render(str(self.score), False, (0, 0, 0))
        self.screen.blit(textsurface,(10,self.h-100))
        self.drawTime()
        if self.wintext!=None:
            pygame.draw.rect(self.screen,(0, 204, 204 ) , (self.w//2 -150, self.h//2 -100, 500, 120))
            textsurface = myfont.render(self.wintext, False, (0, 0, 0))
            self.screen.blit(textsurface,(self.w//2-100,self.h//2-100))
            pygame.display.update()
            pygame.time.delay(1200)
        if self.losetext!=None:
            pygame.draw.rect(self.screen,(200, 0, 0 ) , (self.w//2 -300, self.h//2 -100, 700, 120))
            textsurface = myfont.render(self.losetext, False, (0, 0, 0))
            self.screen.blit(textsurface,(self.w//2-275,self.h//2-100))
            pygame.display.update()
            pygame.time.delay(1200)
        pygame.display.update()
        
        
    
    def addBall(self, b):
        self.b = b

    def addWall(self, wl):
        self.walls.append(wl)

    def addFinish(self, fin):
        self.fin = fin

    def doesIntersect(self, r):
        for i in self.walls:
            rw = Rectangle(i.x, i.y, i.w, i.h)
            if rw.intersect(r):
                return True,i
        return False,None

    def doesIntersectWithGem(self, r):
        for g in self.gems:
            rw = Rectangle(g.x, g.y, g.w, g.h)
            if rw.intersect(r):
                return True,g
        return False,None

    def removeGem(self, gm):
        self.gems = [g for g in self.gems if g.x != gm.x and g.y != gm.y]

    def addGem(self, gm):
        self.gems.append(gm)
    
    def spawnGems(self):
        num = random.randint(0,100)
        if num==0:
            x,y, posfound = self.findPosition()
            if posfound and len(self.gems)<self.maxGems:
                self.addGem(Gem(x, y, self))
                

    def findPosition(self):
        for i in range(999):
            x= random.randint(0,700)
            y= random.randint(0,700)
            r = Rectangle(x,y,self.gemw, self.gemh)
            iw, w = self.doesIntersect(r)
            ig, g = self.doesIntersectWithGem(r)
            if not (iw or ig):
                return x,y,True
        return -1,-1,False

    def finishGame(self, r):
        rw = Rectangle(self.fin.x, self.fin.y, self.fin.w, self.fin.h)
        if rw.intersect(r):
            return True
        return False
    
    def expireGame(self):
        if time.process_time() - self.startTime>=5:
            return True
        return False



class Ball():
    def __init__(self, x, y, radius, color, env, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.env = env
        self.speed = speed
        
    def moveLeft(self):
        self.x = self.x-self.speed
        print('x', self.x, 'y', self.y)
    def moveRight(self):
        self.x = self.x+self.speed
        print('x', self.x, 'y', self.y)
    def moveUp(self):
        self.y = self.y-self.speed
        print('x', self.x, 'y', self.y)
    def moveDown(self):
        self.y = self.y+self.speed            
        print('x', self.x, 'y', self.y)
    def draw(self):
        pygame.draw.circle(self.env.screen, self.color, (self.x, self.y), self.radius) 

class Finish():
    def __init__(self, x,y,w,h,env):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.col = (200,50,30)
        self.env = env
    def draw(self):
        pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))   

class Wall():
    def __init__(self, x, y, w, h,env):
        self.x =x
        self.y = y
        self.w = w
        self.h = h
        self.col = (150,250,230)
        self.blinkcol =(150,230,250)
        self.env = env
    def draw(self):
        pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))
        tileimg = pygame.transform.scale(env.tilevimg, (self.w, self.h))
        if self.w>self.h:
            tileimg = pygame.transform.scale(env.tilehimg, (self.w, self.h))
        self.env.screen.blit(tileimg,(self.x,self.y))
    '''            
    def blink(self):
        pygame.draw.rect(self.env.screen, self.blinkcol, (self.x, self.y, self.w, self.h))
        pygame.display.update()
        pygame.draw.rect(self.env.screen, self.col, (self.x, self.y, self.w, self.h))
    '''
    
class Gem():
    def __init__(self, x, y, env):
        self.x = x
        self.y = y
        self.env = env
        self.w = env.gemw
        self.h = env.gemh
        self.score = 15
    def draw(self):
        self.env.screen.blit(self.env.gemimg, (self.x, self.y))

#x,y = pygame.mouse.get_pos() #checks position of cursor
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Impact', 100)

cnvh = 1000
cnvw = 1000
maxx = 21
maxy=18
fact = min(cnvw//maxx, cnvh//maxy)
env = Environment(cnvw, cnvh, "winterlandscape.png","brickh.jpg", "brickv.jpg", "gems.png")
b = Ball(int(0.5*fact), int(14.5*fact), 0.25*fact, (20,20,20),env, 5)
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
env.addBall(b)
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
            
            
        
