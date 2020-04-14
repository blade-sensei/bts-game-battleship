# COYLA ET BANNU
##### A EXECUTER SUR PYTHON 2.7 CODAGE - UTF 8 SUR MAC #####

import copy, random

def afficher_grille(s,grille):



	#on recupére quel grille faut afficher (ordi ou joueur)
	joueur = "Ordinateur"
	if s == "u":
		joueur = "Joueur"
	
	print "La grille " + joueur + " : \n"

	#affiche la ligne de nombre horizontale
	print " ",
	for i in range(10):
		print "  " + str(i+1) + "  ",
	print "\n"

	for i in range(10):
	
		#affiche la ligne de nombre  verticale
		if i != 9: 
			print str(i+1) + "  ",
		else:
			print str(i+1) + " ",

		#on créer les cellules de la grille ainsi que la valeurs par defaut qu'elles contiennent
		for j in range(10):
			if grille[i][j] == -1:
				print ' ',	
			elif s == "u":
				print grille[i][j],
			elif s == "c":
				if grille[i][j] == "*" or grille[i][j] == "$":
					print grille[i][j],
				else:
					print " ",
			
			if j != 9:
				print " | ",
		print
		
		#affiche une ligne pour séparé les cellule de la grille
		if i != 9:
			print "   ----------------------------------------------------------"
		else: 
			print 

def placer_bateaux_joueur(grille,bateaux):

	for bateau in bateaux.keys():

		#On verifie si un navire peut etre placé sur le coordonnées donné par le joueur
		valid = False
		while(not valid):

			afficher_grille("u",grille)
			print "Placer le navire : " + bateau
			x,y = saisi_coordonnees()
			positionMod = v_or_h() #on récuprer le poistionnement dans cette varaible
			valid = valider(grille,bateaux[bateau],x,y,positionMod)
			if not valid:
				print "Le navire ne peut être placé ici.\n Regardez la grille  et resaisissez les coordonnées."
				raw_input("ENTREE pour continuer")

		#place un bateau
		grille = place_bateau(grille,bateaux[bateau],bateau[0],positionMod,x,y)
		#afficher_grille("u",grille)
		
	raw_input("Placement des bateaux terminé. ENTREE pour continuer")
	return grille


def placer_bateaux_ordi(grille,bateaux):

	for bateau in bateaux.keys():
	
		#genere aleatoirement des coordonnées et verifie la conformité de celles ci
		valid = False
		while(not valid):

			x = random.randint(1,10)-1
			y = random.randint(1,10)-1
			pos = random.randint(0,1)
			if pos == 0: 
				positionMod = "v"
			else:
				positionMod = "h"
			valid = valider(grille,bateaux[bateau],x,y,positionMod)

		#place un bateau
		print "L'ordinateur place un : " + bateau
		grille = place_bateau(grille,bateaux[bateau],bateau[0],positionMod,x,y)
	
	return grille


def place_bateau(grille,bateau,lettreBateau,positionMod,x,y):

	#place le bateau selon le mode de positionnement h ou v
	if positionMod == "v":
		for i in range(bateau):
			grille[x+i][y] = lettreBateau
	elif positionMod == "h":
		for i in range(bateau):
			grille[x][y+i] = lettreBateau

	return grille
	
def valider(grille,bateau,x,y,positionMod):

	#Fonction qui va verifier si le bateau peut etre placé a l'endroit demandé en prenant en compte la position vertial/horizontale
	if positionMod == "v" and x+bateau > 10:
		return False
	elif positionMod == "h" and y+bateau > 10:
		return False
	else:
		if positionMod == "v":
			for i in range(bateau):
				if grille[x+i][y] != -1:
					return False
		elif positionMod == "h":
			for i in range(bateau):
				if grille[x][y+i] != -1:
					return False
		
	return True

def v_or_h():

	#on recupere la postion du bateau (verticale ou horizontale)
	while(True):
		saisi_joueur = raw_input("verticale ou horizontale (v,h) ? ")
		if saisi_joueur == "v" or saisi_joueur == "h":
			return saisi_joueur
		else:
			print "Saisi incorrect. Veuillez entrez v ou h"

def saisi_coordonnees():
	
	while (True):
		saisi_joueur = raw_input("Veuillez entrer les coordonnées(ligne,colonne) : ")
		try:
			#verifie la saisi est du format (a,b)
			coor = saisi_joueur.split(",")
			if len(coor) != 2:
				raise Exception("Saisi incorrect, vos coordonnées comportent plus/moins d'élements qu'attendu (l,c).");

			#verifie que les saisi sont des entiers
			coor[0] = int(coor[0])-1
			coor[1] = int(coor[1])-1

			#Vérifie qu'ils sont compris entre 1 et 10
			if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
				raise Exception("Saisi incorect. Entrez des valeurs entre 1 et 10 .")

			#si tous les test sont bon on retourne les coordonnées
			return coor
		
		except ValueError:
			print "Saisi incorrect. Veuillez entrer des valeur numérique seulement"
		except Exception as e:
			print e

