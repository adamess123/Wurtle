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
        previous_guesses = []
        if not previous_guesses:
            print("")
        else:
            console.print(previous_guesses, end="")

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
            colored_letters=[]
            # If letter lines up in the same place, print green.
            if word[element] == val[element]:
                green_check[element] = 1
                console.print("[black on green]" + val[element] + "[/]", end="")
                colored_letters.append("[black on green]" + val[element] + "[/]")

            else:
                if letters.get(val[element], 0) == 0:
                    console.print("[black on white]" + val[element] + "[/]", end="")
                    colored_letters.append("[black on white]" + val[element] + "[/]")
                    if val[element] not in incorrect_letters:
                        incorrect_letters.append(val[element].lower())

                elif letters[val[element]] >= 1:
                    console.print("[black on yellow]" + val[element] + "[/]", end="")
                    colored_letters.append("[black on yellow]" + val[element] + "[/]")
                # If yellow is not flagged, then only other option must be white/incorrect letter.
                else:
                    console.print("[black on white]" + val[element] + "[/]", end="")
                    colored_letters.append("[black on white]" + val[element] + "[/]")
                    if val[element] not in incorrect_letters:
                        incorrect_letters.append(val[element].lower())
            for letter in range(0, len(colored_letters)):
                console.print(colored_letters, end="")
            previous_guesses.append(colored_letters)


        print("\nYou have used the following incorrect letters: ")
        print(', '.join(incorrect_letters))

        # Every time a green letter is flagged, check entire green_check list
        # To see if all letters are flagged green. If so, user has won.
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
