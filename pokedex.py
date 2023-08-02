import tkinter as tk 
from tkinter import ttk
from tkinter import *

fenetre = tk.Tk()

# Création du titre de la fenêtre
fenetre.title('POKEDEX')
fenetre.geometry('900x700')
fenetre.resizable(0, 0)

# Création de la fonction de selection
def selection():
    id = listbox.curselection()[0]
    pok_nom.config(text="Nom : " + listPokemons[id].nom)
    pok_type.config(text= "Type : " + listPokemons[id].type)
    pok_taille.config(text= "Taille : " + listPokemons[id].taille)
    pok_poids.config(text= "Poids : " + listPokemons[id].poids)
    pok_talent.config (text= "Talent : " +listPokemons[id].talent)
    pok_faiblesse.config(text= "Faiblesse : " + listPokemons[id].faiblesse)

# if selection == "PIKACHU":
#         pokemon1 = Pokemon("Pikachu", "Electric", "0.4 m", "6 kg", "Statik", "Sol")
#         pokemon1.afficher_informations()
#     elif selection == "BULBIZARRE":
#         pokemon2 = Pokemon("Bulbizarre", "Electrik", "0,7 m", "6,9 kg","Engrais", "Feu, Glace, Vol")
#         pokemon2.afficher_informations()
#     elif selection == "SALAMECHE":
#         pokemon3 = Pokemon("Salameche", "Poison", "0.4 m", "10 kg", "Statik", "Sol")
#         pokemon3.afficher_informations()
#     elif selection == "DRACOLOSSE":
#         pokemon4 = Pokemon("Dracolosse", "Poison", "0.4 m", "10 kg", "Statik", "Sol")
#         pokemon4.afficher_informations()
#     elif selection == "LEVIATOR":
#         pokemon5 = Pokemon("Leviator", "Poison", "0.4 m", "10 kg", "Statik", "Sol")
#         pokemon5.afficher_informations()


# Création de la liste
listbox = tk.Listbox(fenetre)
listbox.pack()
listbox.place(x=700, y=10)
listbox.insert(tk.END, 'PIKACHU')
listbox.insert(tk.END, 'BULBIZARRE')
listbox.insert(tk.END, 'SALAMECHE')
listbox.insert(tk.END, 'DRACOLOSSE')
listbox.insert(tk.END, 'LEVIATOR')

# Créer Boutoun
bouton = tk.Button(fenetre, text="Selection", command=selection)
bouton.place(x=700, y=150)


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
#pokemon1.afficher_informations()
pokemon2= Pokemon("Bulbizarre", "Electrik", "0,7 m", "6,9 kg","Engrais", "Feu, Glace, Vol")
#pokemon2.afficher_informations()
pokemon3= Pokemon("Salamèche", "Feu", "0,6 m", "8,5 kg", "Brasier", "Eau, Sol, Roche")
#pokemon3.afficher_informations()
pokemon4= Pokemon("Dracolosse", "Dragon, Vol", "2,2 m", "210 kg", "Attention", "Glace, Roche, Fée")
#pokemon4.afficher_informations()
pokemon5= Pokemon ("Léviator","Eau, Vol","6,5 m", "235 kg", "Intimidation","Electrik, Roche")
#pokemon5.afficher_informations()

listPokemons = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5]

# # Afficher une image en fonction du choix
# def get_image(choice):
#     if choice == "Pikachu":
#         return pikachu_img
#     elif choice == "Bulbizarre":
#         return bulbasaur_img
#     elif choice == "Salamèche":
#         return charmander_img
#     elif choice == "Dracolosse":
#             return dragonite_img
#     elif choice == "Léviator":
#             return gyarados_img
    
# # Charger les images
# pikachu_img = ImageTk.PhotoImage(Image.open("pikachu.png"))
# bulbasaur_img = ImageTk.PhotoImage(Image.open("bulbasaur.png"))
# charmander_img = ImageTk.PhotoImage(Image.open("charmander.png"))
# dragonite_img = ImageTk.PhotoImage(Image.open("dragonite.png"))
# gyarados_img = ImageTk.PhotoImage(Image.open("gyarados.png"))

# Labels 
pok_nom = tk.Label(fenetre, text="", font=("Arial"))
pok_nom.pack()
#etiquette.place(x=10, y=15)
pok_type= tk.Label(fenetre, text="", font=("Arial"))
pok_type.pack()
pok_taille= tk.Label(fenetre, text="", font=("Arial"))
pok_taille.pack()
pok_poids= tk.Label(fenetre, text="", font=("Arial"))
pok_poids.pack()
pok_talent= tk.Label(fenetre, text="", font=("Arial"))
pok_talent.pack()
pok_faiblesse= tk.Label(fenetre, text="", font=("Arial"))
pok_faiblesse.pack()





# Label pour l'ajout d'un Pokémon
nom= Label(fenetre, text = "Entrez le nom du Pokémon : ")
nom.place(x=50, y=300)
type = Label(fenetre, text = "Entrez le type de Pokémon : ")
type.place(x=50, y=330)
taille = Label(fenetre, text = "Entrez la taille du Pokémon : ")
taille.place(x=50, y=360)
poids = Label(fenetre, text = "Entrez le poids du Pokémon : ")
poids.place(x=50, y=390)
talent = Label(fenetre, text = "Entrez le talent du Pokémon : ")
talent.place(x=50, y=420)
faiblesse = Label(fenetre, text = "Entrez la faiblesse du Pokémon : ")
faiblesse.place(x=50, y=450)

nom_saisie = Entry (fenetre, bd=5, bg='#000', fg='#FFF')
nom_saisie.place(x= 300, y=300)
type_saisie = Entry (fenetre, bd=5, bg='#000', fg='#FFF')
type_saisie.place(x= 300, y=330)
taille_saisie = Entry (fenetre, bd=5, bg='#000', fg='#FFF')
taille_saisie.place(x= 300, y=360)
poids_saisie = Entry (fenetre, bd=5, bg='#000', fg='#FFF')
poids_saisie.place(x= 300, y=390)
talent_saisie = Entry (fenetre, bd=5, bg='#000', fg='#FFF')
talent_saisie.place(x= 300, y=420)
faiblesse_saisie = Entry (fenetre, bd=5, bg='#000', fg='#FFF')
faiblesse_saisie.place(x= 300, y=450)

# Fonction valider le nouveau Pokémon
def valider():
    nom = nom_saisie.get()
    type = type_saisie.get()
    taille = taille_saisie.get()
    poids = poids_saisie.get()
    talent = talent_saisie.get()
    faiblesse = faiblesse_saisie.get()
    listPokemons.append(Pokemon(nom, type, taille, poids,talent, faiblesse))
    listbox.insert(tk.END, nom)

# Bouton valider
bouton = tk.Button(fenetre, text="Valider", command= valider)
bouton.place(x=700, y=300)




fenetre.mainloop() 