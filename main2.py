
class SystemePolitiqueAfricain:
    def __init__(self, pays, president, regime, partis_politiques):
        self.pays = pays
        self.president = president
        self.regime = regime
        self.partis_politiques = partis_politiques
        self.lois = []
        self.gouvernement_forme = False

    def organiser_elections(self):
        print("Organisation des elections au", self.pays)

    def voter_loi(self, loi):
        self.lois.append(loi)
        print("Nouvelle loi vote :", loi)

    def former_gouvernement(self):
        self.gouvernement_forme = True
        print("Gouvernement a Madagascar", self.pays)

    def afficher_informations(self):
        print("Pays :", self.pays)
        print("President :", self.president)
        print("Regime politique :", self.regime)
        print("Partis politiques :", self.partis_politiques)
        print("Lois :", self.lois)
        print("Gouvernement formé :" ,self.gouvernement_forme)
        print("-"* 30)

pays1 = SystemePolitiqueAfricain("Madagascar","President de la Republique",
    "Republique",
    ["Parti A", "Parti B", "Parti C"])
    
pays2 = SystemePolitiqueAfricain("Senegal" , "president de la Republique" ,
    "Republique" ,
    ["Parti X", "Parti Y"]    
)
pays1.afficher_informations()
pays1.organiser_elections()
pays1.voter_loi("Loi sur l'education")
pays1.former_gouvernement()

pays2.organiser_elections()
pays2.voter_loi("Loi dur la santer")
pays2.voter_loi("Loi sur l'agriculture")
pays2.former_gouvernement()
