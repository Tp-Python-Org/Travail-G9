# BOPABE WARMAI 18B607FS
class Banque:
	"""
	classe agent de Banque
	"""
	def __init__(self):
		pass
		print("creation d'une Banque")
		self.nom="UBA"
		self.codeU=1998
		self.personne=Personne
		self.contrôleur=Contrôleur
		self.guichetier=Guichetier
		self.client=Client
		self.compte=Compte
		self.compteep=CompteEp
		self.comptec=CompteC
		self.comptegg=CompteGg
		self.gestionnaire=gestionnaire

		self.caisse = 150000
		self.nbrecompte = 0
		self.capital = 2350000
	def _str_ (self):
		return "\t {0} code : {1}\nCapital : {2} FCFA\nNombre de compte : {3}\n\n".format(self.nom, self.codeB, self.capital,self.nombrecompte)
