

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

def decrypte_message1(chemin):
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

def decrypte_vignère(mot,cle):
    res = ""
    espace=0
    for ind in range(len(mot)):
        if mot[ind] != " " and mot[ind] != "\n":
            res+= chr((ord(mot[ind])-(ord(cle[(ind-espace)%len(cle)]))+26)%26+65)
        else:
            res+=mot[ind]
            espace+=1
    return res
