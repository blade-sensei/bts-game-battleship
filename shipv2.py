import copy, random

def afficher_grille(s,grille):


	joueur = "Ordinateur"
	if s == "u":
		joueur = "Joueur"
	
	print "La grille " + joueur + " : \n"

	#print the horizontal numbers
	print " ",
	for i in range(10):
		print "  " + str(i+1) + "  ",
	print "\n"

	for i in range(10):
	
		#print the vertical line number
		if i != 9: 
			print str(i+1) + "  ",
		else:
			print str(i+1) + " ",

		#print the grille values, and cell dividers
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
		
		#print a horizontal line
		if i != 9:
			print "   ----------------------------------------------------------"
		else: 
			print 

def placer_bateaux_joueur(grille,bateaux):

	for bateau in bateaux.keys():

		#get coordinates from user and vlidate the postion
		valid = False
		while(not valid):

			afficher_grille("u",grille)
			print "Placer le navire : " + bateau
			x,y = saisi_coordonnees()
			positionMod = v_or_h()
			valid = valider(grille,bateaux[bateau],x,y,positionMod)
			if not valid:
				print "Le navire ne peut être placé ici.\n Regardez la grille  et resaisissez les coordonnées."
				raw_input("ENTREE pour continuer")

		#place the bateau
		grille = place_bateau(grille,bateaux[bateau],bateau[0],positionMod,x,y)
		#afficher_grille("u",grille)
		
	raw_input("Placement des bateaux terminé. ENTREE pour continuer")
	return grille


def placer_bateaux_ordi(grille,bateaux):

	for bateau in bateaux.keys():
	
		#genreate random coordinates and vlidate the postion
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

		#place the bateau
		print "L'ordinateur place un : " + bateau
		grille = place_bateau(grille,bateaux[bateau],bateau[0],positionMod,x,y)
	
	return grille


def place_bateau(grille,bateau,lettreBateau,positionMod,x,y):

	#place bateau based on orientation
	if positionMod == "v":
		for i in range(bateau):
			grille[x+i][y] = lettreBateau
	elif positionMod == "h":
		for i in range(bateau):
			grille[x][y+i] = lettreBateau

	return grille
	
def valider(grille,bateau,x,y,positionMod):

	#valider the bateau can be placed at given coordinates
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

	#get bateau orientation from user
	while(True):
		saisi_joueur = raw_input("vertical or horizontal (v,h) ? ")
		if saisi_joueur == "v" or saisi_joueur == "h":
			return saisi_joueur
		else:
			print "Saisi incorrect. Veuillez entrez v ou h"

def saisi_coordonnees():
	
	while (True):
		saisi_joueur = raw_input("Veuillez entrer les coordonnées(ligne,colonne) : ")
		try:
			#see that user entered 2 values seprated by comma
			coor = saisi_joueur.split(",")
			if len(coor) != 2:
				raise Exception("Saisi incorrect, vos coordonnées comportent plus/moins d'élements qu'attendu (l,c).");

			#check that 2 values are integers
			coor[0] = int(coor[0])-1
			coor[1] = int(coor[1])-1

			#check that values of integers are between 1 and 10 for both coordinates
			if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
				raise Exception("Invalid entry. Please use values between 1 to 10 only.")

			#if everything is ok, return coordinates
			return coor
		
		except ValueError:
			print "Invalid entry. Please enter only numeric values for coordinates"
		except Exception as e:
			print e

def jouer_coup(grille,x,y):
	
	#make a move on the grille and return the result, hit, miss or try again for repeat hit
	if grille[x][y] == -1:
		return "dans l'eau"
	elif grille[x][y] == '*' or grille[x][y] == '$':
		return "rejoue"
	else:
		return "touché"

def coup_joueur(grille):
	
	#get coordinates from the user and try to make move
	#if move is a hit, check bateau sunk and win condition
	while(True):
		x,y = saisi_coordonnees()
		res = jouer_coup(grille,x,y)
		if res == "touché":
			print "Hit at " + str(x+1) + "," + str(y+1)
			verif_touch(grille,x,y)
			grille[x][y] = '$'
			if verif_gagner(grille):
				return "WIN"
		elif res == "dans l'eau":
			print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
			grille[x][y] = "*"
		elif res == "rejoue":
			print "Sorry, that coordinate was already hit. Please try again"	

		if res != "rejoue":
			return grille

def coup_ordi(grille):
	
	#generate user coordinates from the user and try to make move
	#if move is a hit, check bateau sunk and win condition
	while(True):
		x = random.randint(1,10)-1
		y = random.randint(1,10)-1
		res = jouer_coup(grille,x,y)
		if res == "touché":
			print "Hit at " + str(x+1) + "," + str(y+1)
			verif_touch(grille,x,y)
			grille[x][y] = '$'
			if verif_gagner(grille):
				return "WIN"
		elif res == "dans l'eau":
			print "Sorry, " + str(x+1) + "," + str(y+1) + " is a miss."
			grille[x][y] = "*"

		if res != "rejoue":
			
			return grille
	
def verif_touch(grille,x,y):

	#figure out what bateau was hit
	if grille[x][y] == "A":
		bateau = "Aircraft Carrier"
	elif grille[x][y] == "B":
		bateau = "Battlebateau"
	elif grille[x][y] == "S":
		bateau = "Submarine" 
	elif grille[x][y] == "D":
		bateau = "Destroyer"
	elif grille[x][y] == "P": 
		bateau = "Patrol Boat"
	
	#mark cell as hit and check if sunk
	grille[-1][bateau] -= 1
	if grille[-1][bateau] == 0:
		print bateau + " Sunk"
		

def verif_gagner(grille):
	
	#simple for loop to check all cells in 2d grille
	#if any cell contains a char that is not a hit or a miss return false
	for i in range(10):
		for j in range(10):
			if grille[i][j] != -1 and grille[i][j] != '*' and grille[i][j] != '$':
				return False
	return True

def main():

	#types of bateaux
	bateaux = {"Aircraft Carrier":5,
		     "Battlebateau":4,
 		     "Submarine":3,
		     "Destroyer":3,
		     "Patrol Boat":2}

	#setup blank 10x10 grille
	grille = []
	for i in range(10):
		grille_row = []
		for j in range(10):
			grille_row.append(-1)
		grille.append(grille_row)

	#setup user and computer grilles
	grille_joueur = copy.deepcopy(grille)
	grille_ordi = copy.deepcopy(grille)

	#add bateaux as last element in the array
	grille_joueur.append(copy.deepcopy(bateaux))
	grille_ordi.append(copy.deepcopy(bateaux))

	#bateau placement
	grille_joueur = placer_bateaux_joueur(grille_joueur,bateaux)
	grille_ordi = placer_bateaux_ordi(grille_ordi,bateaux)

	#game main loop
	while(1):

		#user move
		afficher_grille("c",grille_ordi)
		grille_ordi = coup_joueur(grille_ordi)

		#check if user won
		if grille_ordi == "WIN":
			print "User WON! :)"
			quit()
			
		#display current computer grille
		afficher_grille("c",grille_ordi)
		raw_input("To end user turn hit ENTER")

		#computer move
		grille_joueur = coup_ordi(grille_joueur)
		
		#check if computer move
		if grille_joueur == "WIN":
			print "Computer WON! :("
			quit()
			
		#display user grille
		afficher_grille("u",grille_joueur)
		raw_input("To end computer turn hit ENTER")
	
if __name__=="__main__":
	main()
