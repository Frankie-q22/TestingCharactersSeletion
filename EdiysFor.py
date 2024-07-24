#edit for BOTH
#edit for main menu
#TestingMenu Options

#LETS DO THIS ONE LAST TIME

import pygame
import sys
from Buttont import Buttons
from fighterEX import FighterEX

pygame.init()


#edit for character selection
import pygame

from fighterEX import FighterEX



#Creates Game Window
Screen_Width = 1000
Screen_Height = 600

Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("The Honor Of Fighting")


StartMenubackground = pygame.image.load("c:/Users/Frank/FFH/Backrounds/Menu.jpg").convert_alpha()
def display_Bg1():
 scaledBG = pygame.transform.scale(StartMenubackground,(Screen_Width, Screen_Height))
 Screen.blit(scaledBG,(0,0))
 
Characterselectbackround = pygame.image.load("c:/Users/Frank/FFH/Backrounds/BackCS.jpg").convert_alpha()
def display_Bg2():
 scaledBG = pygame.transform.scale(Characterselectbackround,(Screen_Width, Screen_Height))
 Screen.blit(scaledBG,(0,0))
 
def Font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("c:/Users/Frank/FFH/Font/Turok.ttf", size)

#Drawing the counter and point system
def lettersnumbers(text,font,text_color,x,y):
  img = font.render(text,True,text_color)
  Screen.blit (img, (x, y))
White = (255,255,255)
Yellow = (255,255,0)
Red = (255,0,0)
Teal = (75,177,180)
Maroon = (128,0,0)
DarkYellow = (164,136,0)
DarkTeal =(0,37,44)

scaleBTN1 = pygame.image.load("NearTransparent.png")
scaleBTN1 = pygame.transform.scale(scaleBTN1,(155, 30))
scaleBTN2 = pygame.image.load("NearTransparent.png")
scaleBTN2 = pygame.transform.scale(scaleBTN2,(100, 30))
scaleBTN3 = pygame.image.load("NearTransparent.png")
scaleBTN3 = pygame.transform.scale(scaleBTN3,(20, 30))

SPButton = Buttons((scaleBTN1),(200,200), "Single Player", Font(25), White, Red)
MPButton = Buttons((scaleBTN1),(200,200), "Multiplayer", Font(25), White, Red)

#define the font
#countingfont = pygame.font.Font("Turok.ttf",150)
#scorefont = pygame.font.Font("Turok.ttf",40)
#Wins = pygame.font.Font("Turok.ttf",50)
#WinsSmaller = pygame.font.Font("Turok.ttf",49)

#define the fighter sizes/sprites
BeetleSizeWidth = 100
BeetleSizeHeight = 100
BeetleScale = 8,2,9
BeetleOffset = [46,38],[43.5,38]
BeetleData01 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[2],BeetleOffset[0]]
BeetleData0 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[1],BeetleOffset[0]]
BeetleData1 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[0],BeetleOffset[0]]
BeetleData2 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[0],BeetleOffset[1]]

FarmerSizeWidth = 128
FarmerSizeHeight = 122.11
FarmerScale = 5.4,1.8
FarmerOffset =[47,58],[66,58]
FarmerData0 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale[1],FarmerOffset[0]]
FarmerData1 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale[0],FarmerOffset[0]]
FarmerData2 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale[0],FarmerOffset[1]]


GhostSizeWidth = 103
GhostSizeHeight = 102.125
GhostScale = 6,2.2
GhostOffset = [46,32.5],[42.5,32.5]
GhostData0 = [GhostSizeWidth,GhostSizeHeight,GhostScale[1],GhostOffset[0]]
GhostData1 = [GhostSizeWidth,GhostSizeHeight,GhostScale[0],GhostOffset[0]]
GhostData2 = [GhostSizeWidth,GhostSizeHeight,GhostScale[0],GhostOffset[1]]

LadySizeWidth = 82
LadySizeHeight = 104
LadyScale = 5,2
LadyOffset = [28,32],[28,32]
LadyData0 = [LadySizeWidth,LadySizeHeight,LadyScale[1],LadyOffset[0]]
LadyData1 = [LadySizeWidth,LadySizeHeight,LadyScale[0],LadyOffset[0]]
LadyData2 = [LadySizeWidth,LadySizeHeight,LadyScale[0],LadyOffset[1]]

MonkSizeWidth = 103
MonkSizeHeight = 103
MonkScale = 5,2
MonkOffset = [40,34],[40,34]
MonkData0 = [MonkSizeWidth,MonkSizeHeight,MonkScale[1],MonkOffset[0]]
MonkData1 = [MonkSizeWidth,MonkSizeHeight,MonkScale[0],MonkOffset[0]]
MonkData2 = [MonkSizeWidth,MonkSizeHeight,MonkScale[0],MonkOffset[1]]

