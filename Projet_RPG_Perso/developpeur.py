import name
import le_modul_pygame
def informations(surface):
    le_modul_pygame.affichage_image_transformée(surface,"images/dev.png",0,0,(1300,700))
    le_modul_pygame.ralentisseur(1.3)
    surface.fill("white")
    name.name(surface)
