class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def cri(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.nom}, {self.age} ans)"


class Chat(Animal):
    def cri(self):
        print("Miaou")


class Chien(Animal):
    def cri(self):
        print("Ouaf")


class Ferme:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)
        print(f"{animal} est né")

    def crier(self):
        for animal in self.animaux:
            animal.cri()

    def tuer(self, nom):
        for animal in self.animaux:
            if animal.nom == nom:
                self.animaux.remove(animal)
                print(f"{animal} est mort")
                return
        print(f"Il n'y a pas d'animal nommé {nom} dans la ferme")

    def __repr__(self):
        return f"Ferme avec {len(self.animaux)} animaux "
