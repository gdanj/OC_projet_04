from chess.Vues.joueurs import JoueursVues
from chess.Vues.tournois import TournoisVues
from chess.Vues.printText import printCustome

newJoueurs = JoueursVues()
newTournois = TournoisVues()

def menu():
	pc = printCustome()
	print('\033[2J')
	while True:
		pc.printText("Entrez ''1'' pour afficher les options des joueur")
		pc.printText("Entrez ''2'' pour créer un tournois")
		pc.printText("Entrez ''3'' afficher la liste des tournois")
		pc.printText("Entrez ''exit'' pour quitter le programme")
		commande = pc.inputClearScreen()
		if commande == '1':
			newJoueurs.listPlayer()
		if commande == '2':
			newTournois.formAddTournois()
		if commande == '3':
			newTournois.listTournoisDisplay()
		if commande == 'exit':
			break
menu()