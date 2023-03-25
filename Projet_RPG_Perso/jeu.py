import netoyeur_d_ecran
import sys
import name
import boutique
import officer
import afficheur_environnement_de_jeu
import le_modul_pygame
import os

def jeu(level, infos, surface, pos_perso):
    sys.setrecursionlimit(5000)#pour ne pas avoir dans la suite de problème de récursion maximale atteiente
    """
    Boucle principale du jeu. Affiche le labyrinthe dans ses différents
    états après les déplacements du joueur.
    level : Labyrinthe
    n_level : numéro du niveau courant
    perso : caractère représentant le personnage
    pos_perso : liste contenant la position du personnage
    [colonne, ligne]
    """
    while True :
        if infos["pv"] <= 0 :
            infos["pv"]= 0
            if infos["po"]*(3/4) >= 10 or infos["armes"] >= 4:
                surface.fill("white")
                le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                le_modul_pygame.petites_infos(surface,"Vous avez assez de pièces ou d'armes à vendre pour vous soigner",None,"Pour vous soigner utilisez la touche <Entrer>")
                decision = le_modul_pygame.decision()
                if str(decision) == "entrer" :
                    boutique.acheter(level,infos, pos_perso,surface)
                else :
                    surface.fill("white")
                    le_modul_pygame.joueur_de_sound("sounds/fin.mp3")
                    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                    le_modul_pygame.petites_infos(surface,"Vous avez PERDU la partie",None,None)
                    le_modul_pygame.ralentisseur(1.2)
                    netoyeur_d_ecran.efface_ecran()
                    surface.fill("white")
                    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                    le_modul_pygame.petites_infos(surface,"   Voulez-vous recommencer ?  ", "             Si OUI           ", "Appuyez sur la touche <Entrer>")
                    decision = le_modul_pygame.decision()
                    if str(decision) == "entrer" :
                        surface.fill("white")
                        name.name(surface)
                    else :
                        netoyeur_d_ecran.efface_ecran()
                        os._exit(1)

            else:
                surface.fill("white")
                le_modul_pygame.petites_infos(surface,"Vous n'avez pas assez de pièces/armes pour pousuivre la partie",None,None)
                le_modul_pygame.joueur_de_sound("sounds/fin.mp3")
                le_modul_pygame.ralentisseur(1.2)
                netoyeur_d_ecran.efface_ecran()
                surface.fill("white")
                le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                le_modul_pygame.petites_infos(surface,"   Voulez-vous recommencer ?  ","             Si OUI           ","Appuyez sur la touche <Entrer>")
                decision = le_modul_pygame.decision()
                if str(decision) == "entrer" :
                    name.name(surface)
                else :
                    netoyeur_d_ecran.efface_ecran()
                    os._exit(1)


        if infos["armes"] <= 0:
            if infos["po"]*(3/4) >= 4 :
                surface.fill("white")
                le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                le_modul_pygame.petites_infos(surface,"Vous avez assez de pièces pour payer des armes",None,"Pour payer d'armes appuyez la touche  <Entrer>")
                decision = le_modul_pygame.decision()
                if str(decision) == "entrer" :
                    boutique.armer(infos,surface)
                else :
                    surface.fill("white")
                    le_modul_pygame.joueur_de_sound("sounds/fin.mp3")
                    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                    le_modul_pygame.petites_infos(surface,"Vous avez PERDU la partie",None,None)
                    le_modul_pygame.ralentisseur(1)
                    netoyeur_d_ecran.efface_ecran()
                    surface.fill("white")
                    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                    le_modul_pygame.petites_infos(surface,"   Voulez-vous recommencer ?  " , "             Si OUI           " , "Appuyez sur la touche <Entrer>")
                    decision = le_modul_pygame.decision()
                    if str(decision) == "entrer" :
                        surface.fill("white")
                        name.name(surface)
                    else :
                        netoyeur_d_ecran.efface_ecran()
                        os._exit(1)

            else:
                le_modul_pygame.petites_infos(surface,"Vous n'avez pas assez de pièces/armes pour pousuivre la partie",None,None)
                le_modul_pygame.joueur_de_sound("sounds/fin.mp3")
                le_modul_pygame.ralentisseur(1.2)
                netoyeur_d_ecran.efface_ecran()
                surface.fill("white")
                le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
                le_modul_pygame.petites_infos(surface,"   Voulez-vous recommencer ?  " , "             Si OUI           " , "Appuyez sur la touche <Entrer>")
                decision = le_modul_pygame.decision()
                if str(decision) == "entrer" :
                    surface.fill("white")
                    name.name(surface)
                else :
                    netoyeur_d_ecran.efface_ecran()
                    os._exit(1)


        if pos_perso == [-1, -1] : 
            le_modul_pygame.affichage_image_transformée(surface,"images/f.png",0,0,(1300,700))
            le_modul_pygame.ralentisseur(0.7)
            surface.fill("green")
            le_modul_pygame.affichage_image_transformée(surface,"images/3d.png",0,0,(1300,700))
            le_modul_pygame.affichage_texte(surface,"50 pièces de plus sont ajoutées à votre solde.",30,300,300,"courier",le_modul_pygame.code_couleur("yellow"))
            le_modul_pygame.ralentisseur(0.2)
            le_modul_pygame.affichage_texte(surface,"Le prochain niveau dans 2 secondes",40,300,370,"courier",le_modul_pygame.code_couleur("red"))
            le_modul_pygame.ralentisseur(1)
            infos["compteur"]=0
            surface.fill("orange")
            le_modul_pygame.ralentisseur(0.3)
            infos["level"] = infos["level"] + 1
            officer.officer(surface,infos)
            break
            
            

        afficheur_environnement_de_jeu.affiche_labyrinthe(level, surface, pos_perso, infos)

