from chess.Models.tournois import TournoisModels

class TournoisControleurs:
	
	def	testListJoueursTournois(list_joueurs_tournois):
		for joueur in list_joueurs_tournois:
			if not joueur:
				return False
		return True

	def add(self, name, lieu, list_joueurs_tournois, typeTournois, nbTours, description):
		verif = name and lieu and list_joueurs_tournois and typeTournois and nbTours and description
		if verif:
			tm = TournoisModels()
			tm.create(name, lieu, list_joueurs_tournois, typeTournois, nbTours, description)
			return True
		else:
			return False

	def tournois_all(self):
		tm = TournoisModels()
		return tm.allTournois()

	def	getPlayerByID(self, id):
		tm = TournoisModels()
		joueurTable = tm.playerDB()
		return joueurTable.get(doc_id=id)

	def testTypeTournois(self, typeTournois):
		if typeTournois.isnumeric():
			nbrTypeTournois = int(typeTournois)
			if 1 <= nbrTypeTournois and nbrTypeTournois <= 3:
				if nbrTypeTournois == 1:
					return "bullet"
				elif nbrTypeTournois == 2:
					return "blitz"
				elif nbrTypeTournois == 3:
					return "coup rapide"
		return 0
	
	def testRoundTournois(self, nbTours):
		if nbTours.isnumeric():
			nbr = int(nbTours)
			if 4 <= nbr and nbr <= 7:
				return True
		return False
	
	def testJoueursInBDD(self, idJoueur, list_joueurs_tournois):
		tm = TournoisModels()
		joueurTable = tm.playerDB()
		if joueurTable.contains(doc_id=int(idJoueur)):
			if int(idJoueur) in list_joueurs_tournois:
				return 1
			else:
				list_joueurs_tournois.append(int(idJoueur))
		else:
			return 2
		return 0

	def closeMatch(self, current_tournois, matchDict, match):
		tm = TournoisModels()
		match["end"] = True
		matchDict["tourEnd"] = matchDict["tour"][0]["end"] and matchDict["tour"][1]["end"] \
			and matchDict["tour"][2]["end"] and matchDict["tour"][3]["end"]
		if matchDict["tourEnd"]:
			tm.closeMatchUpdate(current_tournois)

	def selectTournoix(self, choix):
		tm = TournoisModels()
		tournoisTable = tm.tournoisDB()
		if tournoisTable.contains(doc_id=int(choix)):
			current_tournois = tournoisTable.get(doc_id=int(choix))
			return current_tournois
		else:
			return 0
	
	def testNextRound(seft, current_tournois):
		if current_tournois['currentTour'] == 0 or current_tournois['currentTour'] == 1:
			return True
		return int(current_tournois['currentTour']) <= int(current_tournois['nbToursMax']) \
			and current_tournois['listTour'][-1]["tourEnd"] == True
	
	def tournoisSuisse(self, current_tournois):
		tm = TournoisModels()
		tab_joueur = current_tournois["list_joueurs_tournois"]
		if current_tournois['currentTour'] == 0:
			tm.tourInit(current_tournois, tab_joueur)
		elif current_tournois['currentTour'] == 1 and current_tournois['listTour'] == []:
			tm.firstRound(current_tournois)
		elif int(current_tournois['currentTour']) <= int(current_tournois['nbToursMax']) \
			and current_tournois['listTour'][-1]["tourEnd"] == True:
			tm.tourNextSort(current_tournois)
		elif int(current_tournois['currentTour']) > int(current_tournois['nbToursMax']) \
			and current_tournois['listTour'][-1]["tourEnd"] == True:
			if (current_tournois['dateFinTournois'] == "En cours"):
				tm.lastround(current_tournois)
				from datetime import date
				today = date.today()
				current_tournois['dateFinTournois'] = today.strftime("%d/%m/%Y")
				tm.updateTournoisDB(current_tournois, 'dateFinTournois')