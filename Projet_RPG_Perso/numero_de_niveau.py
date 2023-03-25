
import pygame
import le_modul_pygame
def barre_score(surface,infos) :
    """
Barre de score affichant les données du jeu
data : dictionnaire de données de la barre de score
Pas de valeur de retour
"""
    le_modul_pygame.affichage_texte(surface,"Vie:",20,200,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["pv"]),15,250,0,"arialunicode",le_modul_pygame.code_couleur("green"))
    le_modul_pygame.affichage_texte(surface,"Pièces:",20,350,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["po"]),15,450,0,"arialunicode",le_modul_pygame.code_couleur("green"))
    le_modul_pygame.affichage_texte(surface,"Armes:",20,550,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["armes"]),15,650,0,"arialunicode",le_modul_pygame.code_couleur("green"))
    le_modul_pygame.affichage_texte(surface,"Niveau:",20,700,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["level"]),15,800,0,str(pygame.font.get_fonts()[0]),le_modul_pygame.code_couleur("white"))
    le_modul_pygame.affichage_texte(surface,"Joueur:",20,950,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["name"]),15,1050,0,str(pygame.font.get_fonts()[0]),le_modul_pygame.code_couleur("white"))    


import pygame
import le_modul_pygame
def barre_score_monster(surface,infos) :
    """
Barre de score affichant les données du jeu
data : dictionnaire de données de la barre de score
Pas de valeur de retour
"""
    le_modul_pygame.affichage_texte(surface,"Vie:",20,200,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["pv"]),15,250,0,"arialunicode",le_modul_pygame.code_couleur("green"))
    le_modul_pygame.affichage_texte(surface,"Pièces:",20,350,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["po"]),15,450,0,"arialunicode",le_modul_pygame.code_couleur("green"))
    le_modul_pygame.affichage_texte(surface,"Armes:",20,550,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["armes"]),15,650,0,"arialunicode",le_modul_pygame.code_couleur("green"))
    le_modul_pygame.affichage_texte(surface,"Niveau:",20,700,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["level"]),15,800,0,str(pygame.font.get_fonts()[0]),le_modul_pygame.code_couleur("white"))

    le_modul_pygame.affichage_texte(surface,"Monstre:",20,850,0,"courier",le_modul_pygame.code_couleur("black"))
    le_modul_pygame.affichage_texte(surface,str(infos["monstre"]),15,970,0,"arialunicode",le_modul_pygame.code_couleur("white"))
    le_modul_pygame.affichage_texte(surface,"Joueur:",20,1050,0,"courier",le_modul_pygame.code_couleur("red"))
    le_modul_pygame.affichage_texte(surface,str(infos["name"]),15,1150,0,str(pygame.font.get_fonts()[0]),le_modul_pygame.code_couleur("white"))    