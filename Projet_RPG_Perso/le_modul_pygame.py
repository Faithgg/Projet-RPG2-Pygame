import pygame
import deplacement_joueur
import os
import jeu
import numero_de_niveau
import afficheur_environnement_de_jeu
import sys
def createur_interface(longueur,hauteur):
    pygame.display.init()
    surface = pygame.display.set_mode((longueur, hauteur), vsync=1)
    surface.fill("orange")
    return surface

def stop():
    pygame.display.quit()
    os._exit(1)

def stop_interface() :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.display.quit()
            os._exit(1)


def ralentisseur(m):
    k=-1000000
    while k < m*50000000 :
        k+=1
def titre_de_jeu():
    pygame.display.set_caption("Jeu de Rôles")

def affichage_image_transformée(surface,image,i,j,dimension) :
    img = pygame.transform.scale(pygame.image.load(image),dimension)
    img_rect = img.get_rect()
    img_rect.left = i
    img_rect.top = j
    surface.blit(img,img_rect)
    pygame.display.flip()

def image_transformée_en_mouvement(imgg,surface,image,i,j,cote,vitesse,lab,infos,pos_perso) :
    dimension =(cote,cote)
    sys.setrecursionlimit(5000)#pour ne pas avoir dans la suite de problème de récursion maximale atteiente
    img = pygame.transform.scale(pygame.image.load(image),dimension)
    img_rect = img.get_rect()
    img_rect.left = i
    img_rect.top = j
    imag = pygame.transform.scale(pygame.image.load("images/demon.png"),dimension)
    imag_rect = imag.get_rect()
    if infos["level"]%6 ==0 :
        imag_rect.left = infos["pipip"]
        imag_rect.top = infos["pupup"]
    masque(surface,1300,30,0,0)
    speed =[infos["speed"][0],infos["speed"][1]]
    numero_de_niveau.barre_score_monster(surface,infos)
    while True :
        infos["popop"]= img_rect.left
        infos["papap"]= img_rect.top
        img_rect = img_rect.move(vitesse)
        masque(surface,cote,cote,infos["popop"],infos["papap"])

        if infos["level"]%6 ==0:
            infos["pipip"]= imag_rect.left
            infos["pupup"]= imag_rect.top
            imag_rect = imag_rect.move(speed)
            masque(surface,cote,cote,infos["pipip"],infos["pupup"])

        if img_rect.left < 100 or img_rect.right >  1170:
            vitesse[0]= - vitesse[0]
            infos["vitesse"][0] = vitesse[0]
        if img_rect.top < 100 or img_rect.bottom > 525 :
            vitesse[1]= - vitesse[1]
            infos["vitesse"][1] = vitesse[1]
        surface.blit(img,img_rect)

        if infos["level"]%6 ==0 :
            if imag_rect.left < 100 or imag_rect.right >  1170:
                speed[0]= - speed[0]
                infos["speed"][0] = speed[0]
            if imag_rect.top < 100 or imag_rect.bottom > 525 :
                speed[1]= - speed[1]
                infos["speed"][1] = speed[1]
            surface.blit(imag,imag_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.display.quit()
                os._exit(1)
            if event.type == pygame.KEYDOWN :
                infos["direction"]= str(pygame.key. name (event.key))
                masque(surface,cote,cote,img_rect.left,img_rect.top)
                masque(surface,1300,30,0,0)
                if infos["level"]%6 ==0 :
                    masque(surface,cote,cote,imag_rect.left,imag_rect.top)
                return deplacement_joueur.choix_joueur(lab,surface,infos,pos_perso)
        if pygame.Rect.colliderect(imgg,img_rect) or pygame.Rect.colliderect(imgg,imag_rect):
            affichage_texte(surface,"    !! Le grand monstre attaque !!  ",20,500,675,"courier",code_couleur("red"))
            joueur_de_sound("sounds/boss.mp3")
            infos["pv"]=infos["pv"] - 1
            infos["armes"] = infos["armes"] -3
            masque(surface,1300,30,0,0)
            infos["monstre"] = infos["monstre"] -1
            numero_de_niveau.barre_score_monster(surface,infos)
            if infos["monstre"]== 0:
                masque(surface,1300,30,0,670)
                affichage_texte(surface,"Bravoo! Le monstre est mort",20,500,675,"courier",code_couleur("green"))
                masque(surface,cote,cote,img_rect.left,img_rect.top)
                surface.fill("orange")
                infos["compteur"]=0
                return jeu.jeu(lab,infos,surface,pos_perso)
        if infos["monstre"]== 0:
            masque(surface,1300,30,0,670)
            affichage_texte(surface,"Bravoo! Le monstre est mort",20,500,675,"courier",code_couleur("green"))
            masque(surface,cote,cote,img_rect.left,img_rect.top)
            infos["compteur"]=0
            surface.fill("orange")
            return afficheur_environnement_de_jeu.affiche_labyrinthe(lab,surface,pos_perso,infos)

        if infos["po"]<0 or infos["armes"]<0 :
            infos["compteur"] = 0
            return jeu.jeu(lab,infos,surface,pos_perso)


        pygame.display.flip()


def affichage_texte(surface, texte,taille, i,j,police,couleur) :
    pygame.font.quit()
    pygame.font.init()
    font = pygame.font.Font.render(pygame.font.SysFont(police, taille),texte,True, couleur,None )
    visuel= font.get_rect()
    visuel.left = i
    visuel.top = j
    surface.blit(font,visuel)
    pygame.display.flip()


def code_couleur(arg) :
    if arg == "blue" :
        code = (0, 0, 255)
    elif arg == "yellow" :
        code = (255, 255, 0)

    elif arg == "black" :
        code = (0, 0, 0)

    elif arg == "green" :
        code = (0, 255, 0)

    elif arg == "red" :
        code = (255, 0, 0)

    elif arg == "white" :
        code = (255, 255, 255)

    elif arg == "orange" :
        code = (237, 127, 16)
    
    elif arg == "gray" :
        code = (96, 96, 96)

    elif arg == "grey" :
        code = (132, 132, 132)

    elif arg == "kaki" :
        code = (148, 129, 43)

    return code


def direction() :
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.display.quit()
                os._exit(1)
            if event.type == pygame.KEYDOWN :
                if str(pygame.key. name (event.key)) =="down" :
                    direction = "bas"
                    return  direction
                if str(pygame.key. name (event.key)) =="up" :
                    direction = "haut"
                    return  direction
                if str(pygame.key. name (event.key)) =="left" :
                    direction = "gauche"
                    return  direction
                if str(pygame.key. name (event.key)) =="right" :
                    direction = "droit"
                    return  direction
                if str(pygame.key. name (event.key)) =="escape" :
                    direction = "arret"
                    return  direction

def decision () :
    joueur_de_sound("sounds/decision.mp3")
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.display.quit()
                os._exit(1)
            if event.type == pygame.KEYDOWN :
                if str(pygame.key. name (event.key)) =="return" :
                    choix = "entrer"
                    return  choix
                if str(pygame.key. name (event.key)) =="tab" :
                    choix = "infos"
                    return  choix
                if str(pygame.key. name (event.key)) =="escape" :
                    choix = "arret"
                    return choix


def analiste(surface,i,j,ligne,infos) :
    for composants in ligne :
        if infos["compteur"]<=20 :
            if composants == "O" :
                affichage_image_transformée(surface,"images/sortie.png",i,j,(30,30))

            if composants =="+" or composants == "-" or composants == "_" or composants =="|" :
                affichage_image_transformée(surface,"images/b.png",i,j,(30,30))

            if  composants == "1" :
                affichage_image_transformée(surface,"images/vie.png",i,j,(30,30))

            if  composants == "2" :
                affichage_image_transformée(surface,"images/armes.png",i,j,(30,30))

            if  composants == "3" :
                affichage_image_transformée(surface,"images/tresor.png",i,j,(30,30))

            if  composants =="✘":
                affichage_image_transformée(surface,"images/ennemi.png",i,j,(30,30))
            if  composants =="z" or composants =="b":
                affichage_image_transformée(surface,"images/boss.png",i,j,(30,30))

        i+= 30
    infos["compteur"]=infos["compteur"] + 1

    return i
def affichage_texte_fond(surface, texte,taille, i,j,police,couleur,fond) :
    pygame.font.quit()
    pygame.font.init()
    font = pygame.font.Font.render(pygame.font.SysFont(police, taille),texte,True, couleur,fond )
    visuel= font.get_rect()
    visuel.left = i
    visuel.top = j
    surface.blit(font,visuel)
    pygame.display.flip()

def petites_infos(surface,texte1,texte2,texte3) :
    affichage_texte_fond(surface,texte1,20,200,200,str(pygame.font.get_fonts()[10]),code_couleur("black"),code_couleur("white"))
    ralentisseur(0.1)
    affichage_texte_fond(surface,texte2,20,200,230,str(pygame.font.get_fonts()[10]),code_couleur("black"),code_couleur("white"))
    ralentisseur(0.1)
    affichage_texte_fond(surface,texte3,20,200,260,str(pygame.font.get_fonts()[10]),code_couleur("black"),code_couleur("white"))
    ralentisseur(1)
    surface.fill("orange")

def masque(surface,longueur,hauteur,i,j) :
    img = pygame.Surface((longueur,hauteur))
    img_rect = img.fill("orange")
    img_rect.left = i
    img_rect.top = j
    surface.blit(img, img_rect)



def joueur_de_sound(sound):
    pygame.mixer.init()
    if pygame.mixer.get_init():
        pass
    sound = pygame.mixer.Sound(sound).play()

