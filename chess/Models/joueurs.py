from tinydb import TinyDB

class JoueursModels:
	def create(self, lastname, firstname, birthDate, sexe, classement):
		db = TinyDB('chess/Models/bdd/db.json')
		Joueurs = db.table('Joueurs')
		self.lastname = lastname.capitalize()
		self.firstname = firstname.capitalize()
		self.birthDate = birthDate
		self.sexe = sexe.capitalize()
		self.classement = int(classement)
		Joueurs.insert({'lastname': self.lastname, 'firstname': self.firstname, 'birthDate' : self.birthDate, 'sexe' : self.sexe, 'classement' : self.classement})

	def last(self):
		db = TinyDB('chess/Models/bdd/db.json')
		Joueurs = db.table('Joueurs')
		return Joueurs.get(doc_id=len(Joueurs))

	def allJoueur(self):
		db = TinyDB('chess/Models/bdd/db.json')
		Joueurs = db.table('Joueurs')
		return Joueurs.all()

	def playerDB(self):
		db = TinyDB('chess/Models/bdd/db.json')
		return db.table('Joueurs')


	def update(self, nbrClassement, id):
		db = TinyDB('chess/Models/bdd/db.json')
		Joueurs = db.table('Joueurs')
		Joueurs.update({'classement': nbrClassement}, doc_ids=[id])
		