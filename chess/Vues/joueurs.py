from chess.Controleurs.joueurs import JoueursControleurs

class JoueursVues:
    def formAddJoueur(self):
        print("Entrez le nom du joueur")
        lastname = input()
        print("Entrez le prénom du joueur")
        firstname = input()
        print("Entrez la date de naissance du joueur au format 'dd/mm/aaaa'")
        birthDate = input()
        print("Entrez le genre du joueur,\n'M' pour masculin \n'F' pour féminin")
        sexe = input()
        print("Entrez le classement du joueur")
        classement = input()
        print(lastname, firstname, birthDate, sexe, classement)
        newJoueur = JoueursControleurs()
        print(lastname, firstname, birthDate, sexe, classement)
        newJoueur.add(lastname, firstname, birthDate, sexe, classement)
