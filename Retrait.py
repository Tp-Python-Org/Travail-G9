
#Bademana Bigue Charles 18A047FS         
class Retrait(Guichetieres):
    def __init__(self,gestionRetrait,gestionRetraitchek): 
        self.gestionRetrait=gestionRetrait
        self.gestionRetraitchek=gestionRetraitchek-montant
        return"Retrait:gestionRetrait{0},gestionRetraitchek{1}".format(self.gestionRetrait,self.gestionRetraitchek)
        Retrait=Retrait("")
        Guichetieres.__init__(self,gestionRetrait)
        self.gestionRetraitchek=gestionRetraitchek
  
