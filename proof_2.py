import pygame
import tkinter as tk



pygame.init()
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("First Game")



icon = pygame.image.load('colosseum.jpg')
walk_r = pygame.transform.scale(icon, (30, 30))
walkLeft = pygame.image.load('colosseum.jpg')
walk_l = pygame.transform.scale(walkLeft, (30, 30))
walkDiagonal = pygame.image.load('colosseum.jpg')
walk_d = pygame.transform.scale(walkDiagonal, (30, 30))
backg = pygame.image.load('cicero_map2.png')
mapp = pygame.transform.scale(backg, (640, 480))
char = pygame.image.load('colosseum.jpg')
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

questions = ['Quanto è stupida Mia da 1 a 10 ?',
			 'Question 2:',
			 'Question 3:',
			 'Question 1:',
			 'Question 1:']

answers =[ [("11", 1),
			("0", 2),
    	    ("1", 3),
            ("3", 4),
            ("10", 5)] , 
		  
		  [("11", 1),
			("0", 2),
    	    ("1", 3),
            ("3", 4),
            ("10", 5)] ,
		  [("11", 1),
			("0", 2),
    	    ("1", 3),
            ("3", 4),
            ("10", 5)] ,
		  [("11", 1),
			("0", 2),
    	    ("1", 3),
            ("3", 4),
            ("10", 5)] ,
		  [("11", 1),
			("0", 2),
    	    ("1", 3),
            ("3", 4),
            ("10", 5)] ,
		  ]


	
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

        def CheckChoice():

         if v.get() == 1:
          global risposte_esatte
          risposte_esatte += 1
          root.destroy()
          root.quit()
         else:
          tk.messagebox.showerror('Error','Wrong Answer!')
		  
        root = tk.Tk()
        root.bind('<Escape>', lambda e: root.destroy())		  
        v = tk.IntVar()
		
        tk.Label(root, 
         text=questions[risposte_esatte],
         justify = tk.LEFT,
         padx = 20).pack()

        for ans, val in answers[risposte_esatte]:
			      tk.Radiobutton(root, 
                  text=ans,
                  indicatoron = 0,
                  width = 20,
                  padx = 20, 
                  variable=v, 
                  command=CheckChoice,
                  value=val).pack(anchor=tk.W)
        root.mainloop()
        
    
    
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



run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            run = False
            
                  
    keep_move_mod(target_x[risposte_esatte], target_y[risposte_esatte])
	      
  
    if risposte_esatte == 10:
        
        win.blit(walk_char, (icon_x,icon_y))
        walkCount = 0
        break
                                                                     
    redrawGameWindow() 
pygame.quit()


