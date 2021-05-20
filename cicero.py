import wx
import pygame

pygame.init()

backg = pygame.image.load('/Users/delfo/OneDrive/Desktop/mia/cicero_map3.png')
mapp = pygame.transform.scale(backg, (640, 480))
icon = pygame.image.load('/Users/delfo/OneDrive/Desktop/mia/colosseum.jpeg')
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
data = [["Chi era Marco Tullio Cicerone?", ["Risposte :  ","Politico e filosofo greco", "Politico e filosofo latino", "Commerciante siciliano"], "Politico e filosofo latino"],
		["Dove è nato Marco Tullio Cicerone?", ["Risposte :  ", "Tuscoli           ", "Arpino           ", "Roma                "], "Arpino           "],
### 3 domande   [["Chi incontra M. Cicerone appena sbarcato a Brindisi dopo l'esilio?", ["Risposte :  ", "Tagliandosi le vene", "Bevendo della cicuta", "Di vecchiaia"], "Bevendo della cicuta"], ["Come muore ", ["Risposte :  ", "Tagliandosi le vene", "Bevendo della cicuta", "Di vecchiaia"], "Bevendo della cicuta"], [" M. Cicerone?", ["Risposte :  ", "Tagliandosi le vene", "Bevendo della cicuta", "Di vecchiaia"], "Bevendo della cicuta"]],
		["Come muore il cugino Lucio di M. Cicerone?", ["Risposte :  ", "Tagliandosi le vene", "Bevendo della cicuta", "Di vecchiaia"], "Bevendo della cicuta"],
                ["Chi era soprannominato 'il maestro di ballo' ?", ["Risposte :  ", "Catone", "Pompeo                      ", "Ortensio"], "Ortensio"],
                ["Chi era Gaio Licinio Verre?", ["Risposte :  ", "Famoso avvocato di Roma", "Governatore della Sicilia", "Coraggioso gladiatore macedone"], "Governatore della Sicilia"],
                ["Chi fu il primo marito di Tullia?", ["Risposte :  ", "Dolabella", "Prassipede                  ", "Frugi"], "Frugi"],
                ["Cosa era la flagitatio?", ["Risposte :  ", "Una protesta pacifica    ", "Una protesta violenta        ", "Una repressione violenta"], "Una protesta violenta        "], 
                ["Celio Rufo fu l'allievo di...", ["Risposte :  ", "Crasso", "Cesare                    ", "Cicerone"], "Cicerone"],
                ["Gneo Pompeo Magno contro chi viene \n mandato a combattere per sei anni?", ["Risposte :  ", "A sedare rivolte in Macedonia", "Contro i pirati che stavano nel Mediterraneo", "Contro Crasso"], "Contro i pirati che stavano nel Mediterraneo"],
                ["Chi era Lucio Sergio Catilina?", ["Risposte :  ", "Un martire di religione cristiana  ", "Un nemico di Cicerone", "Amico di lunga data di Cicerone"], "Un nemico di Cicerone"],
                ["Chi era Publio Clodio Pulcro?", ["Risposte :  ", "Il pontefice massimo durante la carica di Cicerone", "Un politico romano amico di Cicerone", "Un politico romano nemico di Cicerone"], "Un politico romano nemico di Cicerone"],
                ["Da chi fu combattuta la battaglia \n a Pharsalus?", ["Risposte :  ", "Pomepo e Crasso          ", "Cesare e Pompeo", "Antonio e Ottaviano"], "Cesare e Pompeo"], 
                ["Chi ordina l'esecuzione di M. Cicerone?", ["Risposte :  ", "Ottaviano", "Cesare             ", "Antonio"], "Antonio"]]
 

class Domande(wx.Frame):

    def __init__(self, data):
        super().__init__(None, pos = (740, 400), size= (450, 250), title="Seleziona una opzione")
        pannello = wx.Panel(self)
        font = wx.Font(14,  wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        
        self.domanda = data[0]
        self.opzioni = data[1]
        self.risposta = data[2]
        self.corretto = 0
        self.sbagliato = 0
        self.pannello = pannello
		
        self.testo = wx.StaticText(pannello, label= self.domanda, pos=(5,10))
        self.rbox = wx.RadioBox(pannello, pos = (130, 60), choices = self.opzioni,
								   majorDimension = 1)
        
        self.pannello.SetBackgroundColour( wx.Colour( 245, 245, 220 ))
        self.testo.SetFont(font)
        
        
        self.texto = wx.StaticText(pannello, label="", pos=(30,170))
        self.texto.SetFont(font)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.domande)
        

    def domande(self, e):
        if self.rbox.GetStringSelection() != self.risposta:
            dial = wx.MessageDialog(None, "Sbagliato", "Errore")
            dial.ShowModal()
            self.Destroy()
            self.sbagliato = 1
    
        else:
            print(self.texto.SetLabel('Corretto! Chiudi la finestra per continuare.'))
            self.corretto = 1

class vinto(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Hai vinto!")
        pannello = wx.Panel(self)
        self.testo = wx.StaticText(pannello, label= ('Vincisti!'), pos=(5,10))
class perso(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Hai perso!")
        pannello = wx.Panel(self)
        self.testo = wx.StaticText(pannello, label= ('Perdidisti!'), pos=(5,10))
        
def CheckChoice(Frame):
            if Frame.corretto == 1:
                global risposte_esatte
                risposte_esatte += 1
            if Frame.sbagliato == 1:
                risposte_esatte -= 1
         
                    
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
        app = wx.App()
        Frame = vinto()
        Frame.Show()
        app.MainLoop()
        win.blit(walk_char, (icon_x,icon_y))
        walkCount = 0
        break
    if  risposte_esatte == -1:
        app = wx.App()
        Frame = perso()
        Frame.Show()
        app.MainLoop()
        win.blit(walk_icon, (icon_x,icon_y))
        walkCount = 0
        break
                                                        
    redrawGameWindow() 
pygame.quit()