NinjaSizeWidth = 93
NinjaSizeHeight = 92.11
NinjaScale = 6.3,2.5
NinjaOffset = [38,33],[38,33]
NinjaData0 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale[1],NinjaOffset[0]]
NinjaData1 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale[0],NinjaOffset[0]]
NinjaData2 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale[0],NinjaOffset[1]]

PirateSizeWidth = 100
PirateSizeHeight = 100
PirateScale = 7,2
PirateOffset = [40,45],[40,45]
PirateData0 = [PirateSizeWidth,PirateSizeHeight,PirateScale[1],PirateOffset[0]]
PirateData1 = [PirateSizeWidth,PirateSizeHeight,PirateScale[0],PirateOffset[0]]
PirateData2 = [PirateSizeWidth,PirateSizeHeight,PirateScale[0],PirateOffset[1]]

RoninSizeWidth = 200
RoninSizeHeight = 200
RoninScale = 3.8,1.5
RoninOffset = [90,75.5],[90,75.5]
RoninData0 = [RoninSizeWidth,RoninSizeHeight,RoninScale[1],RoninOffset[0]]
RoninData1 = [RoninSizeWidth,RoninSizeHeight,RoninScale[0],RoninOffset[0]]
RoninData2 = [RoninSizeWidth,RoninSizeHeight,RoninScale[0],RoninOffset[1]]

SamuraiSizeHeight = 200 
SamuraiSizeWidth = 200
SamuraiScale = 4.5,1.5
SamuraiOffset = [89,77],[89,77]
SamuraiData0 =[SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale[1],SamuraiOffset[0]]
SamuraiData1 = [SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale[0],SamuraiOffset[0]]
SamuraiData2 = [SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale[0],SamuraiOffset[1]]

SenseiSizeWidth = 100
SenseiSizeHeight = 99
SenseiScale = 5,2.1
SenseiOffset =[42,27],[42,27]
SenseiData0 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale[1],SenseiOffset[0]]
SenseiData1 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale[0],SenseiOffset[0]]
SenseiData2 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale[0],SenseiOffset[1]]


ShaolinSizeWidth = 126
ShaolinSizeHeight = 125
ShaolinScale = 2,1.4
ShaolinOffset = [80,80],[80,80]
ShaolinData0 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale[1],ShaolinOffset[0]]
ShaolinData1 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale[0],ShaolinOffset[0]]
ShaolinData2 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale[0],ShaolinOffset[1]]

YasukeSizeWidth = 100
YasukeSizeHeight = 100
YasukeScale = 5,1.8
YasukeOffset = [45,24],[45,24]
YasukeData0 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale[1],YasukeOffset[0]]
YasukeData1 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale[0],YasukeOffset[0]]
YasukeData2 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale[0],YasukeOffset[1]]


#load Spritesheets
Beetlesheet = pygame.image.load("FullBeetleee.png").convert_alpha()
Farmersheet = pygame.image.load("FullFarmer(Fixed).png").convert_alpha()
Ghostsheet = pygame.image.load("FullGhostTT.png").convert_alpha()
Ladysheet = pygame.image.load("FullllLady.png").convert_alpha()
Monksheet = pygame.image.load("FullMonk.png").convert_alpha()
Ninjasheet = pygame.image.load("FullNinja.png").convert_alpha()
Piratesheet = pygame.image.load("FullPirate.png").convert_alpha()
Roninsheet = pygame.image.load("FullRonin.png").convert_alpha()
Samuraisheet = pygame.image.load("FullSamurai.png").convert_alpha()
Senseisheet = pygame.image.load("FullSensei.png").convert_alpha()
Shaolinsheet = pygame.image.load("Shaolinnn.png").convert_alpha()
Yasukesheet = pygame.image.load("FullYasuke.png").convert_alpha()

#steps in each animation
BeetleAnimation = [4,8,2,2,4,4,4,4]
FarmerAnimation = [4,8,2,2,4,4,4,4]
GhostAnimation = [4,8,2,2,4,4,4,4]
LadyAnimation = [4,8,2,2,4,4,4,4,]
MonkAnimation =  [4,8,2,2,4,4,4,4]
NinjaAnimation = [4,8,2,2,4,4,4,4]
PirateAnimation = [4,8,2,2,4,4,4,4]
RoninAnimation = [4,8,2,2,4,4,3,7]
SamuraiAnimation =[8,8,2,2,6,6,4,6]
SenseiAnimation = [4,8,2,2,4,4,4,4]
ShaolinAnimation = [10,8,3,3,7,6,3,11]
YasukeAnimation = [4,8,2,2,4,4,4,4]

