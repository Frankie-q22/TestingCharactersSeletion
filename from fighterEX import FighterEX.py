from fighterEX import FighterEX


Beetlesheet = pygame.image.load("FullBeetleee.png").convert_alpha()
BeetleAnimation = [4,8,2,2,4,4,4,4]

Farmersheet = pygame.image.load("FullFarmer(Fixed).png").convert_alpha()
FarmerAnimation = [4,8,2,2,4,4,4,4]

Ghostsheet = pygame.image.load("FullGhostTT.png").convert_alpha()
GhostAnimation = [4,8,2,2,4,4,4,4]

Ladysheet = pygame.image.load("FullLady.png").convert_alpha()
LadyAnimation = [4,8,2,2,4,4,4,4,]

Monksheet = pygame.image.load("FullMonk.png").convert_alpha()
MonkAnimation =  [4,8,2,2,4,4,4,4]

Ninjasheet = pygame.image.load("FullNinja.png").convert_alpha()
NinjaAnimation = [4,8,2,2,4,4,4,4]


Piratesheet = pygame.image.load("FullPirate.png").convert_alpha()
PirateAnimation = [4,8,2,2,4,4,4,4]

RedSamuraisheet = pygame.image.load("FullRedSamurai.png").convert_alpha()
RedSamuraiAnimation = [4,8,2,2,4,4,4,4]


Roninsheet = pygame.image.load("FullRonin.png").convert_alpha()
RoninAnimation = [4,8,2,2,4,4,3,7]

Samuraisheet = pygame.image.load("FullSamurai.png").convert_alpha()
SamuraiAnimation =[8,8,2,2,6,6,4,6]

Senseisheet = pygame.image.load("FullSensei.png").convert_alpha()
SenseiAnimation = [4,8,2,2,4,4,4,4]


Shaolinsheet = pygame.image.load("FullShaolin(Fixed).png").convert_alpha()
ShaolinAnimation = [10,8,3,3,7,6,3,11]

Yasukesheet = pygame.image.load("FullYasuke.png").convert_alpha()
YasukeAnimation = [4,8,2,2,4,4,4,4]


#Def character selecion (FighterEX(player,x,y,flip,characterData,characetersheet,characteAnimation))
#if player 1 key press button 1
           #FighterEX(player,x,y,flip,characterData,characetersheet,characteAnimation))
           #elif
           #FighterEX(player,x,y,flip,character2Data,characeter2sheet,character2Animation)
           
           
           
           #LETS DO THIS ONE LAST TIME

import pygame
import sys
from Buttont import Buttons


pygame.init()

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
Red = (255,0,0)
Teal = (75,177,180)
Maroon = (128,0,0)


scaleBTN1 = pygame.image.load("NearTransparent.png")
scaleBTN1 = pygame.transform.scale(scaleBTN1,(155, 30))
scaleBTN2 = pygame.image.load("NearTransparent.png")
scaleBTN2 = pygame.transform.scale(scaleBTN2,(100, 30))

SPButton = Buttons((scaleBTN1),(200,200), "Single Player", Font(25), White, Red)
MPButton = Buttons((scaleBTN1),(200,200), "Multiplayer", Font(25), White, Red)

def Character_Select():
 while True:
     CS_Mouse =  pygame.mouse.get_pos()
     display_Bg2()
     lettersnumbers("Character Select", Font(45),White, 600,50)
     lettersnumbers("Player 1", Font(30),White, 100,90)
     lettersnumbers("Player 2", Font(30),White, 100,325)
     

     SP_BACK = Buttons((scaleBTN2),(30,15), "BACK", Font(25), White, Red)

     SP_BACK.changeColor(CS_Mouse)
     SP_BACK.update(Screen)

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
                if SP_BACK.checkForInput(CS_Mouse):
                    Starting_menu()

     pygame.display.update()

def Single_Player_Mode():
 while True:
     SP_Mouse = pygame.mouse.get_pos()

     display_Bg2()
     lettersnumbers("Character Select", Font(45),White, 600,50)
     lettersnumbers("Player 1", Font(30),White, 100,90)
     lettersnumbers("Player 2", Font(30),White, 100,325)
     

     SP_BACK = Buttons((scaleBTN2),(30,15), "BACK", Font(25), White, Red)

     SP_BACK.changeColor(SP_Mouse)
     SP_BACK.update(Screen)

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
                if SP_BACK.checkForInput(SP_Mouse):
                    Starting_menu()

     pygame.display.update()
    
    
    
    
