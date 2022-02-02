from chess.Models.tournois import TournoisModels


class TournoisControleurs:
    def add(self, name, lieu, list_joueurs_tournois, typeTournois, nbTours, description):
        """ transmet les variables au model en vérifiant si les variables sont
        Args:
            name ([str])
            lieu ([str])
            list_joueurs_tournois ([str])
            strTournois ([str])
            nbTours ([str])
            description ([str])

        Returns:
            [bool]
        """
        verif = name and lieu and list_joueurs_tournois and typeTournois and nbTours and description
        if verif:
            tm = TournoisModels()
            tm.create(name, lieu, list_joueurs_tournois, typeTournois, nbTours, description)
            return True
        else:
            return False

    def tournois_all(self):
        """envoie une requette pour le model retourne la liste de tournois

        Returns:
            [liste]
        """
        tm = TournoisModels()
        return tm.allTournois()

    def getPlayerByID(self, id):
        """retourne le joueur correspondant à id

        Args:
            id ([int])

        Returns:
            [dict]
        """
        tm = TournoisModels()
        joueurTable = tm.playerDB()
        return joueurTable.get(doc_id=id)

    def testTypeTournois(self, typeTournois):
        """retourne le type de tournois ou 0

        Args:
            typeTournois ([int])

        Returns:
            [str]: [si typeTournois correspond à 1 2 ou 3 sinon retourne zero]
        """
        if typeTournois.isnumeric():
            nbrTypeTournois = int(typeTournois)
            if 1 <= nbrTypeTournois and nbrTypeTournois <= 3:
                if nbrTypeTournois == 1:
                    return "bullet"
                elif nbrTypeTournois == 2:
                    return "blitz"
                elif nbrTypeTournois == 3:
                    return "coup rapide"
        return 0

    def testRoundTournois(self, nbTours):
        """ si nbtour correspond à 4 5 6 ou 7 retourne true sinon retourne false
        Args:
            nbTours ([int])

        Returns:
            [bool]
        """
        if nbTours.isnumeric():
            nbr = int(nbTours)
            if 4 <= nbr and nbr <= 7:
                return True
        return False

    def testJoueursInBDD(self, idJoueur, list_joueurs_tournois):
        """ ajoute l'id du joueur a la liste si il n'y est pas déjà et si il est dans la BDD


        Args:
            idJoueur ([int])
            list_joueurs_tournois ([list])

        Returns:
            [int]: [0 si le joueur a été ajouté, 1 si il est déjà dans la liste, 2 si il n'est pas dans la BDD]
        """
        tm = TournoisModels()
        joueurTable = tm.playerDB()
        if joueurTable.contains(doc_id=int(idJoueur)):
            if int(idJoueur) in list_joueurs_tournois:
                return 1
            else:
                list_joueurs_tournois.append(int(idJoueur))
        else:
            return 2
        return 0

    def closeMatch(self, current_tournois, matchDict, match):
        """cloture le match et si tout les match du tour sont terminé, current_tournois est MAJ

        Args:
            current_tournois ([dict])
            matchDict ([dict]): [c'est le tour]
            match ([dict])
        """
        tm = TournoisModels()
        match["end"] = True
        tm.updateTournoisDB(current_tournois, 'listTour')
        matchDict["tourEnd"] = matchDict["tour"][0]["end"] and matchDict["tour"][1]["end"] \
            and matchDict["tour"][2]["end"] and matchDict["tour"][3]["end"]
        if matchDict["tourEnd"]:
            c = current_tournois
            tm.closeMatchUpdate(current_tournois)
            if int(c['currentTour']) > int(c['nbToursMax']) and c['listTour'][-1]["tourEnd"]:
                if (c['dateFinTournois'] == "En cours"):
                    tm.lastround(c)
                    from datetime import date
                    today = date.today()
                    c['dateFinTournois'] = today.strftime("%d/%m/%Y")
                    tm.updateTournoisDB(c, 'dateFinTournois')

    def selectTournoix(self, choix):
        """Test le choix de l'utilisateur, si le choix exite dans la BDD retourne

        Args:
            choix ([str]): [c'est l'id du tournois recherché]

        Returns:
            [type]: [description]
        """
        tm = TournoisModels()
        tournoisTable = tm.tournoisDB()
        if tournoisTable.contains(doc_id=int(choix)):
            current_tournois = tournoisTable.get(doc_id=int(choix))
            return current_tournois
        else:
            return 0

    def testNextRound(seft, current_tournois):
        """

        Args:
            seft ([type]): [description]
            current_tournois ([type]): [description]

        Returns:
            [type]: [description]
        """
        if current_tournois['currentTour'] == 0 or current_tournois['currentTour'] == 1:
            return True
        lastRoundEnd = current_tournois['listTour'][-1]["tourEnd"]
        return int(current_tournois['currentTour']) <= int(current_tournois['nbToursMax']) and lastRoundEnd

    def getListPlayer(self, current_tournois):
        """retourne la liste des joueurs trié

        Args:
            current_tournois ([dict])

        Returns:
            [list]
        """
        tm = TournoisModels()
        return tm.listSortPlayer(current_tournois)

    def tournoisSuisse(self, current_tournois):
        """initialise le tornois, actualise les tours et cluture le tournoi

        Args:
            current_tournois ([dict])
        """
        tm = TournoisModels()
        tab_joueur = current_tournois["list_joueurs_tournois"]
        if current_tournois['currentTour'] == 0:
            tm.tourInit(current_tournois, tab_joueur)
        elif current_tournois['currentTour'] == 1 and current_tournois['listTour'] == []:
            tm.firstRound(current_tournois)
        elif int(current_tournois['currentTour']) <= int(current_tournois['nbToursMax']) \
                and current_tournois['listTour'][-1]["tourEnd"]:
            tm.tourNextSort(current_tournois)
