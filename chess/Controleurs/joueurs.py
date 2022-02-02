from chess.Models.joueurs import JoueursModels
import re


class JoueursControleurs:
    def add(self, lastname, firstname, birthDate, sexe, classement):
        """ Envoie les info au model pour creer un nouveau joueur

        Args:
            lastname ([str])
            firstname ([str])
            birthDate ([str])
            sexe ([str])
            classement ([str])
        """
        jm = JoueursModels()
        jm.create(lastname, firstname, birthDate, sexe, classement)

    def testName(self, name):
        """Test le nom passé en parametre correspond à un nom

        Args:
            name ([str]): [nom ou prénom]

        Returns:
            [bool]
        """
        regexName = re.compile(r"^[a-z ,.'-]+$", re.IGNORECASE)
        verifName = regexName.search(name) is not None
        return verifName

    def testDate(self, date):
        """Test le format de la date passée en parametre, format testé dd/mm/yyyy

        Args:
            date ([str])

        Returns:
            [bool]
        """
        regexDate = re.compile(r"(0[1-9]|1[0-9]|2[0-9]|3[01]).(0[1-9]|1[012]).[0-9]{4}")
        verifDate = regexDate.search(date) is not None
        return verifDate

    def testSexe(self, sexe):
        """Test le format du sexe passé en parametre, 'm' ou 'f'

        Args:
            sexe ([str])

        Returns:
            [bool]: True est retourné si le format est respecté ou False dans la cas contraire
        """
        regexSexe = re.compile(r"^(\s)*?[m|M|F|f](\s)*?$")
        verifSexe = regexSexe.search(sexe) is not None
        return verifSexe

    def testClassement(self, classement):
        """ Test le format du classement passé en parametre

        Args:
            classement ([str])

        Returns:
            [bool]: retourn True si la chaine est numérique ou False dans la cas contraire
        """
        return classement.isnumeric()

    def getPlayerByID(self, id):
        """retourne le joueur qui à l'id passé en parametre

        Args:
            id ([int]): [id recherché]

        Returns:
            [dict]: [un dict avec les infos du joueur rechercher]
        """
        jm = JoueursModels()
        joueurTable = jm.playerDB()
        return joueurTable.get(doc_id=id)

    def testJoueursInBDD(self, idJoueur):
        """Test si id du joueur passé en parametre est bien de la base de donné

        Args:
            idJoueur ([int]): [id recherché]

        Returns:
            [bool]: [retourne True si id existe ou False dans la cas contraire]
        """
        jm = JoueursModels()
        joueurTable = jm.playerDB()
        if joueurTable.contains(doc_id=int(idJoueur)):
            return True
        return False

    def joueur_all(self):
        """Retourne la liste des joueurs en base de donnée

        Returns:
            [list]: [retourne une liste dict des joueurs dans l'ordre des id]
        """
        listJoueur = JoueursModels()
        return listJoueur.allJoueur()

    def joueurUpdate(self, nbrClassement, id):
        """Met a jour le classement du joueur possédant l'id

        Args:
            nbrClassement ([int]): [nouveu classement]
            id ([int]): [id joueur]
        """
        jm = JoueursModels()
        jm.update(nbrClassement, id)
