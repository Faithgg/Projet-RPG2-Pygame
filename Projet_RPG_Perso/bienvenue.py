import netoyeur_d_ecran
import pygame
import name
import developpeur
import le_modul_pygame
def bienvenue1(surface) :
    surface.fill("orange")
#______________________________________chargement du texte de bienvenue_________________________________________
    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
    le_modul_pygame.affichage_image_transformée(surface,"images/welcome.png",200,100,(900,509))
    le_modul_pygame.joueur_de_sound("sounds/debut.mp3")
    le_modul_pygame.ralentisseur(1)
    surface.fill("yellow")
    le_modul_pygame.affichage_image_transformée(surface,"images/3d.png",0,0,(1300,700))
    le_modul_pygame.affichage_texte(surface,"1-",30,100,200,"courier",le_modul_pygame.code_couleur("blue"))
    le_modul_pygame.affichage_texte(surface,"Commencer le Jeu en appuyant sur Entrer",30,140,200,"courier",le_modul_pygame.code_couleur("green"))
    le_modul_pygame.ralentisseur(0.1)
    le_modul_pygame.affichage_texte(surface,"2-",30,100,270,"courier",le_modul_pygame.code_couleur("blue"))
    le_modul_pygame.affichage_texte(surface,"Informations sur le developpeur en appuyant sur Tab",30,140,270,"courier",le_modul_pygame.code_couleur("black"))
    le_modul_pygame.ralentisseur(0.2)
    le_modul_pygame.affichage_texte(surface,"3-",30,100,340,"courier",le_modul_pygame.code_couleur("blue"))
    le_modul_pygame.affichage_texte(surface,"Sortez avec Echappe",30,140,340,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.ralentisseur(0.2)
    le_modul_pygame.affichage_texte(surface,"Au cours du jeu, vous pouvez quitter en fermant la fenetre ou en faisant Echappe",25,40,450,"courier",le_modul_pygame.code_couleur("kaki"))

    choice = le_modul_pygame.decision()

    if choice == "entrer" :
        surface.fill("white")
        name.name(surface)
    elif choice=="infos" :
        developpeur.informations(surface)
    else:
        netoyeur_d_ecran.efface_ecran() 
        bienvenue1(surface)