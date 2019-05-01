import os

os.chdir(r'C:\Users\willi\Documents\projet_MPI')

class Fichier :


	def __init__(self, nom_fichier):
		self.nom_fichier = nom_fichier

	def ouvrir_fichier(self, nom_fichier):
		with open(self.nom_fichier, 'r') as fichier_automate:
			automate = (fichier_automate.read()).split("\n")
		#for i in automate :
		#	print(i)
		return automate

class Automate(Fichier) :
	def __init__(self,nom_fichier):
		Fichier.__init__(self,nom_fichier)

	def nb_symbole(self,nom_fichier):
		auto = Fichier.ouvrir_fichier(self,nom_fichier)
		return auto[0]
		
	


def menu():
	num_fichier = input("donnez le num du fichier qui contient l'automate que vous voulez (1-3) : ")
	if num_fichier==1 : 
		return "L2-F5-nb.txt"
	else: 
		return "L2-F5-nb.txt"

def test():
	choix_auto = menu()

	auto = Fichier(choix_auto)
	print(auto.ouvrir_fichier(auto.nom_fichier))

	auto_data = Automate(choix_auto)
	print (auto_data.nb_symbole(choix_auto))

test()