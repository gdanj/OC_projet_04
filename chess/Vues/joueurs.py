from re import search
from chess.Controleurs.joueurs import JoueursControleurs
from chess.Vues.printText import printCustome
from tinydb import TinyDB, Query, table

class JoueursVues:
	def formAddJoueur(self):
		pc = printCustome()
		pc.printText("Pour retourner au menu principal, entrez ''menu'' \nEntrez le nom du joueur")
		lastname = pc.inputClearScreen()
		if lastname == "menu":
			return False
		pc.printText("Pour retourner au menu principal, entrez ''menu'' \nEntrez le prénom du joueur")
		firstname = pc.inputClearScreen()
		if firstname == "menu":
			return False
		pc.printText("Pour retourner au menu principal, entrez ''menu'' \nEntrez la date de naissance du joueur au format ''dd/mm/aaaa''")
		birthDate = pc.inputClearScreen()
		if birthDate == "menu":
			return False
		pc.printText("Pour retourner au menu principal, entrez ''menu'' \nEntrez le genre du joueur,\n''M'' pour masculin \n''F'' pour féminin")
		sexe = pc.inputClearScreen()
		if sexe == "menu":
			return False
		pc.printText("Pour retourner au menu principal, entrez ''menu'' \nEntrez le classement du joueur")
		classement = pc.inputClearScreen()
		if classement == "menu":
			return False
		newJoueur = JoueursControleurs()
		newJoueur.add(lastname, firstname, birthDate, sexe, classement)

	def listJoueurDisplay(self):
		pc = printCustome()
		list_joueurs = JoueursControleurs()
		pc.printText('\n')
		tab = list_joueurs.joueur_all()
		pc.printText("Triez par :\n''1'' Ordre d'arriver \n''2'' Nom \n''3'' Prénom\n''4'' Classement")
		sort_on = pc.inputClearScreen()
		key_dict = ""
		if sort_on == '1':
			key_dict = "a"
		if sort_on == '2':
			key_dict = "firstname"
		if sort_on == '3':
			key_dict = "lastname"
		if sort_on == '4':
			key_dict = "classement"
		if key_dict == "a":
			result = tab
		else:
			result = sorted(tab, key=lambda x: x[key_dict], reverse=True)
		print('\033[2J')
		newTable = [["N°", "Nom" , "Prénom", "Date de naissance", "Sexe", "Classeement"]]
		for joueur in result:
			newTable.append(["''" + str(joueur.doc_id) + "''", joueur["lastname"], joueur["firstname"], joueur["birthDate"], joueur["sexe"], str(joueur["classement"])])
		pc.printTable(newTable)
		return tab

	def listJoueurDisplayFind(self):
		pc = printCustome()
		pc.printText('\n')
		search = True
		while search:
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
			if sort_on == 'menu':
				search = False
			if key_dict:
				tab = list(joueurTable.search(User[key_dict] == pc.inputClearScreen()))
				newTable = [["N°",  "Nom", "Prénom", "Date de naissance", "Sexe", "Classeement"]]
				for joueur in tab:
					newTable.append(["''" + str(joueur.doc_id) + "''", joueur["lastname"], joueur["firstname"], joueur["birthDate"], joueur["sexe"], str(joueur["classement"])])
				pc.printTable(newTable)