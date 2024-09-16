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
Screen_Width =  1000
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
BeetleScale = 8,2,9,4.7
BeetleOffset = [46,38],[43.5,38]
BeetleData01 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[2],BeetleOffset[0]]
BeetleData0 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[1],BeetleOffset[0]]
BeetleData1 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[0],BeetleOffset[0]]
BeetleData2 = [BeetleSizeWidth,BeetleSizeHeight,BeetleScale[0],BeetleOffset[1]]
BeetleDataHover =[BeetleSizeWidth,BeetleSizeHeight,BeetleScale[3],BeetleOffset[1]]

FarmerSizeWidth = 128
FarmerSizeHeight = 122.11
FarmerScale = 5.4,1.8,4
FarmerOffset =[47,58],[66,58]
FarmerData0 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale[1],FarmerOffset[0]]
FarmerData1 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale[0],FarmerOffset[0]]
FarmerData2 = [FarmerSizeWidth,FarmerSizeHeight,FarmerScale[0],FarmerOffset[1]]
FarmerDataHover =[FarmerSizeWidth,FarmerSizeHeight,FarmerScale[2],FarmerOffset[1]]

GhostSizeWidth = 103
GhostSizeHeight = 102.125
GhostScale = 6,2.2,4.5
GhostOffset = [46,32.5],[42.5,32.5]
GhostData0 = [GhostSizeWidth,GhostSizeHeight,GhostScale[1],GhostOffset[0]]
GhostData1 = [GhostSizeWidth,GhostSizeHeight,GhostScale[0],GhostOffset[0]]
GhostData2 = [GhostSizeWidth,GhostSizeHeight,GhostScale[0],GhostOffset[1]]
GhostDataHover=[GhostSizeWidth,GhostSizeHeight,GhostScale[2],GhostOffset[1]]

LadySizeWidth = 82
LadySizeHeight = 104
LadyScale = 5,2,4.2
LadyOffset = [28,32],[28,32]
LadyData0 = [LadySizeWidth,LadySizeHeight,LadyScale[1],LadyOffset[0]]
LadyData1 = [LadySizeWidth,LadySizeHeight,LadyScale[0],LadyOffset[0]]
LadyData2 = [LadySizeWidth,LadySizeHeight,LadyScale[0],LadyOffset[1]]
LadyDataHover=[LadySizeWidth,LadySizeHeight,LadyScale[2],LadyOffset[1]]

MonkSizeWidth = 103
MonkSizeHeight = 103
MonkScale = 5,2,4.3
MonkOffset = [40,34],[40,34]
MonkData0 = [MonkSizeWidth,MonkSizeHeight,MonkScale[1],MonkOffset[0]]
MonkData1 = [MonkSizeWidth,MonkSizeHeight,MonkScale[0],MonkOffset[0]]
MonkData2 = [MonkSizeWidth,MonkSizeHeight,MonkScale[0],MonkOffset[1]]
MonkDataHover=[MonkSizeWidth,MonkSizeHeight,MonkScale[2],MonkOffset[1]]

NinjaSizeWidth = 93
NinjaSizeHeight = 92.11
NinjaScale = 6.3,2.5,4.7
NinjaOffset = [38,33],[38,33]
NinjaData0 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale[1],NinjaOffset[0]]
NinjaData1 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale[0],NinjaOffset[0]]
NinjaData2 = [NinjaSizeWidth,NinjaSizeHeight,NinjaScale[0],NinjaOffset[1]]
NinjaDataHover=[NinjaSizeWidth,NinjaSizeHeight,NinjaScale[2],NinjaOffset[1]]

PirateSizeWidth = 100
PirateSizeHeight = 100
PirateScale = 7,2,4.3
PirateOffset = [40,45],[40,45]
PirateData0 = [PirateSizeWidth,PirateSizeHeight,PirateScale[1],PirateOffset[0]]
PirateData1 = [PirateSizeWidth,PirateSizeHeight,PirateScale[0],PirateOffset[0]]
PirateData2 = [PirateSizeWidth,PirateSizeHeight,PirateScale[0],PirateOffset[1]]
PirateDataHover=[PirateSizeWidth,PirateSizeHeight,PirateScale[2],PirateOffset[1]]

RoninSizeWidth = 200
RoninSizeHeight = 200
RoninScale = 3.8,1.5,3
RoninOffset = [90,75.5],[90,75.5]
RoninData0 = [RoninSizeWidth,RoninSizeHeight,RoninScale[1],RoninOffset[0]]
RoninData1 = [RoninSizeWidth,RoninSizeHeight,RoninScale[0],RoninOffset[0]]
RoninData2 = [RoninSizeWidth,RoninSizeHeight,RoninScale[0],RoninOffset[1]]
RoninDataHover=[RoninSizeWidth,RoninSizeHeight,RoninScale[2],RoninOffset[1]]

