import os

os.chdir(r'C:\Users\willi\Documents\projetMPI')

class Fichier :
	nom_fichier=""

	def __init__(self, nom_fichier):
		self.nom_fichier = nom_fichier

	def ouvrir_fichier(self):
		with open(self.nom_fichier, 'r') as fichier_automate:
			automate = (fichier_automate.read()).split("\n")
		return automate

class Automate(Fichier) :
	def __init__(self,nom_fichier):
		auto = Fichier.__init__(self,nom_fichier)

	def nb_symbole(self):
		auto = Fichier.ouvrir_fichier(self)
		return auto[0]

	def list_symbole(self):
	 	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	 	nb = Automate.nb_symbole(self)
	 	symbole = alpha[:int(nb)]
	 	return symbole

	def nb_etat(self):
		auto = Fichier.ouvrir_fichier(self)
		return auto[1]

	def nb_etat_init(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[2].split()
		return nb[0]

	def list_etat_init(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[2].split()
		etat_init = []
		for i in range(1,int(nb[0])+1) :
			etat_init.append(nb[i])
		return etat_init

	def nb_etat_termi(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[3].split()
		return nb[0]

	def list_etat_termi(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[3].split()
		etat_init = []
		for i in range(1,int(nb[0])+1) :
			etat_init.append(nb[i])
		return etat_init

	def nb_transition(self):
		auto = Fichier.ouvrir_fichier(self)
		return auto[4]

	def transition(self):
		auto = Fichier.ouvrir_fichier(self)
		auto_bis = auto[5:]
		auto = []
		for i in range(int(Automate.nb_transition(self))):
			auto.append([])
			for j in range(3):
				auto[i].append(auto_bis[i][j])
		return auto

	def recherche_transi(self,etat_depart,symbole):
		etat_term = ""
		transi = Automate.transition(self)
		for i in range(int(Automate.nb_transition(self))):
			if transi[i][0] == str(etat_depart) and transi[i][1] == symbole:
				#type(transi[i][2])
				etat_term += transi[i][2]+","
		return etat_term

	def table_transition(self):
		table = []
		transi = Automate.transition(self)
		symbole = Automate.list_symbole(self)
		
		for i in range(int(Automate.nb_etat(self))):
			#print "i : ",i,range(int(Automate.nb_etat(self)))
			table.append([])
			for j in range(int(Automate.nb_symbole(self))):
				#print Automate.recherche_transi(self,i,symbole[j])
				if Automate.recherche_transi(self,i,symbole[j]) == None:
					table[i].append(" ")
			
				table[i].append(Automate.recherche_transi(self,i,symbole[j]))
				#print "j : ",j,range(int(Automate.nb_symbole(self)))	
			#print Automate.recherche_transi(self,i,symbole[1])
			

		for i in range(int(Automate.nb_etat(self))):
			for j in range(int(Automate.nb_symbole(self))):
				print table[i][j],
			print "\n"

##########################################################################

def menu():
	num_fichier = input("donnez le num du fichier qui contient l'automate que vous voulez (1-3) : ")
	if num_fichier==1 : 
		return "L2-F5-nb.txt"
	else: 
		return "L2-F5-nb.txt"

##########################################################################

def test():
	choix_auto = menu()
	auto_data = Automate(choix_auto)
	
	auto = Fichier(choix_auto)
	print(auto.ouvrir_fichier())

	print auto_data.nom_fichier
	
	print "\nnb symbole        : ",auto_data.nb_symbole()
	print "liste symboles    : ",auto_data.list_symbole()
	print "nb etat           : ",auto_data.nb_etat()
	print "nb etat init      : ",auto_data.nb_etat_init()
	print "etat initiaux     : ",auto_data.list_etat_init()
	print "nb etat terminaux : ",auto_data.nb_etat_termi()
	print "etat terminaux    : ",auto_data.list_etat_termi()
	print "nb de transitions : ",auto_data.nb_transition()
	print "transition        : ",auto_data.transition()
	print "table de transi   : \n"
	auto_data.table_transition()

########################################################################

stop = "n"
while stop == "n":
	test()
	stop = raw_input("voulez vous arreter ? ( o - n ) : ")