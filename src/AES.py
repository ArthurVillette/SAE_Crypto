from DES import *
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def cryptage_AES (message:str, clee_chiffrage:str):
    """la fonction renvoie le message crypté avec la méthode AES

    Args:
        message (_String_): le message à crypter
        cle (_String_): la clé de cryptage

    Returns:
        bytes: le message crypté
    """
    clee_chiffrage = clee_chiffrage.ljust(32)[:32].encode()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(clee_chiffrage), modes.CFB(iv), backend=default_backend())
    padder = padding.PKCS7(128).padder()
    data = padder.update(message.encode()) + padder.finalize()
    encryptor = cipher.encryptor()
    texteCrypte = encryptor.update(data) + encryptor.finalize()

    return iv + texteCrypte


def decrypt_AES(texteCrypte:bytes, clee_chiffrage:str):
    """la fonction renvoie le message décrypté avec la méthode AES

    Args:
        texteCrypte (bytes): le message à décrypter
        cle (_String_): la clé de décryptage
        
    Returns:
        _String_: le message décrypté
    """
    iv = texteCrypte[:16]
    texteCrypte = texteCrypte[16:]
    clee_chiffrage = clee_chiffrage.ljust(32)[:32].encode()
    cipher = Cipher(algorithms.AES(clee_chiffrage), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    data = decryptor.update(texteCrypte) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(data) + unpadder.finalize()
    return message.decode()


def cryptage_AES_CBC (message:str, clee_chiffrage:bytes, iv:bytes):
    """la fonction renvoie le message crypté avec la méthode AES, en mode CBC

    Args:
        message (_String_): le message à crypter
        cle (bytes): la clé de cryptage
        iv (bytes) : le vecteur d'initialisation

    Returns:
        bytes: le message crypté
    """
    cipher = Cipher(algorithms.AES(clee_chiffrage), modes.CBC(iv), backend=default_backend())
    padder = padding.PKCS7(128).padder()
    data = padder.update(message.encode()) + padder.finalize()
    encryptor = cipher.encryptor()
    texteCrypte = encryptor.update(data) + encryptor.finalize()

    return texteCrypte

def decrypt_AES_CBC(texteCrypte:bytes, clee_chiffrage:bytes, iv:bytes):
    """la fonction renvoie le message décrypté avec la méthode AES, en mode CBC

    Args:
        texteCrypte (bytes): le message à décrypter
        cle (bytes): la clé de décryptage
        iv (bytes) : le vecteur d'initialisation 
        
    Returns:
        _String_: le message décrypté
    """
    cipher = Cipher(algorithms.AES(clee_chiffrage), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    data = decryptor.update(texteCrypte) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(data) + unpadder.finalize()
    return message.decode()