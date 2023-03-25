
import le_modul_pygame
import jeu
import chargeur_de_niveau
def officer(surface,infos) :
    for n_level in range(infos["level"], 36) :
        if n_level%6 ==0 :
            infos["speed"]=[n_level/2,n_level/2]
        infos["popop"]=510
        infos["papap"]=110
        infos["pipip"]=510
        infos["pupup"]=110
        infos["direction"]=None
        pos_perso = [1,1]
        infos["compteur"]= 0
        if n_level < 20 :
            infos["vitesse"] =[2,2]
        else :
            infos["vitesse"] =[2 + n_level/100, 2+ n_level/100]

        if n_level - 1 > 0 :
            infos["po"] = infos["po"] + 50
        if n_level==1 :
            surface.fill("white")
            le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
            le_modul_pygame.petites_infos(surface,"Bienvenue dans cette première partie de jeu "+str(infos["name"]),"Déplacez-vous grace aux tourches de directions de votre clavier","Ramassez les trésors,les vies et les armes en passant")
            le_modul_pygame.ralentisseur(1.5)
            surface.fill("white")
            le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
            le_modul_pygame.petites_infos(surface,"Un de vos buts est de passez en évitant les ennemis en tête de mort.","Si dangereux qu'ils sont, ils vous feront gaspiller vos vies et vos armes.","Vous avez pour grande tache de retrouver la sortie marquant fin de la partie")
            le_modul_pygame.ralentisseur(2)
            surface.fill("white")
            le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
            le_modul_pygame.affichage_texte(surface,"Vous serez invisible parfois à la rencontre d'eau dans le Labyrinthe.",25,140,400,"courier",le_modul_pygame.code_couleur("kaki"))
            le_modul_pygame.petites_infos(surface,"En cas de manque de vie ou d'armes, vous serez dirrigé vers la boutique","afin de payer des vies ou des armes en fonctions de vos trésors ou armes gagnés.","                                 BONNE CHANCE!                                ")
            le_modul_pygame.ralentisseur(2)
            surface.fill("orange")


        if n_level==2 :
            surface.fill("white")
            le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
            le_modul_pygame.affichage_texte(surface,"Soyez prudent, des  Boss sont cachés sous certaines feuilles pour protéger ces trésors.",20,110,400,"courier",le_modul_pygame.code_couleur("red"))
            le_modul_pygame.affichage_texte(surface,"          Avec ce mystère de feuilles, soyez prêt à tout moment pour attaquer.         ",22,110,430,"courier",le_modul_pygame.code_couleur("green"))
            le_modul_pygame.petites_infos(surface,"Des feuilles courvrent certains plans d'eaux","Des tresors abandonnés par des pirates sont laissés dans le labyrinthe.","D'autres de ces trésors sont cachés sous ces feuilles.")
            le_modul_pygame.ralentisseur(1.6)
            surface.fill("orange")

        if n_level==3 :
            surface.fill("white")
            le_modul_pygame.affichage_image_transformée(surface,"images/bordue.png",0,0,(1300,700))
            le_modul_pygame.affichage_texte(surface,"  Sinon, à chaque rencontre, tu l'attaques en perdant des vies/armes ",22,180,400,"courier",le_modul_pygame.code_couleur("red"))
            le_modul_pygame.affichage_texte(surface,"---> Si t'es plus armé et en Vie que lui, tu le tueras par contre.  ",22,180,430,"courier",le_modul_pygame.code_couleur("green"))
            le_modul_pygame.affichage_texte(surface,"Le combat se fera en terre ferme. Sortez du Lab pour gagner le niveau",22,180,460,"courier",le_modul_pygame.code_couleur("green"))
            le_modul_pygame.affichage_texte(surface,"      -->   ATTENTION! Vous avez droit à 100 déplacements   <--      ",22,180,490,"arialunicode",le_modul_pygame.code_couleur("red"))
            le_modul_pygame.petites_infos(surface,"Ce type de partie est assez spécial et demande de virgilance.","De plus de ce que vous savez déjà, vous devez fuir dans cette partie.","Evitez le monstre jusqu'à sortir du labyrinthe")
            le_modul_pygame.ralentisseur(2)
            surface.fill("orange")

        if n_level%3 ==0 :
            pos_perso= [10,10]
        level = chargeur_de_niveau.charge_labyrinthe("level_" + str(n_level))
        infos["level"]=n_level
        le_modul_pygame.joueur_de_sound("sounds/piano.mp3")
        infos["monstre"] = infos["level"]*2
        jeu.jeu(level, infos, surface, pos_perso)
            
    if infos["level"]>36 :
            print("---------------------------------Bravo! Fin du jeu---------------------------------------")
            le_modul_pygame.stop()

            """
            x=31
            while x <= 45 :
                level= "niveaux/level_"+ str(x)+ ".txt"
                fic = open(level,"w")
                fic.close()
                x+=1
            """