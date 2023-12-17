Arthur VILLETTE
Romain MECHAIN

# SAE CRYPTO

## Fichiers à éxecuter :

- Nous avons choisi de faire un résumé des appelles de fonctions prinipales permettant de répondre aux question de développement dans un fichier jupyter notebook nommé SAE_Crypo.ipynb. On y retrouve uniquement les fonctions répondant directement au questions. 

- Pour les questions portant sur les performances de certaines fonctions, il faudra éxecuter le fichier graphe.py, celui-ci propose un menu permettant de choisir quel graphique afficher. 

## Fichiers sources :

- partie1_crypto : Fonctions permettant de decrypter les messages de la première partie
    - import_texte
    - lettre_la_plus_commune
    - get_decalage
    - decrypte_cesar
    - decrypte_message1
    - decrypte_vignère
    - decrypte_message2
    - premiere_occurence_chaque_lettre
    - cree_dico_substitution
    - decrypte_message3
- AES : Fonctions de cryptage et decrypatge AES
    - crypatge_AES
    - decrypt_AES
    - cryptage_AES_CBC
    - decrypt_AES_CBC
- DES : Fonctions fournis pour le cryptage SDES
- image : Fonction de traitement de l'image avec le message caché
    - analyse_image
    - get_message_image
- reseau : Fonctions pour decrypter les messages cachés dans la trame réseau
    - get_UDP
    - decrypte_UDP
- SDES : Fonctions pour les cryptage/decryptage et le cassage SDES
    - double_cryptage_SDES
    - double_decryptage_SDES
    - cryptage_SDES
    - decryptage_SDES
    - cassage_brutal_SDES
    - cassage_astucieux_SDES
- test : Ensemble des tests unitaires