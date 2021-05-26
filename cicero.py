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
risposte_esatte_s = 0
risposte_esatte_d = 0

target_x = [379, 355, 320, 285, 230, 200, 255, 298, 356, 425, 535, 580, 584, 575, 565, 514, 473, 430, 460, 485, 500]
target_y = [355, 385, 400, 347, 290, 195, 165, 135, 100, 102, 103, 90, 115, 168, 210, 241, 244, 260, 310, 335, 345]


## Schema dati
### [Domanda, [opzioni], risposta]
data = [["Chi era Marco Tullio Cicerone?", ["Risposte :  ","Politico e filosofo greco", "Politico e filosofo latino", "Commerciante siciliano"], "Politico e filosofo latino"],
		["Dove è nato Marco Tullio Cicerone?", ["Risposte :  ", "Tuscoli           ", "Arpino           ", "Roma                "], "Arpino           "],
                ["C", ["Risposte :  ", "Tagliandosi le vene", "Bevendo della cicuta", "Di vecchiaia"], "Bevendo della cicuta"],
                ["Chi era soprannominato 'il maestro di ballo' ?", ["Risposte :  ", "Catone", "Pompeo                      ", "Ortensio"], "Ortensio"],
                ["Come muore il cugino Lucio di M. Cicerone?", ["Risposte :  ", "Tagliandosi le vene", "Bevendo della cicuta", "Di vecchiaia"], "Bevendo della cicuta"],
                ["C", ["Risposte :  ", "Famoso avvocato di Roma", "Governatore della Sicilia", "Coraggioso gladiatore macedone"], "Governatore della Sicilia"],
                ["Chi era Gaio Licinio Verre?", ["Risposte :  ", "Famoso avvocato di Roma", "Governatore della Sicilia", "Coraggioso gladiatore macedone"], "Governatore della Sicilia"],
                ["Chi fu il primo marito di Tullia?", ["Risposte :  ", "Dolabella", "Prassipede                  ", "Frugi"], "Frugi"],
                ["C", ["Risposte :  ", "Una protesta pacifica    ", "Una protesta violenta        ", "Una repressione violenta"], "Una protesta violenta        "],
                ["Cosa era la flagitatio?", ["Risposte :  ", "Una protesta pacifica    ", "Una protesta violenta        ", "Una repressione violenta"], "Una protesta violenta        "],
                ["Celio Rufo fu l'allievo di...", ["Risposte :  ", "Crasso", "Cesare                    ", "Cicerone"], "Cicerone"],
                ["C", ["Risposte :  ", "Crasso", "Cesare                    ", "Cicerone"], "Cicerone"],
                ["Gneo Pompeo Magno contro chi viene \nmandato a combattere per sei anni?", ["Risposte :  ", "A sedare rivolte in Macedonia", "Contro i pirati che stavano nel Mediterraneo", "Contro Crasso"], "Contro i pirati che stavano nel Mediterraneo"],
                ["Chi era Lucio Sergio Catilina?", ["Risposte :  ", "Un martire di religione cristiana  ", "Un nemico di Cicerone", "Amico di lunga data di Cicerone"], "Un nemico di Cicerone"],
                ["C", ["Risposte :  ", "Crasso", "Cesare                    ", "Cicerone"], "Cicerone"],
                ["Chi era Publio Clodio Pulcro?", ["Risposte :  ", "Il pontefice massimo  ", "Un politico romano amico di Cicerone", "Un politico romano nemico di Cicerone"], "Un politico romano nemico di Cicerone"],
                ["Da chi fu combattuta la battaglia \na Pharsalus?", ["Risposte :  ", "Pomepo e Crasso          ", "Cesare e Pompeo", "Antonio e Ottaviano"], "Cesare e Pompeo"], 
                ["C", ["Risposte :  ", "Crasso", "Cesare                    ", "Cicerone"], "Cicerone"],
                ["Chi ordina l'esecuzione di M. Cicerone?", ["Risposte :  ", "Ottaviano", "Cesare             ", "Antonio"], "Antonio"],
                ["M. Cicerone e Terenzia \nrimasero sempre sposati?", ["Risposte :  ", "No, dopo l'esilio di Cicerone, divorziarono", "Si, anche se per alcuni anni vissero separati", "si, morirono vittime di un attentato"], "No, dopo l'esilio di Cicerone, divorziarono"]]
    
                
 
