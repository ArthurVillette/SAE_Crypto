from PIL import Image

def analyse_image(chemin:str)->None:
    """la fonction affiche l'image

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