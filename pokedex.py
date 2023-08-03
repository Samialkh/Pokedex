import tkinter as tk 
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk


fenetre = tk.Tk()

# Création du titre de la fenêtre
fenetre.title('POKEDEX')
fenetre.geometry('900x700')
fenetre.resizable(0, 0)

# Essai frame
frame1 = Frame(fenetre, bg="white") 
frame1.place(x=0, y=0, width=900, height=400) 

frame2 = Frame(fenetre, bg="grey") 
frame2.place(x=0, y=400, width=900, height=300)

# Création de la fonction de selection
def selection():
    id = listbox.curselection()[0]
    pok_nom.config(text="Nom : " + listPokemons[id].nom)
    pok_type.config(text= "Type : " + listPokemons[id].type)
    pok_taille.config(text= "Taille : " + listPokemons[id].taille)
    pok_poids.config(text= "Poids : " + listPokemons[id].poids)
    pok_talent.config (text= "Talent : " +listPokemons[id].talent)
    pok_faiblesse.config(text= "Faiblesse : " + listPokemons[id].faiblesse)
    img = Image.open(listPokemons[id].img)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)
    default_label.config(image=photo)
    default_label.image = photo
    

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
listbox = tk.Listbox(fenetre, font="Verdana 10 bold", height=7, width=15, bg="black", fg="white")
listbox.place(x=700, y=10)
listbox.insert(tk.END, 'PIKACHU')
listbox.insert(tk.END, 'BULBIZARRE')
listbox.insert(tk.END, 'SALAMECHE')
listbox.insert(tk.END, 'DRACOLOSSE')
listbox.insert(tk.END, 'LEVIATOR')

# Créer Boutoun selectionner
bouton = tk.Button(fenetre, text="Selectionner", command=selection, font="Verdana 10 bold", bg="white")
bouton.place(x=700, y=150)


# Afficher les informations

class Pokemon :
    def __init__(self, nom, type, taille, poids,talent, faiblesse, image):
        self.nom = nom
        self.type = type
        self.taille = taille
        self.poids = poids
        self.talent = talent
        self.faiblesse = faiblesse
        self.img = image 
        

    def afficher_informations(self):
        print("Informations du Pokemon : ")
        print("Nom: ", self.nom)
        print("Type: ", self.type)
        print("Taille: ", self.taille)
        print("Poids: ", self.poids)
        print("Talent: ", self.talent)
        print("Faiblesse: ", self.faiblesse)
        print("", self.img)
        

pokemon1= Pokemon("Pikachu", "Electric", "0.4 m", "6 kg", "Statik", "Sol", "img/pikachu.png")
#pokemon1.afficher_informations()
pokemon2= Pokemon("Bulbizarre", "Electrik", "0,7 m", "6,9 kg","Engrais", "Feu, Glace, Vol", "img/bulbasaur.png")
#pokemon2.afficher_informations()
pokemon3= Pokemon("Salamèche", "Feu", "0,6 m", "8,5 kg", "Brasier", "Eau, Sol, Roche", "img/charmander.png")
#pokemon3.afficher_informations()
pokemon4= Pokemon("Dracolosse", "Dragon, Vol", "2,2 m", "210 kg", "Attention", "Glace, Roche, Fée", "img/dragonite.png")
#pokemon4.afficher_informations()
pokemon5= Pokemon ("Léviator","Eau, Vol","6,5 m", "235 kg", "Intimidation","Electrik, Roche", "img/gyarados.png")
#pokemon5.afficher_informations()

listPokemons = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5]


