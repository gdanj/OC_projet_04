from re import search
from chess.Controleurs.joueurs import JoueursControleurs
from tinydb import TinyDB, Query

class JoueursVues:
	def formAddJoueur(self):
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le nom du joueur")
		lastname = input()
		if lastname == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le prénom du joueur")
		firstname = input()
		if firstname == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez la date de naissance du joueur au format 'dd/mm/aaaa'")
		birthDate = input()
		if birthDate == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le genre du joueur,\n'M' pour masculin \n'F' pour féminin")
		sexe = input()
		if sexe == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le classement du joueur")
		classement = input()
		if classement == "menu":
			return False
		newJoueur = JoueursControleurs()
		newJoueur.add(lastname, firstname, birthDate, sexe, classement)

	def listJoueurDisplay(self):
		list_joueurs = JoueursControleurs()
		print('\n')
		tab = list_joueurs.joueur_all()
		print("Triez par :\n'1' Ordre d'arriver \n'2' Nom \n'3' Prénom\n'4' Classement")
		sort_on = input()
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
			decorated = [(dict_[key_dict], dict_) for dict_ in tab]
			decorated.sort(reverse=True)
			result = [dict_ for (key, dict_) in decorated]
		print("N°" + "\t Nom "  + "\t Prénom " + "\t Date de naissance " + "\t Sexe " + "\t Classeement ")
		for joueur in result:
			print(str(joueur.doc_id) + "\t" +joueur["lastname"] + "\t\t" + joueur["firstname"] + "\t\t" + joueur["birthDate"] + "\t\t" + joueur["sexe"] + "\t\t" + str(joueur["classement"]))
		print('\n')
		return tab

	def listJoueurDisplayFind(self):
		print('\n')
		search = True
		while search:
			print("Recherchez par :\n'1' Nom \n'2' Prénom \n")
			sort_on = input()
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
				tab = list(joueurTable.search(User[key_dict] == input().capitalize()))
				i = 1
				print("N°" + "\t Nom "  + "\t Prénom " + "\t Date de naissance " + "\t Sexe " + "\t Classeement ")
				for joueur in tab:
					print(str(joueur.doc_id) + "\t" +joueur["lastname"] + "\t\t" + joueur["firstname"] + "\t\t" + joueur["birthDate"] + "\t\t" + joueur["sexe"] + "\t\t" + str(joueur["classement"]))
				print('\n')