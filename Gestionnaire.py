
#Adoumadji Noudjalbaye Herve 18A880FS        
class Gestionnaires(Banque):
    def __init__(self,nom,phone,email):
        self.nom= nom
        self.tel= phone
        self.email= email
        return "gestionnaire{0},nimero telephone{1},compte email{2}".format(self.nom,self.tel,self.email)
        gestionnaire=gestionnaire("Mamadou ali",+10000000000,m@email.com)
        Banque.__init__(self,nom,email)
        #qui fait l'appel au constructeur de la classe mére
        self.tel=phone
        
