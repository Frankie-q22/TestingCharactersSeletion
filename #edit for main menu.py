#edit for main menu
#TestingMenu Options

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


scaleBTN1 = pygame.image.load("ButtonFolder/NearTransparent.png")
scaleBTN1 = pygame.transform.scale(scaleBTN1,(155, 30))
scaleBTN2 = pygame.image.load("ButtonFolder/NearTransparent.png")
scaleBTN2 = pygame.transform.scale(scaleBTN2,(100, 30))

SPButton = Buttons((scaleBTN1),(200,200), "Single Player", Font(25), White, Red)
MPButton = Buttons((scaleBTN1),(200,200), "Multiplayer", Font(25), White, Red)

def CharacterSelectMenu():
    while True:
     Mouse = pygame.mouse.get_pos()

     display_Bg2()
     lettersnumbers("Character Select", Font(45),White, 600,50)
     lettersnumbers("Player 1", Font(30),White, 100,90)
     lettersnumbers("Player 2", Font(30),White, 100,325)
     

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
        

 
 