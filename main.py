class Etudiant : 
    pass
etudiant1 = Etudiant()
print(etudiant1) 

class Etudiant :
    def __init__(self , nom , age):
        self.nom = nom
        self.age = age

etudiant1 = Etudiant ("Nivo" , 25) 
print(etudiant1.nom)
print(etudiant1.age)       
 
class Etudiant :
    def _init_(self , nom , age) : 
        self.nom = nom
        self.age = age   
    
    def se_presenter (self) :
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")
        
        etudiant1 = Etudiant("Niry",25)
        etudiant1.se_presenter()
        
class Etudiant :
    def __init__(self , nom , age ):
        self.nom = nom
        self.age = age
    
    def se_presenter (self):
        print(f"Bonjour , Je m'appelle {self.nom} et j'ai {self.age} ans.")

etudiant1 = Etudiant ("Nivo" , 25)
etudiant2 = Etudiant ("Jean" , 22) 

etudiant1.se_presenter()
etudiant2.se_presenter()                    
        
class Etudiant :
    def __init__(self , nom , age ):
        self.nom = nom
        self.age = age
    
    def se_presenter (self):
        print(f"Bonjour , Je m'appelle {self.nom} et j'ai {self.age} ans.")

etudiant1 = Etudiant ("Nivo" , 25)
etudiant2 = Etudiant ("Jean" , 22)
etudiant3 = Etudiant ("Marie" , 21)  

etudiant1.se_presenter()
etudiant2.se_presenter()
etudiant3.se_presenter()                            