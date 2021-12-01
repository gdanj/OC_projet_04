from chess.Models.tournois import TournoisModels
import re

class TournoisControleurs:
	def	testListJoueursTournois(list_joueurs_tournois):
		for joueur in list_joueurs_tournois:
			if not joueur:
				return False
		return True

	def add(self, name, lieu, list_joueurs_tournois, typeTournois, description):
		verif = name and lieu and list_joueurs_tournois and typeTournois and description
		if verif:
			newJoueur = TournoisModels()
			newJoueur.create(name, lieu, list_joueurs_tournois, typeTournois, description)
			return True
		else:
			return False

	def joueur_all(self):
		listTournois = TournoisModels()
		return listTournois.allTournois()