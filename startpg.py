import pygame
from start.button import Button
from maze import mainrun
import pygame, sys, random
from start.leaderboard import LeadEnvironment
from start.infoboard import InfoEnvironment
from maze.scorepg import ScoreEnvironment
from start.CompProjMySQL import scoreboard as sb
import getpass

pygame.init()



class StartEnvironment():  #This is a class which makes the start page and all elements on it when the program is executed
    def __init__(self, background):
        pygame.font.init() # you have to call this at the start, 
                        # if you want to use this module.
        self.headsize = 100
        self.h = 700 #screen height
        self.w = 700 #screen width
        self.maxxy = 20
        self.fact = self.h//self.maxxy #this variable helps to easily transform size of the screen if required. It just needs to be multiplied to whatever is to be changed
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.startbimg1 = "start/startbtnonclick.jpg"               #following are all the images that are used in this program
        self.startbimg2 = "start/startbtnnoclick.jpg"
        self.headbimg1 = self.headbimg2 = "start/mazebtnbg.jpg"
        self.btnimg1 = "start/genbtnonclick.jpg"
        self.btnimg2 = "start/genbtn.jpg"
        self.leaderbimg1 = "start/leaderboard.jfif"
        self.leaderbimg2 = "start/leaderboardonclick.jfif"
        self.infobimg = "start/info.png"
        #the following 5 variables initialise the buttons on the screen. The buttons are created by the button class.
        self.headb = Button(6*self.fact,6*self.fact,10*self.fact,3*self.fact,self.headbimg1, self.headbimg2,(255, 255, 255),self.screen,'Arena',self.headsize)
        self.leadb = Button(7*self.fact,10*self.fact,8*self.fact,2*self.fact,self.leaderbimg1, self.leaderbimg2,(0,0,0),self.screen,'Leaderboard')
        self.startb = Button(8*self.fact,13*self.fact,6*self.fact,2*self.fact,self.startbimg1, self.startbimg2,(0,0,0),self.screen,'Start')
        self.quitb = Button(8*self.fact,16*self.fact,6*self.fact,2*self.fact,self.btnimg1, self.btnimg2,(0,0,0),self.screen,'Quit')
        self.infob = Button(18*self.fact, 18*self.fact, 1*self.fact, 1*self.fact, self.infobimg, self.infobimg, (0,0,0), self.screen, ' ')
        
        self.infoenv = InfoEnvironment() #This is the enivronment of the info page - a subpage of the start page.
        self.running = True
        self.bgimg = pygame.image.load(background)
        self.bgimg = pygame.transform.scale(self.bgimg,(self.w,self.h)) 

    def run(self): #This function runs all individual parts of the start page.
        running=True
        self.draw() #the draw function draws all the required images, texts, buttons 
        while running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    running = False
                coord = pygame.mouse.get_pos() 
                if self.quitb.intersect(coord): #checking if the mouse pointer is within the area of the quit button
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        running=False
                elif self.startb.intersect(coord): #checking if the mouse pointer is within the area of the start button
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #running=False
                        self.score = mainrun.runGame()
                        if self.score ==None:
                            self.score=0
                        sb(getpass.getuser(), self.score)
                        self.scoreenv = ScoreEnvironment(self.score)
                        self.scoreenv.run()
                        self.screen = pygame.display.set_mode((self.w, self.h))
                elif self.leadb.intersect(coord): #checking if the mouse pointer is within the area of the leaderboard button
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.leadenv = LeadEnvironment()
                        self.leadenv.run()
                        pygame.init()
                elif self.infob.intersect(coord): #checking if the mouse pointer is within the area of the info button
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.infoenv.run()
                        pygame.init()
            self.draw()
        pygame.quit()
    
    def draw(self):
        #self.screen.fill((0, 200, 150))
        self.screen.blit(self.bgimg,[0,0])
        self.headb.draw()
        self.leadb.draw()
        self.startb.draw()
        self.quitb.draw()
        self.infob.draw()
        pygame.display.update()
 
env = StartEnvironment("start/startbg.jpg")
env.run()






