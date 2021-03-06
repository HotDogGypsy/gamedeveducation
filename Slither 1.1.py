import pygame
import time
import random
import cx_Freeze

#Initialize Pygmae
pygame.init()

#RGB Color Definitions
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
pink = (255,102,204)

#Window Size
display_width = 800
display_height = 600

#Surface (Or Screen)
gameDisplay = pygame.display.set_mode((display_width,display_height))
#caption
pygame.display.set_caption('Slither')

#32x32 is best Icon size for Pygame
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

#snake head picture
img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')

#Frames Per Second
clock = pygame.time.Clock()

#Block size of the snake
block_size = 20

#Apple Block
AppleThickness = 30
        


#FPS Def
FPS = 15

direction = "right"

def randAppleGen():
     randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
     randAppleY = round (random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

     return randAppleX,randAppleY

def pause():

    paused = True

    message_to_screen("Paused",
                     black,
                     -100,
                     size="large")
    message_to_screen("press C to continue or Q to quit.",
                     black,
                     25)
   
    pygame.display.update()
 
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)
    
        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text,[0,0])

#Text Fone
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                  pygame.quit()
                  quit()

            
        #Make Snake Story 
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither", green, -100, "large")

        message_to_screen("The objective of the game is to eat red apples.", black, -30,)

        message_to_screen("The more apples you eat the longer you get!.", black, 10,)

        message_to_screen("If you run into yourself or the edges, you lose!.", black, 50,)

        message_to_screen("Press C to start game or Q to quit! Press P to pause at any time!", black, 180,)

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)



    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
                     
    for XnY in snakelist[:-1]: 
        pygame.draw.rect(gameDisplay, green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color, size):
    if size == "small": 
        textSurface = smallfont.render(text, True, color)
    elif size == "medium": 
        textSurface = medfont.render(text, True, color)
    elif size == "large": 
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()

#Text on screen function
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
   

    
#Game Loop
def gameLoop():
    global direction

    direction = "right"
    gameExit = False
    gameOver = False

    #Movement Definitions
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    

    randAppleX, randAppleY= randAppleGen()


    
    while not gameExit:

        #Gameover Loop

        if gameOver == True:
            message_to_screen("Game Over", red, y_displace = -50, size="large")
            message_to_screen("Press C to play again or Q to quit",black, 50, size="medium")
            pygame.display.update()
 
         
        while gameOver == True:
            #gameDisplay.fill(white)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    
            
            
        #Quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            #Movement - Left/Right  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                 #movement = Up/Down
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        #Boundaries 
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        


        #Adding direction to Movement                          
        lead_x += lead_x_change
        lead_y += lead_y_change



        
        #Background
        gameDisplay.fill(white)

      
        #pygame.draw.rect(gameDisplay,red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(appleimg, (randAppleX,randAppleY))

        #Call Snake Function
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

     
        snake(block_size, snakeList)

        score(snakeLength-1)
        
        
        #Update
        pygame.display.update()


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY= randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY= randAppleGen()
                snakeLength += 1
  

            
        
        #FPS
        clock.tick(FPS)
        
    
    pygame.quit()
    quit()
game_intro()
gameLoop()



