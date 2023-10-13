

mot_cripté = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE. YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD"

def import_texte(chemin) :
    fichier = open(chemin,"r")
    res = fichier.read()
    fichier.close()
    return res
    

def lettre_la_plus_commune(mot_cripte):
    alphabe= dict()
    for lettre in mot_cripte:
        if lettre.upper() in alphabe:
            alphabe[lettre.upper()] += 1
        else:
            if lettre != " ":
                alphabe[lettre.upper()] = 1
    return max(alphabe, key=alphabe.get)

def get_decalage(lettre_la_plus_commune):
    return ord(lettre_la_plus_commune) - ord("E")


def decrypte_cesar(mot,decalage) :
    rep = ""
    for char in mot :
        if char.isalpha() :
            rep += chr((ord(char) - decalage - 65) % 26 + 65)
        else :
            rep += char
    return rep