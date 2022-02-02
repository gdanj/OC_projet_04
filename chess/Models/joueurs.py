from tinydb import TinyDB


class JoueursModels:
    def create(self, lastname, firstname, birthDate, sexe, classement):
        """Ajoute l'utilisateur à la base de donnée

        Args:
            lastname ([str])
            firstname ([str])
            birthDate ([str])
            sexe ([str])
            classement ([str])
        """
        db = TinyDB('chess/Models/bdd/db.json')
        Joueurs = db.table('Joueurs')
        self.lastname = lastname.capitalize()
        self.firstname = firstname.capitalize()
        self.birthDate = birthDate
        self.sexe = sexe.capitalize()
        self.classement = int(classement)
        Joueurs.insert({
            'lastname': self.lastname,
            'firstname': self.firstname,
            'birthDate': self.birthDate,
            'sexe': self.sexe,
            'classement': self.classement
            })

    def last(self):
        """retourne le dernier joueur en base

        Returns: [dict]
        """
        db = TinyDB('chess/Models/bdd/db.json')
        Joueurs = db.table('Joueurs')
        return Joueurs.get(doc_id=len(Joueurs))

    def allJoueur(self):
        """Retourne la liste des joueur

        Returns:
            [list]: [les joueur seront trié par id]
        """
        db = TinyDB('chess/Models/bdd/db.json')
        Joueurs = db.table('Joueurs')
        return Joueurs.all()

    def playerDB(self):
        """retourne la table joueur

        Returns: [dict]
        """
        db = TinyDB('chess/Models/bdd/db.json')
        return db.table('Joueurs')

    def update(self, nbrClassement, id):
        """Met à jour la base de donnée du classement de l'utilisateur

        Args:
            nbrClassement ([int]): [nouveau classement]
            id ([int])
        """
        db = TinyDB('chess/Models/bdd/db.json')
        Joueurs = db.table('Joueurs')
        Joueurs.update({'classement': nbrClassement}, doc_ids=[id])
