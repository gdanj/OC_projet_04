from tinydb import TinyDB


class TournoisModels:
    def tournoisDB(self):
        """Retourne la table Tournois

        Returns:
            [dict]
        """
        db = TinyDB('chess/Models/bdd/db.json')
        return db.table('Tournois')

    def playerDB(self):
        """Retourne la table Joueurs

        Returns:
            [dict]
        """
        db = TinyDB('chess/Models/bdd/db.json')
        return db.table('Joueurs')

    def allTournois(self):
        """Retourne la liste des tournois

        Returns:
            [list]
        """
        Tournois = self.tournoisDB()
        return Tournois.all()

    def updateTournoisDB(self, current_tournois, key):
        """met à jour élément

        Args:
            current_tournois ([dict]): [nouvelle information]
            key ([str]): [cle de information mise à jour]
        """
        tournoisTable = self.tournoisDB()
        id = current_tournois.doc_id
        tournoisTable.update({key: current_tournois[key]}, doc_ids=[id])

    def getTime(self, pattern):
        """Retourne la date et l'heure en fonction du pattern

        Args:
            pattern ([str]): [correspond au format de la date/heur demandé]

        Returns:
            [str]: [date/heur]
        """
        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime(pattern)
        return dt_string

    def create(self, name, lieu, list_joueurs_tournois, typeTournois, nbTours, description):
        """Un nouveau tournoi est créé avec les informations passé en paramètre

        Args:
            name ([str])
            lieu ([str])
            list_joueurs_tournois ([list])
            typeTournois ([str])
            nbTours ([int])
            description ([str])
        """
        Tournois = self.tournoisDB()
        self.name = name.capitalize()
        self.lieu = lieu.capitalize()
        d1 = self.getTime("%d/%m/%Y")
        self.dateDebutTournois = d1
        self.dateFinTournois = "En cours"
        self.list_joueurs_tournois = list_joueurs_tournois
        self.typeTournois = typeTournois.capitalize()
        self.nbTours = nbTours
        self.description = description
        Tournois.insert({
            'name': self.name,
            'lieu': self.lieu,
            'dataTournois': self.dateDebutTournois,
            'dateFinTournois': self.dateFinTournois,
            'list_joueurs_tournois': self.list_joueurs_tournois,
            'listTour': [],
            'infoJoueur': [],
            'typeTournois': self.typeTournois,
            'nbToursMax': self.nbTours,
            'currentTour': 0,
            'description': self.description
        })

    def tourInit(self, current_tournois, tab_joueur):
        """Met à jour les informations du tournois, chaque joueur disposera d'informations sur son classement,
        son historique des adversaires et les points obtenus

        Args:
            current_tournois ([dict])
            tab_joueur ([list])
        """
        joueurTable = self.playerDB()
        for joueur_id in tab_joueur:
            current_tournois['infoJoueur'].append({
                'id': joueur_id,
                'classement': joueurTable.get(doc_id=int(joueur_id))['classement'],
                'point': 0,
                "history": []
            })
        current_tournois['currentTour'] += 1
        self.updateTournoisDB(current_tournois, 'infoJoueur')
        self.updateTournoisDB(current_tournois, 'currentTour')

    def listPlayerSort(self, current_tournois):
        """retourne la list des infojoueur trié

        Args:
            current_tournois (dict)

        Returns:
            [list]: [infoJoueur trie]
        """
        tab = [[dict_['classement'], dict_] for dict_ in list(current_tournois['infoJoueur'])]
        tab2 = [dict_['classement'] for dict_ in list(current_tournois['infoJoueur'])]
        tab2.sort(reverse=True)
        result = []
        for nbr in tab2:
            for t in tab:
                if nbr == t[0]:
                    if not t[1] in result:
                        result.append(t[1])
        return result

    def firstRound(self, current_tournois):
        """réparti les joueurs pour le premier tour du tournois Suisse et met à jour 'infoJoueur' et 'listTour'

        Args:
            current_tournois ([dict])
        """
        result = self.listPlayerSort(current_tournois)
        dt_string = self.getTime("%d/%m/%Y %H:%M")
        current_tournois['listTour'].append({
            "id": 1,
            "tour": [
                {"match": ([result[0]['id'], 0], [result[4]['id'], 0]), "end": False},
                {"match": ([result[1]['id'], 0], [result[5]['id'], 0]), "end": False},
                {"match": ([result[2]['id'], 0], [result[6]['id'], 0]), "end": False},
                {"match": ([result[3]['id'], 0], [result[7]['id'], 0]), "end": False}
            ],
            "startTime": dt_string,
            "endTime": "",
            "tourEnd": False
        })
        self.updateTournoisDB(current_tournois, 'infoJoueur')
        self.updateTournoisDB(current_tournois, 'listTour')

    def cleanTour(self, tour):
        """remplie la list de zero à partir du premier zero
        Args:
            tour ([list])

        Returns:
            [list]
        """
        i = 0
        zero = False
        while i < len(tour):
            if zero:
                tour[i] = 0
            if tour[i] == 0:
                zero = True
            i += 1
        return tour

    def backtrackingSuisse(self, infoJoueur, tabId, tour, i):
        """reparti les joueurs avec les joueurs les plus fort contre lequel il n'ont pas encore joué.
        les joueur

        Args:
            infoJoueur ([list])
            tabId ([list]): [la list des id des joueurs du tournoi en partant du meilleur]
            tour ([list]): [list de 8 zeros]
            i ([int]): [compteur]

        Returns:
            [list]: [list des id. Le premier jouera contre le deuxieme, le troixieme contre le quatrieme...]
        """
        test = False
        for id in tabId:
            if id not in tour:
                tour[i] = id
                if (i + 1) % 2 == 0:
                    for info in infoJoueur:
                        if tour[i] == info["id"]:
                            if tour[i - 1] in info["history"]:
                                tour[i] = 0
                                tour = self.cleanTour(tour)
                                i += -1
                            else:
                                if tour[7] == 0:
                                    test = self.backtrackingSuisse(infoJoueur, tabId, tour, i + 1)
                                    if isinstance(test, list):
                                        return test
                                    else:
                                        tour[i] = 0
                                        tour = self.cleanTour(tour)
                                        i += -1
                                else:
                                    return tour
                            break
                i += 1
        return False

    def closeMatchUpdate(self, current_tournois):
        """cloture le tour actuelle

        Args:
            current_tournois ([type])
        """
        current_tournois['listTour'][current_tournois['currentTour'] - 1]['endTime'] = self.getTime("%d/%m/%Y %H:%M")
        current_tournois['currentTour'] += 1
        self.updateTournoisDB(current_tournois, 'currentTour')
        self.updateTournoisDB(current_tournois, 'listTour')
        self.updateInfoJoueur(current_tournois)

    def listSortPlayer(self, current_tournois):
        """Trie les joueurs par leurs 'point' puis effectu un trie a bull de l'heur classement si ils
        ont le même nombre de point

        Args:
            current_tournois ([dict])

        Returns:
            [list]: [trie par point puis par classement]
        """
        result = sorted(current_tournois['infoJoueur'], key=lambda x: x['point'], reverse=True)
        i = 0
        while i < 7:
            if result[i]['point'] == result[i + 1]['point'] and result[i]['classement'] < result[i + 1]['classement']:
                swap = result[i]
                result[i] = result[i + 1]
                result[i + 1] = swap
                i = -1
            i += 1
        return result

    def tourNextSort(self, current_tournois):
        """Lance le prochain tour, les 'infoJoueur' sont mise à jour puis la methode de backtracking
        retourn une list de joueur, le premier est matché contre le deuxième...
        Les informations du nouveau tour sont ajoutées à 'listTour'

        Args:
            current_tournois ([dict])
        """
        current_tournois['infoJoueur'] = self.listSortPlayer(current_tournois)
        tabId = [dict_['id'] for dict_ in current_tournois['infoJoueur']]
        tour = [0, 0, 0, 0, 0, 0, 0, 0]
        i = 0
        tour = self.backtrackingSuisse(current_tournois['infoJoueur'], tabId, tour, i)
        listTour = [
                {"match": ([tour[0], 0], [tour[1],  0]), "end": False},
                {"match": ([tour[2], 0], [tour[3],  0]), "end": False},
                {"match": ([tour[4], 0], [tour[5],  0]), "end": False},
                {"match": ([tour[6], 0], [tour[7],  0]), "end": False}
            ]
        dt_string = self.getTime("%d/%m/%Y %H:%M")
        current_tournois['listTour'].append({
            "id": current_tournois['currentTour'],
            "tour": listTour,
            "startTime": dt_string,
            "endTime": "",
            "tourEnd": False
        })
        self.updateTournoisDB(current_tournois, 'infoJoueur')
        self.updateTournoisDB(current_tournois, 'listTour')

    def lastround(self, current_tournois):
        """Cloture le tournoi

        Args:
            current_tournois ([dict])
        """
        current_tournois['dateFinTournois'] = self.getTime("%d/%m/%Y")
        self.updateTournoisDB(current_tournois, 'dateFinTournois')
        self.updateInfoJoueur(current_tournois)

    def updateInfoJoueur(self, current_tournois):
        """met à jour les informations des jours

        Args:
            current_tournois ([dict])
        """
        matchList = current_tournois["listTour"][-1]["tour"]
        infoJoueurList = current_tournois["infoJoueur"]
        for match in matchList:
            for i in range(8):
                if match["match"][0][0] == infoJoueurList[i]["id"]:
                    infoJoueurList[i]["point"] += match["match"][0][1]
                    infoJoueurList[i]["history"].append(match["match"][1][0])
                if match["match"][1][0] == infoJoueurList[i]["id"]:
                    infoJoueurList[i]["point"] += match["match"][1][1]
                    infoJoueurList[i]["history"].append(match["match"][0][0])
        self.updateTournoisDB(current_tournois, 'infoJoueur')
