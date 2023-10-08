from colorama import Fore
from termcolor import cprint, colored
from pyfiglet import figlet_format


def word_coloring(word):
    losses = 0  # tracks user losses
    incorrect_letters = []  # stores incorrect letters
    previous_guesses = ""  # used to store guess of previous attempts

    for element in range(0, 6):
        print(Fore.WHITE)  # prevents color bleeding in terminal

        # checks if a word is correct, if it is then it gets appended
        green_check = []
        for x in range(0, len(word)):
            green_check.append(0)

        # tracks if a yellow character has to print or not
        letters = {}
        for keys in word:
            letters[keys] = letters.get(keys, 0) + 1

        # infinitely prompts user for input until a valid value is received
        while True:
            val = input("Enter word attempt: ")
            if len(val) != 5:
                print("Must be 5 characters.")
            elif not val.isalpha():
                print("Input must be letters.")
            else:
                print("Attempted Word is: " + val + "")
                break

        # Pre-check count decrease before printing
        for element in range(0, len(word)):
            if word[element] == val[element]:
                letters[val[element]] -= 1

        for element in range(0, len(word)):
            colored_letters = ""
            # If letter lines up in the same place, print green.
            if word[element] == val[element]:
                green_check[element] = 1

                # add correct letter and position w/ color to the string
                guess = colored(val[element], 'black', 'on_green')
                colored_letters += guess

            else:
                # add incorrect letter and incorrect position w/ color to the string
                if letters.get(val[element], 0) == 0:
                    guess = colored(val[element], 'black', 'on_white')
                    colored_letters += guess

                    # appends any incorrect letters to be displayed after turn
                    if val[element] not in incorrect_letters:
                        incorrect_letters.append(val[element].lower())

                # add correct letter and incorrect position w/ color to the string
                elif letters[val[element]] >= 1:
                    guess = colored(val[element], 'black', 'on_yellow')
                    colored_letters += guess

                # If yellow is not flagged, then only other option must be white/incorrect letter.
                else:
                    guess = colored(val[element], 'black', 'on_white')
                    colored_letters += guess

                    if val[element] not in incorrect_letters:
                        # appends any incorrect letters to be displayed after turn
                        incorrect_letters.append(val[element].lower())

            # appends current turns guess to be displayed next turn
            previous_guesses += colored_letters
        previous_guesses += '\n'

        # displays incorrect letters
        print("\nYou have used the following incorrect letters: ")
        print(', '.join(incorrect_letters))
        print()

        # splits up previous guesses and stacks them
        if not previous_guesses:
            print("")
        else:
            split_guess = previous_guesses.split('\n')
            for i in range(0, len(split_guess)):
                print(split_guess[i])

        for check in range(0, len(word)):
            if green_check[check] == 0:  # if not correct increment losses
                losses += 1
                if losses == 6:  # if user loses 6 times, end game
                    print("\nYou lost, the word was " + word)
                break

            # case for when user wins
            if check == len(word) - 1 and green_check[check] == 1:
                print()
                cprint(figlet_format('Winner', font='starwars'), 'yellow', attrs=['bold'])
                return 0
        print()
