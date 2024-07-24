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




#define the fighter sizes/sprites
BeetleSizeWidth = 100
BeetleSizeHeight = 100
BeetleScale = 8
BeetleOffset = [46,38],[43.5,38]
BeetleData1 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale,BeetleOffset[0]]
BeetleData2 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale,BeetleOffset[1]]

FarmerSizeWidth = 128
FarmerSizeHeight = 122.11
FarmerScale = 5.4
FarmerOffset =[47,58],[66,58]
FarmerData1 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale,FarmerOffset[0]]
FarmerData2 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale,FarmerOffset[1]]


GhostSizeWidth = 103
GhostSizeHeight = 102.125
GhostScale = 6
GhostOffset = [46,32.5],[42.5,32.5]
GhostData1 = [GhostSizeWidth,GhostSizeHeight,GhostScale,GhostOffset[0]]
GhostData2 = [GhostSizeWidth,GhostSizeHeight,GhostScale,GhostOffset[1]]

LadySizeWidth = 82
LadySizeHeight = 104
LadyScale = 5
LadyOffset = [28,32],[28,32]
LadyData1 = [LadySizeWidth,LadySizeHeight,LadyScale,LadyOffset[0]]
LadyData2 = [LadySizeWidth,LadySizeHeight,LadyScale,LadyOffset[1]]

MonkSizeWidth = 103
MonkSizeHeight = 103
MonkScale = 5
MonkOffset = [40,34],[40,34]
MonkData1 = [MonkSizeWidth,MonkSizeHeight,MonkScale,MonkOffset[0]]
MonkData2 = [MonkSizeWidth,MonkSizeHeight,MonkScale,MonkOffset[1]]

NinjaSizeWidth = 93
NinjaSizeHeight = 92.11
NinjaScale = 6.3
NinjaOffset = [38,33],[38,33]
NinjaData1 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale,NinjaOffset[0]]
NinjaData2 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale,NinjaOffset[1]]

PirateSizeWidth = 100
PirateSizeHeight = 100
PirateScale = 7
PirateOffset = [40,45],[40,45]
PirateData1 = [PirateSizeWidth,PirateSizeHeight,PirateScale,PirateOffset[0]]
PirateData2 = [PirateSizeWidth,PirateSizeHeight,PirateScale,PirateOffset[1]]
#need to edit
RedSamuraiSizeWidth = 200
RedSamuraiSizeHeight = 198
RedSamuraiScale = 5
RedSamuraiOffset = [80,80],[80,80]
RedSamuraiData1 = [RedSamuraiSizeWidth,RedSamuraiSizeHeight,RedSamuraiScale,RedSamuraiOffset[0]]
RedSamuraiData2 = [RedSamuraiSizeWidth,RedSamuraiSizeHeight,RedSamuraiScale,RedSamuraiOffset[1]]

RoninSizeWidth = 200
RoninSizeHeight = 200
RoninScale = 3.8
RoninOffset = [90,75.5],[90,75.5]
RoninData1 = [RoninSizeWidth,RoninSizeHeight,RoninScale,RoninOffset[0]]
RoninData2 = [RoninSizeWidth,RoninSizeHeight,RoninScale,RoninOffset[1]]

SamuraiSizeHeight = 200 
SamuraiSizeWidth = 200
SamuraiScale = 4.5
SamuraiOffset = [89,77],[89,77]
SamuraiData1 = [SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale,SamuraiOffset[0]]
SamuraiData2 = [SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale,SamuraiOffset[1]]

SenseiSizeWidth = 100
SenseiSizeHeight = 99
SenseiScale = 5
SenseiOffset =[42,27],[42,27]
SenseiData1 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale,SenseiOffset[0]]
SenseiData2 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale,SenseiOffset[1]]

#need to edit
ShaolinSizeWidth = 125
ShaolinSizeHeight = 125
ShaolinScale = 2
ShaolinOffset = [80,80],[80,80]
ShaolinData1 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale,ShaolinOffset[0]]
ShaolinData2 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale,ShaolinOffset[1]]

YasukeSizeWidth = 100
YasukeSizeHeight = 100
YasukeScale = 5
YasukeOffset = [45,24],[45,24]
YasukeData1 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale,YasukeOffset[0]]
YasukeData2 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale,YasukeOffset[1]]


