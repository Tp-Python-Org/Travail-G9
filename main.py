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
        
        
