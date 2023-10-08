from colorama import Fore
from termcolor import cprint, colored
from pyfiglet import figlet_format


def word_coloring(word):
    losses = 0 
    incorrect_letters = []  
    previous_guesses = ""  

    for element in range(0, 6):
        print(Fore.WHITE)       # Prevents color bleeding in terminal

        # Checks if a word is correct, if it is then it gets appended
        green_check = []
        for x in range(0, len(word)):
            green_check.append(0)

        # Tracks if a yellow character has to print or not
        letters = {}
        for keys in word:
            letters[keys] = letters.get(keys, 0) + 1

        # Infinitely prompts user for input until a valid value is received
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

                # Add correct letter and position w/ color to the string
                guess = colored(val[element], 'black', 'on_green')
                colored_letters += guess

            else:
                # Add incorrect letter and incorrect position w/ color to the string
                if letters.get(val[element], 0) == 0:
                    guess = colored(val[element], 'black', 'on_white')
                    colored_letters += guess

                    # Appends any incorrect letters to be displayed after turn
                    if val[element] not in incorrect_letters:
                        incorrect_letters.append(val[element].lower())

                # Add correct letter and incorrect position w/ color to the string
                elif letters[val[element]] >= 1:
                    guess = colored(val[element], 'black', 'on_yellow')
                    colored_letters += guess

                # If yellow is not flagged, then only other option must be white/incorrect letter.
                else:
                    guess = colored(val[element], 'black', 'on_white')
                    colored_letters += guess

                    if val[element] not in incorrect_letters:
                        # Appends incorrect_letters to be displayed after turn
                        incorrect_letters.append(val[element].lower())

            # Appends current turns guess to be displayed next turn
            previous_guesses += colored_letters
        previous_guesses += '\n'

        # Displays incorrect letters
        print("\nYou have used the following incorrect letters: ")
        print(', '.join(incorrect_letters))
        print()

        # Splits up previous guesses and stacks them
        if not previous_guesses:
            print("")
        else:
            split_guess = previous_guesses.split('\n')
            for i in range(0, len(split_guess)):
                print(split_guess[i])

        # Updates and checks amount of losses
        for check in range(0, len(word)):
            if green_check[check] == 0:  
                losses += 1
                if losses == 6: 
                    print("\nYou lost, the word was " + word)
                break

            # Case for when user wins
            if check == len(word) - 1 and green_check[check] == 1:
                print()
                cprint(figlet_format('Winner', font='starwars'),
                                     'yellow', attrs=['bold'])
                return 0
        print()
