from PIL import Image

def analyse_image(chemin:str)->None:
    """la fonction retourne l'image en binaire en fonction de si ces pixels sont paire ou non

    Args:
        chemin (_String_): le chemin de l'image
    """
    image = Image.open(chemin)
    res = ""
    widht, height = image.size
    for i in range(height):
        for j in range(widht):
            couleur = image.getpixel((j,i))
            if couleur % 2 == 0:
                res += "0"
            else:
                res += "1"
    return res

def get_message_image(chemin:str)->str :
    """ Renvoit le message caché dans l'image

    Args:
        chemin (str): Le chemin de l'image 

    Returns:
        str: le message caché
    """    
    res = analyse_image(chemin)
    return res[:64]