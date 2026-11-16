class Employe :
    def __init__(self, nom , age):
        self.nom = nom
        self.age = age
        
    def se_presenter(self) :
        print(f"Nom : {self.nom}")
        print(f"Age :{self.age }")                
        
class Developeur(Employe):
    def __init__(self, nom , age , langage_prefere):
        super().__init__(nom , age)
        self.langage_prefere = langage_prefere
        
    def se_presenter(self):
        super().se_presenter()
        print(f"Langage prefere: {self.langage_prefere}")
            
dev = Developeur ("Soa" , 25 , "Python")
dev.se_presenter()
          