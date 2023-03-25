from random import randint
def combat(infos,type) :
    """
Détermine le nombre de points de vie perdus lors d’un combat
infos : données de jeu (niveaux, nombre de pièces d’or et points de vie)
"""
    if type == "✘" :
        ennemis = randint(2, 7) # Le nombre d'ennemis présents succeptible d'etre tué par le joueur
        infos["pv"] = infos["pv"] - randint(4, 10) #Le nombre de vie du joueur qui descend aléatoirement
        infos["armes"] = infos["armes"] - ennemis #Les armes du joueur qui diminuent en fonction du nombre d'ennemis 
    #(disons un ennemi, une balle)
    elif type == "b" :
        ennemis = randint(10, 20) # Le nombre d'ennemis présents succeptible d'etre tué par le joueur
        infos["pv"] = infos["pv"] - randint(8, 15) #Le nombre de vie du joueur qui descend aléatoirement
        infos["armes"] = infos["armes"] - ennemis #Les armes du joueur qui diminuent en fonction du nombre d'ennemis 

