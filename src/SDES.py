from DES import *
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


def double_cryptage_SDES(message, cle1, cle2) :
    byte_mess = bytes(message, "utf-8")
    byte_cle1 = cle1.to_bytes(3, "big")
    byte_cle2 = cle2.to_bytes(3, "big")
    c1 = [encrypt(int.from_bytes(byte_cle1, "big"), m) for m in byte_mess]
    c2 = [encrypt(int.from_bytes(byte_cle2, "big"), m) for m in c1]
    return c2

def cryptage_SDES(message, cle) :
    byte_mess = bytes(message, "utf-8")
    byte_cle = cle.to_bytes(3, "big")
    c = [encrypt(int.from_bytes(byte_cle, "big"), m) for m in byte_mess]
    return c

def decryptage_SDES(message, cle) :
    byte_cle = cle.to_bytes(3, "big")
    d = [decrypt(int.from_bytes(byte_cle, "big"), m) for m in message]
    return d

def double_decryptage_SDES(message, cle1, cle2) :
    byte_cle1 = cle1.to_bytes(3, "big")
    byte_cle2 = cle2.to_bytes(3, "big")
    d2 = [decrypt(int.from_bytes(byte_cle2, "big"), m) for m in message]
    d1 = [decrypt(int.from_bytes(byte_cle1, "big"), m) for m in d2]
    return bytes(d1).decode("utf-8")

def cassage_brutal_SDES(message_clair,message_chiffre) :
    """la fonction renvoie la clé de chiffrement de SDES

    Args:
        message_clair (_String_): le message clair
        message_chiffre (_String_): le message chiffré

    Returns:
        tuple: la clé de chiffrement
    """
    for i in range(1024) :
        for j in range(1024) :
            if double_cryptage_SDES(message_clair,i,j) == message_chiffre :
                return (i,j)
    return None


def cassage_Astucieux_SDES(message_clair,message_chiffre):
    """la fonction renvoie la clé de chiffrement de SDES

    Args:
        message_clair (_String_): le message clair
        message_chiffre (_String_): le message chiffré

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
            
