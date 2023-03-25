from random import randint
def gains(infos, categorie) :
    """
La catégorie ici ne signifie que le chiffre rencontré par le joueur. Si 1, c'est la Vie; si 2, c'est les armes et si 3, 
c'est de l'argent ou tresor
"""
    if categorie == "1" :
        infos["pv"] = infos["pv"] + randint(1, 8)
    elif categorie == "2" :
        infos["armes"] = infos["armes"] + randint(5, 15)
    else :
        infos["po"] = infos["po"] + randint(10, 50)

