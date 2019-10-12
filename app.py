import pygame, sys
from pygame.locals import *
import glob
from PIL import Image
#import cv2
pygame.init()

FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((1600, 900), 0, 32, HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('Animation')

white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)
networkImg = pygame.image.load('data/qubits_node.png').convert()
networkImg.set_alpha(120)
catImg = pygame.image.load('data/cat.png')

im = Image.open('data/test.png')
width, height = im.size
#print(width,height)
circImg = pygame.image.load('data/test.png').convert()
circImg = pygame.transform.scale(circImg, (int(width/0.8),int(height/0.8)))
circImg.set_alpha(140)
circImg

images = []

for image in glob.glob('data/user_images/*.png'):
    #cv2.imread()
    im = Image.open(image)
    width, height = im.size
    #print(width,height)
    images.append(pygame.image.load(image).convert())



for image in images:
    image.set_alpha(140)


#gate = pd.read_csv()
circx = 200
circy = 0
catx = 0
caty = 0
direction = 'left'
gameover = False
originx = 0
originy = 700
font_obj = pygame.font.Font('freesansbold.ttf', 32)
fail_text = font_obj.render('You failed', True, green, blue)
text_surface_obj = font_obj.render('Press R to restart', True, green, blue)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (200, 150)


coords = []
while True: # the main game loop
    screen.fill(black)

    # if direction == 'right':
    #     circx += 5
    # elif direction == 'down':
    #     circy += 5
    # elif direction == 'left':
    #     circx -= 5
    # elif direction == 'up':
    #     circy -= 5
    originx = 0
    for idx, image in enumerate(images):
        #print(len(images))
        originx += 200
        image = pygame.transform.scale(image, (int(width / 2), int(height / 2)))
        screen.blit(image, (originx, originy))

        coords.append((originx,originy))

    screen.blit(catImg, (catx, caty))
    screen.blit(circImg, (circx, circy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x,y)

            for idx,image in enumerate(images):
                #print(image.get_rect())
                if image.get_rect(topleft=coords[idx]).collidepoint(x, y):
                    print(idx)
                    print('clicked on image at location %i, %i' % (x,y))
            #if gate[0] == 'cx' and gate[1] in keys[]

    if circx<-500:
        gameover=True

    #handle game state
    if not gameover:
        #move the cat position at multiples of some pixel distance
        if circx < -50 and circx % 50 == 0:
            catx = catx + 50
        pygame.display.flip()
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

