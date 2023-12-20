import unittest
import partie1_crypto as dec
import SDES as sdes
import AES as aes
import image as img
import reseau as res
mot_cripté = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE. YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD"

class Testing(unittest.TestCase):
    def test_lettre_la_plus_commune(self):
        self.assertEqual(dec.lettre_la_plus_commune(mot_cripté), "Q")
        self.assertEqual(dec.lettre_la_plus_commune("Le principe de l'évolution est beaucoup plus rapide en informatique que chez le bipède."), "E")
        self.assertEqual(dec.lettre_la_plus_commune("L'informatique n'est qu'un outil, comme un pinceau ou un crayon."), "U")
        
    def test_get_decalage(self):
        self.assertEqual(dec.get_decalage("Q"), 12)
        self.assertEqual(dec.get_decalage("E"), 0)
        self.assertEqual(dec.get_decalage("U"), 16)

    def test_import_texte_indice1(self):
        self.assertEqual(dec.import_texte("./txt/indice1_chiffre.txt"),"BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD\nMOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD\nZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG\nSDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ\nDAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ\nMZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE.\nYMUE MFFQZFUAZ M ZQ BME XQE ODACGQD,\nYQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE,\nQZ MGOGZ OME FG ZQ PAUE EGOOAYNQD")
        self.assertEqual(dec.import_texte("./txt/motCrypteTest.txt"),"Lfuzfco'sftd olyd wl uzt\nClatop wpd tydelye alddp\nEctdep wl qtylwtep\nSlmtwp pde opdety\nFetwp pde wl apydpc\nClatop pde wp epxad")
        
    def test_decrypte_cesar(self) :
        self.assertEqual(dec.decrypte_cesar(mot_cripté,12),"PRES DU CHEMIN SE CACHE UN TRESOR ACCROCHE A UN ARBRE TOUT RECOUVERT D'OR NE NEGLIGE PAS LA JEUNE POUCE FEUILLU GRAND EST SON SECRET MALGRE SA TAILLE MENUE RONDES ET COLOREES SONT LES BAIES QU'IL PORTE ANISEES ET SUCREES, LEURS SAVEURS SONT FORTES. MAIS ATTENTION A NE PAS LES CROQUER, MEME SI LA FAIM TIRAILLE TES ENTRAILLES, EN AUCUN CAS TU NE DOIS SUCCOMBER")
        self.assertEqual(dec.decrypte_cesar("B",1),"A")
        self.assertEqual(dec.decrypte_cesar("A",1),"Z")
        
    def test_decrypte_message1(self):
        self.assertEqual(dec.decrypte_message1("./txt/indice1_chiffre.txt"),"PANGRAMME")
        self.assertEqual(dec.decrypte_message1("./txt/motCrypteTest.txt"),"ARTHUR")
    
    def test_decrypte_vignère(self):
        self.assertEqual(dec.decrypte_vignère(dec.import_texte("./txt/indice2_chiffre.txt"),"PANGRAMME"),"LE VIF ZEPHYR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX\nIL CACHE DANS LA REPETITION LE SECRET DE CES MURMURES MALHEUREUX\nNE GARDEZ DU PREMIER SOUFFLE QUE LES PREMIERES APPARITIONS\nET AINSI DEVOILEZ LE MESSAGE CACHE DERRIERE LA SUBSTITUTION")

    def test_premiere_occurence_chaque_lettre(self) :
        self.assertEqual(dec.premiere_occurence_chaque_lettre("ARTHUR"),"ARTHU")
        self.assertEqual(dec.premiere_occurence_chaque_lettre("PANGRAMME"),"PANGRME")
        self.assertEqual(dec.premiere_occurence_chaque_lettre("LE VIF ZEPHYR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX"),"LEVIFZPHYRJUBSKMQATDCOWNGX")

    def test_cree_dico_substitution(self) :
        self.assertEqual(dec.cree_dico_substitution("QSD"),{"Q":"A","S":"B","D":"C"})
        self.assertEqual(dec.cree_dico_substitution("RTYUZ"),{"R":"A","T":"B","Y":"C","U":"D","Z":"E"})
        self.assertEqual(dec.cree_dico_substitution("ETLWKOPDF"),{"E":"A","T":"B","L":"C","W":"D","K":"E","O":"F","P":"G","D":"H","F":"I"})
        
    def test_decrypte_message2(self) :
        self.assertEqual(dec.decrypte_message2("./txt/indice2_chiffre.txt"),"LE VIF ZEPHYR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX\nIL CACHE DANS LA REPETITION LE SECRET DE CES MURMURES MALHEUREUX\nNE GARDEZ DU PREMIER SOUFFLE QUE LES PREMIERES APPARITIONS\nET AINSI DEVOILEZ LE MESSAGE CACHE DERRIERE LA SUBSTITUTION")
        
    def test_decrypte_message3(self) :
        self.assertEqual(dec.decrypte_message3("./txt/indice3_chiffre_correct.txt"),"BRAVO, VOUS AVEZ GAGNE! LE CODE A FOURNIR EST: ELIZEBETH")
        
    def test_double_cryptage_SDES(self) :
        self.assertEqual(sdes.double_cryptage_SDES("test",2,5),[180, 36, 90, 180])
        self.assertEqual(sdes.double_cryptage_SDES("t",2,2),[95])
        self.assertEqual(sdes.double_cryptage_SDES("ceci est un test",2,5),[103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180])
        
    def test_double_decryptage_SDES(self) :
        self.assertEqual(sdes.double_decryptage_SDES([180, 36, 90, 180],2,5),"test")
        self.assertEqual(sdes.double_decryptage_SDES([95],2,2),"t")
        self.assertEqual(sdes.double_decryptage_SDES([103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180],2,5),"ceci est un test")
        
    def test_cassage_brutal_SDES(self) :
        self.assertEqual(sdes.cassage_brutal_SDES("test",[180, 36, 90, 180]),(2,5))
        self.assertEqual(sdes.cassage_brutal_SDES("ceci est un test",[103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180]),(2,5))
    
    def test_cryptage_SDES(self) :
        self.assertEqual(sdes.cryptage_SDES("test",2),[179, 64, 77, 179])
        self.assertEqual(sdes.cryptage_SDES("t",5),[138])
        self.assertEqual(sdes.cryptage_SDES("ceci est un test",10),[104, 6, 104, 173, 234, 6, 249, 213, 234, 69, 210, 234, 213, 6, 249, 213])
        
    def test_cassage_Astucieux_SDES(self):
        self.assertEqual(sdes.cassage_Astucieux_SDES("test",[180, 36, 90, 180]),(2,5))
        self.assertEqual(sdes.cassage_Astucieux_SDES("ceci est un test",[103, 36, 103, 128, 73, 36, 90, 180, 73, 92, 175, 73, 180, 36, 90, 180]),(2,5))
    
    def test_decryptage_AES(self) :
        self.assertEqual(aes.decrypt_AES(b'\x85\x03DK\x07\xe3Gw\x9e\x9c\x7f\x98\xfa\x08\xa4\xdd^\xa0L\xf1>\xf6\n\x92\xd8]\xd5f\x8dg\xa5a',"SUPER CLE"),"AES")
        self.assertEqual(aes.decrypt_AES(b"(\x973\xd5/'\x94\xd79?\xed\xc5\xc9/\xef\xe5fH\xa3\x00\xaa\x82\x86\xd4~\xb7\xda\x87\xc6p\xda\xf1","Arthur"),"Bourrito")
        self.assertEqual(aes.decrypt_AES(b'\xc1\x867Y\x08\xd8\xc8\xc7C\x06\t\xf2\xc9\xe5\xd4/b\xd0,\xe8\xa9\xded\xfe\xbf\x8c*<,\xf3\xd1P',"Romain"),"SAE")
        
    def test_get_message_image(self) :
        self.assertEqual(img.get_message_image("images/rossignol2.bmp"),"1110011101101101001100010011111110010010101110011001000001001100")

    def test_decryptage_AES_CBC(self) :
        cle_256 = 0b1110011101101101001100010011111110010010101110011001000001001100111001110110110100110001001111111001001010111001100100000100110011100111011011010011000100111111100100101011100110010000010011001110011101101101001100010011111110010010101110011001000001001100
        cle_256_bytes = cle_256.to_bytes(32, "big")
        self.assertEqual(aes.decrypt_AES_CBC(b'k\xeb\xc3\xf17\xc5R|u\x92\xfa\xcbl\xb1\xcf\x17', cle_256_bytes, b'$\x91k\x10\xa3\x8b2\x9d\xb4\xc8\x93\xd1I\x02i\x89'), "le message")
        self.assertEqual(aes.decrypt_AES_CBC(b'#\xd4\x1e\xb0\xcf%\xe1=W\xf7\xf5b\xb3\x962/NzO\xe0?\xeb\x1d\x94\xe5\xa9\x14l\xac\x0c\xf4\xd7', cle_256_bytes, b'\x9dG\x00\x13\x0fB\xe7+\x90V\x9d\xfeQ\xdb\x159'), "un autre message")
        self.assertEqual(aes.decrypt_AES_CBC(b'\x08H\xe8\x8e\x81\x14\xa5e\x02\x1b\xac\xd3\x00\xe2@i0\xd1<JocX\xaeZ\x94\x89\x0f|\xce\xd6\xe7', cle_256_bytes, b'DV\x7f\xa7\x94\xf2J\x84\xcb\xe6\xf5\xd2P\xf2\x9el'), "un dernier message")

    def test_decrypte_UDP(self) :
        self.assertEqual(res.decrypte_UDP("traces/trace_sae.cap"), ["La crypto c'est trop bien!", "Je suis complètement d'accord!"])



if __name__ == '__main__':
    unittest.main()