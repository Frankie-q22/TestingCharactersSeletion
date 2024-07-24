#edit for characters

 
  
  
    
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

while True:
    
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
 

 
 
      
 #event handler
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         run = False
            
 #Updates display for background
 pygame.display.update()


#exit pygame
pygame.quit()




#Def character selecion (FighterEX(player,x,y,flip,characterData,characetersheet,characteAnimation))
#if player 1 key press button 1
           #FighterEX(player,x,y,flip,characterData,characetersheet,characteAnimation))
           #elif
           #FighterEX(player,x,y,flip,character2Data,characeter2sheet,character2Animation)
           
           
           
           #LETS DO THIS ONE LAST TIME