#load Spritesheets
Beetlesheet = pygame.image.load("FullBeetleee.png").convert_alpha()
Farmersheet = pygame.image.load("FullFarmer(Fixed).png").convert_alpha()
Ghostsheet = pygame.image.load("FullGhostTT.png").convert_alpha()
Ladysheet = pygame.image.load("FullllLady.png").convert_alpha()
Monksheet = pygame.image.load("FullMonk.png").convert_alpha()
Ninjasheet = pygame.image.load("FullNinja.png").convert_alpha()
Piratesheet = pygame.image.load("FullPirate.png").convert_alpha()
RedSamuraisheet = pygame.image.load("FullRedSamurai.png").convert_alpha()
Roninsheet = pygame.image.load("FullRonin.png").convert_alpha()
Samuraisheet = pygame.image.load("FullSamurai.png").convert_alpha()
Senseisheet = pygame.image.load("FullSensei.png").convert_alpha()
Shaolinsheet = pygame.image.load("FullShaolin(Fixed).png").convert_alpha()
Yasukesheet = pygame.image.load("FullYasuke.png").convert_alpha()

#steps in each animation
BeetleAnimation = [4,8,2,2,4,4,4,4]
FarmerAnimation = [4,8,2,2,4,4,4,4]
GhostAnimation = [4,8,2,2,4,4,4,4]
LadyAnimation = [4,8,2,2,4,4,4,4,]
MonkAnimation =  [4,8,2,2,4,4,4,4]
NinjaAnimation = [4,8,2,2,4,4,4,4]
PirateAnimation = [4,8,2,2,4,4,4,4]
RedSamuraiAnimation = [4,8,2,2,4,4,4,4]
RoninAnimation = [4,8,2,2,4,4,3,7]
SamuraiAnimation =[8,8,2,2,6,6,4,6]
SenseiAnimation = [4,8,2,2,4,4,4,4]
ShaolinAnimation = [10,8,3,3,7,6,3,11]
YasukeAnimation = [4,8,2,2,4,4,4,4]





#Creates Game Window
Screen_Width = 1000
Screen_Height = 600

Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("The Honor Of Fighting")


StartMenubackground = pygame.image.load("c:/Users/Frank/FFH/Backrounds/Menu.jpg").convert_alpha()
def display_Bg1():
 scaledBG = pygame.transform.scale(StartMenubackground,(Screen_Width, Screen_Height))
 Screen.blit(scaledBG,(0,0))
 
Characterselectbackround = pygame.image.load("c:/Users/Frank/FFH/Backrounds/Characterselect.jpg").convert_alpha()
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


scaleBTN1 = pygame.image.load("ButtonFolder/NearTransparent.png")
scaleBTN1 = pygame.transform.scale(scaleBTN1,(155, 30))
scaleBTN2 = pygame.image.load("ButtonFolder/NearTransparent.png")
scaleBTN2 = pygame.transform.scale(scaleBTN2,(100, 30))

SPButton = Buttons((scaleBTN1),(200,200), "Single Player", Font(25), White, Red)
MPButton = Buttons((scaleBTN1),(200,200), "Multiplayer", Font(25), White, Red)

#define the font
#countingfont = pygame.font.Font("Turok.ttf",150)
#scorefont = pygame.font.Font("Turok.ttf",40)
#Wins = pygame.font.Font("Turok.ttf",50)
#WinsSmaller = pygame.font.Font("Turok.ttf",49)




def CharacterSelectMenu():
    while True:
     Mouse = pygame.mouse.get_pos()

     display_Bg2()
     lettersnumbers("Character Select", Font(45),White, 600,50)
     lettersnumbers("Player 1", Font(30),White, 100,90)
     lettersnumbers("Player 2", Font(30),White, 100,325)
     
     Beetle2= FighterEX(0,700,360,True,BeetleData2,Beetlesheet,BeetleAnimation)
     Farmer2=FighterEX(0,700,360,True,FarmerData2,Farmersheet,FarmerAnimation)
     Ghost2=FighterEX(0,700,360,True,GhostData2,Ghostsheet,GhostAnimation)
     Lady2=FighterEX(0,700,360,True,LadyData2,Ladysheet,LadyAnimation)
     Monk2=FighterEX(0,700,360,True,MonkData2,Monksheet,MonkAnimation)
     Ninja2=FighterEX(0,700,360,True,NinjaData2,Ninjasheet,NinjaAnimation)
     Pirate2=FighterEX(0,700,360,True,PirateData2,Piratesheet,PirateAnimation)
     RedSamurai2=FighterEX(0,700,360,True,RedSamuraiData2,RedSamuraisheet,RedSamuraiAnimation)
     Ronin2 = FighterEX(0,700,360,True,RoninData2,Roninsheet,RoninAnimation)
     Samurai2 = FighterEX(0,700,360,True,SamuraiData2,Samuraisheet,SamuraiAnimation)
     Sensei2=FighterEX(0,700,360,True,SenseiData2,Senseisheet,SenseiAnimation)
     Shaolin2=FighterEX(0,700,360,True,ShaolinData2,Shaolinsheet,ShaolinAnimation)
     Yasuke2 = FighterEX(0,700,360,True,YasukeData2,Yasukesheet,YasukeAnimation)
     

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
        