def Multiplayer_Mode():  
 while True:
     MP_Mouse = pygame.mouse.get_pos()

     display_Bg2()
     lettersnumbers("Character Select", Font(45),White, 600,50)
     lettersnumbers("Player 1", Font(30),White, 100,90)
     lettersnumbers("Player 2", Font(30),White, 100,325)
     Monk2.Draw()
     

     MP_BACK = Buttons((scaleBTN2),(30,15), "BACK", Font(25), White, Red)

     MP_BACK.changeColor(MP_Mouse)
     MP_BACK.update(Screen)

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
                if MP_BACK.checkForInput(MP_Mouse):
                    Starting_menu()
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
                 Single_Player_Mode()
             if MPButton.checkForInput(S_M_mouse):
                 Multiplayer_Mode()    
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



#creates Game Window
Screen_Width = 1000
Screen_Height = 600

Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Fighting For Honor")


#Set Framerate
clock = pygame.time.Clock()
FPS = 60

#Define colors
Red = (255,0,0)
Yellow = (255,255,0)
White = (255,255,255)

#starting /end counter sequence (and points)
introcount = 3
endcount = 5
lastcountupdate = pygame.time.get_ticks()
#player score
score = [0,0]
Round_over = False
Round_over_cooldown = 5000

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







#load BackGround Image
background = pygame.image.load("Characterselect.jpg").convert_alpha()
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
#define the font
countingfont = pygame.font.Font("Turok.ttf",150)
scorefont = pygame.font.Font("Turok.ttf",40)
Wins = pygame.font.Font("Turok.ttf",50)
WinsSmaller = pygame.font.Font("Turok.ttf",49)



#Drawing the counter and point system
def lettersnumbers(text,font,text_color,x,y):
  img = font.render(text,True,text_color)
  Screen.blit (img, (x, y))
#Function that displays background
def display_Bg():
 scaledBG = pygame.transform.scale(background,(Screen_Width, Screen_Height))
 Screen.blit(scaledBG,(0,0))
    
    
 
  
#Function for drawing the health bars
# bottom bar is character's health in yellow. length of color has to be set to character's health value in order for character to take damage
def Health_Bar(Health, x, y): 
  pygame.draw.rect (Screen, White, (x-2,y-2,404,35))
  pygame.draw.rect (Screen, Red, (x,y, 400,30))
  pygame.draw.rect (Screen, Yellow, (x,y, Health,30))
  
    
#Creates Characters # Player 1
Beetle1= FighterEX(1,200,360,False,BeetleData1,Beetlesheet,BeetleAnimation)
Farmer1=FighterEX(1,200,360,False,FarmerData1,Farmersheet,FarmerAnimation)
Ghost1=FighterEX(1,200,360,False,GhostData1,Ghostsheet,GhostAnimation)
Lady1=FighterEX(1,200,360,False,LadyData1,Ladysheet,LadyAnimation)
Monk1=FighterEX(1,200,360,False,MonkData1,Monksheet,MonkAnimation)
Ninja1=FighterEX(1,200,360,False,NinjaData1,Ninjasheet,NinjaAnimation)
Pirate1=FighterEX(1,200,360,False,PirateData1,Piratesheet,PirateAnimation)
RedSamurai1=FighterEX(1,200,360,False,RedSamuraiData1,RedSamuraisheet,RedSamuraiAnimation)
Ronin1 = FighterEX(1,200,360,False,RoninData1,Roninsheet,RoninAnimation)
Samurai1 = FighterEX(2,200,360,True,SamuraiData1,Samuraisheet,SamuraiAnimation)
Sensei1=FighterEX(1,200,360,False,SenseiData1,Senseisheet,SenseiAnimation)
Shaolin1=FighterEX(1,200,360,False,ShaolinData1,Shaolinsheet,ShaolinAnimation)
Yasuke1 = FighterEX(1,200,360,False,YasukeData1,Yasukesheet,YasukeAnimation)

  
#Creates Characters # Player 2
Beetle2= FighterEX(2,700,360,True,BeetleData2,Beetlesheet,BeetleAnimation)
Farmer2=FighterEX(2,700,360,True,FarmerData2,Farmersheet,FarmerAnimation)
Ghost2=FighterEX(2,700,360,True,GhostData2,Ghostsheet,GhostAnimation)
Lady2=FighterEX(2,700,360,True,LadyData2,Ladysheet,LadyAnimation)
Monk2=FighterEX(2,700,360,True,MonkData2,Monksheet,MonkAnimation)
Ninja2=FighterEX(2,700,360,True,NinjaData2,Ninjasheet,NinjaAnimation)
Pirate2=FighterEX(2,700,360,True,PirateData2,Piratesheet,PirateAnimation)
RedSamurai2=FighterEX(2,700,360,True,RedSamuraiData2,RedSamuraisheet,RedSamuraiAnimation)
Ronin2 = FighterEX(2,700,360,True,RoninData2,Roninsheet,RoninAnimation)
Samurai2 = FighterEX(2,700,360,True,SamuraiData2,Samuraisheet,SamuraiAnimation)
Sensei2=FighterEX(2,700,360,True,SenseiData2,Senseisheet,SenseiAnimation)
Shaolin2=FighterEX(2,700,360,True,ShaolinData2,Shaolinsheet,ShaolinAnimation)
Yasuke2 = FighterEX(2,700,360,True,YasukeData2,Yasukesheet,YasukeAnimation)

