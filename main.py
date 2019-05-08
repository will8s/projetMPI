import os

os.chdir(r'C:\Users\willi\Documents\projetMPI\AUtomatetest-F5')

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
		liste_symb = Automate.list_symbole(self)
		liste_symb.append("*")

		auto_bis = auto[5:]
		
		for i in range(int(Automate.nb_transition(self))):
			for k in range(int(Automate.nb_symbole(self))+1):
				if liste_symb[k] in auto_bis[i]:
					auto_bis[i] = auto_bis[i].split(liste_symb[k])
					auto_bis[i].insert(1,liste_symb[k])
		return auto_bis

	def recherche_transi(self,etat_depart,symbole):
		etat_term = ""
		
		transi = Automate.transition(self)
		for i in range(int(Automate.nb_transition(self))):
			if transi[i][0] == str(etat_depart) and transi[i][1] == symbole:
				#type(transi[i][2])
				etat_term += transi[i][2]
		return etat_term

	def table_transition(self):
		j=0
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
			if i<10:
				print "0"+str(i),"|",
			else:	
				print i,"|",
			for j in range(int(Automate.nb_symbole(self))):
				if table[i][j]=="" and int(Automate.nb_etat(self))>9:
					print "  ","|",
				elif table[i][j]=="":
					print " ","|",
				elif int(table[i][j])<10 and int(Automate.nb_etat(self))>9:
					print "0"+table[i][j],"|",
				else:
				    print table[i][j],"|",
			print "\n--"
#######################################################################
	def est_un_automate_asynchrone(self):
		transi = Automate.transition(self)
		for i in range(int(Automate.nb_transition(self))):
			if transi[i][1] == "*":
				return True
		return False

	def etat_meme_symbole(self):
		cmpt = 0
		transi = Automate.transition(self)
		symbole = Automate.list_symbole(self)

		for i in range(int(Automate.nb_transition(self))):
			for j in range(int(Automate.nb_transition(self))):
				if transi[i][1] == transi[j][1] and transi[i][0] == transi[j][0]:
					cmpt+=1
					if cmpt>1 : 
						return False
			#print "-",cmpt
			cmpt = 0
		return True

	def est_un_automate_deterministe(self):
		if Automate.nb_etat_init(self)==1 and Automate.etat_meme_symbole(self):
			return True
		return "Il n a pas une seule entree ou Il y a des etats d ou sort plus d une fleche libellee par le meme caractere."

	def est_un_automate_complet(self):
		cmpt = 0
		cmpt_bis = 0
		transi = Automate.transition(self)
		symbole = Automate.list_symbole(self)
		if int(Automate.nb_symbole(self)==1):
			return True

		for i in range(int(Automate.nb_transition(self))):
			for j in range(int(Automate.nb_transition(self))):
				if transi[i][1] != transi[j][1] and transi[i][0] == transi[j][0]:
					cmpt+=1
					
			if cmpt == (int(Automate.nb_symbole(self))-1) : 
				cmpt_bis+=1
			#print cmpt,
			cmpt = 0
			#print "-",cmpt_bis
		if cmpt_bis == int(Automate.nb_etat(self))*2:
			return True
		return False
		
##########################################################################

def menu():
	num_fichier = input("donnez le num du fichier qui contient l'automate que vous voulez (1-5-32) : ")
	if num_fichier==1 : 
		return "L2-F5-nb.txt"
	elif num_fichier == 5: 
		return "L2-F5-05.txt"
	elif num_fichier == 32 :
		return "L2-F5-32.txt"
	elif num_fichier == 31 :
		return "L2-F5-31.txt"

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
	print "----------------------------------------------------------"
	print "asynchrone        : ",auto_data.est_un_automate_asynchrone()
	print "deterministe      : ",auto_data.est_un_automate_deterministe()
	print "complet           : ",auto_data.est_un_automate_complet()

########################################################################

encore = "o"
while encore == "o":
	test()
	encore = raw_input("voulez vous continuer ? ( o - n ) : ")