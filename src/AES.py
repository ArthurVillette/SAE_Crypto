from DES import *
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def cryptage_AES (message, clee_chiffrage):
    """la fonction renvoie le message crypté avec la méthode AES

    Args:
        message (_String_): le message à crypter
        cle (_String_): la clé de cryptage

    Returns:
        _String_: le message crypté
    """
    clee_chiffrage = clee_chiffrage.ljust(32)[:32].encode()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(clee_chiffrage), modes.CFB(iv), backend=default_backend())
    padder = padding.PKCS7(128).padder()
    data = padder.update(message.encode()) + padder.finalize()
    encryptor = cipher.encryptor()
    texteCrypte = encryptor.update(data) + encryptor.finalize()

    return iv + texteCrypte


def decrypt_AES(texteCrypte, clee_chiffrage):
    """la fonction renvoie le message décrypté avec la méthode AES

    Args:
        texteCrypte (_String_): le message à décrypter
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