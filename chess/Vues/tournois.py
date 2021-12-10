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
			print(joueur_id)
			current_tournois['infoJoueur'].append({
				'id' : joueur_id,
				'classement' : joueurTable.get(doc_id=int(joueur_id))['classement'],
				'point' : 0,
				"history" : []
			})
		tournoisTable.update({'infoJoueur' : current_tournois['infoJoueur']}, User.name == current_tournois['name'])
		tournoisTable.update({'currentTour' : 1}, User.name == current_tournois['name'])

	def firstRound(self, current_tournois):
		db = TinyDB('chess/Models/bdd/db.json')
		User = Query()
		tournoisTable = db.table('Tournois')
		tab = [[dict_['classement'], dict_] for dict_ in list(current_tournois['infoJoueur'])]
		tab2 = [dict_['classement'] for dict_ in list(current_tournois['infoJoueur'])]
		tab2.sort(reverse=True)
		result = []
		i = 0
		for nbr in tab2:
			for t in tab:
				if nbr == t[0]:
					if not t[1] in result:
						result.append(t[1])
			i += 1
		print(result)
		current_tournois['listTour'].append({
			"id": 1,
			"tour": [
				{"match": [result[0]['id'], result[4]['id']], "score": [0, 0], "end": False},
				{"match": [result[1]['id'], result[5]['id']], "score": [0, 0], "end": False},
				{"match": [result[2]['id'], result[6]['id']], "score": [0, 0], "end": False},
				{"match": [result[3]['id'], result[7]['id']], "score": [0, 0], "end": False}
			],
			"tourEnd": False
		})
		tournoisTable.update({'infoJoueur' : result}, User.name == current_tournois['name'])
		tournoisTable.update({'listTour' : current_tournois['listTour']}, User.name == current_tournois['name'])
	
	def	displayRoundAll(self, current_tournois):
		current_tournois
		print(current_tournois["name"])
		print(current_tournois["lieu"])
		for round in current_tournois["listTour"]:
			print("Tour " + str(round["id"]) + " Statut " + "Terminé" if round["tourEnd"] else "En cours")
		print("Entrez le numéro du tour que vous souhaitez séletionner\n")
		choix = input().strip()
		if choix == "menu":
			pass
		if int(choix) <= len(current_tournois["listTour"]) and int(choix) >= 0:
			self.displayRound(current_tournois, int(choix) - 1)
	
	def	displayRound(self, current_tournois, roundId):
		print(current_tournois["name"])
		print(current_tournois["lieu"])
		print("Round N°" + str(roundId + 1) + "\n")
		db = TinyDB('chess/Models/bdd/db.json')
		joueurTable = db.table('Joueurs')
		matchDict = current_tournois["listTour"][roundId]
		menu = False
		while not menu and not matchDict["tourEnd"]:
			i = 1
			for match in matchDict["tour"]:
				print("match : " + str(i) + "\n" + str(joueurTable.get(doc_id=match["match"][0])["firstname"]) + " vs " + str(joueurTable.get(doc_id=match["match"][1])["lastname"]))
				print("Score" + str(match["score"][0]) + " " + str(match["score"][1]) + "\t\t" + " Statut " + "Terminé" if match["end"] else "En cours" + "\n\n")
				i += 1
			print("Entrez le numéro du match que vous souhaitez cloturé\n")
			choix = input().strip()
			if choix == "menu":
				menu = True
			if int(choix) <= len(matchDict["tour"]) and int(choix) >= 0:
				if matchDict["tour"][int(choix) - 1]["end"]:
					print("Le match N°" + str(choix) + " est cloturé")
				else:
					self.addResult(current_tournois, roundId, int(choix) - 1)

	def updateInfoJoueur(self, current_tournois):
		db = TinyDB('chess/Models/bdd/db.json')
		User = Query()
		tournoisTable = db.table('Tournois')
		joueurTable = db.table('Joueurs')
		matchList = current_tournois["listTour"][-1]["tour"]
		infoJoueurList = current_tournois["infoJoueur"]
		for match in matchList:
			for i in range(8):
				if match["match"][0] == infoJoueurList[i]["id"]:
					infoJoueurList[i]["point"] += match["score"][0]
					infoJoueurList[i]["history"].append(match["match"][1])
				if match["match"][1] == infoJoueurList[i]["id"]:
					infoJoueurList[i]["point"] += match["score"][1]
					infoJoueurList[i]["history"].append(match["match"][0])
		tournoisTable.update({'infoJoueur' : current_tournois["infoJoueur"]}, User.name == current_tournois['name'])

	def addResult(self, current_tournois, roundId, matchId):
		db = TinyDB('chess/Models/bdd/db.json')
		User = Query()
		tournoisTable = db.table('Tournois')
		joueurTable = db.table('Joueurs')
		matchDict = current_tournois["listTour"][roundId]
		match = matchDict["tour"][matchId]
		while True:
			print("Entrez '0' si le résultat du macht est nul")
			print("Entrez '1' si " + str(joueurTable.get(doc_id=match["match"][0])["firstname"]) + " " + str(joueurTable.get(doc_id=match["match"][0])["lastname"]) + " à ganier")
			print("Entrez '2' si " + str(joueurTable.get(doc_id=match["match"][1])["firstname"]) + " " + str(joueurTable.get(doc_id=match["match"][1])["lastname"]) + " à ganier")
			choix = input().strip()
			if choix == "menu":
				break
			elif int(choix) == 0 or int(choix) == 1 or int(choix) == 2:
				if choix == "0":
					match["score"][0] = 0.5
					match["score"][1] = 0.5
				if choix == "1":
					match["score"][0] = 1
					match["score"][1] = 0
				if choix == "2":
					match["score"][0] = 0
					match["score"][1] = 1
				print("match : " + str(matchId) + "\n" + str(joueurTable.get(doc_id=match["match"][0])["firstname"]) + " vs " + str(joueurTable.get(doc_id=match["match"][1])["firstname"]))
				print("Score" + str(match["score"][0]) + " " + str(match["score"][1]) + "\t\t" + " Statut " + ("Terminé" if match["end"] else "En cours") + "\n\n")
				print("Vous souhaitez concerver ces données et cloturer le matche ?\nEntrez 'Oui' ou 'Non'")
				choix = input().strip()
				if choix == "menu":
					pass
				if choix == "Oui" or choix == "O":
					match["end"] = True
					matchDict["tourEnd"] = matchDict["tour"][0]["end"] and matchDict["tour"][1]["end"] and matchDict["tour"][2]["end"] and matchDict["tour"][3]["end"]
					if matchDict["tourEnd"]:
						tournoisTable.update({'currentTour' : current_tournois["currentTour"] + 1}, User.name == current_tournois['name'])
						self.updateInfoJoueur(current_tournois)
					tournoisTable.update({'listTour' : current_tournois["listTour"]}, User.name == current_tournois['name'])
					print("Match cloturé\n")
					break
				if choix == "Non" or choix == "N":
					continue
			else:
				continue
	
	def	tourNext(self, current_tournois):
		pass

	def tournoisSuisse(self, tournois_id):
		db = TinyDB('chess/Models/bdd/db.json')
		joueurTable = db.table('Tournois')
		current_tournois = joueurTable.get(doc_id=int(tournois_id))
		tab_joueur = current_tournois["list_joueurs_tournois"]
		if current_tournois['currentTour'] == 0:
			self.tourInit(current_tournois, tab_joueur)
		db = TinyDB('chess/Models/bdd/db.json')
		joueurTable = db.table('Tournois')
		current_tournois = joueurTable.get(doc_id=int(tournois_id))
		if current_tournois['currentTour'] == 1 and current_tournois['listTour'] == []:
			self.firstRound(current_tournois)
		if current_tournois['listTour'][-1]["tourEnd"] == False:
			self.displayRoundAll(current_tournois)
		elif int(current_tournois['currentTour']) < int(current_tournois['nbToursMax']):
			self.tourNext(current_tournois)