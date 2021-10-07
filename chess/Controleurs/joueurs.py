from chess.Models.joueurs import JoueursModels
import re

class JoueursControleurs:
    
    def add(self, lastname, firstname, birthDate, sexe, classement):
        regexName = re.compile(r"^[a-z ,.'-]+$", re.IGNORECASE)
        regexBirthDate = re.compile(r"(0[1-9]|1[0-9]|2[0-9]|3[01]).(0[1-9]|1[012]).[0-9]{4}")
        regexSexe = re.compile(r"^(\s)*?[m|M|F|f](\s)*?$")
        verifLastname = regexName.search(lastname) is not None
        verifFistname = regexName.search(firstname) is not None
        verifBirthDate = regexBirthDate.search(birthDate) is not None
        verifSexe = regexSexe.search(sexe) is not None
        verifclassement =  isinstance(classement, float) or isinstance(classement, int) or classement.isnumeric()
        verif = verifLastname and verifFistname and verifBirthDate and verifSexe and verifclassement
        print(verifLastname, verifFistname, verifBirthDate, verifSexe, verifclassement)

        if verif:
            newJoueur = JoueursModels(lastname, firstname, birthDate, sexe, classement)
            return True
        else:
            return False
