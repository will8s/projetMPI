import os,sys
#os.chdir(r'C:\Users\willi\Documents\projetMPI\AUtomatetest-F5')

path = os.path.dirname(sys.argv[0])+"\Automatetest-F5\\"

class Fichier :
	nom_fichier=""

	def __init__(self, nom_fichier):
		self.nom_fichier = nom_fichier

	def ouvrir_fichier(self):
		with open(path + self.nom_fichier, 'r') as fichier_automate:
			automate = (fichier_automate.read()).split("\n")
		return automate

class Automate(Fichier) :
	def __init__(self,nom_fichier):
		auto = Fichier.__init__(self,nom_fichier)
		self.automate = Fichier.ouvrir_fichier(self)
		self.nb_symbole = self.automate[0]
		self.nb_etat = self.automate[1]
		self.nb_etat_init = self.automate[2].split()[0]
		self.nb_etat_termi = self.automate[3].split()[0]
		self.nb_transition = self.automate[4]
		self.transition = Automate.transition(self)
		self.list_etat_init = Automate.list_etat_init(self)
		self.list_etat_termi = Automate.list_etat_termi(self)
	"""def nb_symbole(self):
		auto = Fichier.ouvrir_fichier(self)
		return auto[0]"""

	def list_symbole(self):
	 	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	 	nb = self.nb_symbole
	 	symbole = alpha[:int(nb)]
	 	return symbole

	"""def nb_etat(self):
		auto = Fichier.ouvrir_fichier(self)
		return auto[1]"""

	"""def nb_etat_init(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[2].split()
		return nb[0]"""

	def list_etat_init(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[2].split()
		etat_init = []
		for i in range(1,int(nb[0])+1) :
			etat_init.append(nb[i])
		return etat_init

	"""def nb_etat_termi(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[3].split()
		return nb[0]"""

	def list_etat_termi(self):
		auto = Fichier.ouvrir_fichier(self)
		nb = auto[3].split()
		etat_init = []
		for i in range(1,int(nb[0])+1) :
			etat_init.append(nb[i])
		return etat_init

	"""def nb_transition(self):
		auto = Fichier.ouvrir_fichier(self)
		return auto[4]"""

	def transition(self):
		auto = Fichier.ouvrir_fichier(self)
		liste_symb = Automate.list_symbole(self)
		liste_symb.append("*")

		auto_bis = auto[5:]
		
		for i in range(int(self.nb_transition)):
			for k in range(int(self.nb_symbole)+1):
				if liste_symb[k] in auto_bis[i]:
					auto_bis[i] = auto_bis[i].split(liste_symb[k])
					auto_bis[i].insert(1,liste_symb[k])
		return auto_bis

	def recherche_transi_termi(self,etat_depart,symbole):
		etat_term = ""
		
		transi = self.transition
		for i in range(int(self.nb_transition)):
			if transi[i][0] == str(etat_depart) and transi[i][1] == symbole:
				#type(transi[i][2])
				etat_term += transi[i][2]
		return etat_term

	def recherche_transi_depart(self,etat_termi,symbole):
		etat_term = ""
		
		transi = self.transition
		for i in range(int(self.nb_transition)):
			if transi[i][2] == str(etat_termi) and transi[i][1] == symbole:
				#type(transi[i][2])
				etat_term += transi[i][0]
		return etat_term

	def table_transition(self):
		j=0
		table = []
		transi = self.transition
		symbole = Automate.list_symbole(self)
		etat=[]

		######## ajout de l'etat i
		if "i" in self.list_etat_init:
			for x in range(int(self.nb_etat)-1):
				etat.append(str(x))
			etat.append("i")
		########
		else:
			for x in range(int(self.nb_etat)):
				etat.append(str(x))
		
		######## ajout de l'etat p et i
		presence_p = 0
		for x in self.transition:
			for y in range(3):
				if "p" == x[y]:#on verifie si l etat poubelle est utilise
					presence_p = 1
		if presence_p == 1 and "i" in self.list_etat_init:
			etat = []
			for x in range(int(self.nb_etat)-2):
				etat.append(str(x))
			etat.append("i")
			etat.append("p")
		######## ajout de l'etat p
		elif presence_p == 1:
			etat = []
			for x in range(int(self.nb_etat)-1):
				etat.append(str(x))
			etat.append("p")
		print "etat === ",etat
		########

		for i in range(int(self.nb_etat)):
			table.append([])
			for j in range(int(self.nb_symbole)):
				if Automate.recherche_transi_termi(self,etat[i],symbole[j]) == "p":
					table[i].append("p")
				elif Automate.recherche_transi_termi(self,etat[i],symbole[j]) == None:
					table[i].append(" ")
				else:
					table[i].append(Automate.recherche_transi_termi(self,etat[i],symbole[j]))

		print "table === ",table		
		for i in range(int(self.nb_etat)):
			if str(etat[i]) in self.list_etat_init:
				print "\n-->>"#les entree sont placees au dessus des etats
			if i<10:
				print "0"+etat[i],"|",
			else:	
				print etat[i],"|",
			for j in range(int(self.nb_symbole)):
				if table[i][j]=="" and int(self.nb_etat)>9:
					print "  ","|",
				elif table[i][j]=="":
					print " ","|",
				elif (table[i][j]=="p" and (int(self.nb_etat)-1)>9):
					print ".p","|",
				elif "p" in table[i][j] or table[i][j]=="p":
					print "p","|",
				elif (int(table[i][j])<10 and int(self.nb_etat)>9):
					print "."+table[i][j],"|",
				else:
				    print table[i][j],"|",

			if str(etat[i]) in self.list_etat_termi:
				print "\n<<--"#les sorties sont placees en dessous des etats
			elif str(i+1) not in self.list_etat_init:
				print "\n--"
		
###################################Determinisation et completion####################################
	def est_un_automate_asynchrone(self):
		transi = self.transition
		for i in range(int(self.nb_transition)):
			if transi[i][1] == "*":
				return True
		return False

	def etat_meme_symbole(self):
		cmpt = 0
		transi = self.transition
		symbole = Automate.list_symbole(self)

		for i in range(int(self.nb_transition)):
			for j in range(int(self.nb_transition)):
				if transi[i][1] == transi[j][1] and transi[i][0] == transi[j][0]:
					cmpt+=1
					if cmpt>1 : 
						return False
			#print "-",cmpt
			cmpt = 0
		return True

	def est_un_automate_deterministe(self):
		if self.nb_etat_init==1 and Automate.etat_meme_symbole(self):
			return True
		return "Il n a pas une seule entree ou Il y a des etats d ou sort plus d une fleche libellee par le meme caractere."

	def est_un_automate_complet(self):
		cmpt = 0
		cmpt_bis = 0
		transi = self.transition
		symbole = Automate.list_symbole(self)
		if int(self.nb_symbole==1):
			return True

		for i in range(int(self.nb_transition)):
			for j in range(int(self.nb_transition)):
				if transi[i][1] != transi[j][1] and transi[i][0] == transi[j][0]:
					cmpt+=1
					
			if cmpt == (int(self.nb_symbole)-1) : 
				cmpt_bis+=1
			#print cmpt,
			cmpt = 0
			#print "-",cmpt_bis
		if cmpt_bis == int(self.nb_etat)*2:
			return True
		return False
	
	def determinisation(self):
		listetat_init = self.list_etat_init
		listetat_termi = self.list_etat_termi
		liste_symb = Automate.list_symbole(self)
		transi = self.transition
		nb_transi = self.nb_transition

		new_transi = []
		stock = []
		stock_associ = []

		for i in listetat_init:
			for t in transi:
				if t[0]==i:
					stock.append([i,t[1],t[2]])
		#print "stock",stock

		save = [[],[],[]]

		for i in stock:
			for x in range(3):
				#save=i[x]
				save[x].append(i[x])
		stock_associ = save

		#print "stock_asso",stock_associ

		save=[[],[],[]]

		for T in range(len(stock_associ)):
			for x in range(len(transi)):
				if transi[0] in stock_associ[2]:
					for etat in range(3):
						save[etat].append(x[etat])
						#stock_associ[-1].append(x[etat])
			stock_associ.append(save)
			save=[[],[],[]]
		#print stock_associ
		"""		
		for i in stock:
			for t in transi:
				if t[0]==i[0]:
					stock.append([i,t[1],t[2]])

		print "stock---",stock
		"""

		"""
		for x in transi:
			for y in nb_transi:
				for s in liste_symb:
					if y == Automate.recherche_transi_termi(self,y,s)
						stock = [y,s,]
				new_transi[i].append([int(x)+1,s,Automate.recherche_transi_depart(self,,s)])
				i+=1
		"""
	def completion(self):

		new_transi = []
		compt_transi = 0
		for i in range(int(self.nb_etat)):
			for s in Automate.list_symbole(self):
				if Automate.recherche_transi_termi(self,i,s)=="":
					new_transi.append([str(i),s,"p"])					
		for s in Automate.list_symbole(self):			
			new_transi.append(["p",s,"p"])
		print new_transi

		for x in new_transi:
			self.transition.append(x)
			compt_transi+=1

		self.nb_transition = int(self.nb_transition)
		self.nb_transition += compt_transi
		self.nb_transition = str(self.nb_transition)
		self.nb_etat = int(self.nb_etat)
		self.nb_etat += 1
		self.nb_etat = str(self.nb_etat)

		print Automate.table_transition(self)
	
##########################################################################
#####################################Standardisation#####################################
	def standardisation(self):
		new_etat = "i"
		stock = []
		i = 0

		if self.nb_etat_init=="1":
			for x in self.transition:
				if x[2] not in self.list_etat_init:#on verifie si la transition sortante est reliee e une entree
					return "automate deja standard"
		else: 
			for x in self.transition:
				if x[0] in self.list_etat_init:#on debute la creation de la transition
					self.transition.append([new_etat,x[1],x[2]])
					self.nb_transition=int(self.nb_transition)
					self.nb_transition+=1
					self.nb_transition=str(self.nb_transition)
			print "nouvelle transition",self.transition

			self.list_etat_init = ["i"]

			self.nb_etat=int(self.nb_etat)
			self.nb_etat+=1
			self.nb_etat=str(self.nb_etat)
			self.nb_etat_init="1"
			Automate.table_transition(self)

##########################################################################

def menu():
	num_fichier = int(input("donnez le num du fichier qui contient l'automate que vous voulez (1-5-32) : "))
	if num_fichier<10 and num_fichier>0:
		num_fichier = "0"+str(num_fichier)
		return "L2-F5-"+str(num_fichier)+".txt"
	if num_fichier<45 and num_fichier>0: 
		return "L2-F5-"+str(num_fichier)+".txt"

##########################################################################

def test():
	choix_auto = menu()
	auto_data = Automate(choix_auto)
	
	auto = Fichier(choix_auto)
	print(auto.ouvrir_fichier())

	print auto_data.nom_fichier
	
	print "\nnb symbole        : ",auto_data.nb_symbole
	print "liste symboles    : ",auto_data.list_symbole()
	print "nb etat           : ",auto_data.nb_etat
	print "nb etat init      : ",auto_data.nb_etat_init
	print "etat initiaux     : ",auto_data.list_etat_init
	print "nb etat terminaux : ",auto_data.nb_etat_termi
	print "etat terminaux    : ",auto_data.list_etat_termi
	print "nb de transitions : ",auto_data.nb_transition
	print "transition        : ",auto_data.transition
	print "table de transi   : \n"
	auto_data.table_transition()
	print "----------------------------------------------------------"
	print "asynchrone        : ",auto_data.est_un_automate_asynchrone()
	print "deterministe      : ",auto_data.est_un_automate_deterministe()
	print "complet           : ",auto_data.est_un_automate_complet()
	print "completion        : ",auto_data.completion()
	#print "determinisation   : ",auto_data.determinisation()
	print "----------------------------------------------------------"
	#print "standardisation   : ",auto_data.standardisation()




########################################################################

encore = "o"
while encore == "o":
	test()
	encore = raw_input("voulez vous continuer ? ( o - n ) : ") 