SamuraiSizeHeight = 200 
SamuraiSizeWidth = 200
SamuraiScale = 4.5,1.5,3.2
SamuraiOffset = [89,77],[89,77]
SamuraiData0 =[SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale[1],SamuraiOffset[0]]
SamuraiData1 = [SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale[0],SamuraiOffset[0]]
SamuraiData2 = [SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale[0],SamuraiOffset[1]]
SamuraiDataHover=[SamuraiSizeWidth,SamuraiSizeHeight,SamuraiScale[2],SamuraiOffset[1]]

SenseiSizeWidth = 100
SenseiSizeHeight = 99
SenseiScale = 5,2.1,4.5
SenseiOffset =[42,27],[42,27]
SenseiData0 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale[1],SenseiOffset[0]]
SenseiData1 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale[0],SenseiOffset[0]]
SenseiData2 = [SenseiSizeWidth,SenseiSizeHeight,SenseiScale[0],SenseiOffset[1]]
SenseiDataHover=[SenseiSizeWidth,SenseiSizeHeight,SenseiScale[2],SenseiOffset[1]]

ShaolinSizeWidth = 126
ShaolinSizeHeight = 125
ShaolinScale = 2,1.4,3.2
ShaolinOffset = [80,80],[80,80]
ShaolinData0 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale[1],ShaolinOffset[0]]
ShaolinData1 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale[0],ShaolinOffset[0]]
ShaolinData2 = [ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale[0],ShaolinOffset[1]]
ShaolinDataHover=[ShaolinSizeWidth,ShaolinSizeHeight,ShaolinScale[2],ShaolinOffset[1]]

YasukeSizeWidth = 100
YasukeSizeHeight = 100
YasukeScale = 5,1.8,4.5
YasukeOffset = [45,24],[45,24]
YasukeData0 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale[1],YasukeOffset[0]]
YasukeData1 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale[0],YasukeOffset[0]]
YasukeData2 = [YasukeSizeWidth,YasukeSizeHeight,YasukeScale[0],YasukeOffset[1]]
YasukeDataHover=[YasukeSizeWidth,YasukeSizeHeight,YasukeScale[2],YasukeOffset[1]]

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
Farmer0=FighterEX(0,560,300,True,FarmerData0,Farmersheet,FarmerAnimation)#2nd row
Ghost0=FighterEX(0,700,86,True,GhostData0,Ghostsheet,GhostAnimation)#1st Row
Lady0=FighterEX(0,800,80,True,LadyData0,Ladysheet,LadyAnimation)#1st Row
Monk0=FighterEX(0,575,80,True,MonkData0,Monksheet,MonkAnimation)#1st Row
Ninja0=FighterEX(0,470,290,True,NinjaData0,Ninjasheet,NinjaAnimation)#2nd Row
Pirate0=FighterEX(0,700,310,True,PirateData0,Piratesheet,PirateAnimation)#2nd Row
Ronin0 = FighterEX(0,370,80,True,RoninData0,Roninsheet,RoninAnimation)#1st Row
Samurai0 = FighterEX(0,810,300,True,SamuraiData0,Samuraisheet,SamuraiAnimation)#2nd Row
Sensei0=FighterEX(0,470,80,True,SenseiData0,Senseisheet,SenseiAnimation)#1st Row
Shaolin0=FighterEX(0,510,490,True,ShaolinData0,Shaolinsheet,ShaolinAnimation)#3rd Row
Yasuke0 = FighterEX(0,650,420,True,YasukeData0,Yasukesheet,YasukeAnimation)#3rd Row

