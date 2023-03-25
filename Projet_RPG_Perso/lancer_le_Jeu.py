import le_modul_pygame
import bienvenue

#----------------------Définition de ma surface de jeu-------------------------------------------------------
surface = le_modul_pygame.createur_interface(1300,700)

                     #La fameuse boucle du jeu
while True :
    le_modul_pygame.titre_de_jeu()
    le_modul_pygame.stop_interface()
    bienvenue.bienvenue1(surface)

    