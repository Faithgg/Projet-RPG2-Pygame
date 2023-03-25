import officer
import le_modul_pygame
import pygame
import os
def recherche(liste, element):
    for composants in liste :
        if composants == element :    
            return element
    return ""


def name(surface):
    le_modul_pygame.ralentisseur(0.1)
    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
    le_modul_pygame.affichage_texte_fond(surface,"Ecrivez votre pseudo puis cliquez sur <Entrer>",30,200,330,"courier",le_modul_pygame.code_couleur("black"),le_modul_pygame.code_couleur("white"))
    le_modul_pygame.ralentisseur(0.1)
    le_modul_pygame.affichage_texte_fond(surface,"                    ALLEZ-Y!                  ",30,200,370,"courier",le_modul_pygame.code_couleur("kaki"),le_modul_pygame.code_couleur("white"))
    nom = ""
    liste = "abcdefghijklmnopqrstuvwxyz0123456789@"

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.display.quit()
                os._exit(1)

            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN or len(nom)>10:
                    if (str(pygame.key. name (event.key)) =="return" and len(nom)!=0) or len(nom)>10 :
                        name = nom
                        infos = {
                                "po" : 0,
                                "pv" : 25,
                                "level" : 1,
                                "name" : name,
                                "armes" : 1,
                                "pop" : 1270,
                                "pap" : 670,
                                "popop":510,
                                "papap":110,
                                "pipip":510,
                                "pupup":110,
                                "vitesse" : [2,2],
                                "speed" :[3,2],
                                "direction":None
}

                        surface.fill("orange")
                        return officer.officer(surface,infos)
                elif event.type == pygame.KEYUP:
                    nom = nom + recherche(liste,str(pygame.key. name (event.key)))
