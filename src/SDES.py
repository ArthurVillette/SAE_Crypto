from DES import *
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


def double_cryptage_SDES(message:str, cle1:str, cle2:str) :
    """Permet de crypter un message deux fois à l'aide de SEDS

    Args:
        message (String): le message à crypter
        cle1 (String)): la clé du premier chiffrage
        cle2 (String): la clé du deuxième chiffrage

    Returns:
        bytes: le message crypté
    """    
    byte_mess = bytes(message, "utf-8")
    byte_cle1 = cle1.to_bytes(3, "big")
    byte_cle2 = cle2.to_bytes(3, "big")
    c1 = [encrypt(int.from_bytes(byte_cle1, "big"), m) for m in byte_mess]
    c2 = [encrypt(int.from_bytes(byte_cle2, "big"), m) for m in c1]
    return c2

def cryptage_SDES(message:str, cle:str) :
    """ Permet d'applique un cryptage SDES à un message 

    Args:
        message (str): le message à crypter
        cle (str): la clé de chiffrement 

    Returns:
        bytes: le message crypté
    """    
    byte_mess = bytes(message, "utf-8")
    byte_cle = cle.to_bytes(3, "big")
    c = [encrypt(int.from_bytes(byte_cle, "big"), m) for m in byte_mess]
    return c

def decryptage_SDES(message:bytes, cle:str) :
    """ Permet de decrypté un message SDES

    Args:
        message (bytes): le message crypté
        cle (str): la clé de chiddrement 

    Returns:
        String: le message decrypté 
    """    
    byte_cle = cle.to_bytes(3, "big")
    d = [decrypt(int.from_bytes(byte_cle, "big"), m) for m in message]
    return d

def double_decryptage_SDES(message:bytes, cle1:str, cle2:str) :
    """Permet de decrypter un message chiffré deux fois à l'aide de SDES

    Args:
        message (bytes): le message chiffré 
        cle1 (str): la première clé de chiffrement 
        cle2 (str): la deuxième clé de chiffrement 

    Returns:
        String : le message claire
    """    
    byte_cle1 = cle1.to_bytes(3, "big")
    byte_cle2 = cle2.to_bytes(3, "big")
    d2 = [decrypt(int.from_bytes(byte_cle2, "big"), m) for m in message]
    d1 = [decrypt(int.from_bytes(byte_cle1, "big"), m) for m in d2]
    return bytes(d1).decode("utf-8")

def cassage_brutal_SDES(message_clair:str,message_chiffre:bytes) :
    """la fonction renvoie la clé de chiffrement de SDES

    Args:
        message_clair (_String_): le message clair
        message_chiffre (bytes): le message chiffré

    Returns:
        tuple: la clé de chiffrement
    """
    for i in range(1024) :
        for j in range(1024) :
            if double_cryptage_SDES(message_clair,i,j) == message_chiffre :
                return (i,j)
    return None


def cassage_Astucieux_SDES(message_clair:str,message_chiffre:bytes):
    """la fonction renvoie la clé de chiffrement de SDES

    Args:
        message_clair (_String_): le message clair
        message_chiffre (bytes): le message chiffré

    Returns:
        tuple: la clé de chiffrement
    """
    dico = {}
    for i in range(1024) :
        dico[str(cryptage_SDES(message_clair,i))] = i
        if str(decryptage_SDES(message_chiffre,i)) in dico :
            return (dico[str(decryptage_SDES(message_chiffre,i))],i)
    for j in range(1024) :
        if str(decryptage_SDES(message_chiffre,j)) in dico :
            return (dico[str(decryptage_SDES(message_chiffre,j))],j)
            
