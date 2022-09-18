import pygame
screensize=[700, 700]
pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('HUNTER')
clock = pygame.time.Clock()
xpos=screensize[0]/2-20
ypos=screensize[1]/2-80
pl2xpos=screensize[0]/2-20
pl2ypos=screensize[1]/2+80
screencolor=[118, 172, 51]
playersize=40
speed=8
while True:
    screen.fill(screencolor)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(xpos,ypos,playersize, playersize))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(pl2xpos,pl2ypos,playersize, playersize))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
     #exit the game
            pygame.quit()
            break
#400,400 cordinates 40 is the width 40 is the height
    keys = pygame.key.get_pressed()
    #get all the keys in a dictionary keys[K_left] return 1 if its pressed 0 otherwise
    if keys[pygame.K_LEFT] and xpos>speed/2:
    	xpos-=speed#great job lol see if its greater than 8 then you can subtract
    if keys[pygame.K_RIGHT] and xpos<screensize[0]-playersize-speed:
    	xpos+=speed #if its less than the creen-8 can increase
    if keys[pygame.K_UP] and ypos>0:
      	ypos-=speed
    if keys[pygame.K_DOWN] and ypos<screensize[1]-playersize-speed/2:
      	ypos+=speed
    if keys[pygame.K_a]and pl2xpos>speed/2:
    	pl2xpos-=speed
    if keys[pygame.K_d]and pl2xpos<screensize[0]-playersize-speed:
    	pl2xpos+=speed
    if keys[pygame.K_w]and pl2ypos>0:
    	pl2ypos-=speed
    if keys[pygame.K_s] and pl2ypos<screensize[1]-playersize-speed/2:
      	pl2ypos+=speed#lets run this bad boy
        #print("hello mom!")
    #http://www.pygame.org/docs/ref/key.html
    pygame.display.update()
    clock.tick(30)