data_d =[["Da chi studiò retorica M. Cicerone?", ["Risposte :  ", "Apollonio Molone", "Ortensio", "Epicuro"], "Apollonio Molone"], ["Cicerone aderiva alla scuola...", ["Risposte :  ", "Asiana", "Attica         ", "Rodiese"], "Rodiese"], ["Come veniva punito il parricipio?", ["Risposte :  ", "Con il lavoro forzato", "Con la poena culliei", "Con la decapitazione da parte della famiglia"], "Con la poena culliei"],
          ["Dove si recò M. Cicerone per scappare \nalla possibile vendetta di Lucio Cornelio Silla?", ["Risposte :  ", "Sicilia        ", "Grecia", "Macedonia"], "Grecia"], ["Chi fu a dare inizio al processo \na Gaio Licinio Verre?", ["Risposte :  ", "Stenio di Terme", "Publio Ovidio Nasone", "Gaio Popilio Lenate"], "Stenio di Terme"], ["A chi veniva affidata l'educazione \ndei giovani romani?", ["Risposte :  ", "Ai grammatici e ai rhetoris", "A pater e mater", "Agli schiavi istruiti"], "Ai grammatici e ai rhetoris"],
          ["Per cosa fu accusato Gaio Licinio Verre?", ["Risposte :  ", "Concussione e spionaggio", "Parricidio    ", "Omicidio"], "Concussione e spionaggio"], ["Chi amministrava i beni della moglie Terenzia?", ["Risposte :  ", "Clodio", "Tirone", "Filotimo"], "Filotimo"], ["Nelle antiche famiglie romane \ncos'era il famulus?", ["Risposte :  ", "L'animale domestico", "Il servo", "Il figlio esiliato"], "Il servo"],
          ["Chi incontra M. Cicerone appena sbarcato \na Brindisi dopo l'esilio?", ["Risposte :  ", "Cesare", "Terenzia   ", "Tullia"], "Tullia"], ["Il fedele schiavo Tirone di M. Cicerone \nsarà mai liberato?", ["Risposte :  ", "Si mentre Cicerone era ancora in vita", "Mai", "Solo dopo la morte di Cicerone"], "Si mentre Cicerone era ancora in vita"], ["Nell'Antica Roma, com'era la condizione della \ndonna rispetto a quella dell'uomo?", ["Risposte :  ", "La donna aveva pari diritti", "Era sottomessa all'autorità del padre", "Partecipava attivamente alla vita sociale"], "Era sottomessa all'autorità del padre"],
          ["Come morì Lucio Sergio Catilina?", ["Risposte :  ", "Suicidato", "In esilio a Marsiglia    ", "In battaglia a Pistoia"], "In battaglia a Pistoia"], ["Da chi fu formato il primo triumvirato?", ["Risposte :  ", "Lepido - Crasso - Pompeo", "Cesare - Crasso - Pompeo", "Ottaviano - Antonio - Lepido"], "Cesare - Crasso - Pompeo"], ["Qual era la condizione dello straniero \nnell'Antica Roma?", ["Risposte :  ", "Gli veniva data la cittadinanza romana", "Era accolto come un foederato (alleato)", "Veniva segregato a vita nelle prigioni"], "Era accolto come un foederato (alleato)"],
          ["M. Cicerone diventò console insieme a chi?", ["Risposte :  ", "Catilina       ", "Crasso", "Hybrida"], "Hybrida"], ["Come e da chi venne ucciso \nPublio Clodio Pulcro?", ["Risposte :  ", "Venne ucciso in battaglia da Cesare in Gallia", "Venne ucciso da Milone sul ciglio di una strada", "Cicerone lo proclamò nemico di Stato"], "Venne ucciso da Milone sul ciglio di una strada"],["Cos'erano i tributi?", ["Risposte :  ", "Le tasse che doveva pagare il popolo", "Le donazioni volontarie dell'aristocrazia", "Coloro che garantivano la sicurezza della plebe"], "Le tasse che doveva pagare il popolo"],
          ["Cosa riguarda il Commentarius \nde bello Gallico?", ["Risposte :  ", "Le rivolte dei popoli germani sedate da Catone", "La guerra in Gallia con il comandante Pompeo", "La guerra in Gallia con il comandante Cesare"], "La guerra in Gallia con il comandante Cesare"], ["Da chi venne dichiarato nemico pubblico \n e dove si ritirò in esilio M. Cicerone?", ["Risposte :  ", "Clodio, Sicilia", "Cesare, Macedonia", "Clodio, Macedonia"], "Clodio, Macedonia"], ["Com'erano chiamati i trascinatori del popolo e \nperchè furono così importanti?", ["Risposte :  ", "Profeti, che narravano le gesta delle divinità", "Demagoghi, perchè lusingavano il popolo", "Il massimo comandante, colui che guidava il popolo"], "Demagoghi, perchè lusingavano il popolo"], ["Cos'era il Mos Maiorum?", ["Risposte :  ", "Rappresentava i valori della tradizione romana", "La suprema autorità politica e religiosa", "Il titolo che veniva dato ai nobili"], "Rappresentava i valori della tradizione romana"]]
        




          

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
        
        
        self.texto = wx.StaticText(pannello, label="", pos=(30,175))
        self.texto.SetFont(font)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.domande)


    def domande(self, e):
        if self.rbox.GetStringSelection() != self.risposta:
            dial = wx.MessageDialog(None, "Male fecisti!", "Error")
            dial.ShowModal()
            self.Destroy()
            self.sbagliato = 1
    
        else:
            print(self.texto.SetLabel('Bene fecisti! Chiudi la finestra per continuare.'))
            self.corretto = 1
            
            
