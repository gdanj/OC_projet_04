from chess.Vues.joueurs import JoueursVues
from chess.Vues.tournois import TournoisVues
from prettytable import PrettyTable  
import colorama
  
# Creating a new table   
newTable = PrettyTable(["Student Name", "Class", "Subject", "Makrs"])  
  
  

colorama.init()

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[34m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset

# Add rows  
newTable.add_row([RED + "Camron" + RESET, "X", "English", "91"])  
newTable.add_row(["Haris", "X", "Math", "63"])  
newTable.add_row(["Jenny", "X", "Science", "90"])  
newTable.add_row(["Bernald", "X", "Art", "92"])  
newTable.add_row(["Jackson", "X", "Science", "98"])  
newTable.add_row(["Samual", "X", "English", "88"])  
newTable.add_row(["Stark", "X", "English", "95"])  
print(newTable)  
newJoueurs = JoueursVues()
newTournois = TournoisVues()

def menu():
	while True:
		print("Entrez '1' pour afficher la liste des joueur")
		print("Entrez '2' pour ajouter un joueur")
		print("Entrez '3' pour créer un tournois")
		print("Entrez '4' afficher la liste des tournois")
		print("Entrez 'exit' pour quitter le programme")
		commande = input()
		if commande == '1':
			newJoueurs.listJoueurDisplay()
			print(colorama.ansi.clear_screen())
		if commande == '2':
			newJoueurs.formAddJoueur()
		if commande == '3':
			newTournois.formAddTournois()
		if commande == '4':
			newTournois.listTournoisDisplay()
		if commande == 'exit':
			break
menu()