BeetleHovered1 = FighterEX(0,120,200,True,BeetleDataHover,Beetlesheet,BeetleAnimation)#1st Row
BeetleHovered2 = FighterEX(0,120,445,True,BeetleDataHover,Beetlesheet,BeetleAnimation)#1st Row
FarmerHovered1 = FighterEX(0,120,170,True,FarmerDataHover,Farmersheet,FarmerAnimation)#2nd row
FarmerHovered2 = FighterEX(0,120,425,True,FarmerDataHover,Farmersheet,FarmerAnimation)
GhostHovered1 = FighterEX(0,120,175,True,GhostDataHover,Ghostsheet,GhostAnimation)#1st Row
GhostHovered2 = FighterEX(0,120,420,True,GhostDataHover,Ghostsheet,GhostAnimation)
LadyHovered1 = FighterEX(0,95,152,True,LadyDataHover,Ladysheet,LadyAnimation)#1st Row
LadyHovered2 = FighterEX(0,95,402,True,LadyDataHover,Ladysheet,LadyAnimation)
MonkHovered1 = FighterEX(0,85,150,True,MonkDataHover,Monksheet,MonkAnimation)#1st Row
MonkHovered2 = FighterEX(0,85,400,True,MonkDataHover,Monksheet,MonkAnimation)
NinjaHovered1 = FighterEX(0,100,175,True,NinjaDataHover,Ninjasheet,NinjaAnimation)#2nd Row
NinjaHovered2 = FighterEX(0,100,425,True,NinjaDataHover,Ninjasheet,NinjaAnimation)
PirateHovered1 = FighterEX(0,120,195,True,PirateDataHover,Piratesheet,PirateAnimation)#2nd Row
PirateHovered2 = FighterEX(0,120,445,True,PirateDataHover,Piratesheet,PirateAnimation)
RoninHovered1 = FighterEX(0,120,160,True,RoninDataHover,Roninsheet,RoninAnimation)#1st Row
RoninHovered2 = FighterEX(0,120,410,True,RoninDataHover,Roninsheet,RoninAnimation)
SamuraiHovered1 = FighterEX(0,115,180 ,True,SamuraiDataHover,Samuraisheet,SamuraiAnimation)#2nd Row
SamuraiHovered2 = FighterEX(0,115,430,True,SamuraiDataHover,Samuraisheet,SamuraiAnimation)
SenseiHovered1 = FighterEX(0,120,150,True,SenseiDataHover,Senseisheet,SenseiAnimation)#1st Row
SenseiHovered2 = FighterEX(0,120,400,True,SenseiDataHover,Senseisheet,SenseiAnimation)
ShaolinHovered1 = FighterEX(0,205,315,True,ShaolinDataHover,Shaolinsheet,ShaolinAnimation)#3rd Row
ShaolinHovered2 = FighterEX(0,205,565,True,ShaolinDataHover,Shaolinsheet,ShaolinAnimation)
YasukeHovered1 = FighterEX(0,150,140,True,YasukeDataHover,Yasukesheet,YasukeAnimation)#3rd Row
YasukeHovered2 = FighterEX(0,150,390,True,YasukeDataHover,Yasukesheet,YasukeAnimation)

