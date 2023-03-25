import os
import sys
import les_donnees
import fights
import le_modul_pygame
import afficheur_environnement_de_jeu
import jeu
import pygame
import netoyeur_d_ecran
def verification_deplacement(surface,lab,infos, pos_col, pos_ligne):
    sys.setrecursionlimit(5000)#pour ne pas avoir dans la suite de problème de récursion maximale atteiente
    """
    Indique si le déplacement du personnage est autorisé ou pas.
    lab : Labyrinthe
    pos_ligne : position du personnage sur les lignes
    pos_col : position du personnage sur les colonnes
    Valeurs de retour :
    None : déplacement interdit
    [col, ligne] : déplacement autorisé sur la case indiquée
    par la liste
    """
        # Calcul de la taille du labyrinthe
    n_cols = len(lab[0])
    n_lignes = len(lab)
    # Teste si le déplacement conduit le personnage en dehors de l’aire
    # de jeu
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or pos_col > (n_cols -1) :
    #le symbole \ indique que la ligne n’est pas terminée
        return None
    elif lab[pos_ligne][pos_col] == "O" : 
        infos["compteur"]=0
        pygame.mixer.stop()
        le_modul_pygame.joueur_de_sound("sounds/sortie.mp3")
    # On retournera une position hors labyrinthe pour conduire à la victoire
        return[-1, -1] 
    #on attaque maintenant les objets à gagner.
    elif lab[pos_ligne][pos_col] == "1":
        le_modul_pygame.affichage_texte(surface,"    Vies Gagnées   ",20,500,675,"courier",le_modul_pygame.code_couleur("green"))
        pygame.display.flip()
        le_modul_pygame.joueur_de_sound("sounds/YEAY.mp3")
# teste si le personnage se déplace sur l'objet "Vie"

        les_donnees.gains( infos , lab[pos_ligne][pos_col] )
# On supprime le trésor découvert chap_chap
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " + lab[pos_ligne][pos_col +1:]
        return [pos_col, pos_ligne]


    elif lab[pos_ligne][pos_col] == "2" :
        le_modul_pygame.affichage_texte(surface,"   Armes Chargées  ",20,500,675,"courier",le_modul_pygame.code_couleur("green"))
        le_modul_pygame.joueur_de_sound("sounds/armes.mp3")
# teste si le personnage se déplace sur des ames
# fonction qui calcule le nombre d'armes rapporté 
        les_donnees.gains( infos , lab[pos_ligne][pos_col] )
# On supprime les armes découvertes chap_chap
        pygame.display.flip()
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " + lab[pos_ligne][pos_col +1:]
        return [pos_col, pos_ligne]


    elif lab[pos_ligne][pos_col] == "3" :
        le_modul_pygame.affichage_texte(surface,"Des trésors Gagnées",20,500,675,"courier",le_modul_pygame.code_couleur("green"))
        le_modul_pygame.joueur_de_sound("sounds/pieces.mp3")
# teste si le personnage se déplace sur un trésor
# Découverte d’un trésor
# fonction qui calcule le montant rapporté par le trésor
        les_donnees.gains( infos , lab[pos_ligne][pos_col] )
# On supprime le trésor découvert chap_chap
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " + lab[pos_ligne][pos_col +1:]
        return [pos_col, pos_ligne]

        #Les ennemis sont représentés par ✘ 
    elif lab[pos_ligne][pos_col] == "✘" :
        le_modul_pygame.affichage_texte(surface,"    !! COMBATS !!  ",20,500,675,"courier",le_modul_pygame.code_couleur("red"))
        le_modul_pygame.joueur_de_sound("sounds/Quack.mp3")
    # cCombat à la rencontre d’un ennemi
        fights.combat(infos,lab[pos_ligne][pos_col])
