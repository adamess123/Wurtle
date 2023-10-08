from colorama import Fore
from termcolor import cprint
from pyfiglet import figlet_format
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax

def word_coloring(word):
    console = Console()
    losses = 0
    incorrect_letters=[]
    for element in range(0, 6):

        print(Fore.WHITE)

        green_check = []
        for x in range(0, len(word)):
            green_check.append(0)

        letters = {}

        for keys in word:
            letters[keys] = letters.get(keys, 0) + 1

        # print("Count of chars:\n" + str(letters))

        while True:
            val = input("Enter word attempt: ")
            if len(val) != 5:
                print("Must be 5 characters.")
            if not val.isalpha():
                print("Input must be letters.")
            else:
                print("Attempted Word is: " + val + "")
                break

        # Pre check count decrease before printing
        for element in range(0, len(word)):
            if word[element] == val[element]:
                letters[val[element]] -= 1

        for element in range(0, len(word)):
            # If letter lines up in the same place, print green.
            if word[element] == val[element]:
                green_check[element] = 1
                console.print("[black on green]" + val[element] + "[/]", end="")

            else:
                if letters.get(val[element], 0) == 0:
                    console.print("[black on white]" + val[element] + "[/]", end="")
                    if val[element] not in incorrect_letters:
                        incorrect_letters.append(val[element].lower())

                elif letters[val[element]] >= 1:
                    console.print("[black on yellow]" + val[element] + "[/]", end="")
                # If yellow is not flagged, then only other option must be white/incorrect letter.
                else:
                    console.print("[black on white]" + val[element] + "[/]", end="")
                    if val[element] not in incorrect_letters:
                        incorrect_letters.append(val[element].lower())


                # Every time a green letter is flagged, check entire green_check list
                # To see if all letters are flagged green. If so, user has won.
        print("\nYou have used the following incorrect letters: ")
        print(', '.join(incorrect_letters))

        for check in range(0, len(word)):
            if green_check[check] == 0:
                losses += 1
                if losses == 6:
                    print("\nYou lost, the word was " + word)
                break

            if check == len(word) - 1 and green_check[check] == 1:
                print()
                cprint(figlet_format('Winner', font='starwars'), 'yellow', attrs=['bold'])
                return 0
        print()