Beetle0= FighterEX(0,370,320,True,BeetleData0,Beetlesheet,BeetleAnimation)#2nd row
Beele01 = FighterEX(0,350,320,True,BeetleData01,Beetlesheet,BeetleAnimation)#2nd row
Farmer0=FighterEX(0,560,300,True,FarmerData0,Farmersheet,FarmerAnimation)#2nd row
Ghost0=FighterEX(0,700,86,True,GhostData0,Ghostsheet,GhostAnimation)#1st Row
Lady0=FighterEX(0,800,80,True,LadyData0,Ladysheet,LadyAnimation)#1st Row
Monk0=FighterEX(0,575,80,True,MonkData0,Monksheet,MonkAnimation)#1st Row
Ninja0=FighterEX(0,470,290,True,NinjaData0,Ninjasheet,NinjaAnimation)#2nd Row
Pirate0=FighterEX(0,700,320,True,PirateData0,Piratesheet,PirateAnimation)#2nd Row
Ronin0 = FighterEX(0,370,80,True,RoninData0,Roninsheet,RoninAnimation)#1st Row
Samurai0 = FighterEX(0,810,310,True,SamuraiData0,Samuraisheet,SamuraiAnimation)#2nd Row
Sensei0=FighterEX(0,470,80,True,SenseiData0,Senseisheet,SenseiAnimation)#1st Row
Shaolin0=FighterEX(0,400,490,True,ShaolinData0,Shaolinsheet,ShaolinAnimation)#3rd Row
Yasuke0 = FighterEX(0,490,420,True,YasukeData0,Yasukesheet,YasukeAnimation)#3rd Row



def CharacterSelectMenu():
    while True:
     clock 
        
        
     Mouse = pygame.mouse.get_pos()

     display_Bg2()
     lettersnumbers("Character Select", Font(45),DarkTeal, 375,10)
     lettersnumbers("Player 1", Font(30),DarkYellow, 100,90)
     lettersnumbers("Player 2", Font(30),White, 100,325)
     
     Beetle0.update()
     Beele01.update()
     Farmer0.update()
     Ghost0.update()
     Lady0.update()
     Monk0.update()
     Ninja0.update()
     Pirate0.update()
     Ronin0.update()
     Samurai0.update()
     Sensei0.update()
     Shaolin0.update()
     Yasuke0.update()  
     Beetle0.Draw(Screen)
     Farmer0.Draw(Screen)
     Ghost0.Draw(Screen)
     Lady0.Draw(Screen)
     Monk0.Draw(Screen)
     Ninja0.Draw(Screen)
     Pirate0.Draw(Screen)
     Ronin0.Draw(Screen)
     Samurai0.Draw(Screen)
     Sensei0.Draw(Screen)
     Shaolin0.Draw(Screen)
     Yasuke0.Draw(Screen)
     
     Beetle1buon = Buttons((scaleBTN3),(425,310), "1", Font(25), White, Red)
     Beetle1buon.changeColor(Mouse)
     Beetle1buon.update(Screen)
     Beetle2buon = Buttons((scaleBTN3),(425,350), "2", Font(25), White, Red)
     Beetle2buon.changeColor(Mouse) 
     Beetle2buon .update(Screen)
     Farmer1buon= Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Farmer1buon.changeColor(Mouse)
     Farmer1buon.update(Screen)
     Farmer2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Farmer2buon .changeColor(Mouse)
     Farmer2buon .update(Screen)
     Ghost1buon = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Ghost1buon.changeColor(Mouse)
     Ghost1buon.update(Screen)
     Ghost2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Ghost2buon.changeColor(Mouse)
     Ghost2buon.update(Screen)
     Lady1buon = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Lady1buon .changeColor(Mouse)
     Lady1buon .update(Screen)
     Lady2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Lady2buon.changeColor(Mouse)
     Lady2buon.update(Screen)
     Monk1buon= Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Monk1buon.changeColor(Mouse)
     Monk1buon.update(Screen)
     Monk2buon  = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Monk2buon.changeColor(Mouse)
     Monk2buon.update(Screen)
     Ninja1buon = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Ninja1buon.changeColor(Mouse)
     Ninja1buon.update(Screen)
     Ninja2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Ninja2buon.changeColor(Mouse)
     Ninja2buon.update(Screen)
     Pirate1buon = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Pirate1buon.changeColor(Mouse)
     Pirate1buon.update(Screen)
     Pirate2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Pirate2buon.changeColor(Mouse)
     Pirate2buon.update(Screen)
     Ronin1buon= Buttons((scaleBTN3),(45,100), "1", Font(25), White, Red)
     Ronin1buon.changeColor(Mouse)
     Ronin1buon.update(Screen)
     Ronin2buon = Buttons((scaleBTN3),(425,200), "2", Font(25), White, Red)
     Ronin2buon.changeColor(Mouse)
     Ronin2buon.update(Screen)
     Samurai1buon = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Samurai1buon.changeColor(Mouse)
     Samurai1buon.update(Screen)
     Samurai2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Samurai2buon.changeColor(Mouse)
     Samurai2buon.update(Screen)
     Sensei1buon = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Sensei1buon.changeColor(Mouse)
     Sensei1buon.update(Screen)
     Sensei2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Sensei2buon.changeColor(Mouse)
     Sensei2buon.update(Screen)
     Shaolin1buon = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Shaolin1buon.changeColor(Mouse)
     Shaolin1buon.update(Screen)
     Shaolin2buon = Buttons((scaleBTN3),(200,200), "2", Font(25), White, Red)
     Shaolin2buon.changeColor(Mouse)
     Shaolin2buon.update(Screen)
     Yasuke1buon  = Buttons((scaleBTN3),(200,200), "1", Font(25), White, Red)
     Yasuke1buon.changeColor(Mouse)
     Yasuke1buon.update(Screen)
     Yasuke2buon = Buttons((scaleBTN3),(20,10), "2", Font(25), White, Red)
     Yasuke2buon.changeColor(Mouse)
     Yasuke2buon.update(Screen)
     
     BACK = Buttons((scaleBTN2),(30,15), "BACK", Font(25), White, Red)

     BACK.changeColor(Mouse)
     BACK.update(Screen)
     
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(Mouse):
                    Starting_menu()
     pygame.display.update()
     

