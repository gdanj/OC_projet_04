from chess.Vues.joueurs import JoueursVues
from chess.Vues.tournois import TournoisVues
from chess.Vues.printText import printCustome

newJoueurs = JoueursVues()
newTournois = TournoisVues()

def menu():
	pc = printCustome()
	while True:
		print('\033[2J')
		pc.printText("Entrez ''1'' pour afficher la liste des joueur")
		pc.printText("Entrez ''2'' pour ajouter un joueur")
		pc.printText("Entrez ''3'' pour créer un tournois")
		pc.printText("Entrez ''4'' afficher la liste des tournois")
		pc.printText("Entrez ''exit'' pour quitter le programme")
		commande = input()
		if commande == '1':
			newJoueurs.listJoueurDisplay()
		if commande == '2':
			newJoueurs.formAddJoueur()
		if commande == '3':
			newTournois.formAddTournois()
		if commande == '4':
			newTournois.listTournoisDisplay()
		if commande == 'exit':
			break
menu()