class vinto(wx.Frame):
    def __init__(self):
        super().__init__(None, pos = (675, 330), size=(568, 440), title="Hai vinto!")
        pannello = wx.Panel(self)
        png = wx.Image('/Users/delfo/OneDrive/Desktop/mia/7.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
        
        
        
class perso(wx.Frame):
    def __init__(self):
        super().__init__(None, pos = (675, 330), size=(568, 440), title="Hai perso!")
        pannello = wx.Panel(self)
        png = wx.Image('/Users/delfo/OneDrive/Desktop/mia/7.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))

class uno(wx.Frame):
    def __init__(self):
        super().__init__(None, pos = (675, 330), size=(568, 440), title="Complimenti!")
        pannello = wx.Panel(self)
        png = wx.Image('/Users/delfo/OneDrive/Desktop/mia/1.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))
        self.Destroy()
        
def CheckChoice(Frame):
      if Frame.corretto == 1:
         global risposte_esatte
         global risposte_esatte_s
         risposte_esatte += 1
      if Frame.sbagliato == 1:
          risposte_esatte -= 1
          if risposte_esatte_s == 3:
              risposte_esatte_s = 0
          if risposte_esatte_s == 6:
              risposte_esatte_s = 3
          if risposte_esatte_s == 9:
              risposte_esatte_s = 6
          if risposte_esatte_s == 12:
              risposte_esatte_s = 9
          if risposte_esatte_s == 15:
              risposte_esatte_s = 12
          if risposte_esatte_s == 18:
              risposte_esatte_s = 15
          if risposte_esatte_s == 21:
              risposte_esatte_s = 18
	
          
def CheckChoice2(Frame):
      if Frame.corretto == 1:
         global risposte_esatte_s
         global risposte_esatte
         risposte_esatte_s += 1
         if risposte_esatte_s == 3:
             risposte_esatte += 1 
             risposte_esatte_s = 3
         if risposte_esatte_s == 6:
             risposte_esatte += 1 
             risposte_esatte_s = 6
         if risposte_esatte_s == 9:
             risposte_esatte += 1 
             risposte_esatte_s = 9
         if risposte_esatte_s == 12:
             risposte_esatte += 1 
             risposte_esatte_s = 12
         if risposte_esatte_s == 15:
             risposte_esatte += 1 
             risposte_esatte_s = 15
         if risposte_esatte_s == 18:
             risposte_esatte += 1 
             risposte_esatte_s = 18
         if risposte_esatte_s == 21:
             risposte_esatte += 1 
             risposte_esatte_s = 21
             
      if Frame.sbagliato == 1 and risposte_esatte_s == 0:
         risposte_esatte -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 1:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 2:
          risposte_esatte_s -= 1

      if Frame.sbagliato == 1 and risposte_esatte_s == 3:
         risposte_esatte -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 4:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 5:
          risposte_esatte_s -= 1
          
      if Frame.sbagliato == 1 and risposte_esatte_s == 6:
         risposte_esatte -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 7:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 8:
          risposte_esatte_s -= 1
          
      if Frame.sbagliato == 1 and risposte_esatte_s == 9:
         risposte_esatte -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 10:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 11:
          risposte_esatte_s -= 1

      if Frame.sbagliato == 1 and risposte_esatte_s == 12:
         risposte_esatte -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 13:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 14:
          risposte_esatte_s -= 1

      if Frame.sbagliato == 1 and risposte_esatte_s == 15:
         risposte_esatte -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 16:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 17:
          risposte_esatte_s -= 1
          
      if Frame.sbagliato == 1 and risposte_esatte_s == 18:
         risposte_esatte -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 19:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 20:
          risposte_esatte_s -= 1
      if Frame.sbagliato == 1 and risposte_esatte_s == 21:
          risposte_esatte_s -= 1
       

          
def keep_move_mod(target_x, target_y):
    global icon_x
    global icon_y
    global risposte_esatte
    global risposte_esatte_s
    
    if icon_x == target_x or  icon_y == target_y:
        if risposte_esatte == 2:
            app = wx.App()
            Frame = Domande(data_d[risposte_esatte_s])
            Frame.Show()
            app.MainLoop()
            CheckChoice2(Frame)

            
        elif risposte_esatte == 5:
            app = wx.App()
            Frame = Domande(data_d[risposte_esatte_s])
            Frame.Show()
            app.MainLoop()
            CheckChoice2(Frame)
            
        elif risposte_esatte == 8:
            app = wx.App()
            Frame = Domande(data_d[risposte_esatte_s])
            Frame.Show()
            app.MainLoop()
            CheckChoice2(Frame)
            
        elif risposte_esatte == 11:
            app = wx.App()
            Frame = Domande(data_d[risposte_esatte_s])
            Frame.Show()
            app.MainLoop()
            CheckChoice2(Frame)
            
        elif risposte_esatte == 14:
            app = wx.App()
            Frame = Domande(data_d[risposte_esatte_s])
            Frame.Show()
            app.MainLoop()
            CheckChoice2(Frame)
            
        elif risposte_esatte == 17:
            app = wx.App()
            Frame = Domande(data_d[risposte_esatte_s])
            Frame.Show()
            app.MainLoop()
            CheckChoice2(Frame)
            
        elif risposte_esatte == 20:
            app = wx.App()
            Frame = Domande(data_d[risposte_esatte_s])
            Frame.Show()
            app.MainLoop()
            CheckChoice2(Frame)
        
        else:
            app = wx.App()
            Frame = Domande(data[risposte_esatte])
            Frame.Show()
            app.MainLoop()
            CheckChoice(Frame)
    else:
        coef = (target_y - icon_y) / (target_x - icon_x)
        sign_x = (target_x - icon_x)/abs(target_x - icon_x)
        sign_y = (target_y - icon_y)/abs(target_y - icon_y)
        icon_x += 1 * sign_x
        icon_y += abs(coef)  * sign_y
    
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
    
    if risposte_esatte == 3:
        app = wx.App()
        Frame = vinto()
        Frame.Show()
        app.MainLoop()
    
    if risposte_esatte == 21:
        app = wx.App()
        Frame = vinto()
        Frame.Show()
        app.MainLoop()
        win.blit(walk_char, (icon_x,icon_y))
        walkCount = 0
        
      
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
