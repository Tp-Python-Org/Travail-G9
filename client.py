#Arnaud Daoukare 18A862FS
class Client:        
    def __init__(self, nom, prenom, init_solde=0):
        """Déclaration des attributs"""
        self.nom = nom
        self.prenom = prenom
        self.solde=init_solde
        self.numeroCompte = 1000000

    def retrait(self, montant):
        if montant > self.solde:
            return False
        self.solde -= montant
return True
