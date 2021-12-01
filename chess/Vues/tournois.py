from chess.Controleurs.tournois import TournoisControleurs
from chess.Vues.joueurs import JoueursVues

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
				print("\nEntrez 1 pour ajouter un joueur\nEntrez 2 pour rechercher un joueur\nEntre 3 pour afficher la liste complète")
				choix = input()
				if choix == "1":
					newJoueur = JoueursVues()
					if newJoueur.formAddJoueur():
						break
				if choix == "2":
					findJoueur = JoueursVues()
					result = findJoueur.listJoueurDisplayFind()
					if result:
						list_joueurs_tournois.append(int(result))
					else:
						continue
				if choix == "3":
					newDisplay = JoueursVues()
					newDisplay.listJoueurDisplay()
				if choix == "menu":
					return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le type de tournois :\t 'bullet', 'blitz' ou 'coup rapide'")
		typeTournois = input()
		if typeTournois == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez la description du tournois")
		description = input()
		if description == "menu":
			return False
		newTournois = TournoisControleurs()
		newTournois.add(name, lieu, list_joueurs_tournois, typeTournois, description)