#ZOUTCHIBE PALLAI 18B486FS

class Guichetieres(Banque):
     def __init__(self,nomGuichetier,prenomGuichetier,poste):
        self.nom= nomGuichetier
        self.prenom= prenomGuichetier
        self.poste= poste
        return "Guichetier:nom{0},prenom{1},poste{2}".format(self.nom,self.prenom,self.poste)
        guichetier=guichetier("Ousmanou","Amadou",12)
        Banque.__init__(self,nomGuichetuier,prenomGuichetier)
        self.poste= poste
