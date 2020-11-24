import pygame, sys, random, winsound
from pygame.locals import *
from rectangle import Rectangle
import time
from ball import Ball
from gem import Gem
from finish import Finish
from wall import Wall

class Environment(): 
    def __init__(self, w, h, background, tileh, tilev, gemimg, fact):
        pygame.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        self.myfont = pygame.font.SysFont('Impact', 100)
        self.w = w
        self.h = h
        self.fact = fact
        self.b = Ball(int(0.5*self.fact), int(14.5*self.fact), 0.25*self.fact, (20,20,20),self, 5)
        self.running = True
        self.score=0
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
        self.mouse = pygame.mouse.get_pos()
        

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
        frequency = 200  # Set Frequency To 200 Hertz
        duration = 500  # Set Duration To 500 ms == 1 second
        winsound.Beep(frequency, duration)
    

    def run(self):
        self.draw()
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_q:
                    self.running = False

     
                #if the mouse is clicked on the 
                # button the game is terminated 
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn.x <= self.mouse[0] <= self.btn.x+self.btn.w and self.btn.y <= self.mouse[1] <= self.btn.h+self.btn.y: 
                        print('Intersecting')
                    if self.doesIntersectWithButton():
                        self.running==False
                '''


            self.spawnGems()     
            if self.expireGame():
                self.losetext = 'Your Time is Up!'
                #self.running = False
                #self.beep()
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
                    self.b.moveRight()
                else:
                    self.beep()
            elif keys[pygame.K_LEFT]:
                futureball = Rectangle.fromCircle(self.b.x-self.b.speed, self.b.y, self.b.radius)
                self.handleGems(futureball)
                di, w = self.doesIntersect(futureball)
                if  not di:
                    self.b.moveLeft()
                else:
                    self.beep()
            elif keys[pygame.K_UP]:
                futureball = Rectangle.fromCircle(self.b.x, self.b.y-self.b.speed, self.b.radius)
                self.handleGems(futureball)
                di, w = self.doesIntersect(futureball)
                if  not di:
                    self.b.moveUp()
                else:
                    self.beep()                        
            elif keys[pygame.K_DOWN]:
                futureball = Rectangle.fromCircle(self.b.x, self.b.y+self.b.speed, self.b.radius)
                self.handleGems(futureball)
                di, w = self.doesIntersect(futureball)
                if  not di:
                    self.b.moveDown()
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
        textsurface = self.myfont.render(str(self.score), False, (0, 0, 0))
        self.screen.blit(textsurface,(10,self.h-100))
        self.drawTime()
        if self.wintext!=None:
            pygame.draw.rect(self.screen,(0, 204, 204 ) , (self.w//2 -150, self.h//2 -100, 500, 120))
            textsurface = self.myfont.render(self.wintext, False, (0, 0, 0))
            self.screen.blit(textsurface,(self.w//2-100,self.h//2-100))
            pygame.display.update()
            pygame.time.delay(1200)
        if self.losetext!=None:
            self.loseGameEnd()
            '''
            pygame.draw.rect(self.screen,(200, 0, 0 ) , (self.w//2 -300, self.h//2 -100, 700, 120))
            textsurface = self.myfont.render(self.losetext, False, (0, 0, 0))
            self.screen.blit(textsurface,(self.w//2-275,self.h//2-100))
            pygame.display.update()
            pygame.time.delay(1200)
            '''
        pygame.display.update()
     
    '''   
    def addButton(self,btn):
        self.btn =btn
    '''

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
    
    def doesIntersectWithButton(self):
        if self.btn.x <= self.mouse[0] <= self.btn.x+self.btn.w and self.btn.y <= self.mouse[1] <= self.btn.h+self.btn.y: 
            print('Intersecting')

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
        if time.process_time() - self.startTime>=10:
            return True
        return False

    def loseGameEnd(self):
        #pygame.draw.rect(self.screen,(200, 0, 0 ) , (self.w//2 -300, self.h//2 -100, 700, 120))
        self.screen.fill((200, 0, 0))
        textsurface1 = self.myfont.render(self.losetext, False, (0, 0, 0))
        self.screen.blit(textsurface1,(self.w//2-275,10))
        textsurface2 = self.myfont.render('Your Score: {}'.format(self.score), False, (0, 0, 0))
        self.screen.blit(textsurface2,(self.w//2-275,self.h//2-100))
        '''
        self.btn.draw()
        textsurface3 = self.myfont.render('Quit'.format(self.score), False, (200, 200, 200))
        # superimposing the text onto our button 
        self.screen.blit(textsurface3 , (self.w/2+50,self.h/2)) 
        '''


        pygame.display.update()
        pygame.time.delay(1200)


