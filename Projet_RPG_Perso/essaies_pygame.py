import le_modul_pygame
import pygame

import os

liste = [
"IIIIIIIIIIIIIIIII",
"I I             I",
"I               I",
"I               I",
"I             I I",
"I      I        I",
"I  IIIIIIIIII   I",
"I      I        I",
"I      I        I",
"I               I",
"I  I            I",
"I               I",
"I        I      I",
"I               I",
"I               I",
"IIIIIIIIIIIIIIIII"
]
pygame.display.init()
longueur = 1300
hauteur = 700
surface1 = pygame.display.set_mode((longueur, hauteur), vsync=1)

def stop_interface() :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            r=2
            pygame.display.quit()
            os._exit(1)


pygame.font.init()
#print(pygame.font.get_fonts())

while True :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print(pygame.key. name (event.key)) 
    
    stop_interface()

    """


    j = 0
    for jfj in liste :
        i= 0
        for fff in jfj :
            
            if fff == "I" :
        #affichage d'image sur l'écran
                img = pygame.Surface((200,200))
                img_rect = img.fill("black")
                img_rect.left = i
                img_rect.top = j
                pygame.Surface.set_colorkey(img,(0,0,0))
                surface1.blit(img, img_rect)
            i = i + 20
        j +=20
    le_modul_pygame.petites_infos(surface1,"Le texte oooo","     None    ","le texte oooo")

    
    pygame.display.flip()
    #affichage de test sur la surface
    """
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print(str(pygame.key. name (event.key))) 
    """
    pygame.font.quit()
    pygame.font.init()
    font = pygame.font.Font.render(pygame.font.SysFont("courier", 60),"L'essai ",True, (245, 245, 220),None )
    police= font.get_rect()
    police.left = 500
    police.top = 500
    surface.blit(font,police)"""
   

    surface1.fill("orange")
    pygame.display.flip()


    

    

