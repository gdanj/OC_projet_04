from chess.Controleurs.joueurs import JoueursControleurs

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
		tab = list(list_joueurs.joueur_all())
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
 			decorated.sort()
 			result = [dict_ for (key, dict_) in decorated]
		for joueur in result:
			print("Nom "  + "\t Prénom " + joueur["firstname"] + "\t Date de naissance " + joueur["birthDate"] + "\t Sexe " + joueur["sexe"] + "\t Classeement " + str(joueur["classement"]))
			print("Nom " + joueur["lastname"] + "\t Prénom " + joueur["firstname"] + "\t Date de naissance " + joueur["birthDate"] + "\t Sexe " + joueur["sexe"] + "\t Classeement " + str(joueur["classement"]))
		print('\n')
	
	def menu(self):
		while True:
			print("Entrez '1' pour afficher la liste des joueur")
			print("Entrez '2' pour ajouter un joueur")
			print("Entrez 'exit' pour quitter le programme")
			commande = input()
			if commande == '1':
				self.listJoueurDisplay()
			if commande == '2':
				self.formAddJoueur()
			if commande == 'exit':
				break