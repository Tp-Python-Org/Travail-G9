#Mahamat Yakhoub 18B249FS         
class GestionversementClients(Guichetieres):
      def __init__(self,versementSimple,versementConfrére):  
        self.versementSimple=versementSimple
        self.versement=versementConfrére
        return "GestionClients:versementsimple{0},versementconfrére{1}".format(self.versermentSimple,self.versement)
        GestionversementClients=GestionversementClients("")
        Guichetieres.__init__(self,versementSimple)
        self.versement=versement
