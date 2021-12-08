from tinydb import TinyDB, Query

class TournoisModels:
	def create(self, name, lieu, list_joueurs_tournois, typeTournois, nbTours, description):
		db = TinyDB('chess/Models/bdd/db.json')
		Tournois = db.table('Tournois')
		self.name = name.capitalize()
		self.lieu = lieu.capitalize()
		from datetime import date
		today = date.today()
		d1 = today.strftime("%d/%m/%Y")
		self.dateDebutTournois = d1
		self.dateFinTournois = "En cours"
		self.list_joueurs_tournois = list_joueurs_tournois
		self.typeTournois = typeTournois.capitalize()
		self.nbTours = nbTours
		self.description = description
		Tournois.insert({
			'name': self.name,
			'lieu': self.lieu,
			'dataTournois' : self.dateDebutTournois,
			'dateFinTournois' : self.dateFinTournois,
			'list_joueurs_tournois' : self.list_joueurs_tournois,
			'listTour' : {},
			'typeTournois' : self.typeTournois,
			'nbToursMax' : self.nbTours,
			'currentTour' : 0,
			'description' : self.description
		})

	def allTournois(self):
		db = TinyDB('chess/Models/bdd/db.json')
		Tournois = db.table('Tournois')
		return Tournois.all()