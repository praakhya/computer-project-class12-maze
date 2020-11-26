import pygame, sys, random
from pygame.locals import *
from maze.rectangle import Rectangle
import time
from maze.ball import Ball
from maze.gem import Gem
from maze.finish import Finish, Finishwall
from maze.wall import Wall
from pygame import mixer
from start.button import Button
class Environment(): 
    def __init__(self, w, h, background, tileh, tilev, gemimg, fact, ballcol, score=0):
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
        self.gemPoint = None
        self.fin = None
        self.finwall=None
        self.gemw = 30
        self.gemh = 30
        self.wintext=None
        self.losetext=None
        self.unlock=False
        self.noGems=5
        self.gemCount = 0
        self.bgimg = pygame.image.load(background)
        self.bgimg = pygame.transform.scale(self.bgimg,(self.w,self.h))
        self.tilehimg = pygame.image.load(tileh)
        self.tilevimg = pygame.image.load(tilev)
        self.gemimg = pygame.image.load(gemimg)
        self.gemimg = pygame.transform.scale(self.gemimg,(self.gemw,self.gemh))
        self.startTime = time.process_time()
        self.futurerunning = True
        mixer.init()
        self.m1 = pygame.mixer.Sound('maze/beep.wav')
        self.m2 = pygame.mixer.Sound('maze/Latch_01.wav')
        self.m1.set_volume(0.7)
        self.btnimg1 = "maze/turqoise.png"
        
        
        

    def drawTime(self):
        elapsedTime = time.process_time() - self.startTime
        elapsedSeconds = int(elapsedTime % 60)
        elapsedTime = elapsedTime // 60
        elapsedMinutes = int(elapsedTime % 60)
        elapsedTime = elapsedTime // 60
        elapsedHours = int(elapsedTime)
        timeString = "{:02d}:{:02d}:{:02d}".format(elapsedHours, elapsedMinutes, elapsedSeconds)
        textsurface = self.myfont.render(timeString, False, (0, 0, 0))
        self.screen.blit(textsurface,(self.w - 400,self.h-100))

    def beep(self):
        self.m1.play(1,200)
    
    def unlocksound(self):
        self.m2.play(1,200)
    

    def run(self):
        self.spawnGems()
        self.draw()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_q:
                    self.running = False  
            if self.expireGame():
                    self.losetext = 'Your Time is Up!'
                    self.running = False
                    self.futurerunning = False
                    self.beep()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                futureball = Rectangle.fromCircle(self.b.x+self.b.speed, self.b.y, self.b.radius)
                if self.finishGame(futureball):
                    self.wintext = 'Level Success!'
                    self.running = False
                    self.beep()
                self.handleGems(futureball)
                di1, w = self.doesIntersect(futureball) 
                di2 = self.doesIntersectWithFinwall(futureball)
                if  not (di1 or di2):
                    self.b.moveRight()
                else:
                    self.beep()
            elif keys[pygame.K_LEFT]:
                futureball = Rectangle.fromCircle(self.b.x-self.b.speed, self.b.y, self.b.radius)
                self.handleGems(futureball)
                di1, w = self.doesIntersect(futureball)
                di2 = self.doesIntersectWithFinwall(futureball)
                if  not (di1 or di2):
                    self.b.moveLeft()
                else:
                    self.beep()
            elif keys[pygame.K_UP]:
                futureball = Rectangle.fromCircle(self.b.x, self.b.y-self.b.speed, self.b.radius)
                self.handleGems(futureball)
                di1, w = self.doesIntersect(futureball)
                di2 = self.doesIntersectWithFinwall(futureball)
                if  not (di1 or di2):
                    self.b.moveUp()
                else:
                    self.beep()                        
            elif keys[pygame.K_DOWN]:
                futureball = Rectangle.fromCircle(self.b.x, self.b.y+self.b.speed, self.b.radius)
                self.handleGems(futureball)
                di1, w = self.doesIntersect(futureball)
                di2 = self.doesIntersectWithFinwall(futureball)
                if  not (di1 or di2):
                    self.b.moveDown()
                else:
                    self.beep() 
            self.draw()
        #self.clock.tick(60)
        #pygame.quit()

    def handleGems(self,futureball):
        gi, g = self.doesIntersectWithGem(futureball)
        if gi:
            self.score+=g.score
            self.removeGem(g)
            if len(self.gems) == 0:
                self.unlock=True
                self.unlocksound()                       



    def draw(self):
        self.screen = pygame.display.set_mode((self.w,self.h))
        self.screen.blit(self.bgimg,[0,0])
        for j in self.gems:
            j.draw()
        self.b.draw()
        self.fin.draw()
        if self.unlock == True:
            self.finwall.w = self.finwall.h = 0
        else:
            self.finwall.draw()
        for i in self.walls:
            i.draw()
        textsurface = self.myfont.render(str(self.score), False, (0, 0, 0))
        self.screen.blit(textsurface,(10,self.h-100))
        self.drawTime()
        if self.wintext!=None:
            '''
            pygame.draw.rect(self.screen,(0, 204, 204 ) , (self.w//2 -300, self.h//2 -100, 700, 120))
            textsurface = self.myfont.render(self.wintext, False, (0, 0, 0))
            self.screen.blit(textsurface,(self.w//2-100,self.h//2-100))
            '''
            self.windisplay = Button(4*self.fact,self.h//2,10*self.fact,2*self.fact,self.btnimg1, self.btnimg1,(0,0,0),self.screen,self.wintext)
            self.windisplay.draw()
            pygame.display.update()
            pygame.time.delay(1200)
        if self.losetext!=None:
            pygame.draw.rect(self.screen,(200, 0, 0 ) , (self.w//2 -300, self.h//2 -100, 700, 120))
            textsurface = self.myfont.render(self.losetext, False, (0, 0, 0))
            self.screen.blit(textsurface,(self.w//2-275,self.h//2-100))
            pygame.display.update()
            pygame.time.delay(1200)
        pygame.display.update()
        
    def addWall(self, wl):
        self.walls.append(wl)

    def addFinish(self, fin):
        self.fin = fin
    
    def addFinishwall(self, finwall):
        self.finwall = finwall

    def doesIntersect(self, r):
        for i in self.walls:
            rw = Rectangle(i.x, i.y, i.w, i.h)
            if rw.intersect(r):
                return True,i
        return False,None

    def doesIntersectWithFinwall(self, r):
        rw = Rectangle(self.finwall.x, self.finwall.y, self.finwall.w, self.finwall.h)
        if rw.intersect(r):
            return True
        return False

    def doesIntersectWithGem(self, r):
        for g in self.gems:
            rw = Rectangle(g.x, g.y, g.w, g.h)
            if rw.intersect(r):
                return True,g
        return False,None

    def removeGem(self, gm):
        self.gems = [g for g in self.gems if g.x != gm.x and g.y != gm.y]

    def addGem(self, gm):
        self.gemPoint=gm.score
        self.gems.append(gm)
    
    def spawnGems(self):
        #num = random.randint(0,20)
        #if num==0: #and self.gemCount<self.maxGems:
        while self.gemCount<self.noGems:
            x,y, posfound = self.findPosition()
            if posfound:
                self.addGem(Gem(x,y,self))
                self.gemCount+=1
        

    def findPosition(self):
        for i in range(10000):
            x= random.randint(0,15*self.fact)
            y= random.randint(0,15*self.fact)
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
        if time.process_time() - self.startTime>=60:
            return True
        return False




