from ferme import Ferme, Chat, Chien

def creer_ferme():
    ferme = Ferme()
    return ferme

def ajouter_animal(ferme):
    print("Quel type d'animal souhaitez-vous ajouter ? (chat / chien)")
    type_animal = input()
    print("Quel est le nom de l'animal ?")
    nom = input()
    print("Quel est l'âge de l'animal ?")
    age = int(input())

    if type_animal == "chat":
        ferme.ajouter_animal(Chat(nom, age))
    elif type_animal == "chien":
        ferme.ajouter_animal(Chien(nom, age))
    else:
        print("Type d'animal non reconnu")

def crier(ferme):
    ferme.crier()

def tuer(ferme):
    print("Quel est le nom de l'animal à tuer ?")
    nom = input()
    ferme.tuer(nom)

def afficher_ferme(ferme):
    print(ferme)

def quitter():
    print("Au revoir !")
    exit()

def afficher_menu():
    print("--- Menu ---")
    print("1. Ajouter un animal")
    print("2. Faire crier tous les animaux")
    print("3. Tuer un animal")
    print("4. Afficher la ferme")
    print("5. Quitter")

def lancer_programme():
    ferme = creer_ferme()

    while True:
        afficher_menu()
        print("Entrez votre choix :")
        choix = int(input())

        if choix == 1:
            ajouter_animal(ferme)
        elif choix == 2:
            crier(ferme)
        elif choix == 3:
            tuer(ferme)
        elif choix == 4:
            afficher_ferme(ferme)
        elif choix == 5:
            quitter()
        else:
            print("Choix non valide")

if __name__ == "__main__":
    lancer_programme()
