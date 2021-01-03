#LEVEL 2 
# Creating an interactive game where user has to avoid obstacles, either by going over them or by ducking under them and collect gems along the way
# Also later show the top 5 hghest scores till then

import sys # Imported to access system commands
import pygame
from pygame.locals import * # Basic pygame imports
import random # For generating random numbers


# Global Variables for the game
FPS = 32 #Frames per second
SCREENWIDTH = 700
SCREENHEIGHT = 700
GROUND_Y = SCREENHEIGHT * 0.75
IMAGES = {}
SOUND = {}
REWARD_POINTS = 5
SCREENCAPTION = 'Game 2'
score = 0
icScore = 0
#Images
PLAYER = 'arushi/gallery/car.png'            
BACKGROUND = 'arushi/gallery/background.jpg' 
OBSTACLE = 'arushi/gallery/obstacle.png'     
REWARD = 'arushi/gallery/diamond.png'


#Initial blank screen
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

def startScreen():
    #instructions and game2 image
    #Position of car-middle of screen
    global FPSCLOCK
    global FPS
    playerX = int((SCREENWIDTH - IMAGES['player'].get_width())/2) 
    playerY = int((SCREENHEIGHT - IMAGES['player'].get_height())/2) 
    messageX = int((SCREENWIDTH - IMAGES['message'].get_width())/2)
    messageY = int(SCREENHEIGHT*0.15)

    basex = 0
    SCREEN.blit(IMAGES['background'], (0, 0))    
    SCREEN.blit(IMAGES['player'], (playerX, playerY))    
    SCREEN.blit(IMAGES['message'], (messageX,messageY ))    
    SCREEN.blit(IMAGES['base'], (basex, GROUND_Y))    
    pygame.display.update()
    FPSCLOCK.tick(FPS)

    SCREEN.blit(IMAGES['background'], (0, 0))    
    SCREEN.blit(IMAGES['player'], (playerX, playerY))    
    SCREEN.blit(IMAGES['message'], (messageX,messageY ))    
    SCREEN.blit(IMAGES['base'], (basex, GROUND_Y))    
    pygame.display.update()
    FPSCLOCK.tick(FPS)
    while True:
        for event in pygame.event.get():
            # If user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): #Esc or crossed
                print("GAME QUIT")
                return False

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                print("Starting Game")
                return True

            elif event.type == KEYDOWN and event.key == K_i:
                print("Instructions")
                return True

                
            else:
                pass

def mainGame(running):
    global FPS
    global score
    playerX = int(SCREENWIDTH/5)
    playerY = int(SCREENWIDTH/2)
    basex = 0

    # Create 2 obstacles for blitting on the screen
    newObstacle1 = getRandomObstacle()
    newObstacle2 = getRandomObstacle()

    # List of upper obstacles
    upperObstacles = [
        {'x': SCREENWIDTH+200, 'y':newObstacle1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newObstacle2[0]['y']},
    ]
    # my List of lower obstacles
    lowerObstacles = [
        {'x': SCREENWIDTH+200, 'y':newObstacle1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newObstacle2[1]['y']},
    ]

    # List of rewards
    rewards = [
        {'x': SCREENWIDTH+random.randint(0, 50), 'y': random.randint(0, SCREENHEIGHT-30)}, # Rewards comes at extreme right
        ]

    obstacleVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playerY > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    SOUND['wing'].play()


        if hitObstacle(playerX, playerY, upperObstacles, lowerObstacles):  # True if player collided with any obstacle
            # Crash happened. Display the score and wait for user input
            print("Game Over")
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        return
                    if event.type == KEYDOWN and (event.key == K_RETURN):
                        return
    
        # Update score
        playerMidPos = playerX + IMAGES['player'].get_width()/2
        for obstacle in upperObstacles:
            obstacleMidPos = obstacle['x'] + IMAGES['obstacle'][0].get_width()/2
            if obstacleMidPos <= playerMidPos < obstacleMidPos +4:  # Crossed the obstacle
                score +=1
                print(f"Your score is {score}") 
                SOUND['point'].play()

        # Check if reward collected
        if rewardCollected(playerX, playerY, rewards):
            print("reward collected")
            score += REWARD_POINTS
            SOUND['point'].play()
            # Remove this reward as already claimed. Add a new reward
            rewards = [
                {'x': SCREENWIDTH+random.randint(0, 50), 'y': random.randint(0, SCREENHEIGHT-30)}, # Rewards enter at extreme right
                ]
        
        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = IMAGES['player'].get_height()
        playerY = playerY + min(playerVelY, GROUND_Y - playerY - playerHeight)

        # move obstacles to the left
        for upperObstacle , lowerObstacle in zip(upperObstacles, lowerObstacles):
            upperObstacle['x'] += obstacleVelX
            lowerObstacle['x'] += obstacleVelX

        for reward in rewards:
            reward['x'] += obstacleVelX


        # Add a new obstacle when the first is about to cross the leftmost part of the screen
        if 0<upperObstacles[0]['x']<5:
            newobstacle = getRandomObstacle()
            upperObstacles.append(newobstacle[0])
            lowerObstacles.append(newobstacle[1])

        # if the obstacle is out of the screen, remove it
        if upperObstacles[0]['x'] < -IMAGES['obstacle'][0].get_width():
            upperObstacles.pop(0)
            lowerObstacles.pop(0)
        
        # if the reward is out of the screen, add a new one
        if rewards[0]['x'] < -IMAGES['rewardImage'].get_width():
            rewards = [
                {'x': SCREENWIDTH+random.randint(0, 50), 'y': random.randint(0, SCREENHEIGHT-30)}, # Rewards enter at extreme right
                ]
        
        # Update the screen now
        SCREEN.blit(IMAGES['background'], (0, 0))
        for upperObstacle, lowerObstacle, in zip(upperObstacles, lowerObstacles):
            SCREEN.blit(IMAGES['obstacle'][0], (upperObstacle['x'], upperObstacle['y']))
            SCREEN.blit(IMAGES['obstacle'][1], (lowerObstacle['x'], lowerObstacle['y']))

        for reward in rewards:
            SCREEN.blit(IMAGES['rewardImage'], (reward['x'], reward['y']))

        SCREEN.blit(IMAGES['base'], (basex, GROUND_Y))
        SCREEN.blit(IMAGES['player'], (playerX, playerY))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += IMAGES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width - 10)

        for digit in myDigits:
            SCREEN.blit(IMAGES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.9))
            Xoffset += IMAGES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS+(score - icScore)/2)

