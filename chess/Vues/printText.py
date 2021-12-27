from prettytable import PrettyTable

class printCustome:

	def addColor(self, text):
		CLEAR_SCREEN = '\033[2J'
		RED = '\033[34m'   # mode 31 = red forground
		RESET = '\033[0m'  # mode 0  = reset
		listText = text.split("''")
		result = ""
		for i in range(len(listText)):
			if i % 2 != 0:
				result += RED + listText[i] + RESET
			else:
				result += listText[i]
		return result

	def printText(self, text):
		result = self.addColor(text)
		print(result)

	def printTable(self, table):
		newTable = PrettyTable()
		newTable.field_names = table[0]
		for i in range(1, len(table)):
			tabTable = []
			for text in table[i]:
				tabTable.append(self.addColor(text))
			newTable.add_row(tabTable)
		print(newTable)
		print('\n\n\n')

	def inputClearScreen(self):
		choice = input().strip().lower()
		CLEAR_SCREEN = '\033[2J'
		print(CLEAR_SCREEN)
		return choice