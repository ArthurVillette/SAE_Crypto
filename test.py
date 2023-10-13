import unittest


import decryptage as dec

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
        
mot_cripté = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE. YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD"

if __name__ == '__main__':
    unittest.main()