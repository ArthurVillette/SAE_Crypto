import partie1_crypto as dec
import SDES as sdes
import AES as aes
import time
import matplotlib.pyplot as plt

arsene= open("./txt/arsene_lupin_extrait.txt","r",encoding="utf-8").read()

def timeur (message_clair,message_chiffre) :
    """renvoit le temps d'execution du cassage brutal et astucieux

    Args:
        message_clair (String): le message decrypté
        message_chiffre (String): le message crypté

    Returns:
        tuple : les temps d'execution 
    """    
    t1 = time.perf_counter()
    sdes.cassage_brutal_SDES(message_clair,message_chiffre)
    t2 = time.perf_counter()
    sdes.cassage_Astucieux_SDES(message_clair,message_chiffre)
    t3 = time.perf_counter()
    return (t2-t1,t3-t2)




def compteur_brutal (message_clair,message_chiffre) :
    """la fonction compte le nombre d'essaie pour trouver la clé de chiffrement de SDES

    Args:
        message_clair (_String_): le message clair
        message_chiffre (_String_): le message chiffré

    Returns:
        tuple: la clé de chiffrement
    """
    compteur = 0
    for i in range(1024) :
        for j in range(1024) :
            compteur += 1
            if sdes.double_cryptage_SDES(message_clair,i,j) == message_chiffre :
                return compteur
    return compteur  


def compteur_astucieux (message_clair,message_chiffre):
    """la fonction renvoie la clé de chiffrement de SDES

    Args:
        message_clair (_String_): le message clair
        message_chiffre (_String_): le message chiffré

    Returns:
        tuple: la clé de chiffrement
    """
    dico = {}
    compteur = 0
    for i in range(1024) :
        compteur += 1
        dico[str(sdes.cryptage_SDES(message_clair,i))] = i
        if str(sdes.decryptage_SDES(message_chiffre,i)) in dico :
            return compteur
    for j in range(1024) :
        compteur += 1
        if str(sdes.decryptage_SDES(message_chiffre,j)) in dico :
            return compteur




def timeur_cryptage(phrase_claire,clee_SDES1, clee_SDES12,clee_AES):
    """renvoit le temps de cryptage pour un chiffrement SDES et AES

    Args:
        phrase_claire (String): le message decrypté 
        clee_SDES1 (String): la première clé SDES
        clee_SDES12 (String): la deuxième clé SDES
        clee_AES (String): La clé AES

    Returns:
        tuple : les temps d'execution 
    """    
    t1 = time.perf_counter()
    SDES= sdes.double_cryptage_SDES(phrase_claire,clee_SDES1, clee_SDES12)
    t2 = time.perf_counter()
    AES= aes.cryptage_AES(phrase_claire,clee_AES)
    t3 = time.perf_counter()
    return (t2-t1,t3-t2)

def timeur_decryptage(phrase_crypte_SDES,phrase_crypte_AES,clee_SDES1,clee_SDES2,clee_AES):
    """renvoit le temps de decryptage pour un chiffrement SDES et AES

    Args:
        phrase_claire (String): le message decrypté 
        clee_SDES1 (String): la première clé SDES
        clee_SDES12 (String): la deuxième clé SDES
        clee_AES (String): La clé AES

    Returns:
        tuple : les temps d'execution 
    """    
    t1 = time.perf_counter()
    SDES= sdes.double_decryptage_SDES(phrase_crypte_SDES,clee_SDES1,clee_SDES2)
    t2 = time.perf_counter()
    AES= aes.decrypt_AES(phrase_crypte_AES,clee_AES)
    t3 = time.perf_counter()
    return (t2-t1,t3-t2)





