import wx
import pygame

pygame.init()

backg = pygame.image.load('cicero_map3.png')
mapp = pygame.transform.scale(backg, (640, 480))
icon = pygame.image.load('colosseum.jpg')
walk_icon = pygame.transform.scale(icon, (30, 30))

width = 640
height = 480

def create_window(mapp, width, height):
    win = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("Cicero Game")
    pygame.display.flip()
    return win

win = create_window(mapp, width, height)

icon_x = 400
icon_y = 350

clock = pygame.time.Clock()

walkCount = 0
risposte_esatte = 0

target_x = [379, 355, 320, 285, 230, 200, 255, 298, 356, 425, 535, 580, 584, 575, 565, 514, 473, 430, 460, 485, 500]
target_y = [355, 385, 400, 347, 290, 195, 165, 135, 100, 102, 103, 90, 115, 168, 210, 241, 244, 260, 310, 335, 345]

## Schema dati
### [Domanda, [opzioni], risposta]
data = [["Chi era Cicerone?", ["Maschio", "Femmina", "Porco", "Teiera"], "Teiera"],
		["Chi era il padre di Cicerone?", ["Un Vagabondo", "Femmina", "Porco", "Teiera"], "Un Vagabondo"],
		["Chi era il padre di Cicerone?", ["Un Vagabondo", "Femmina", "Porco", "Teiera"], "Un Vagabondo"]]

class Domande(wx.Frame):

    def __init__(self, data):
        super().__init__(None, title="Seleziona una opzione")
        pannello = wx.Panel(self)
        
        self.domanda = data[0]
        self.opzioni = data[1]
        self.risposta = data[2]
        self.corretto = 0
		
        self.testo = wx.StaticText(pannello, label= self.domanda, pos=(5,10))
        self.rbox = wx.RadioBox(pannello, pos = (5,80), choices = self.opzioni ,
								   majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
		
        self.texto = wx.StaticText(pannello, label="", pos=(5,200))
         
        self.rbox.Bind(wx.EVT_RADIOBOX, self.domande)
		
    def domande(self, e):
        if self.rbox.GetStringSelection() == self.risposta:
            print(self.texto.SetLabel('Corretto! Chiudi la finestra per continuare.'))
            self.corretto = 1
        else:
            print(self.texto.SetLabel('Sbagliato!'))
        


def CheckChoice(Frame):
            if Frame.corretto == 1:
                global risposte_esatte
                risposte_esatte += 1
         
                    
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
        app = wx.App()
        Frame = Domande(data[risposte_esatte])
        Frame.Show()
        app.MainLoop()
        CheckChoice(Frame)

                
def redrawGameWindow():
    global walkCount
    win.blit(mapp, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0    
    else:
        win.blit(walk_icon, (icon_x,icon_y))
        walkCount = 0
        
    pygame.display.update() 

            
run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            run = False
            
    keep_move_mod(target_x[risposte_esatte], target_y[risposte_esatte])

    if risposte_esatte == 21:
        
        win.blit(walk_char, (icon_x,icon_y))
        walkCount = 0
        break   
                                                        
    redrawGameWindow() 
pygame.quit()