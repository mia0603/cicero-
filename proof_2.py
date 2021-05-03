import pygame
import math
import time


pygame.init()
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("First Game")


icon = pygame.image.load('/Users/miagalante/Desktop/cicero_game /Codice/colosseum.jpg')
walk_r = pygame.transform.scale(icon, (30, 30))
walkLeft = pygame.image.load('/Users/miagalante/Desktop/cicero_game /Codice/colosseum.jpg')
walk_l = pygame.transform.scale(walkLeft, (30, 30))
walkDiagonal = pygame.image.load('/Users/miagalante/Desktop/cicero_game /Codice/colosseum.jpg')
walk_d = pygame.transform.scale(walkDiagonal, (30, 30))
backg = pygame.image.load('/Users/miagalante/Desktop/cicero_game /Codice/cicero_map2.png')
mapp = pygame.transform.scale(backg, (640, 480))
char = pygame.image.load('/Users/miagalante/Desktop/cicero_game /Codice/colosseum.jpg')
walk_char = pygame.transform.scale(char, (30, 30))



BLUE=(0,0,255)
GREEN = (0,255,0)
WHITE=(255,255,255)
RED=(255, 0, 0)
BLACK=(0,0,0)

icon_x = 360
icon_y = 350


clock = pygame.time.Clock()

left = False
right = False
down = False

walkCount = 0
risposte_esatte = 0

target_x = [320, 135, 185, 240, 345, 580, 555, 480, 420, 500, 530]
target_y = [400, 330, 210, 153, 100, 110, 222, 223, 270, 347, 530] 

def keep_move_mod(target_x, target_y):
    global icon_x
    global icon_y
    global risposte_esatte
    if icon_x != target_x or  icon_y != target_y:
        coef = (target_y - icon_y) / (target_x - icon_x)
        sign_x = (target_x - icon_x)/abs(target_x - icon_x)
        sign_y = (target_y - icon_y)/abs(target_y - icon_y)
        icon_x += 1 * sign_x
        icon_y += abs(coef)  * sign_y
    else:
        risposte_esatte += 1 
    
        
def num_risposte_esatte():
    global risposte_esatte
    if risposte_esatte == 10:
        pygame.quit()
   
        
    
def redrawGameWindow():
    global walkCount
    win.blit(mapp, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walk_l, (icon_x,icon_y))
        walkCount += 1

    if right:
        win.blit(walk_r, (icon_x,icon_y))
        walkCount += 1

    if down:
        win.blit(walk_d, (icon_x,icon_y))
        walkCount += 1
        
    else:
        win.blit(walk_char, (icon_x,icon_y))
        walkCount = 0
        
    pygame.display.update() 


def isCollision(icon_x, icon_y, target_x, target_y):
    distance = math.sqrt((math.pow(icon_x - target_x, 2)) + (math.pow( icon_y - target_y, 2)))
    if distance < 1:
        return True
    else:
        return False
    
            
run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
            
                  
    keep_move_mod(target_x[risposte_esatte], target_y[risposte_esatte])
    collision = isCollision(icon_x, icon_y, target_x[risposte_esatte], target_y[risposte_esatte])
    
    if collision:
        pygame.time.delay(10)
        
  
    if risposte_esatte == 10:
        
        win.blit(walk_char, (icon_x,icon_y))
        walkCount = 0
        break
                                                                     
    redrawGameWindow() 
pygame.quit()

