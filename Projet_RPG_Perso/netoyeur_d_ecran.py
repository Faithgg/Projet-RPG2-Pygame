import sys
import os

def efface_ecran() :
    """
    Efface l’écran de la console
    """
    if sys.platform.startswith("win") :
    # Si système Windows
        os.system("cls")
    else :
    # Si système Linux ou OS X
        os.system("clear")