def hitObstacle(playerX, playerY, upperObstacles, lowerObstacles):
    if playerY > (GROUND_Y - 25)  or playerY < 0:
        SOUND['hit'].play()
        return True
    
    for obstacle in upperObstacles:
        obstacleHeight = IMAGES['obstacle'][0].get_height()
        if(playerY < obstacleHeight + obstacle['y'] and abs(playerX - obstacle['x']) < IMAGES['obstacle'][0].get_width()):
            SOUND['hit'].play()
            return True

    for obstacle in lowerObstacles:
        if (playerY + IMAGES['player'].get_height() > obstacle['y']) and abs(playerX - obstacle['x']) < IMAGES['obstacle'][0].get_width():
            SOUND['hit'].play()
            return True

    return False

def rewardCollected(playerX, playerY, rewards):
    
    for reward in rewards:
        obstacleHeight = IMAGES['obstacle'][0].get_height()
        if(playerY > reward['y'] and (playerY < reward['y']+IMAGES['rewardImage'].get_height()) and abs(playerX - reward['x']) < IMAGES['rewardImage'].get_width()):
            return True
    return False

def getRandomObstacle():
    """
    Generate positions of two obstacles(one bottom straight and one top rotated ) for blitting on the screen
    """
    obstacleHeight = IMAGES['obstacle'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - IMAGES['base'].get_height()  - 1.2 *offset))
    obstacleX = SCREENWIDTH + 10
    y1 = obstacleHeight - y2 + offset
    obstacle = [
        {'x': obstacleX, 'y': -y1}, #upper Obstacle
        {'x': obstacleX, 'y': y2} #lower Obstacle
    ]
    return obstacle

def runcargame(incomingscore=0, running=True):
    global SCREEN 
    global FPSCLOCK
    global FPS
    global score
    global icScore
    score = incomingscore
    icScore = incomingscore
    if not running:
        return score
    SCREEN= pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption(SCREENCAPTION)
    IMAGES['numbers'] = ( 
        pygame.image.load('arushi/gallery/images/0.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/1.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/2.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/3.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/4.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/5.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/6.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/7.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/8.png').convert_alpha(),
        pygame.image.load('arushi/gallery/images/9.png').convert_alpha(),
    )

    IMAGES['message'] =pygame.image.load('arushi/gallery/firstScreen.png').convert_alpha()
    IMAGES['base'] =pygame.transform.scale(pygame.image.load('arushi/gallery/base.png').convert_alpha(),(SCREENWIDTH,300))
    IMAGES['background'] = pygame.image.load(BACKGROUND).convert()
    IMAGES['player'] = pygame.image.load(PLAYER).convert_alpha()
    IMAGES['rewardImage'] = pygame.image.load(REWARD).convert_alpha()
    IMAGES['obstacle'] =(pygame.transform.rotate(pygame.image.load( OBSTACLE).convert_alpha(), 180), 
    pygame.image.load(OBSTACLE).convert_alpha()
    )

    # Game sounds
    SOUND['die'] = pygame.mixer.Sound('arushi/gallery/audio/die.wav')
    SOUND['hit'] = pygame.mixer.Sound('arushi/gallery/audio/hit.wav')
    SOUND['point'] = pygame.mixer.Sound('arushi/gallery/audio/point.wav')
    SOUND['swoosh'] = pygame.mixer.Sound('arushi/gallery/audio/swoosh.wav')
    SOUND['wing'] = pygame.mixer.Sound('arushi/gallery/audio/wing.wav')


    #The program is run
    # Shows welcome screen to the user until a button is pressed
    # This is the main game function 
    mainGame(startScreen())
    return score


if __name__ == "__main__":
    runcargame()
    