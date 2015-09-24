import all_strings
import riddle_game

class Menu(object):

    menu_options = ["1. New", "2. Load"]
    ingame_menu_options = ["1. New", "2. Save", "3. Load", "4. Continue"]
    menu = {1: ["Start a New Game", "new"], 2: ["Load Game", "load"]}
    ingame_menu = {1: ["Start a New Game", "pam"], 2: ["Save Game", "bam"],
                    3: ["Load Game", "uncle sam"],
                    4: ["Continue Game", "roger roger"]}

    def run(self, version):
        if version == 1:
            self.print_menu(1)
            confirmed = False
            while not confirmed:
                try:
                    num = int(raw_input("\nUse a number to pick > "))
                except ValueError:
                    continue
                if num not in range(1, 3):
                    continue
                print "Are you sure you want to %s?" % self.menu[num][0]
                confirm = raw_input("Type 'yes' to confirm > ")
                if confirm.lower() == 'yes':
                    confirmed = True
            return self.menu[num][1]
        if version == 2:
            self.print_menu(2)
            confirmed = False
            while not confirmed:
                try:
                    num = int(raw_input("\nUse a number to pick > "))
                except ValueError:
                    continue
                if num not in range(1, 5):
                    continue
                print "Are you sure you want to %s?" % self.ingame_menu[num][0]
                confirm = raw_input("Type 'yes' to confirm > ")
                if confirm.lower() == 'yes':
                    confirmed = True
            return self.ingame_menu[num][1]

    def print_menu(self, version):
        if version == 1:
            for option in self.menu_options:
                print option
        if version == 2:
            for option in self.ingame_menu_options:
                print option


if __name__ == "__main__":
    tester = Menu()
    tester.run(2)
