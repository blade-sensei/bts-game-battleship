def grille():
    liste_lettre = ["1","2","3","4","5"]
    liste_nombre = ["1","2","3","4","5"]
    liste_trait = ["_______"] #7 under_scores
    liste_ver = ["|"]
    taille_lettre= len(liste_lettre)
    taille_nombre= len(liste_nombre)
    liste_cordo = []
    ligne_lettre=""
    ligne_trait=""
    ligne_vertical=""
    espace_7="       "
    espace_4="    "
    espace_8="        "

    #On créer et on affiche une ligne de 10 litres de A à J
    for i in range(taille_lettre):
        ligne_lettre=ligne_lettre+liste_lettre[i]+espace_7
    print ("       "+ligne_lettre)
    
    #On Créer et on affiche une ligne horizontal de traits
    for i in range(0,5):
        ligne_trait=ligne_trait+liste_trait[0]+" "
    print(espace_4+ligne_trait)

    #On créer une ligne horizontal de traits verticaux |
    for i in range(0,6):
        ligne_vertical= ligne_vertical+liste_ver[0]+"       " #espaces de 6

    #On affiche 4 lignes
    for i in range(5):
        print("   "+ligne_vertical) #ligne horizontal de traits verticaux
        print(liste_nombre[i]+"  "+ligne_vertical) #au début on affiche un chiffre allant de 1 à 9
        print("   "+ligne_vertical) #Pareil que la 1er ligne
        print(espace_4+ligne_trait) #Ligne de traits horizontaux

    #Affichage de la 10 ligne séparé car il y avait une erreur d'espace
 
        

    