def Single_Player_Mode():
 while True:
     CharacterSelectMenu()
     pygame.display.update()

def Multiplayer_Mode():  
 while True:
     CharacterSelectMenu()
     pygame.display.update()


def Starting_menu():
 while True:
     S_M_mouse = pygame.mouse.get_pos()

     display_Bg1()
     pygame.display.set_caption("Fighting For Honor")
     lettersnumbers("Select a Mode:",Font(35),White,25,350)
     SPButton = Buttons((scaleBTN1),(115,415), "Single Player", Font(26), White, Red)
     MPButton = Buttons((scaleBTN1),(110,465), "Multiplayer", Font(26), White, Red)
     lettersnumbers("Select a Mode:",Font(35),White,25,350) 
    
     for button in [SPButton,MPButton]:
            button.changeColor(S_M_mouse)
            button.update(Screen)
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
             if SPButton.checkForInput(S_M_mouse):
                 #assign ai 
                 #self.Player = AI
                 CharacterSelectMenu() 
                 
             if MPButton.checkForInput(S_M_mouse):
                 #assign p2
                 #self.Player = 2
                 CharacterSelectMenu()    
     pygame.display.update()
     
clock = pygame.time.Clock()

def main_menu():
 clock 
        
 orig_surf = Font(25).render('Press "Space" To Start', Font(25), White)
 txt_surf = orig_surf.copy()
 # This surface is used to adjust the alpha of the txt_surf.
 alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
 alpha = 255  # The current alpha value of the surface.
    
 menu_state = "space_menu"  # Initial menu state
 
 
 while True:
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if menu_state == "space_menu":
                        menu_state = "starting_menu"


     if alpha > 0:
         # Reduce alpha each frame, but make sure it doesn't get below 0.
         alpha = max(alpha-4, 0)
         txt_surf = orig_surf.copy()  # Don't modify the original text surf.
         # Fill alpha_surf with this color to set its alpha value.
         alpha_surf.fill((255, 255, 255, alpha))
         # To make the text surface transparent, blit the transparent
         # alpha_surf onto it with the BLEND_RGBA_MULT flag.
         txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
         if alpha <=0: 
             # Reduce alpha each frame, but make sure it doesn't get below 0.
             alpha = max(alpha + 1, 200)
             txt_surf = orig_surf.copy()  # Don't modify the original text surf.
             # Fill alpha_surf with this color to set its alpha value.
             alpha_surf.fill((255, 255, 255, alpha))
             # To make the text surface transparent, blit the transparent
             # alpha_surf onto it with the BLEND_RGBA_MULT flag.
             txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

         Screen.fill((30, 30, 30))
         display_Bg1()
         Screen.blit(txt_surf, (600, 245))
         lettersnumbers("The Honor Of Fighting",Font(40),White,535,200) 
         
         if menu_state == "starting_menu":
            # Render and display the next menu
             Starting_menu()
         
         pygame.display.flip()
         pygame.display.update()
         clock.tick(30)
main_menu()
        