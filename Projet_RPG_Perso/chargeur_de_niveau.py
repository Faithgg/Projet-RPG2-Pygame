import os
import le_modul_pygame
def charge_labyrinthe(nom) :
    """
Charge le labyrinthe depuis le fichier nom.txt
nom : nom du fichier contenant le labyrinthe (sans l’extension .txt)
Valeur de retour :
Tuple contenant les données du labyrinthe
"""
    le_modul_pygame.joueur_de_sound("sounds/niveau.mp3")
    try :
        fichier = open("niveaux/"+ nom + ".txt", "r")
# Lecture des données dans le fichier
        data = fichier.readlines()
        fichier.close()
    except IOError :
        return print("Vous avez terminé les niveaux disponibles pour le jeu")

# Parcours de la liste pour supprimer les caractères invisibles
    for i in range(len(data)) :
        data[i] = data[i].strip()
        return data 