# On supprime l'ennemi rencontré et on retourne les nouvelles positions de notre joueur
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " + lab[pos_ligne][pos_col +1:]
        return [pos_col, pos_ligne]

    elif lab[pos_ligne][pos_col] == "b" :
        le_modul_pygame.affichage_texte(surface,"    !! Le Boss attaque !!  ",20,500,675,"courier",le_modul_pygame.code_couleur("red"))
        le_modul_pygame.joueur_de_sound("sounds/boss.mp3")
    # Combat à la rencontre du boss
        fights.combat(infos,lab[pos_ligne][pos_col])
# On supprime l'ennemi rencontré et on retourne les nouvelles positions de notre joueur
        lab[pos_ligne] = lab[pos_ligne][:pos_col] + " " + lab[pos_ligne][pos_col +1:]
        le_modul_pygame.ralentisseur(0.3)
        return [pos_col, pos_ligne]

    elif lab[pos_ligne][pos_col] != " " and lab[pos_ligne][pos_col] != "z":
        return None
    else :
        return [pos_col, pos_ligne]



def choix_joueur(lab,surface, infos, pos_perso):
    sys.setrecursionlimit(5000)#pour ne pas avoir dans la suite de problème de récursion maximale atteiente
    """
Demande au joueur de saisir son déplacement
et vérifie s’il est possible.
Si ce n’est pas le cas affiche un message,
sinon modifie la position du perso
dans la liste pos_perso
lab : Labyrinthe
pos_perso : liste contenant la position du personnage
[colonne, ligne]
Pas de valeur de retour
    """
    dep = None
    if infos["direction"]=="down" or infos["direction"]=="left" or infos["direction"]=="right" or infos["direction"]=="up":
        if infos["direction"]=="up" :
            dep = verification_deplacement(surface,lab, infos,pos_perso[0], pos_perso[1] -1)
        elif infos["direction"]=="down" :
            dep = verification_deplacement(surface,lab,infos, pos_perso[0], pos_perso[1] +1)
        elif infos["direction"]=="left" :
            dep = verification_deplacement(surface,lab,infos, pos_perso[0] -1, pos_perso[1])
        elif infos["direction"]=="right" :
            dep = verification_deplacement(surface,lab,infos, pos_perso[0] +1, pos_perso[1])
        elif infos["direction"]=="escape" :
            os._exit(1)
    else :
        direction = le_modul_pygame.direction()
        if direction =="haut" :
            dep = verification_deplacement(surface,lab, infos,pos_perso[0], pos_perso[1] -1)
        elif direction =="bas" :
            dep = verification_deplacement(surface,lab,infos, pos_perso[0], pos_perso[1] +1)
        elif direction =="gauche" :
            dep = verification_deplacement(surface,lab,infos, pos_perso[0] -1, pos_perso[1])
        elif direction =="droit" :
            dep = verification_deplacement(surface,lab,infos, pos_perso[0] +1, pos_perso[1])
        elif direction =="arret" :
            os._exit(1)
    # attention il faut importer le module os
    # en début de script il faut écrire : import os
    infos["direction"]=None
    le_modul_pygame.masque(surface,1300,30,0,670) #Masquons rapidement l'informations envoyée après le déplacement
    if dep == None :
        le_modul_pygame.affichage_texte(surface,"Déplacement Impossible",20,500,675,"courier",le_modul_pygame.code_couleur("red"))
        le_modul_pygame.joueur_de_sound("sounds/echec.mp3")
        le_modul_pygame.ralentisseur(0.1)
        le_modul_pygame.masque(surface,1300,30,0,670)
    else :
        pos_perso[0] = dep[0] # modification du contenu de la liste
        pos_perso[1] = dep[1] # pos_perso
        if pos_perso == [-1, -1] or  infos["pv"] <= 0 or infos["armes"] <= 0 :
            netoyeur_d_ecran.efface_ecran()#Bah de la console hein 😄
            infos["compteur"]=0
            jeu.jeu(lab, infos, surface, pos_perso)
        else :
            le_modul_pygame.masque(surface,30,30,infos["pop"],infos["pap"])
            le_modul_pygame.masque(surface,1300,30,0,0)

            netoyeur_d_ecran.efface_ecran()
            afficheur_environnement_de_jeu.affiche_labyrinthe(lab,surface, pos_perso, infos)

        
        

