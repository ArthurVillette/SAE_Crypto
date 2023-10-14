

mot_cripté = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE. YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD"

def import_texte(chemin:str) -> str :
    """la fonction importe un texte d'un fichier texte

    Args:
        chemin (String): emplacement du fichier texte

    Returns:
        _String_: le texte du fichier
    """
    fichier = open(chemin,"r")
    res = fichier.read()
    fichier.close()
    return res
    

def lettre_la_plus_commune(mot_cripte:str) -> str:
    """la fonction renvoie la lettre la plus commune dans un texte

    Args:
        mot_cripte (string): le texte

    Returns:
        _string_: la lettre la plus commune
    """
    alphabe= dict()
    for lettre in mot_cripte:
        if lettre.upper() in alphabe:
            alphabe[lettre.upper()] += 1
        else:
            if lettre != " ":
                alphabe[lettre.upper()] = 1
    return max(alphabe, key=alphabe.get)

def get_decalage(lettre_la_plus_commune:str)->int:
    """la fonction renvoie le décalage entre la lettre la plus commune et la lettre E

    Args:
        lettre_la_plus_commune (string): la lettre la plus commune

    Returns:
        _int_: le décalage
    """
    return ord(lettre_la_plus_commune) - ord("E")


def decrypte_cesar(mot:str,decalage:int)->str:
    """la fonction renvoie le texte décrypté avec la méthode de César

    Args:
        mot (_String_): le texte à décrypter
        decalage (_int_): le décalage entre la lettre la plus commune et la lettre E

    Returns:
        _String_: le texte décrypté
    """
    rep = ""
    for char in mot :
        if char.isalpha() :
            rep += chr((ord(char) - decalage - 65) % 26 + 65)
        else :
            rep += char
    return rep

def decrypte_message1(chemin:str)->str:
    """la fonction renvoie le message 1 décrypté

    Args:
        chemin (_String_): le chemin du fichier texte

    Returns:
        _String_: le message 1 décrypté
    """
    mot=True
    res=""
    texte_crypté=import_texte(chemin)
    lettre_courant= lettre_la_plus_commune(texte_crypté)
    decalage = get_decalage(lettre_courant)
    message_clair = decrypte_cesar(texte_crypté,decalage)
    for lettre in message_clair:
        if lettre == "\n":
            mot = True
        else :
            if mot :
                res += lettre.upper()
                mot = False
    return res

def decrypte_vignère(mot:str,cle:str)->str:
    """la fonction renvoie le texte décrypté avec la méthode de Vignère
    Args:
        mot (_String_): le texte à décrypter
        cle (_String_): la clé de décryptage
    Returns:
        _String_: le texte décrypté
    """
    res = ""
    espace=0
    for ind in range(len(mot)):
        if mot[ind] != " " and mot[ind] != "\n":
            res+= chr((ord(mot[ind])-(ord(cle[(ind-espace)%len(cle)]))+26)%26+65)
        else:
            res+=mot[ind]
            espace+=1
    return res
