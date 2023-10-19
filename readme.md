Arthur VILLETTE
Romain MECHAIN

# SAECRYPTO

## Indice 1:

Pour déchiffrer l'indice 1 nous avons regarder le message crypte et nous avons vue qu'une lettre apparaissaient plus souvent que les autres, la lettre 'q', donc on fais un fonction pour s'en assurer. Ensuite on sait que la lettre la plus courante est 'e', donc on a fais une fonction de décalage entre 'q' et 'e' pour savoir de combien on va décaler les autres lettres selon la méthode de césar, car on pence que le message a étét chiffrer avec le chiffrement de césar. En utilisant notre fonction on trouve un message claire. 

Le message trouvé est donc : `PRES DU CHEMIN SE CACHE UN TRESOR ACCROCHE A UN ARBRE TOUT RECOUVERT D'OR NE NEGLIGE PAS LA JEUNE POUCE FEUILLU GRAND EST SON SECRET MALGRE SA TAILLE MENUE RONDES ET COLOREES SONT LES BAIES QU'IL PORTE ANISEES ET SUCREES, LEURS SAVEURS SONT FORTES. MAIS ATTENTION A NE PAS LES CROQUER, MEME SI LA FAIM TIRAILLE TES ENTRAILLES, EN AUCUN CAS TU NE DOIS SUCCOMBER`

## clée 1:

Cependant, la clé ne pouvait pas être tout le message, nous avons donc pensé qu'un autre message était caché dans celui-ci. Nous avons, avons donc essayer de prendre la première lettre de chaque ligne, et en effet, c'etait ce qu'il fallait faire. 

Le message était donc : `PANGRAMME`

## Indice 2:

Au vue du message numéro 2, et de la réponse du prècedent, nous avons pensé que la clé devait être le message caché dans le message 1. Et grâce à cela nous avons detérminé qu'il s'agissait d'un cryptage de vigenère. 

En decryptant le message 2 nous avons obtenue : ̀`LE VYF ZEPHIR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX\nIL CACHE DANS LA REPETITION LE SECRET DE CES MURMURES MALHEUREUX\nNE GARDEZ DU PREMIER SOUFFLE QUE LES PREMIERES APPARITIONS\nET AINSI DEVOILEZ LE MESSAGE CACHE DERRIERE LA SUBSTITUTION`

## Clé 2:

Ici, la clé était caché par une enigme, le premier soufle correspond à la première ligne du message, et on indique de garder uniquement la première apparition de chaque lettre. Comme on nous parle de substitution, il suffisait de créer une clé de substitution, avec les premières occurances. 

On obtient : `ABCDEFGHIJKLMNOPQRSTUVWXYZ --> LEVIFZPHYRJUBSKMQATDCOWNGX`

## réponce: 

Enfin, il ne reste plus qu'a appliquer la substitution.

On obtient : `BRAVO, VOUS AVEZ GAGNEZ! LE CODE A FOURNIR EST: ELIZEBETH`