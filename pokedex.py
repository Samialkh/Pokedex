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
listbox = tk.Listbox(fenetre, font="Verdana 10 bold", height=7, width=15)
listbox.place(x=700, y=10)
listbox.insert(tk.END, 'PIKACHU')
listbox.insert(tk.END, 'BULBIZARRE')
listbox.insert(tk.END, 'SALAMECHE')
listbox.insert(tk.END, 'DRACOLOSSE')
listbox.insert(tk.END, 'LEVIATOR')
# Créer Boutoun
bouton = tk.Button(fenetre, text="Selection", command=selection, font="Verdana 10 bold", bg="white")
bouton.place(x=700, y=150)


# Afficher les informations

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


# Labels 
pok_nom = tk.Label(fenetre, text="", font=("Verdana 15"), bg="white", fg= "black")
pok_nom.place(x=30, y=0)
pok_type= tk.Label(fenetre, text="", font=("Verdana 15"), bg="white", fg= "black")
pok_type.place(x=30, y=50)
pok_taille= tk.Label(fenetre, text="", font=("Verdana 15"), bg="white", fg= "black")
pok_taille.place(x=30, y=100)
pok_poids= tk.Label(fenetre, text="", font=("Verdana 15"), bg="white", fg= "black")
pok_poids.place(x=30, y=150)
pok_talent= tk.Label(fenetre, text="", font=("Verdana 15"), bg="white", fg= "black")
pok_talent.place(x=30, y=200)
pok_faiblesse= tk.Label(fenetre, text="", font=("Verdana 15"), bg="white", fg= "black")
pok_faiblesse.place(x=30, y=250)


# Label pour l'ajout d'un Pokémon
nom= Label(fenetre, text = "Entrez le nom du Pokémon : ")
nom.place(x=50, y=500)
type = Label(fenetre, text = "Entrez le type de Pokémon : ")
type.place(x=50, y=530)
taille = Label(fenetre, text = "Entrez la taille du Pokémon : ")
taille.place(x=50, y=560)
poids = Label(fenetre, text = "Entrez le poids du Pokémon : ")
poids.place(x=50, y=590)
talent = Label(fenetre, text = "Entrez le talent du Pokémon : ")
talent.place(x=50, y=620)
faiblesse = Label(fenetre, text = "Entrez la faiblesse du Pokémon : ")
faiblesse.place(x=50, y=650)

nom_saisie = Entry (fenetre, bd=5, bg="white", fg="black")
nom_saisie.place(x= 300, y=500)
type_saisie = Entry (fenetre, bd=5, bg="white", fg="black")
type_saisie.place(x= 300, y=530)
taille_saisie = Entry (fenetre, bd=5, bg="white", fg="black")
taille_saisie.place(x= 300, y=560)
poids_saisie = Entry (fenetre, bd=5, bg="white", fg="black")
poids_saisie.place(x= 300, y=590)
talent_saisie = Entry (fenetre, bd=5, bg="white", fg="black")
talent_saisie.place(x= 300, y=620)
faiblesse_saisie = Entry (fenetre, bd=5, bg="white", fg="black")
faiblesse_saisie.place(x= 300, y=650)

# Label Ajouter nouveau Pokémon
pok_nouveau = tk.Label(fenetre, text= "Ajouter un nouveau Pokémon", font=("Verdana 20"), fg= "black")
pok_nouveau.place(x=50, y=450)
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
bouton.place(x=600, y=575)


# Importer des images

# pokemon_image= Image.open('img/pikachu.png')
# pokemon_image = pokemon_image.resize((200,200))
# pokemon_image = ImageTk.PhotoImage(pokemon_image)

# l_icon_1 = Label(fenetre, image=pokemon_image)
# l_icon_1.place(x=200, y=10)

# Afficher une image en fonction du choix
# def get_image(choice):
#     if choice == "PIKACHU":
#         return pikachuimg
#     elif choice == "BULBIZARRE":
#         return bulbasaurimg
    # elif choice == "Salamèche":
    #     return charmander_img
    # elif choice == "Dracolosse":
    #     return dragonite_img
    # elif choice == "Léviator":
    #     return gyarados_img

# pikachuimg = ImageTk.PhotoImage(Image.open('img/pikachu.png'))
# bulbasaurimg = ImageTk.PhotoImage(Image.open('img/bulbasaur.png'))

# listImages = [pikachuimg, bulbasaurimg ] # pokemon3, # pokemon4, # pokemon5

# # Charger les images
# # pikachu_img = ImageTk.PhotoImage(Image.open('img/pikachu.png'))
# # bulbasaur_img = ImageTk.PhotoImage(Image.open('img/bulbasaur.png'))
# # charmander_img = ImageTk.PhotoImage(Image.open("charmander.png"))
# # dragonite_img = ImageTk.PhotoImage(Image.open("dragonite.png"))
# # gyarados_img = ImageTk.PhotoImage(Image.open("gyarados.png"))

# l_icon_1 = Label(fenetre, image=pikachuimg)
# l_icon_1.place(x=20, y=10)
# l_icon_2 = Label(fenetre, image=bulbasaurimg)
# l_icon_2.place(x=20, y=10)

# def changer_image(image_name):
#     img = Image.open(image_name)
#     img = img.resize((200,200))
#     photo = ImageTk.PhotoImage(img)
#     image_label.config(image=photo)
#     image_label.image = photo

# pikachu_img= "img/pikachu.png"
# bulbasaur_img= "img/bulbasaur.png"

# default_image = Image.open(pikachu_img)
# default_image = default_image.resize((200,200))
# default_photo = ImageTk.PhotoImage(default_image)
# image_label = Label(fenetre, image=default_photo)
# image_label.place(x=20, y=10)
# default_image = Image.open(bulbasaur_img)
# default_image = default_image.resize((200,200))
# default_photo = ImageTk.PhotoImage(default_image)
# image_label = Label(fenetre, image=default_photo)
# image_label.place(x=100, y=200)



fenetre.mainloop() 