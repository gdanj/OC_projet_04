from prettytable import PrettyTable  
import colorama

class printCustome:

	def printText(self, text):
		"""Supprime fait un clean du shell et imprime 'text'"""
		# Creating a new table   
		newTable = PrettyTable(["Student Name", "Class", "Subject", "Makrs"])  
		
		

		colorama.init()

		# Now regular ANSI codes should work, even in Windows
		CLEAR_SCREEN = '\033[2J'
		RED = '\033[34m'   # mode 31 = red forground
		RESET = '\033[0m'  # mode 0  = reset

		# Add rows  
		"""newTable.add_row([RED + "Camron" + RESET, "X", "English", "91"])  
		newTable.add_row(["Haris", "X", "Math", "63"])  
		newTable.add_row(["Jenny", "X", "Science", "90"])  
		newTable.add_row(["Bernald", "X", "Art", "92"])  
		newTable.add_row(["Jackson", "X", "Science", "98"])  
		newTable.add_row(["Samual", "X", "English", "88"])  
		newTable.add_row(["Stark", "X", "English", "95"])  
		print(newTable)  """
		listText = text.split("''")
		result = ""
		for i in range(len(listText)):
			if i % 2 != 0:
				result += RED + listText[i] + RESET
			else:
				result += listText[i]
		print(result)