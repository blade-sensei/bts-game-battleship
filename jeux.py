from tkinter import *

TAILLE_CASE=64
GRILLE_H=512+TAILLE_CASE
GRILLE_W=512+TAILLE_CASE

WIN_H=800
WIN_W=800

#trace une grille en prenant en parametre un canevas c(zone_dessin)
def grille(c):
    i=0
    while i<GRILLE_W:
        c.create_line(0,i,GRILLE_W,i)
        c.create_line(i,0,i,GRILLE_H)
        i=i+TAILLE_CASE


# Création de la fenêtre principale (main window)
window = Tk()
window.title('BattleShip')





# Dans Fenetre nous allons créer un objet type Canvas qui se nomme zone_dessin
# Nous donnons des valeurs aux propriétés "width", "height", "bg", "bd", "relief"

zone_dessin = Canvas(window,width=GRILLE_W,height=GRILLE_H,bg='red',bd=2,relief="ridge")
#Affiche le Canvas
zone_dessin.grid(row=2)
#dessin grille
grille(zone_dessin)
#texte
text = Label(window, text="A" color="green")
text.grid(row=0,sticky=E)
window.mainloop()

