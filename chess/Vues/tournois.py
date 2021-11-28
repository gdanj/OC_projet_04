from chess.Controleurs.tournois import TournoisControleurs

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
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez la date de début du tournois au format 'dd/mm/aaaa'")
		dataTournois = input()
		if dataTournois == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez les indices des joueurs du tournois")
		list_joueurs_tournois = []
		for i in range(8):
			joueur = input()
			if joueur == "menu":
				return False
			list_joueurs_tournois.append(int(joueurs))
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez le type de tournois :\t 'bullet', 'blitz' ou 'coup rapide'")
		typeTournois = input()
		if typeTournois == "menu":
			return False
		print("Pour retourner au menu principal, entrez 'menu' \nEntrez la description du tournois")
		description = input()
		if description == "menu":
			return False
		newTournois = TournoisControleurs()
		newTournois.add(name, lieu, dataTournois, list_joueurs_tournois, typeTournois, description)