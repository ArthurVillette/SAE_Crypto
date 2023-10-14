import unittest


import decryptage as dec
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
        self.assertEqual(dec.import_texte("indice1_chiffre.txt"),"BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD\nMOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD\nZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG\nSDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ\nDAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ\nMZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE.\nYMUE MFFQZFUAZ M ZQ BME XQE ODACGQD,\nYQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE,\nQZ MGOGZ OME FG ZQ PAUE EGOOAYNQD")
        self.assertEqual(dec.import_texte("motCrypteTest.txt"),"Lfuzfco'sftd olyd wl uzt\nClatop wpd tydelye alddp\nEctdep wl qtylwtep\nSlmtwp pde opdety\nFetwp pde wl apydpc\nClatop pde wp epxad")
        
    def test_decrypte_cesar(self) :
        self.assertEqual(dec.decrypte_cesar(mot_cripté,12),"PRES DU CHEMIN SE CACHE UN TRESOR ACCROCHE A UN ARBRE TOUT RECOUVERT D'OR NE NEGLIGE PAS LA JEUNE POUCE FEUILLU GRAND EST SON SECRET MALGRE SA TAILLE MENUE RONDES ET COLOREES SONT LES BAIES QU'IL PORTE ANISEES ET SUCREES, LEURS SAVEURS SONT FORTES. MAIS ATTENTION A NE PAS LES CROQUER, MEME SI LA FAIM TIRAILLE TES ENTRAILLES, EN AUCUN CAS TU NE DOIS SUCCOMBER")
        self.assertEqual(dec.decrypte_cesar("B",1),"A")
        self.assertEqual(dec.decrypte_cesar("A",1),"Z")
        
    def test_decrypte_message1(self):
        self.assertEqual(dec.decrypte_message1("indice1_chiffre.txt"),"PANGRAMME")
        self.assertEqual(dec.decrypte_message1("motCrypteTest.txt"),"ARTHUR")



if __name__ == '__main__':
    unittest.main()