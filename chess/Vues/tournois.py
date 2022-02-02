from chess.Controleurs.tournois import TournoisControleurs
from chess.Vues.joueurs import JoueursVues
from chess.Vues.printText import printCustome


class TournoisVues:
    def addPlayerTournois(self):
        """Cette fonction permet d'ajouter les 8 joueur du tornois

        Returns:
            [list]: [les 8 ID sont retournés dans une list]
            [int]: [0 si l'utilisateur veut retourné au menu]
        """
        pc = printCustome()
        list_joueurs_tournois = []
        for i in range(8):
            while True:
                pc.printText("Pour retourner au menu principal, entrez ''menu''\
                    joueur n° " + str(i + 1) + "\nEntrez ''1'' pour ajouter l'ID d'un joueur\
                    \nEntrez ''2'' pour rechercher l'ID un joueur\
                    \nEntrez ''3'' pour afficher la liste complète\
                    \nEntrez ''4'' pour ajouté un nouveau joueur à la base de donnée")
                choix = pc.inputClearScreen()
                if choix == "menu":
                    return 0
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
                    idJoueur = pc.inputClearScreen()
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
        """Cette fontion est un formulaire de création de tournoi

        Returns:
            [bool]: [return false si l'utilisateur souhaite retourner au menu principal]
            [bool]: [return true si l'utilisateur complete tout le formulaire]
        """
        pc = printCustome()
        while True:
            pc.printText("Pour retourner au menu principal, entrez ''menu''\
                \nEntrez le nom du tournois")
            name = pc.inputClearScreen()
            if name == "menu":
                return False
            if not name:
                print("saisie incorrect")
            else:
                break
        while True:
            pc.printText("Pour retourner au menu principal, entrez ''menu''\
                \nEntrez le lieu du tournois")
            lieu = pc.inputClearScreen()
            if lieu == "menu":
                return False
            if not lieu:
                print("saisie incorrect")
            else:
                break
        pc.printText("Pour retourner au menu principal, entrez ''menu''\
            \nVous devez ajouter 8 joueurs")
        list_joueurs_tournois = self.addPlayerTournois()
        if not list_joueurs_tournois:
            return False
        while True:
            pc.printText("Pour retourner au menu principal, entrez ''menu''\
                \nEntrez ''1'' pour un tournois du type 'bullet'\
                \nEntrez ''2'' pour un tournois du type 'blitz'\
                \nEntrez ''3'' pour un tournois du type 'coup rapide'")
            typeTournoisInput = pc.inputClearScreen()
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
            pc.printText("Pour retourner au menu principal, entrez ''menu''\
                \nEntrez le nombre de tours, entre ''4'' nim et ''7'' max")
            nbTours = pc.inputClearScreen()
            tc = TournoisControleurs()
            if nbTours == "menu":
                return False
            if tc.testRoundTournois(nbTours):
                break
            else:
                pc.printText("Entrez un chiffre de 4 à 7")
        while True:
            pc.printText("Pour retourner au menu principal, entrez ''menu''\
                \nEntrez la description du tournois")
            description = pc.inputClearScreen()
            if description == "menu":
                return False
            if not description:
                print("saisie incorrect")
            else:
                break
        tc.add(name, lieu, list_joueurs_tournois, typeTournois, int(nbTours), description)
        return True

    def backMenu(self):
        """Cette fonction évite la répétion des options de retours
        """
        pc = printCustome()
        pc.printText("Entrez ''menu'' pour retourner au menu principal\
            \nEntrez ''back'' pour retourner en arrière")

    def listTournoisDisplay(self):
        """Affiche la liste des tournois et interroge l'utilisateur.
        Si l'utilisateur entre l'id d'un tournoi displayAllRound() est appelée
        """
        pc = printCustome()
        pc.printText('\n')
        tc = TournoisControleurs()
        tab = tc.tournois_all()
        while True:
            newTable = [["N°", "Nom", "Lieu", "Date de début", "date de fin"]]
            for tournois in tab:
                newTable.append([
                    "''" + str(tournois.doc_id) + "''",
                    tournois["name"],
                    tournois["lieu"],
                    tournois["dataTournois"],
                    tournois["dateFinTournois"]
                ])
            pc.printTable(newTable)
            pc.printText("Entrez le numéro du tournoi que vous souhaitez sélectionner\
                \nEntrez ''menu'' pour retourner au menu principal")
            choix = pc.inputClearScreen()
            res = 2
            if choix == 'menu':
                break
            if choix.isnumeric():
                current_tournois = tc.selectTournoix(choix)
                if current_tournois == 0:
                    pc.printText("Le tournois N°" + choix + " n'est pas dans la base de donnée")
                else:
                    res = self.displayAllRound(current_tournois)
            if res == 0:
                break

    def displayAllRound(self, current_tournois):
        """Si le tournoi n'est pas initialisé (création des "infoJoueur") initialisation est lancé.
        Si il n'y a pas de rounde en cours et que le tournoi n'est pas fini le user peut lancer le prochain round
        avec l'option 'next'.
        Le user peut affiche le score avec l'option 'score'

        Args:
            current_tournois ([dict])

        Returns:
            [int]: [0 pour retourner au menu principale, 1 pour retourne au menu précédent]
        """
        pc = printCustome()
        tc = TournoisControleurs()
        while True:
            self.backMenu()
            if current_tournois['currentTour'] == 0:
                tc.tournoisSuisse(current_tournois)
            print(current_tournois["name"])
            print(current_tournois["lieu"], '\n')
            for round in current_tournois["listTour"]:
                pc.printText(
                    "Tour ''" + str(round["id"]) + "''\n" + round["startTime"] + " " +
                    (round["endTime"] if round["tourEnd"] else "En cours"))
            if current_tournois['currentTour'] != 1:
                print("Entrez le numéro du tour que vous souhaitez séletionner\n")
            if current_tournois['currentTour'] > 0:
                pc.printText("Entrez ''score'' pour afficher le classement")
            if tc.testNextRound(current_tournois):
                pc.printText("Entrez ''next'' pour lancer le tour suivant")
            choix = pc.inputClearScreen()
            res = 2
            if choix == "next" and tc.testNextRound(current_tournois):
                tc.tournoisSuisse(current_tournois)
            if choix == "score" and current_tournois['currentTour'] > 0:
                res = self.displayScore(current_tournois)
            if choix.isnumeric():
                if int(choix) <= len(current_tournois["listTour"]) and int(choix) >= 1:
                    res = self.displayRound(current_tournois, int(choix) - 1)
            if choix == "menu" or res == 0:
                return 0
            if res == 1:
                continue
            if choix == "back":
                return 1

    def displayScore(self, current_tournois):
        """Affiche un tableau trie des joueurs du tournoi

        Args:
            current_tournois ([dict])
        """
        pc = printCustome()
        tc = TournoisControleurs()
        listInfo = tc.getListPlayer(current_tournois)
        newTable = [["Position", "Nom", "Prénom", "Date de naissance", "Sexe", "Classeement", "Score", "N°"]]
        i = 0
        for info in listInfo:
            player = tc.getPlayerByID(info['id'])
            i += 1
            newTable.append([str(i), player['lastname'], player["firstname"], player["birthDate"], player["sexe"],
                            str(player["classement"]), str(info["point"]), "''" + str(player.doc_id) + "''"])
        pc.printTable(newTable)

    def displayRound(self, current_tournois, roundId):
        """Affche les matchs du round passé en paramètre

        Args:
            current_tournois ([dict])
            roundId ([int])

        Returns:
            [int]: [0 pour retourner au menu principale, 1 pour retourne au menu précédent]
        """
        matchDict = current_tournois["listTour"][roundId]
        menu = False
        pc = printCustome()
        tc = TournoisControleurs()
        while not menu:
            i = 1
            self.backMenu()
            print(current_tournois["name"])
            print(current_tournois["lieu"])
            for match in matchDict["tour"]:
                player1 = str(tc.getPlayerByID(match["match"][0][0])["firstname"]).capitalize()
                player2 = str(tc.getPlayerByID(match["match"][1][0])["firstname"]).capitalize()
                pc.printText("match : ''" + str(i) + "''\n" + player1 + " vs " + player2)
                print("Score : " + str(match["match"][0][1]) + " " + str(match["match"][1][1]) + "\t\t" + " \
                    Statut " + ("Terminé" if match["end"] else "En cours") + "\n\n")
                i += 1
            if not matchDict['tourEnd']:
                print("Entrez le numéro du match que vous souhaitez cloturé\n")
            choix = pc.inputClearScreen()
            res = 2
            if choix.isnumeric():
                if int(choix) <= len(matchDict["tour"]) and int(choix) >= 1:
                    if matchDict["tour"][int(choix) - 1]["end"]:
                        print("Le match N°" + str(choix) + " est cloturé")
                    else:
                        res = self.addResult(current_tournois, roundId, int(choix) - 1)
            if choix == "menu" or res == 0:
                return 0
            if res == 1:
                continue
            if choix == "back":
                return 1

    def addResult(self, current_tournois, roundId, matchId):
        """Affiche la liste des options de cloturations du match

        Args:
            current_tournois ([dict])
            roundId ([int])
            matchId ([int])

        Returns:
            [int]: [0 pour retourner au menu principale, 1 pour retourne au menu précédent]
        """
        matchDict = current_tournois["listTour"][roundId]
        match = matchDict["tour"][matchId]
        tc = TournoisControleurs()
        pc = printCustome()
        while True:
            self.backMenu()
            player1Fname = str(tc.getPlayerByID(match["match"][0][0])["firstname"]).capitalize()
            player1Lname = str(tc.getPlayerByID(match["match"][0][0])["lastname"]).upper()
            player2Fname = str(tc.getPlayerByID(match["match"][1][0])["firstname"]).capitalize()
            player2Lname = str(tc.getPlayerByID(match["match"][1][0])["lastname"]).upper()
            pc.printText("Entrez ''0'' si le résultat du macht est nul")
            pc.printText("Entrez ''1'' si " + player1Fname + " " + player1Lname + " a ganié")
            pc.printText("Entrez ''2'' si " + player2Fname + " " + player2Lname + " a ganié")
            choix = pc.inputClearScreen()
            if choix == "menu":
                return 0
            if choix == "back":
                return 1
            elif choix.isnumeric():
                if int(choix) == 0 or int(choix) == 1 or int(choix) == 2:
                    if choix == "0":
                        match["match"][0][1] = 0.5
                        match["match"][1][1] = 0.5
                    if choix == "1":
                        match["match"][0][1] = 1
                        match["match"][1][1] = 0
                    if choix == "2":
                        match["match"][0][1] = 0
                        match["match"][1][1] = 1
                    pc.printText("match : ''" + str(matchId) + "''\n" + player1Fname + " vs " + player2Fname)
                    print(
                        "Score : " + str(match["match"][0][1]) + " " + str(match["match"][1][1]) + "\t\t" +
                        " Statut " + ("Terminé" if match["end"] else "En cours") + "\n\n")
                    print("Vous souhaitez concerver ces données et cloturer le matche ?\
                            \nEntrez ''Oui'' ou ''Non''")
                    choix = pc.inputClearScreen()
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
