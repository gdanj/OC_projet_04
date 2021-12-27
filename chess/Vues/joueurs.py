from re import search
from chess.Controleurs.joueurs import JoueursControleurs
from chess.Vues.printText import printCustome
from tinydb import TinyDB, Query

class JoueursVues:
	def formAddJoueur(self):
		jc = JoueursControleurs()
		while True:
			lastname = self.addPlayer("Entrez le nom du joueur", jc.testName)
			if lastname == 0: return 0
			if lastname == 1: break
			firstname = self.addPlayer("Entrez le prénom du joueur", jc.testName)
			if firstname == 0: return 0
			if firstname == 1: break
			birthDate = self.addPlayer("Entrez la date de naissance du joueur au format ''dd/mm/aaaa''", jc.testDate)
			if birthDate == 0: return 0
			if birthDate == 1: break
			sexe = self.addPlayer("Entrez le genre du joueur,\n''M'' pour masculin \n''F'' pour féminin", jc.testSexe)
			if sexe == 0: return 0
			if sexe == 1: break
			classement = self.addPlayer("Entrez le classement du joueur", jc.testClassement)
			if classement == 0: return 0
			if classement == 1: break
			jc.add(lastname, firstname, birthDate, sexe, classement)
			break
			
	def addPlayer(self, string, ftTest):
		pc = printCustome()
		while True:
			self.backMenu()
			pc.printText(string)
			choix = pc.inputClearScreen()
			if choix == "menu":
				return 0
			elif choix == "back":
				return 1
			if ftTest(choix):
				pc.printText("Vous avez saisi ''" + choix.capitalize() + "'' vous souhaitez le valider ?\
					\nEntrez ''o'' ou ''oui'' pour valider\
					\nEntrez ''n'' ou ''non'' pour effectuer une nouvelle saisie")
				valid = input().strip().lower()
				if valid == 'o' or valid == 'oui':
					return choix
				if valid == 'n' or valid == 'non':
					continue
			else:
				print("Saisie incorrecte")

	def listPlayer(self):
		pc = printCustome()
		while True:
			self.backMenu()
			pc.printText("Entrez ''1'' pour afficher la liste des joueurs\
				\nEntrez ''2'' pour ajouter un nouveau joueur\
				\nEntrez ''3'' pour mettre a jour le classemnt du joueur")
			choix = pc.inputClearScreen()
			if choix == '1':
				self.listJoueurDisplay()
			if choix == '2':
				res = self.formAddJoueur()
				if res == 0:
					break
				else:
					continue
			elif choix == '3':
				res = self.playerUpdate()
				if res == 0:
					break
				else:
					continue
			elif choix == 'menu':
				break

	def backMenu(self):
		pc = printCustome()
		pc.printText("Entrez ''menu'' pour retourner au menu principal\
			\nEntrez ''back'' pour retourner en arrière")
	
	def playerUpdate(self):
		jc = JoueursControleurs()
		pc = printCustome()
		while True:
			self.backMenu()
			print("Entrez le numero du joueur de vous souhaité modifier")
			choix = pc.inputClearScreen()
			if choix.isnumeric():
				if jc.testJoueursInBDD:
					player = jc.getPlayerByID(int(choix))
					newTable = [["N°", "Nom" , "Prénom", "Date de naissance", "Sexe", "Classeement"]]
					newTable.append(["''" + str(player.doc_id) + "''", player["lastname"],\
						player["firstname"], player["birthDate"], player["sexe"], str(player["classement"])])
					pc.printTable(newTable)
					pc.printText("Entrez le nouveau classement du joueur\
						\nEntrez ''autre'' pour choisir un autre joueur")
					choix = pc.inputClearScreen()
					if choix.isnumeric():
						jc.joueurUpdate(int(choix), player.doc_id)
						return 2
					elif choix == "menu":
						return 0
					elif choix == "autre":
						continue
					elif choix == "back":
						return 1
				else:
					print("Le numero entré n'est pas dans la BDD")
			elif choix == "menu":
				return 0
			elif choix == "back":
				return 1
			else:
				print("Entrez un nombre ex: 5")

	def listJoueurDisplay(self):
		pc = printCustome()
		list_joueurs = JoueursControleurs()
		pc.printText('\n')
		tab = list_joueurs.joueur_all()
		self.backMenu()
		pc.printText("Triez par :\n''1'' Ordre d'arriver \n''2'' Nom \n''3'' Prénom\n''4'' Classement")
		sort_on = pc.inputClearScreen()
		key_dict = ""
		if sort_on == '1':
			result = tab
		if sort_on == '2':
			key_dict = "firstname"
		if sort_on == '3':
			key_dict = "lastname"
		if sort_on == '4':
			key_dict = "classement"
		if sort_on == 'menu':
			return 0
		if sort_on == 'back':
			return 1
		if key_dict != '':
			result = sorted(tab, key=lambda x: x[key_dict], reverse=True)
		print('\033[2J')
		newTable = [["N°", "Nom" , "Prénom", "Date de naissance", "Sexe", "Classeement"]]
		for joueur in result:
			newTable.append(["''" + str(joueur.doc_id) + "''", joueur["lastname"],\
				 joueur["firstname"], joueur["birthDate"], joueur["sexe"], str(joueur["classement"])])
		pc.printTable(newTable)
		return tab

	def listJoueurDisplayFind(self):
		pc = printCustome()
		pc.printText('\n')
		search = True
		while search:
			self.backMenu()
			pc.printText("Recherchez par :\n''1'' Nom \n''2'' Prénom \n")
			sort_on = pc.inputClearScreen()
			User = Query()
			db = TinyDB('chess/Models/bdd/db.json')
			joueurTable = db.table('Joueurs')
			key_dict = ""
			if sort_on == '1':
				key_dict = "lastname"
				print("Entrez le nom du joueuer")
			if sort_on == '2':
				key_dict = "firstname"
				print("Entrez le prénom du joueuer")
			if sort_on == 'back':
				return 1
			if sort_on == 'menu':
				return 0
			if key_dict:
				tab = list(joueurTable.search(User[key_dict] == pc.inputClearScreen()))
				newTable = [["N°",  "Nom", "Prénom", "Date de naissance", "Sexe", "Classeement"]]
				for joueur in tab:
					newTable.append(["''" + str(joueur.doc_id) + "''", joueur["lastname"],\
						 joueur["firstname"], joueur["birthDate"], joueur["sexe"], str(joueur["classement"])])
				pc.printTable(newTable)