import pygame
import os
import le_modul_pygame
import numero_de_niveau
import deplacement_joueur
def affiche_labyrinthe(lab,surface, pos_perso, infos):

    """
    Affichage d’un labyrinthe
    lab : Variable contenant le labyrinthe
    perso : caractère représentant le personnage
    pos_perso : liste contenant la position du personnage
    [ligne, colonne]
    Pas de valeur de retour
    """
    n_ligne = 0
    j= 30
    numero_de_niveau.barre_score(surface,infos)

    for ligne in lab[:pos_perso[1]]:
        i= 15
        le_modul_pygame.analiste(surface,i,j,ligne,infos)
        j+= 30
        n_ligne += 1
                
    i=15
    i=le_modul_pygame.analiste(surface,i,j,lab[n_ligne][0 :pos_perso[0]],infos)
    

    #affichage de notre personne
    img = pygame.transform.scale(pygame.image.load("images/perso.png"),(30,30))
    img_rect = img.get_rect()
    infos["pop"] = i
    infos["pap"] = j
    img_rect.left = i
    img_rect.top = j
    surface.blit(img, img_rect)
    i =i+30
    le_modul_pygame.analiste(surface,i,j,lab[n_ligne][pos_perso[0]+1:],infos)
    n_ligne= pos_perso[1] + 1       
    j= j+30

    for ligne in lab[n_ligne:]:
        i= 15
        le_modul_pygame.analiste(surface,i,j,ligne,infos)
        j+=30
        n_ligne = n_ligne +1

    if infos["level"]% 3 ==0 and infos["monstre"] >0:
        if infos["level"] < 24 :
            cote = 40
        else:
            cote = infos["level"]*2
        le_modul_pygame.image_transformée_en_mouvement(img_rect,surface,"images/monster.png",infos["popop"],infos["papap"],cote,infos["vitesse"],lab,infos,pos_perso)
    else :
        infos["monstre"] = -10
    pygame.display.flip()

    deplacement_joueur.choix_joueur(lab,surface,infos, pos_perso)


