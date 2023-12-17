from scapy.all import *
import AES as aes

def get_UDP(chemin:str) :
    fichier = rdpcap(chemin)
    lst_udp = []
    for ligne in fichier :
        if "UDP" in ligne :
            lst_udp.append(ligne)
    return lst_udp

def decrypte_UDP(chemin:str) :
    lst_UDP = get_UDP(chemin)
    cle_256 = 0b1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100
    cle_256_bytes = cle_256.to_bytes(32, "big")
    lst_res = []
    for ligne in lst_UDP :
        iv = ligne[Raw].load[:16]
        message_crypte = ligne[Raw].load[16:]
        lst_res.append(aes.decrypt_AES_CBC(message_crypte, cle_256_bytes, iv))
    return lst_res


print(decrypte_UDP("traces/trace_sae.cap"))