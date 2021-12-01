from chess.Vues.joueurs import JoueursVues
from chess.Vues.tournois import TournoisVues

newJoueurs = JoueursVues()
newTournois = TournoisVues()

def menu():
	while True:
		print("Entrez '1' pour afficher la liste des joueur")
		print("Entrez '2' pour ajouter un joueur")
		print("Entrez '3' pour créer un tournois")
		print("Entrez 'exit' pour quitter le programme")
		commande = input()
		if commande == '1':
			newJoueurs.listJoueurDisplay()
		if commande == '2':
			newJoueurs.formAddJoueur()
		if commande == '3':
			newTournois.formAddTournois()
		if commande == 'exit':
			break
menu()