#gameloop
run = True
while run:
    
 clock.tick(FPS)
    
 #Display Background
 display_Bg()
    
 #Show Health Bars
 #Health_Bar(Beetle1.Health,20,20)
 #Health_Bar(Farmer1.Health,20,20)
 #Health_Bar(Ghost1.Health,20,20)
 #Health_Bar(Lady1.Health,20,20)
 Health_Bar(Monk1.Health,20,20)
 #Health_Bar(Ninja1.Health,20,20)
 #Health_Bar(Pirate1.Health,20,20)
 #Health_Bar(RedSamurai1.Health,20,20)
 #Health_Bar(Ronin1.Health,20,20)
 #Health_Bar(Samurai1.Health, 20,20)
 #Health_Bar(Sensei1.Health, 20,20)
 #Health_Bar(Shaolin1.Health,20,20)
 #Health_Bar(Yasuke1.Health,20,20)
 
 #Health_Bar(Beetle2.Health,580,20)
 #Health_Bar(Farmer2.Health,580,20)
 #Health_Bar(Ghost2.Health,580,20)
 #Health_Bar(Lady2.Health,580,20)
 #Health_Bar(Monk2.Health,580,20)
 #Health_Bar(Ninja2.Health,580,20)
 #Health_Bar(Pirate2.Health,580,20)
 #Health_Bar(RedSamurai2.Health,580,20)
 Health_Bar(Ronin2.Health,580,20)
 #Health_Bar(Samurai2.Health, 580,20)
 #Health_Bar(Sensei2.Health, 580,20)
 #Health_Bar(Shaolin2.Health,580,20)
 #Health_Bar(Yasuke2.Health,580,20)
#player points
 lettersnumbers("Ronin: "+(str(score[0])), scorefont,White,20,60)
 lettersnumbers("Samurai: "+(str(score[1])), scorefont,White,800,60)
