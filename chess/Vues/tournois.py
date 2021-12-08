from chess.Controleurs.tournois import TournoisControleurs
from chess.Vues.joueurs import JoueursVues
from tinydb import TinyDB, Query

class TournoisVues:
	def formAddTournois(self):
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le nom du tournois")
		name = input()
		if name == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le lieu du tournois")
		lieu = input()
		if lieu == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu'")
		print("Vous devez ajouter 8 joueurs")
		list_joueurs_tournois = []
		for i in range(8):
			while True:
				print("joueur n° " + str(i + 1))
				print("\nEntrez '1' pour ajouter l'ID d'un joueur\nEntrez 2 pour rechercher l'ID un joueur\nEntre 3 pour afficher la liste complète\nEntrez '4' pour ajouté un nouveau joueur à la base de donnée")
				choix = input()
				if choix == "4":
					newJoueur = JoueursVues()
					if newJoueur.formAddJoueur():
						break
				if choix == "2":
					findJoueur = JoueursVues()
					findJoueur.listJoueurDisplayFind()
					continue
				if choix == "1":
					print("Entrez le numero du joueur")
					idJoueur = input().strip()
					db = TinyDB('chess/Models/bdd/db.json')
					joueurTable = db.table('Joueurs')
					print(joueurTable.get(doc_id=int(idJoueur)))
					if joueurTable.contains(doc_id=int(idJoueur)):
						if int(idJoueur) in list_joueurs_tournois:
							print("Le joueur n°" + idJoueur + " est déjà dans la liste")
							continue
						else:
							list_joueurs_tournois.append(int(idJoueur))
							break
					else:
						print("Le joueur N°" + idJoueur + " n'est pas dans la base de donnée")
				if choix == "3":
					newDisplay = JoueursVues()
					newDisplay.listJoueurDisplay()
				if choix == "menu":
					return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le type de tournois :\t 'bullet', 'blitz' ou 'coup rapide'")
		typeTournois = input().strip()
		if typeTournois == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le nombre de tours, entre 4 nim et 7 max")
		nbTours = input().strip()
		if nbTours == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez la description du tournois")
		description = input()
		if description == "menu":
			return False
		newTournois = TournoisControleurs()
		print(name, lieu, list_joueurs_tournois, typeTournois, description)
		newTournois.add(name, lieu, list_joueurs_tournois, typeTournois, int(nbTours), description)

	def listTournoisDisplay(self):
		list_tournois = TournoisControleurs()
		print('\n')
		tab = list_tournois.tournois_all()
		db = TinyDB('chess/Models/bdd/db.json')
		joueurTable = db.table('Tournois')
		print("N°" + "\t Nom "  + "\t Lieu" + "\t Date de début" + "\t date de fin")
		for tournois in tab:
			print(str(tournois.doc_id) + "\t" + tournois["name"] + "\t" + tournois["lieu"] + "\t" + tournois["dataTournois"] + "\t" + tournois["dateFinTournois"])
		print('\n')
		while True:
			print("Entrez l'ID du tournois que vous souhaitez sélection\nEntrez 'menu' pour retourner au menu principal")
			choix = input()
			if joueurTable.contains(doc_id=int(choix)):
				self.tournoisSuisse(choix)
			if choix == 'menu':
				break
			


	def	tourInit(self, current_tournois, tab_joueur):
		db = TinyDB('chess/Models/bdd/db.json')
		User = Query()
		joueurTable = db.table('Joueurs')
		tournoisTable = db.table('Tournois')
		for joueur_id in tab_joueur:
			current_tournois['listTour'][joueur_id] = {
				'classement' : joueurTable.get(doc_id=int(joueur_id))['classement'],
				'point' : 0
			}
		tournoisTable.update({'listTour' : current_tournois['listTour']}, User.name == current_tournois['name'])
		tournoisTable.update({'currentTour' : 1}, User.name == current_tournois['name'])

	def tournoisSuisse(self, tournois_id):
		db = TinyDB('chess/Models/bdd/db.json')
		joueurTable = db.table('Tournois')
		current_tournois = joueurTable.get(doc_id=int(tournois_id))
		tab_joueur = current_tournois["list_joueurs_tournois"]
		if current_tournois['currentTour'] == 0:
			self.tourInit(current_tournois, tab_joueur)
		elif current_tournois['currentTour'] < current_tournois['nbToursMax']:
			self.tourNext(current_tournois, tab_joueur)