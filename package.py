#PUN SYSTEME QUI GERE UN COMPTE BANCAIRE
#coding:utf-8

#Bopabe Warmai 18B607FS
class Banque:
    def __init__(self,Banque,adresseBanque):
        self.Banque=Banque
        self.adresseBanque=adresseBanque
        nomBanque=Banque("B.A.C",52-41)
        return"Banque:nom {0},dresse{1}".format(self.nom,self.adresse)

compte = {}

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
        
#Mouaromtog Djimhognan 18B371FS
class Controleurs(Banque):
    def __init__(self,nom,matricule):
        self.nom=nom
        self.matricule=matricule
        return "controleur{0},matricule{1}".format(self.nom,self.matricule)
        controleur=controleur("bravo zoulou",123-456)
        Banque.__init__(self,nom)
        #qui fait l'appel au constructeur de la classe mére
        self.matricule=matricule
        
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
        
#Zoutchibe Pallai 18B486FS        
class Guichetieres(Banque):
     def __init__(self,nomGuichetier,prenomGuichetier,poste):
        self.nom= nomGuichetier
        self.prenom= prenomGuichetier
        self.poste= poste
        return "Guichetier:nom{0},prenom{1},poste{2}".format(self.nom,self.prenom,self.poste)
        guichetier=guichetier("Ousmanou","Amadou",12)
        Banque.__init__(self,nomGuichetuier,prenomGuichetier)
        self.poste= poste
          
 #Mahamat Yakhoub 18B249FS         
class GestionversementClients(Guichetieres):
      def __init__(self,versementSimple,versementConfrére):  
        self.versementSimple=versementSimple
        self.versement=versementConfrére
        return "GestionClients:versementsimple{0},versementconfrére{1}".format(self.versermentSimple,self.versement)
        GestionversementClients=GestionversementClients("")
        Guichetieres.__init__(self,versementSimple)
        self.versement=versement
            
 #Bademana Bigue Charles 18A047FS         
class Retrait(Guichetieres):
    def __init__(self,gestionRetrait,gestionRetraitchek): 
        self.gestionRetrait=gestionRetrait
        self.gestionRetraitchek=gestionRetraitchek-montant
        return"Retrait:gestionRetrait{0},gestionRetraitchek{1}".format(self.gestionRetrait,self.gestionRetraitchek)
        Retrait=Retrait("")
        Guichetieres.__init__(self,gestionRetrait)
        self.gestionRetraitchek=gestionRetraitchek
        
#Lagnaba Doufiene Fabrice 18B485FS   
class Virement(Guichetieres):
    def __init__(self,virementEpargné,virementCourant): 
        self.virementEpargné=virementEpargné
        self.virementCourant=virementCourant
        return"Virement:virement epargné{0},virement courant{1},virement multiple{2}".format(self.virementEpargné,self.virementCourant,self.virementMultiple)
        virement=virement("")
        Guichetiers.__init__(self,virementEpargné,viermentCourant)
        self.virementMultiple=virementMultiple
        
#Adelphe Rilembaye 18B708FS        
class OperationInternationale(Guichetieres):
    def __init__(self,compasation,dette):
        self.compasation=compasation
        self.dette=dette
        return"operationInternationale:compasation{0},dette{1}".format(self.compasation,self.dette)
        OperationInternationale=OperationInternationale("")
        Guichetieres.__init__(self,copasation,dette)
        self.dette=dette

#Fingbayle Josias-Perseverant 18A866FS     
#Programmme principal         

# seul la fonctionnalité client a été devéloppée
def menu():
    print('\t\tMENU')
    print('1 - Connectez vous en tant que Client')
    print('2 - Connectez vous en tant que Gestionnaire')
    print('3 - Connectez vous en tant que Guichetier')
    print()

def menu_client():
    print()
    print('\t \tMENU CLIENT')
    print('1  - operation de virement')
    print('2  - operation de retrait')
    print()
# Cas d'un seul client dans la base de données
client = Client("lambnda", "bravo", 90000)

continuer = 'oui'
while continuer == 'oui':
    menu()
    reponse=input("Faites votre choix : ")
    if reponse == '1':
        menu_client()
        rep_client = input("Faites votre choix : ")
        if rep_client == '2':
            montant = input("Entrez la somme a retirer : ")
            if client.retrait(int(montant)):
                print('Le retrait de {} a été effectué'.format(montant))
                print('Votre nouveau solde est : {} \n'.format(client.solde))
            else:
                print('Le montant est trop grand entrez un montant inferieur a votre solde')
        else:
            print('La fonctionnalité reste à developper !')

    else:
        print('Cette fonctionnalité n\'a pas été devéloppée')

    continuer=input("Voulez vous continuer ? (oui/non) : ")
        
                
                
