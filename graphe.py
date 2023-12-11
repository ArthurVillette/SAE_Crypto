from decryptage import *
import time
import matplotlib.pyplot as plt

def timeur (message_clair,message_chiffre) :
    t1 = time.perf_counter()
    cassage_brutal_SDES(message_clair,message_chiffre)
    t2 = time.perf_counter()
    cassage_Astucieux_SDES(message_clair,message_chiffre)
    t3 = time.perf_counter()
    return (t2-t1,t3-t2)
t1= timeur("ceci est un test",[171, 205, 171, 225, 168, 205, 83, 252, 168, 253, 134, 168, 252, 205, 83, 252])
print(t1)
t2= timeur("ceci est un test",[103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180])
print(t2)
t3= timeur("SAE CRYPTOGRAPHIE",[198, 202, 38, 252, 114, 188, 210, 89, 226, 48, 64, 188, 202, 89, 143, 110, 38])
print(t3)
# t4= timeur("SAE CRYPTOGRAPHIE",[62, 129, 136, 45, 17, 18, 177, 219, 154, 36, 15, 18, 129, 219, 166, 167, 136])
# print(t4)
# t5= timeur("la crypto ses chouette",[129, 36, 101, 202, 23, 220, 189, 185, 42, 101, 115, 32, 115, 101, 202, 133, 42, 144, 32, 185, 185, 32])
# print(t5)
# t6= timeur("Arsène Lupin parmi nous! l'insaisissable cambrioleur dont on racontait les prouesses dans tous les journaux depuis des mois!",[65, 114, 115, 195, 168, 110, 101, 32, 76, 117, 112, 105, 110, 32, 112, 97, 114, 109, 105, 32, 110, 111, 117, 115, 33, 32, 108, 39, 105, 110, 115, 97, 105, 115, 105, 115, 115, 97, 98, 108, 101, 32, 99, 97, 109, 98, 114, 105, 111, 108, 101, 117, 114, 32, 100, 111, 110, 116, 32, 111, 110, 32, 114, 97, 99, 111, 110, 116, 97, 105, 116, 32, 108, 101, 115, 32, 112, 114, 111, 117, 101, 115, 115, 101, 115, 32, 100, 97, 110, 115, 32, 116, 111, 117, 115, 32, 108, 101, 115, 32, 106, 111, 117, 114, 110, 97, 117, 120, 32, 100, 101, 112, 117, 105, 115, 32, 100, 101, 115, 32, 109, 111, 105, 115, 33])
# print(t6)
size=["0","[1,1]","[2,5]","[20,50]"]
time_brutal=[0,t1[1],t2[1],t3[1]]
time_Astucieux=[0,t1[0],t2[0],t3[0]]
plt.plot(size, time_brutal)
plt.plot(size, time_Astucieux)
plt.show()  

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
            if double_cryptage_SDES(message_clair,i,j) == message_chiffre :
                return compteur
    return compteur  


def cassage_Astucieux_SDES(message_clair,message_chiffre):
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
        dico[str(cryptage_SDES(message_clair,i))] = i
        if str(decryptage_SDES(message_chiffre,i)) in dico :
            return compteur
    for j in range(1024) :
        compteur += 1
        if str(decryptage_SDES(message_chiffre,j)) in dico :
            return compteur

c1= compteur_brutal("ceci est un test",[171, 205, 171, 225, 168, 205, 83, 252, 168, 253, 134, 168, 252, 205, 83, 252])
print(c1)
c2= compteur_brutal("test",[180, 36, 90, 180])
print(c2)
c3= compteur_brutal("SAE CRYPTOGRAPHIE",[198, 202, 38, 252, 114, 188, 210, 89, 226, 48, 64, 188, 202, 89, 143, 110, 38])
print(c3)
Ca1= cassage_Astucieux_SDES("ceci est un test",[171, 205, 171, 225, 168, 205, 83, 252, 168, 253, 134, 168, 252, 205, 83, 252])
print(Ca1)
Ca2= cassage_Astucieux_SDES("test",[180, 36, 90, 180])
print(Ca2)
Ca3= cassage_Astucieux_SDES("SAE CRYPTOGRAPHIE",[198, 202, 38, 252, 114, 188, 210, 89, 226, 48, 64, 188, 202, 89, 143, 110, 38])
print(Ca3)


size=["[1,1]","[2,5]","[20,50]"]
compteur_brutal=[c1,c2,c3]
comteur_astucieux=[Ca1,Ca2,Ca3]
plt.plot(size,compteur_brutal)
plt.plot(size,comteur_astucieux)
plt.show()