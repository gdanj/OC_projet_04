from chess.Models.joueurs import JoueursModels
import re

class JoueursControleurs:
		
	def add(self, lastname, firstname, birthDate, sexe, classement):
		jm = JoueursModels()
		jm.create(lastname, firstname, birthDate, sexe, classement)
		
	def testName(self, name):
		regexName = re.compile(r"^[a-z ,.'-]+$", re.IGNORECASE)
		verifName = regexName.search(name) is not None
		return verifName
		
	def testDate(self, date):
		regexDate = re.compile(r"(0[1-9]|1[0-9]|2[0-9]|3[01]).(0[1-9]|1[012]).[0-9]{4}")
		verifDate = regexDate.search(date) is not None
		return verifDate
		
	def testSexe(self, sexe):
		regexSexe = re.compile(r"^(\s)*?[m|M|F|f](\s)*?$")
		verifSexe = regexSexe.search(sexe) is not None
		return verifSexe
		
	def testClassement(self, string):
		return string.isnumeric()

	def	getPlayerByID(self, id):
		jm = JoueursModels()
		joueurTable = jm.playerDB()
		return joueurTable.get(doc_id=id)

	def testJoueursInBDD(self, idJoueur):
		jm = JoueursModels()
		joueurTable = jm.playerDB()
		if joueurTable.contains(doc_id=int(idJoueur)):
			return True
		return False

	def joueur_all(self):
		listJoueur = JoueursModels()
		return listJoueur.allJoueur()

	def joueurUpdate(self, nbrClassement, id):
		jm = JoueursModels()
		jm.update(nbrClassement, id)