def CharacterSelectMenu():
    while True:
     clock 
        
        
     Mouse = pygame.mouse.get_pos()

     display_Bg2()
     lettersnumbers("Character Select", Font(45),DarkTeal, 375,10)
     lettersnumbers("Player 1 : ", Font(30),DarkYellow, 100,90)
     lettersnumbers("Player 2 : ", Font(30),White, 100,325)
     
     
     characters = [Beetle0, Farmer0, Ghost0, Lady0, Monk0, Ninja0, Pirate0, Ronin0, Samurai0, Sensei0, Shaolin0, Yasuke0]
     for character in characters:
         character.update()
         character.Draw(Screen)
    
     Beetle1button = Buttons((scaleBTN3),(425,310), "1", Font(25), White, Red)
     Beetle2button = Buttons((scaleBTN3),(425,350), "2", Font(25), White, Red)
     Farmer1button= Buttons((scaleBTN3),(650,310), "1", Font(25), White, Red)
     Farmer2button = Buttons((scaleBTN3),(650,350), "2", Font(25), White, Red)
     Ghost1button = Buttons((scaleBTN3),(760,100), "1", Font(25), White, Red)
     Ghost2button = Buttons((scaleBTN3),(760,140), "2", Font(25), White, Red)
     Lady1button = Buttons((scaleBTN3),(880,100), "1", Font(25), White, Red)
     Lady2button = Buttons((scaleBTN3),(880,140), "2", Font(25), White, Red)
     Monk1button= Buttons((scaleBTN3),(650,100), "1", Font(25), White, Red)
     Monk2button  = Buttons((scaleBTN3),(650,140), "2", Font(25), White, Red)
     Ninja1button = Buttons((scaleBTN3),(525,310), "1", Font(25), White, Red)
     Ninja2button = Buttons((scaleBTN3),(525,350), "2", Font(25), White, Red)
     Pirate1button = Buttons((scaleBTN3),(760,310), "1", Font(25), White, Red)
     Pirate2button = Buttons((scaleBTN3),(760,350), "2", Font(25), White, Red)
     Ronin1button= Buttons((scaleBTN3),(425,100), "1", Font(25), White, Red)
     Ronin2button = Buttons((scaleBTN3),(425,140), "2", Font(25), White, Red)
     Samurai1button = Buttons((scaleBTN3),(880,310), "1", Font(25), White, Red)
     Samurai2button = Buttons((scaleBTN3),(880,350), "2", Font(25), White, Red)
     Sensei1button = Buttons((scaleBTN3),(525,100), "1", Font(25), White, Red)
     Sensei2button = Buttons((scaleBTN3),(525,140), "2", Font(25), White, Red)
     Shaolin1button = Buttons((scaleBTN3),(525,450), "1", Font(25), White, Red)
     Shaolin2button = Buttons((scaleBTN3),(525,490), "2", Font(25), White, Red)
     Yasuke1button  = Buttons((scaleBTN3),(700,450), "1", Font(25), White, Red)
     Yasuke2button = Buttons((scaleBTN3),(700,490), "2", Font(25), White, Red)


     buttons_p1 = [Beetle1button, Farmer1button, Ghost1button, Lady1button, Monk1button, Ninja1button, Pirate1button, Ronin1button, Samurai1button, Sensei1button, Shaolin1button, Yasuke1button]
     buttons_p2 =  [Beetle2button, Farmer2button, Ghost2button, Lady2button, Monk2button, Ninja2button, Pirate2button, Ronin2button, Samurai2button, Sensei2button, Shaolin2button, Yasuke2button]

     for button in buttons_p1 + buttons_p2:
         button.changeColor(Mouse)
         button.update(Screen)
     
    
     
     if Ronin1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Ronin", Font(30),DarkYellow, 100,90)
         RoninHovered1.Draw(Screen)
         RoninHovered1.update()
     if Ronin2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Ronin", Font(30),White, 100,325)
         RoninHovered2.Draw(Screen)
         RoninHovered2.update()
     if Sensei1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Sensei", Font(30),DarkYellow, 100,90)
         SenseiHovered1.Draw(Screen)
         SenseiHovered1.update()
     if Sensei2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Sensei", Font(30),White, 100,325)
         SenseiHovered2.Draw(Screen)
         SenseiHovered2.update()
     if Ghost1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Ghost", Font(30),DarkYellow, 100,90)
         GhostHovered1.Draw(Screen)
         GhostHovered1.update()
     if Ghost2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Ghost", Font(30),White, 100,325)
         GhostHovered2.Draw(Screen)
         GhostHovered2.update()
     if Monk1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Monk", Font(30),DarkYellow, 100,90)
         MonkHovered1.Draw(Screen)
         MonkHovered1.update()
     if Monk2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Monk", Font(30),White, 100,325)
         MonkHovered2.Draw(Screen)
         MonkHovered2.update()
     if Lady1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Lady", Font(30),DarkYellow, 100,90)
         LadyHovered1.Draw(Screen)
         LadyHovered1.update()
     if Lady2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Lady", Font(30),White, 100,325)
         LadyHovered2.Draw(Screen)
         LadyHovered2.update()
     if Beetle1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Beetle", Font(30),DarkYellow, 100,90)
         BeetleHovered1.Draw(Screen)
         BeetleHovered1.update()
     if Beetle2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Beetle", Font(30),White, 100,325)
         BeetleHovered2.Draw(Screen)
         BeetleHovered2.update()
     if Ninja1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Ninja", Font(30),DarkYellow, 100,90)
         NinjaHovered1.Draw(Screen)
         NinjaHovered1.update()
     if Ninja2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Ninja", Font(30),White, 100,325)
         NinjaHovered2.Draw(Screen)
         NinjaHovered2.update()
     if Farmer1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Farmer", Font(30),DarkYellow, 100,90)
         FarmerHovered1.Draw(Screen)
         FarmerHovered1.update()
     if Farmer2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Farmer", Font(30),White, 100,325)
         FarmerHovered2.Draw(Screen)
         FarmerHovered2.update()
     if Pirate1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Pirate", Font(30),DarkYellow, 100,90)
         PirateHovered1.Draw(Screen)
         PirateHovered1.update()
     if Pirate2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Pirate", Font(30),White, 100,325)
         PirateHovered2.Draw(Screen) 
         PirateHovered2.update()
     if Samurai1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Samurai", Font(30),DarkYellow, 100,90)
         SamuraiHovered1.Draw(Screen)
         SamuraiHovered1.update()
     if Samurai2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Samurai", Font(30),White, 100,325)
         SamuraiHovered2.Draw(Screen)
         SamuraiHovered2.update()
     if Shaolin1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Shaolin", Font(30),DarkYellow, 100,90)
         ShaolinHovered1.Draw(Screen)
         ShaolinHovered1.update()
     if Shaolin2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Shaolin", Font(30),White, 100,325)
         ShaolinHovered2.Draw(Screen)
         ShaolinHovered2.update()
     if Yasuke1button.checkForInput(Mouse):
         lettersnumbers("Player 1 : Yasuke", Font(30),DarkYellow, 100,90)
         YasukeHovered1.Draw(Screen)
         YasukeHovered1.update()
     if Yasuke2button.checkForInput(Mouse):
         lettersnumbers("Player 2 : Yasuke", Font(30),White, 100,325)
         YasukeHovered2.Draw(Screen)
         YasukeHovered2.update()
     
     Player_1 = None
     Player_2 = None
     
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
        