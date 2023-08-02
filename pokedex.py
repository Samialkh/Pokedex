import tkinter as tk
from tkinter import ttk
from tkinter import *

fenetre = tk.Tk()

# Création du titre de la fenêtre
fenetre.title('POKEDEX')
fenetre.geometry('900x700')
fenetre.resizable(0, 0)

# Création de la liste
listbox = tk.Listbox(fenetre)
listbox.pack()
listbox.place(x=700, y=10)
listbox.insert(tk.END, 'Pokémon 1')
listbox.insert(tk.END, 'Pokémon 2')
listbox.insert(tk.END, 'Pokémon 3')
listbox.insert(tk.END, 'Pokémon 4')
listbox.insert(tk.END, 'Pokémon 5')

# Création de la classe pour les informations

class Pokemon :
    def __init__(self, nom, type, taille, poids,talent, faiblesse):
        self.nom = nom
        self.type = type
        self.taille = taille
        self.poids = poids
        self.talent = talent
        self.faiblesse = faiblesse

    def afficher_informations(self):
        print("Informations du Pokemon : ")
        print("Nom: ", self.nom)
        print("Type: ", self.type)
        print("Taille: ", self.taille)
        print("Poids: ", self.poids)
        print("Talent: ", self.talent)
        print("Faiblesse: ", self.faiblesse)

pokemon1= Pokemon("Pikachu", "Electric", "0.4 m", "6 kg", "Statik", "Sol")
pokemon1.afficher_informations()
pokemon2= Pokemon("Bulbizarre", "Electrik", "0,7 m", "6,9 kg","Engrais", "Feu, Glace, Vol")
pokemon2.afficher_informations()
pokemon3= Pokemon("Salamèche", "Feu", "0,6 m", "8,5 kg", "Brasier", "Eau, Sol, Roche")
pokemon3.afficher_informations()
pokemon4= Pokemon("Dracolosse", "Dragon, Vol", "2,2 m", "210 kg", "Attention", "Glace, Roche, Fée")
pokemon4.afficher_informations()
pokemon5= Pokemon ("Léviator","Eau, Vol","6,5 m", "235 kg", "Intimidation","Electrik, Roche" )
pokemon5.afficher_informations()




fenetre.mainloop() 