while(True):
    print("Menu graphique:")
    print("1: temps de cassage de SDES")
    print("2: nombre d'essaie de cassage de SDES")
    print("3: temps de cryptage de SDES et AES")
    print("4: temps de decryptage de SDES et AES")
    print("5: quitter")
    choix= input("choisissez un menu: ")
    if (choix=="1"):
        t1= timeur("ceci est un test",[171, 205, 171, 225, 168, 205, 83, 252, 168, 253, 134, 168, 252, 205, 83, 252])
        print(t1)
        t2= timeur("ceci est un test",[103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180])
        print(t2)
        t3= timeur("ceci est un test",[33, 6, 33, 166, 252, 6, 122, 115, 252, 58, 201, 252, 115, 6, 122, 115])
        print(t3)
        size=["0","[1,1]","[2,5]","[20,50]"]
        time_brutal=[0,t1[1],t2[1],t3[1]]
        time_Astucieux=[0,t1[0],t2[0],t3[0]]
        plt.plot(size, time_brutal)
        plt.plot(size, time_Astucieux)
        plt.suptitle('Temps de cassage astucieux et brutal en fonction de la clé') 
        plt.xlabel('Taille de la clé')
        plt.ylabel('Temps de cassage')
        plt.legend(["asctucieux","brutal"])
        plt.show()
        
        
    elif (choix=="2"):
        c1= compteur_brutal("ceci est un test",[171, 205, 171, 225, 168, 205, 83, 252, 168, 253, 134, 168, 252, 205, 83, 252])
        print(c1)
        c2= compteur_brutal("ceci est un test",[103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180])
        print(c2)
        c3= compteur_brutal("ceci est un test",[33, 6, 33, 166, 252, 6, 122, 115, 252, 58, 201, 252, 115, 6, 122, 115])
        print(c3)
        Ca1= compteur_astucieux("ceci est un test",[171, 205, 171, 225, 168, 205, 83, 252, 168, 253, 134, 168, 252, 205, 83, 252])
        print(Ca1)
        Ca2= compteur_astucieux("ceci est un test",[103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180])
        print(Ca2)
        Ca3= compteur_astucieux("ceci est un test",[33, 6, 33, 166, 252, 6, 122, 115, 252, 58, 201, 252, 115, 6, 122, 115])
        print(Ca3)


        size=["[1,1]","[2,5]","[20,50]"]
        brutal=[c1,c2,c3]
        astucieux=[Ca1,Ca2,Ca3]
        plt.plot(size,brutal)
        plt.plot(size,astucieux)
        plt.suptitle('nombre d essaye  de cassage astucieux et brutal en fonction de la clé')
        plt.xlabel('Taille de la clé')
        plt.ylabel('nombre d essaye')
        plt.legend(["brutal","astucieux"])
        plt.show()
    elif (choix=="3"):
        c1= timeur_cryptage(arsene[:1],10,5,"AES")
        print(c1)
        c2= timeur_cryptage(arsene[:10],10,5,"AES")
        print(c2)
        c3= timeur_cryptage(arsene[:100],10,5,"AES")
        print(c3)
        c4= timeur_cryptage(arsene[:200],10,5,"AES")
        print(c4)
        c5= timeur_cryptage(arsene[:500],10,5,"AES")
        print(c5)
        c6= timeur_cryptage(arsene[:800],10,5,"AES")
        print(c6)
        c7= timeur_cryptage(arsene[:1000],10,5,"AES")
        print(c7)
        c8= timeur_cryptage(arsene[:1500],10,5,"AES")
        print(c8)
        size="1","10","100","200","500","800","1000","1500"
        SDES= [c1[0],c2[0],c3[0],c4[0],c5[0],c6[0],c7[0],c8[0]]
        AES= [c1[1],c2[1],c3[1],c4[1],c5[1],c6[1],c7[1],c8[1]]
        plt.plot(size,SDES)
        plt.plot(size,AES)
        plt.suptitle('Temps de cryptage SDES et AES en fonction de la taille du message')
        plt.xlabel('Taille du message')
        plt.ylabel('Temps de cryptage')
        plt.legend(["SDES","AES"])
        plt.show()
    elif (choix=="4"):
        d1= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:1],10,5),aes.cryptage_AES(arsene[:1],"AES"),10,5,"AES")
        print(d1)
        d2= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:10],10,5),aes.cryptage_AES(arsene[:10],"AES"),10,5,"AES")
        print(d2)
        d3= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:100],10,5),aes.cryptage_AES(arsene[:100],"AES"),10,5,"AES")
        print(d3)
        d4= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:200],10,5),aes.cryptage_AES(arsene[:200],"AES"),10,5,"AES")
        print(d4)
        d5= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:500],10,5),aes.cryptage_AES(arsene[:500],"AES"),10,5,"AES")
        print(d5)
        d6= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:800],10,5),aes.cryptage_AES(arsene[:800],"AES"),10,5,"AES")
        print(d6)
        d7= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:1000],10,5),aes.cryptage_AES(arsene[:1000],"AES"),10,5,"AES")
        print(d7)
        d8= timeur_decryptage(sdes.double_cryptage_SDES(arsene[:1500],10,5),aes.cryptage_AES(arsene[:1500],"AES"),10,5,"AES")
        print(d8)
        size="1","10","100","200","500","800","1000","1500"
        SDES= [d1[0],d2[0],d3[0],d4[0],d5[0],d6[0],d7[0],d8[0]]
        AES= [d1[1],d2[1],d3[1],d4[1],d5[1],d6[1],d7[1],d8[1]]
        plt.plot(size,SDES)
        plt.plot(size,AES)
        plt.suptitle('Temps de decryptage SDES et AES en fonction de la taille du message')
        plt.xlabel('Taille du message')
        plt.ylabel('Temps de decryptage')
        plt.legend(["SDES","AES"])
        plt.show()
    elif (choix=="5"):
        print("Au revoir")
        exit()
    else:
        print("erreur de saisie")
        exit()
    