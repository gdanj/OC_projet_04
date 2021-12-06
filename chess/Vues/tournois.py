from chess.Controleurs.tournois import TournoisControleurs
from chess.Vues.joueurs import JoueursVues
from tinydb import TinyDB

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
					print(joueurTable.get(doc_id=3))
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


	