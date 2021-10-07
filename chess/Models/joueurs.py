from tinydb import TinyDB, Query
from pprint import pprint

class JoueursModels:
    def create(self, lastname, firstname, birthDate, sexe, classement):
        db = TinyDB('/bdd/db.json')
        Joueurs = db.table('Joueurs')
        self.lastname = lastname.capitalize()
        self.firstname = firstname.capitalize()
        self.birthDate = birthDate
        self.sexe = sexe.capitalize()
        self.classement = int(classement)
        Joueurs.insert({'lastname': self.lastname, 'firstname': self.firstname, 'birthDate' : self.birthDate, 'sexe' : self.sexe, 'classement' : self.classement})
        
    
    def update(self, lastname = "", firstname = "", birthDate = "", sexe = "", classement = ""):
        self.lastname = lastname or self.lastname
        self.firstname = firstname or self.firstname
        self.birthDate = birthDate or self.birthDate
        self.sexe = sexe or self.sexe
        self.classement = classement or self.classement
        