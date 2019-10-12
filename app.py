import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)
catImg = pygame.image.load('test.png')
circImg = pygame.image.load('test.png')
circx = 0
circy = 0
direction = 'left'
gameover = False

font_obj = pygame.font.Font('freesansbold.ttf', 32)
fail_text = font_obj.render('You failed', True, green, blue)
text_surface_obj = font_obj.render('Press R to restart', True, green, blue)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (200, 150)

while True: # the main game loop
    screen.fill(white)

    if direction == 'right':
        circx += 5
    elif direction == 'down':
        circy += 5
    elif direction == 'left':
        circx -= 5
    elif direction == 'up':
        circy -= 5

    screen.blit(circImg, (circx, circy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                print("CX applied")
                circx = circx - 10
            elif event.key == pygame.K_s:
                print("S applied")
                circx = circx - 20
    if circx>500:
        gameover=True

    #handle game state
    if not gameover:
        pygame.display.update()
        fpsClock.tick(FPS)
    else:
        screen.fill(black)
        #print('You failed')
        screen.blit(fail_text,(200,100))
        screen.blit(text_surface_obj, text_rect_obj)
        #pygame.draw.rect(screen,red, (200, 150, 100, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("restarting")

        fpsClock.tick(FPS)
        pygame.display.update()

