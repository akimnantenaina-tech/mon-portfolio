class Moteur :
    def __init__(self, marque , puissance):
        self.marque = marque
        self.puisance = puissance
        
    def demarrer (self) :
        print(f"Le moteur {self .marque} de {self.puisance} chevaux demarre.")
        
class Voiture :
    def __init__(self , modele , moteur):
        self.modele = modele
        self.moteur = moteur
        
    def demarrer (self):
        print (f"La voiture {self.modele} se prepare a demarrer...")
        self.moteur. demarrer()

moteur = Moteur('Toyota' , 120)
voiture = Voiture("Corolla", moteur )
voiture.demarrer()        