# Labels 
pok_nom = tk.Label(fenetre, text="", font=("Verdana 15 bold"), bg="white", fg= "red")
pok_nom.place(x=30, y=10)
pok_type= tk.Label(fenetre, text="", font=("Verdana 15 bold"), bg="white", fg= "red")
pok_type.place(x=30, y=60)
pok_taille= tk.Label(fenetre, text="", font=("Verdana 15 bold"), bg="white", fg= "red")
pok_taille.place(x=30, y=110)
pok_poids= tk.Label(fenetre, text="", font=("Verdana 15 bold"), bg="white", fg= "red")
pok_poids.place(x=30, y=160)
pok_talent= tk.Label(fenetre, text="", font=("Verdana 15 bold"), bg="white", fg= "red")
pok_talent.place(x=30, y=210)
pok_faiblesse= tk.Label(fenetre, text="", font=("Verdana 15 bold"), bg="white", fg= "red")
pok_faiblesse.place(x=30, y=260)

default_img = Image.open("img/Pokemon_logo.png")
default_img = default_img.resize((200, 200))
default_photo = ImageTk.PhotoImage(default_img)
default_label = Label(fenetre, image=default_photo, bg="white")
default_label.place(x=300, y=50)

pikachu_img = ImageTk.PhotoImage(Image.open('img/pikachu.png'))
bulbasaur_img = ImageTk.PhotoImage(Image.open('img/bulbasaur.png'))
charmander_img = ImageTk.PhotoImage(Image.open("img/charmander.png"))
dragonite_img = ImageTk.PhotoImage(Image.open("img/dragonite.png"))
gyarados_img = ImageTk.PhotoImage(Image.open("img/gyarados.png"))


# Label pour l'ajout d'un Pokémon
nom= Label(fenetre, text = "Entrez le nom du Pokémon : ", bg="grey", fg="black", font="Verdana 12 bold")
nom.place(x=50, y=500)
type = Label(fenetre, text = "Entrez le type de Pokémon : ",bg="grey", fg="black", font="Verdana 12 bold")
type.place(x=50, y=530)
taille = Label(fenetre, text = "Entrez la taille du Pokémon : ", bg="grey", fg="black", font="Verdana 12 bold")
taille.place(x=50, y=560)
poids = Label(fenetre, text = "Entrez le poids du Pokémon : ", bg="grey", fg="black", font="Verdana 12 bold")
poids.place(x=50, y=590)
talent = Label(fenetre, text = "Entrez le talent du Pokémon : ", bg="grey", fg="black", font="Verdana 12 bold")
talent.place(x=50, y=620)
faiblesse = Label(fenetre, text = "Entrez la faiblesse du Pokémon : ",bg="grey", fg="black", font="Verdana 12 bold")
faiblesse.place(x=50, y=650)

nom_saisie = Entry (fenetre, bd=2, bg="white", fg="black")
nom_saisie.place(x= 300, y=500)
type_saisie = Entry (fenetre, bd=2, bg="white", fg="black")
type_saisie.place(x= 300, y=530)
taille_saisie = Entry (fenetre, bd=2, bg="white", fg="black")
taille_saisie.place(x= 300, y=560)
poids_saisie = Entry (fenetre, bd=2, bg="white", fg="black")
poids_saisie.place(x= 300, y=590)
talent_saisie = Entry (fenetre, bd=2, bg="white", fg="black")
talent_saisie.place(x= 300, y=620)
faiblesse_saisie = Entry (fenetre, bd=2, bg="white", fg="black")
faiblesse_saisie.place(x= 300, y=650)

# Label Ajouter nouveau Pokémon
pok_nouveau = tk.Label(fenetre, text= "Ajouter un nouveau Pokémon", font=("Verdana 20 bold"), fg= "black", bg="grey")
pok_nouveau.place(x=50, y=450)
# Fonction valider le nouveau Pokémon
def valider():
    nom = nom_saisie.get()
    type = type_saisie.get()
    taille = taille_saisie.get()
    poids = poids_saisie.get()
    talent = talent_saisie.get()
    faiblesse = faiblesse_saisie.get()
    image = None
    listPokemons.append(Pokemon(nom, type, taille, poids,talent, faiblesse, image))
    listbox.insert(tk.END, nom)
# Bouton valider
bouton = tk.Button(fenetre, text="Valider", command= valider, font= "Verdana 10 bold", bg="white", border=0)
bouton.place(x=600, y=575)





fenetre.mainloop() 