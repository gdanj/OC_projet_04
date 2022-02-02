from prettytable import PrettyTable


class printCustome:
    def addColor(self, text):
        """Ajout la couleur blue au text en ''

        Args:
            text ([str])

        Returns:
            [str]
        """
        BLUE = '\033[34m'
        RESET = '\033[0m'  # mode 0  = reset
        listText = text.split("''")
        result = ""
        for i in range(len(listText)):
            if i % 2 != 0:
                result += BLUE + listText[i] + RESET
            else:
                result += listText[i]
        return result

    def printText(self, text):
        """print le text

        Args:
            text ([str])
        """
        result = self.addColor(text)
        print(result)

    def printTable(self, table):
        """imprime un table appartir d'une liste de liste

        Args:
            table ([list list])
        """
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
        """ajoute du vide à l'écran

        Returns:
            [str]
        """
        choice = input().strip().lower()
        CLEAR_SCREEN = '\033[2J'
        print(CLEAR_SCREEN)
        return choice
