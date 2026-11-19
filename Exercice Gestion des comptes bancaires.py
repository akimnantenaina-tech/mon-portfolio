class CompteBancaire:
    def __init__(self ,titulaire , solde):
        self.titulaire = titulaire
        self.solde = solde
    
    def afficher_solde(self):
        print(f"Titulaire: {self.titulaire}")
        print(f"Solde disponible: {self.solde}")
        
class CompteEpargne(CompteBancaire):
    
    def __init__(self , titulaire , solde , taux_interet):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet
        
    def afficher_solde(self):
        super().afficher_solde()
        print(f"Taux_interet : {self.taux_interet} %")
     
    def calculer_interet(self):
         return self.solde * self.taux_interet / 100
     
compte = CompteEpargne(" Miora" , 500000 , 5 )
compte.afficher_solde()
print(f"Interet : {compte.calculer_interet():.2f} Ar")                  
    