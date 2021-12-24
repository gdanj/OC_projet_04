from chess.Controleurs.tournois import TournoisControleurs
from chess.Vues.joueurs import JoueursVues
from chess.Vues.printText import printCustome
class TournoisVues:

	def	addPlayerTournois(self, list_joueurs_tournois):
		pc = printCustome()
		for i in range(8):
			while True:
				pc.printText("joueur n° " + str(i + 1) + "\nEntrez ''1'' pour ajouter l'ID d'un joueur\nEntrez ''2'' pour rechercher l'ID un joueur\nEntrez ''3'' pour afficher la liste complète\nEntrez ''4'' pour ajouté un nouveau joueur à la base de donnée")
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
					pc.printText("Entrez le numero du joueur")
					idJoueur = input().strip()
					tc = TournoisControleurs()
					playerIn = tc.testJoueursInBDD(idJoueur, list_joueurs_tournois)
					if playerIn == 0:
						break
					elif playerIn == 1:
						pc.printText("Le joueur n°''" + idJoueur + "'' est déjà dans la liste")
					elif playerIn == 2:
						pc.printText("Le joueur N°''" + idJoueur + "'' n'est pas dans la base de donnée")
				if choix == "3":
					newDisplay = JoueursVues()
					newDisplay.listJoueurDisplay()
		return list_joueurs_tournois

	def formAddTournois(self):
		pc = printCustome()
		pc.printText("Pour retourner au menu principal, entrez ''menu''\nEntrez le nom du tournois")
		name = input()
		if name == "menu":
			return False
		pc.printText("Pour retourner au menu principal, entrez ''menu''\nEntrez le lieu du tournois")
		lieu = input()
		if lieu == "menu":
			return False
		pc.printText("Pour retourner au menu principal, entrez ''menu''\nVous devez ajouter 8 joueurs")
		list_joueurs_tournois = []
		if not self.addPlayerTournois(list_joueurs_tournois):
			return False
		else:
			print(list_joueurs_tournois)
		while True:
			pc.printText("Pour retourner au menu principal, entrez ''menu''\nEntrez ''1'' pour un tournois du type 'bullet'\nEntrez ''2'' pour un tournois du type 'blitz'\nEntrez ''3'' pour un tournois du type 'coup rapide'")
			typeTournoisInput = input().strip()
			if typeTournoisInput == "menu":
				return False
			tc = TournoisControleurs()
			typeTournois = tc.testTypeTournois(typeTournoisInput)
			if typeTournois == 0:
				pc.printText("\nEntrez un chiffre de 1 à 3")
			else:
				break
		while True:
			pc = printCustome()
			pc.printText("Pour retourner au menu principal, entrez ''menu''\nEntrez le nombre de tours, entre ''4'' nim et ''7'' max")
			nbTours = input().strip()
			tc = TournoisControleurs()
			if nbTours == "menu":
				return False
			if tc.testRoundTournois(nbTours):
				break
			else:
				pc.printText("Entrez un chiffre de 4 à 7")
		pc.printText("Pour retourner au menu principal, entrez ''menu''\nEntrez la description du tournois")
		description = input()
		if description == "menu":
			return False
		tc.add(name, lieu, list_joueurs_tournois, typeTournois, int(nbTours), description)

	def listTournoisDisplay(self):
		pc = printCustome()
		pc.printText('\n')
		tc = TournoisControleurs()
		tab = tc.tournois_all()
		pc.printText("N°" + "\t Nom "  + "\t Lieu" + "\t Date de début" + "\t date de fin")
		for tournois in tab:
			pc.printText(str(tournois.doc_id) + "\t" + tournois["name"] + "\t" + tournois["lieu"] + "\t" + tournois["dataTournois"] + "\t" + tournois["dateFinTournois"])
		pc.printText('\n')
		while True:
			pc.printText("Entrez le numéro du tournois que vous souhaitez sélection\nEntrez 'menu' pour retourner au menu principal")
			choix = input().strip()
			current_tournois = tc.selectTournoix(choix)
			if current_tournois == 0:
				pc.printText("Le tournois N°" + choix + " n'est pas dans la base de donnée")
			else:
				self.displayAllRound(current_tournois)
			if choix == 'menu':
				break
	
	def	displayAllRound(self, current_tournois):
		pc = printCustome()
		while True:
			print(current_tournois["name"])
			print(current_tournois["lieu"])
			for round in current_tournois["listTour"]:
				pc.printText("Tour ''" + str(round["id"]) + "'' Statut " + ("Terminé" if round["tourEnd"] else "En cours"))
			print("Entrez le numéro du tour que vous souhaitez séletionner\n")
			choix = input().strip()
			if choix == "menu":
				break
			if choix.isnumeric():
				if int(choix) <= len(current_tournois["listTour"]) and int(choix) >= 0:
					self.displayRound(current_tournois, int(choix) - 1)
					tc = TournoisControleurs()
					tc.tournoisSuisse(current_tournois)
	
	def	displayRound(self, current_tournois, roundId):
		print(current_tournois["name"])
		print(current_tournois["lieu"])
		matchDict = current_tournois["listTour"][roundId]
		menu = False
		pc = printCustome()
		tc = TournoisControleurs()
		while not menu:
			i = 1
			for match in matchDict["tour"]:
				pc.printText("match : ''" + str(i) + "''\n" + str(tc.getPlayerByID(match["match"][0])["firstname"]) + " vs " + str(tc.getPlayerByID(match["match"][1])["lastname"]))
				print("Score : " + str(match["score"][0]) + " " + str(match["score"][1]) + "\t\t" + " Statut " + ("Terminé" if match["end"] else "En cours") + "\n\n")
				i += 1
			if not matchDict['tourEnd']:
				print("Entrez le numéro du match que vous souhaitez cloturé\n")
			pc.printText("Entrez ''0'' pour retourner au meunu précédent")
			choix = input().strip()
			if choix == "0":
				menu = True
			if int(choix) <= len(matchDict["tour"]) and int(choix) >= 1:
				if matchDict["tour"][int(choix) - 1]["end"]:
					print("Le match N°" + str(choix) + " est cloturé")
				else:
					self.addResult(current_tournois, roundId, int(choix) - 1)

	def addResult(self, current_tournois, roundId, matchId):
		matchDict = current_tournois["listTour"][roundId]
		match = matchDict["tour"][matchId]
		tc = TournoisControleurs()
		pc = printCustome()
		while True:
			pc.printText("Entrez ''0'' si le résultat du macht est nul")
			pc.printText("Entrez ''1'' si " + str(tc.getPlayerByID(match["match"][0])["firstname"]) + " " + str(tc.getPlayerByID(match["match"][0])["lastname"]) + " a ganié")
			pc.printText("Entrez ''2'' si " + str(tc.getPlayerByID(match["match"][1])["firstname"]) + " " + str(tc.getPlayerByID(match["match"][1])["lastname"]) + " a ganié")
			choix = input().strip().lower()
			if choix == "menu":
				break
			elif choix.isnumeric():
				if int(choix) == 0 or int(choix) == 1 or int(choix) == 2:
					if choix == "0":
						match["score"][0] = 0.5
						match["score"][1] = 0.5
					if choix == "1":
						match["score"][0] = 1
						match["score"][1] = 0
					if choix == "2":
						match["score"][0] = 0
						match["score"][1] = 1
					pc.printText("match : ''" + str(matchId) + "''\n" + str(tc.getPlayerByID(match["match"][0])["firstname"]) + " vs " + str(tc.getPlayerByID(match["match"][1])["firstname"]))
					print("Score : " + str(match["score"][0]) + " " + str(match["score"][1]) + "\t\t" + " Statut " + ("Terminé" if match["end"] else "En cours") + "\n\n")
					print("Vous souhaitez concerver ces données et cloturer le matche ?\nEntrez ''Oui'' ou ''Non''")
					choix = input().strip().lower()
					if choix == "menu":
						break
					if choix == "oui" or choix == "o":
						tc.closeMatch(current_tournois, matchDict, match)
						print("Match cloturé\n")
						break
					if choix == "non" or choix == "n":
						continue
			else:
				pc.printText("\nEntrez un chiffre de 0 à 2")
				continue