def jouer_coup(grille,x,y):
	
	#Vérifie le contenu de la cellule joué et renvoi si touché/dans l'eau ou renvoi rejoue si la case a déjà été joué
	if grille[x][y] == -1:
		return "dans l'eau"
	elif grille[x][y] == '*' or grille[x][y] == '$':
		return "rejoue"
	else:
		return "touché"

def coup_joueur(grille):
	
	#on procede coup du joueur après verif
	#et on met a jour la grille selon touche/dans l'eau, et on verifie si les conditions pour gagner sont reuni.
	while(True):
		x,y = saisi_coordonnees()
		res = jouer_coup(grille,x,y)
		if res == "touché":
			print "touché en : " + str(x+1) + "," + str(y+1)
			verif_touch(grille,x,y)
			grille[x][y] = '$'
			if verif_gagner(grille):
				return "WIN"
		elif res == "dans l'eau":
			print "Désolé, " + str(x+1) + "," + str(y+1) + " c'est dans l'eau."
			grille[x][y] = "*"
		elif res == "rejoue":
			print "Rejouez, ces coordonnées ont déjà été joué."	

		if res != "rejoue":
			return grille

def coup_ordi(grille):
	
	#on procede coup de l'ordinateur après verif
	#et on met a jour la grille selon touche/dans l'eau, et on verifie si les conditions pour gagner sont reuni.
	while(True):
		x = random.randint(1,10)-1
		y = random.randint(1,10)-1
		res = jouer_coup(grille,x,y)
		if res == "touché":
			print "touché en " + str(x+1) + "," + str(y+1)
			verif_touch(grille,x,y)
			grille[x][y] = '$'
			if verif_gagner(grille):
				return "WIN"
		elif res == "dans l'eau":
			print "Désolé, " + str(x+1) + "," + str(y+1) + " c'est dans l'eau."
			grille[x][y] = "*"

		if res != "rejoue":
			
			return grille
	
def verif_touch(grille,x,y):

	#Affiche quel bateau a été touché
	if grille[x][y] == "P":
		bateau = "Porte-avions"
	elif grille[x][y] == "C":
		bateau = "Croiseur"
	elif grille[x][y] == "S":
		bateau = "Sous-Marin" 
	elif grille[x][y] == "D":
		bateau = "Destructeur"
	elif grille[x][y] == "T": 
		bateau = "Torpilleur"
	
	#marque la cellule comme touché et on verifié si le bateau à coulé
	grille[-1][bateau] -= 1
	if grille[-1][bateau] == 0:
		print bateau + " Coulé"
		

def verif_gagner(grille):
	
	#on check toutes les cellules
	#si toutes les cellules contiennent un caractère qui n'est pas un $(touché) ou un *(dans l'eau) ->retourner faux
	for i in range(10):
		for j in range(10):
			if grille[i][j] != -1 and grille[i][j] != '*' and grille[i][j] != '$':
				return False
	return True

def main():

	#Nom et type de bateau
	bateaux = {"Porte-avions":5,
		     "Croiseur":4,
 		     "Sous-Marin":3,
		     "Destructeur":3,
		     "Torpilleur":2}

	#on fait la grille vide 10*10
	
	grille = []
	for i in range(10):
		grille_row = []
		for j in range(10):
			grille_row.append(-1)
		grille.append(grille_row)

	#on fait la grille de l'ordi et du joueur
	
	grille_joueur = copy.deepcopy(grille)
	grille_ordi = copy.deepcopy(grille)

	#on ajoute "bateaux" comme dernier élément du tableau.
	grille_joueur.append(copy.deepcopy(bateaux))
	grille_ordi.append(copy.deepcopy(bateaux))

	#placement des bateaux
	grille_joueur = placer_bateaux_joueur(grille_joueur,bateaux)
	grille_ordi = placer_bateaux_ordi(grille_ordi,bateaux)

	#Main() boucle principale du jeu
	while(1):

		#coup joueur
		afficher_grille("c",grille_ordi)
		grille_ordi = coup_joueur(grille_ordi)

		#verification si le joueur a gagné
		if grille_ordi == "WIN":
			print "Le joueur Gagne! :)"
			quit()
			
		#affichage de la grille courante de l'ordinateur
		afficher_grille("c",grille_ordi)
		raw_input("Entrer, pour terminer le tour joueur")

		#coup de l'ordi
		grille_joueur = coup_ordi(grille_joueur)
		
		#verification si l'ordi a gagné
		if grille_joueur == "WIN":
			print "L'ordinateur Gagne!! "
			quit()
			
		#affichage grille joueur
		afficher_grille("u",grille_joueur)
		raw_input("Entrer, pour terminer le tour de l'ordinateur")
	
if __name__=="__main__":
	main()