#update countdown
 if introcount <=0:
   
    #Move Player 1
   #Beetle1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Farmer1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Ghost1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Lady1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   Monk1.Move(Screen_Width, Screen_Height,Screen,Ronin2)
   #Ninja1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Pirate1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #RedSamurai1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Ronin1.Move(Screen_Width, Screen_Height,Screen, Samurai1)
   #Samurai1.Move(Screen_Width, Screen_Height,Screen, Ronin1)
   #Sensei1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Shaolin1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Yasuke1.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   
   
   #Move Player 2
   #Beetle2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Farmer2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Ghost2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Lady2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Monk2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Ninja2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Pirate2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #RedSamurai2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   Ronin2.Move(Screen_Width, Screen_Height,Screen, Monk1)
   #Samurai2.Move(Screen_Width, Screen_Height,Screen, Ronin1)
   #Sensei2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Shaolin2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
   #Yasuke2.Move(Screen_Width, Screen_Height,Screen,Samurai1)
 else:
   #Displays count timer
   lettersnumbers(str(introcount), countingfont, Yellow, Screen_Width/2.1, Screen_Height/5)

   # Update count timer
   if (pygame.time.get_ticks() - lastcountupdate) >= 1000:
     introcount -= 1
     lastcountupdate = pygame.time.get_ticks()
    # print(introcount)
   
 
 #updates the sprites for Player 1
 #Beetle1.update()
 #Farmer1.update()
 #Ghost1.update()
 #Lady1.update()
 Monk1.update()
 #Ninja1.update()
 #Pirate1.update()
 #RedSamurai1.update
 #Ronin1.update()
 #Samurai1.update()
 #Sensei1.update()
 #Shaolin1.update()
 #Yasuke1.update()
 
 #updates the sprites for Player 2
 #Beetle2.update()
 #Farmer2.update()
 #Ghost2.update()
 #Lady2.update()
 #Monk2.update()
 #Ninja2.update()
 #Pirate2.update()
 #RedSamurai2.update
 Ronin2.update()
 #Samurai2.update()
 #Sensei2.update()
 #Shaolin2.update()
 #Yasuke2.update()
 
 
 
 #Draw Fighters A

 #Beetle1.Draw(Screen)
 #Farmer1.Draw(Screen)
 #Ghost1.Draw(Screen)
 #Lady1.Draw(Screen)
 Monk1.Draw(Screen)
 #Ninja1.Draw(Screen)
 #Pirate1.Draw(Screen)
 #RedSamurai1.Draw(Screen)
 #Ronin1.Draw(Screen)
 #Samurai1.Draw(Screen)
 #Sensei1.Draw(Screen)
 #Shaolin1.Draw(Screen)
 #Yasuke1.Draw(Screen)
 
 #Draw Fighters B

 #Beetle2.Draw(Screen)
 #Farmer2.Draw(Screen)
 #Ghost2.Draw(Screen)
 #Lady2.Draw(Screen)
 #Monk2.Draw(Screen)
 #Ninja2.Draw(Screen)
 #Pirate2.Draw(Screen)
 #RedSamurai2.Draw(Screen)
 Ronin2.Draw(Screen)
 #Samurai2.Draw(Screen)
 #Sensei2.Draw(Screen)
 #Shaolin2.Draw(Screen)
 #Yasuke2.Draw(Screen)
 
 
 
 
 
 Ronin_Wins = 'The Samurai Fought Honorably' 
 Samurai_Wins = 'The Ronin Fought Honorably'
    
 
 
 #CHeck for player death/defeat
 if Round_over == False:
   if Ronin1.Alive == False:
     
     Round_over = True
     Round_over_time = pygame.time.get_ticks()
     score[1] += 1
       
   elif Samurai1.Alive == False:
     score[0] += 1
     Round_over = True
     Round_over_time = pygame.time.get_ticks()
     #print(score)
 else:
   if pygame.time.get_ticks() - Round_over_time > Round_over_cooldown:
       Round_over = False
       introcount = 3
       endcount = 5 
       
       Ronin1 = FighterEX(1,200,360,False,RoninData1,Roninsheet,RoninAnimation)
       Samurai1 = FighterEX(2,700,360,True,SamuraiData1,Samuraisheet,SamuraiAnimation)
   if Ronin1.Alive == False:
     lettersnumbers(str(Samurai_Wins), Wins, Red, Screen_Width/4, Screen_Height/3)
     lettersnumbers(str(Samurai_Wins), WinsSmaller, White, Screen_Width/4, Screen_Height/3)
     lettersnumbers(str(endcount), Wins, Red, Screen_Width/2.1, Screen_Height/12)
     if (pygame.time.get_ticks() - lastcountupdate) >= 1000:
      endcount -= 1
      lastcountupdate = pygame.time.get_ticks()
      #print(endcount)
      
   if Samurai1.Alive ==False:
     lettersnumbers(str(Ronin_Wins), Wins, Red, Screen_Width/4, Screen_Height/3)
     lettersnumbers(str(Ronin_Wins), WinsSmaller, White, Screen_Width/4, Screen_Height/3)
     lettersnumbers(str(endcount), Wins, Red, Screen_Width/2.1, Screen_Height/12)
     if (pygame.time.get_ticks() - lastcountupdate) >= 1000:
      endcount -= 1
      lastcountupdate = pygame.time.get_ticks()
      #print(endcount)
      
 #event handler
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         run = False
            
 #Updates display for background
 pygame.display.update()


#exit pygame
pygame.quit()
