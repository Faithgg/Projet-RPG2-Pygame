import le_modul_pygame
import pygame

def acheter_avec_pieces(level,infos, pos_perso,surface) :
    if infos["po"]*(3/4) < 10 :
        surface.fill("white")
        le_modul_pygame.joueur_de_sound("sounds/echec.mp3")
        le_modul_pygame.petites_infos(surface,"Vue votre solde actuel, on vous retourne vers la vente de vos armes",None,None)
        le_modul_pygame.ralentisseur(0.5)
        acheter_avec_armes(level,infos, pos_perso,surface)
    else :
        vie_ajoutee = (infos["po"]*(3/4))//10
        infos["pv"] = infos["pv"] + vie_ajoutee
        infos["po"] =(infos["po"]*(1/4)) + (infos["po"]*(3/4)) % 10
        surface.fill("white")
        le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
        le_modul_pygame.petites_infos(surface,"Vous avez chargé " + str(vie_ajoutee) + " vies de plus",None,"Du courage pour la suite, soyez prudent!")
        le_modul_pygame.ralentisseur(1.5)
        surface.fill("orange")

        

def acheter_avec_armes(level,infos, pos_perso,surface) :
    if infos["armes"] < 4 :
        surface.fill("white")
        le_modul_pygame.joueur_de_sound("sounds/echec.mp3")
        le_modul_pygame.petites_infos(surface,"Vue votre solde actuel, on vous retourne vers l'achat avec vos pièces",None,None)
        le_modul_pygame.ralentisseur(0.5)
        acheter_avec_pieces(level,infos, pos_perso,surface)
    else :
        vie_ajoutee = infos["armes"]//5
        infos["pv"] = infos["pv"] + vie_ajoutee
        infos["armes"] = infos["armes"] % 5
        surface.fill("white")
        le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
        le_modul_pygame.petites_infos(surface,"Vous avez chargé " + str(vie_ajoutee) + " vies de plus",None,"Du courage pour la suite, soyez prudent!")
        le_modul_pygame.ralentisseur(1.5)
        surface.fill("orange")



def acheter(level,infos, pos_perso,surface) :
    surface.fill("white")
    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
    le_modul_pygame.petites_infos(surface,"D'abord! Vous avez le choix entre Vous soigner avec le reste de votre argent  ","ou Vendre le reste de votre armement pour vous soigner.                       ",None)
    le_modul_pygame.ralentisseur(1.5)
    surface.fill("white")
    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
    le_modul_pygame.petites_infos(surface,"         !!!!!!!!!!!            A SAVOIR              !!!!!!           ","Vue le marché, une Vie est vendue à une valeur équivalente de 10 pièces","                  ou à une valeur équivalente de 5 armes.              ")
    le_modul_pygame.ralentisseur(1)
    le_modul_pygame.affichage_texte(surface,"Pour payer avec votre armement, veuillez cliquer <Entrer>",30,120,300,str(pygame.font.get_fonts()[10]),le_modul_pygame.code_couleur("black"))
    le_modul_pygame.affichage_texte(surface,"Pour payer avec vos trésors, veuillez cliquer <Tab>",30,120,350,str(pygame.font.get_fonts()[10]),le_modul_pygame.code_couleur("green"))
    decision = le_modul_pygame.decision()
    if str(decision) == "entrer" :
        acheter_avec_armes(level,infos, pos_perso,surface)
    elif str(decision) == "infos" :
        acheter_avec_pieces(level,infos, pos_perso,surface)
    else :
        acheter(level,infos, pos_perso,surface)


def armer(infos,surface) :

    armes_ajoutees = (infos["po"]*(3/4))//4
    infos["armes"] = infos["armes"] + armes_ajoutees
    infos["po"] = (infos["po"]*(1/4))+(infos["po"]*(3/4)) % 4 #Au cas où le reste serait zéro, ne pas dirriger diectement vers achat d'armes
    surface.fill("white")
    le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
    le_modul_pygame.petites_infos(surface,"Vous avez payé " + str(armes_ajoutees) + " armes de plus",None,"Du courage pour la suite, soyez prudent!")
    le_modul_pygame.ralentisseur(1.5)
    surface.fill("orange")


