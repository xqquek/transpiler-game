import pygame, sys
from pygame.locals import *
import glob
from PIL import Image
from Compare_cir import *
#import cv2
pygame.init()

FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((1600, 900), 0, 32, HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption('transpiler-game')

white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)

im = Image.open('data/qubits_node.png')
width, height = im.size
networkImg = pygame.image.load('data/qubits_node.png').convert()
networkImg.set_alpha(200)
networkImg = pygame.transform.scale(networkImg, (int(width / 2), int(height / 2)))
catImg = pygame.image.load('data/cat.png')

im = Image.open('data/test.png')
width, height = im.size
#print(width,height)
circImg = pygame.image.load('data/test.png').convert()
circImg = pygame.transform.scale(circImg, (int(width/0.8),int(height/0.8)))
circImg.set_alpha(200)
circImg

images = []
counter = 0

cat_separation = 110

for image in glob.glob('data/user_images/*.png'):
    #cv2.imread()
    im = Image.open(image)
    width, height = im.size
    #print(width,height)
    images.append(pygame.image.load(image).convert())


small_images = []
for image in images:
    image.set_alpha(200)
    small_images.append(pygame.transform.scale(image, (int(width / 2), int(height / 2))))


#gate = pd.read_csv()
circx = 400
circy = 200
catx = circx+50
caty = circy-200
networkx = 600
networky = -50
direction = 'up'
gameover = False
originx = 0
originy = 700
font_obj = pygame.font.Font('freesansbold.ttf', 32)
fail_text = font_obj.render('Meow!', True, green, blue)
text_surface_obj = font_obj.render('Congratulations!', True, green, blue)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (300, 150)
is_occupied=False

coords = []
selected_cards = []
while True: # the main game loop
    screen.fill(black)

    # if direction == 'right':
    #     circx += 5
    # elif direction == 'down':
    #     circy += 5
    # elif direction == 'left':
    #     circx -= 5
    if direction == 'up':
        if caty<circy-80:
            sign = 1
            caty += sign*2
        elif caty>circy-120:
            sign = -1
            caty += sign*2
        if networky<circy-220:
            networky+=2
    originx = 0
    center_image = small_images[0]

    for idx, image in enumerate(small_images):
        #print(len(images))
        originx += 200
        #image = pygame.transform.scale(image, (int(width / 2), int(height / 2)))
        screen.blit(image, (originx, originy))
        coords.append((originx,originy))

    screen.blit(networkImg, (networkx, networky))
    screen.blit(catImg, (catx, caty))
    screen.blit(circImg, (circx, circy))
    displacement = 0
    for card_idx in selected_cards:
        #image = pygame.transform.scale(images[card_idx], (int(width / 2), int(height / 2)))
        displacement += 120
        screen.blit(small_images[card_idx], (500 + displacement,550))
    #if is_occupied:
    #    screen.blit(center_image, (500, 800))

    #handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #handle mouse clicks to select cards
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x,y)

            for idx,image in enumerate(small_images):
                #print(image.get_rect())
                if image.get_rect(topleft=coords[idx]).collidepoint(x, y):
                    is_occupied=True
                    center_image = image
                    selected_cards.append(idx)
                    #screen.blit()
                    #print(idx)
                    print('clicked on image at location %i, %i' % (x,y))
            #if gate[0] == 'cx' and gate[1] in keys[]
        #handle enter to confirm input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(tot_oper(selected_cards))
                if cir_is_equal(tot_oper(selected_cards),counter):
                    counter += 1
                    print(counter)
                    selected_cards = []
                    catx += cat_separation
                else:
                    print('Wrong answer!')
                    screen.fill(red)
                    #pygame.mixer.music.load('data/fail-buzzer-04.wav')
                    #pygame.mixer.music.play()
                    selected_cards = []
                #is_occupied = False


    if catx > circx + cat_separation*6:
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

