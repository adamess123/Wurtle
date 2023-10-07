import requests
import json
from colorama import Fore, Back, Style
import sys
from colorama import init
init(strip = not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('WORDLE', font='starwars'), 'yellow', 'on_blue', attrs=['bold'])

api_url = 'https://api.api-ninjas.com/v1/randomword'

word = None

while True:
    response = requests.get(api_url, headers = {
        'X-Api-Key': '5mZJECPTxfUjrteYfn47zg==qRVV0l9npNg4rL9p'
    }). json()

    if len(response["word"]) == 5:
        word = response["word"].lower()
        break
# ===================================================

print("Given Word: " + word)
# List to check if all letters become green (WIN)
# List is full of zeros. If user gets a green letter, index will flag = 1.
green_check = []
for x in range (0, len(word)):
    green_check.append(0)

for element in range(0, 6):
    print(Fore.WHITE)
    val = input("Enter word attempt: ")
    print("Attempted Word is: " + val)

    for element in range(0, len(word)):
        yellow = 0

        # If letter lines up in the same place, print green.
        if (word[element] == val[element]):
            green_check[element] = 1
            print(Fore.GREEN + val[element], end="")
            
        else:
            # Nested for-loop to check for yellow color coding.
            for check in range(0, len(word)):
                temp = word[check]
                if (val[element] == word[check]):
                    print(Fore.YELLOW + val[element], end ="")
                    yellow = 1
                    break
            # If yellow is not flagged, then only other option must be white/incorrect letter.
            if (yellow == 0):
                print(Fore.WHITE + val[element], end ="")

    # Every time a green letter is flagged, check entire green_check list
<<<<<<< HEAD
    # To see if all letters are flagged green. If so, user has won.
=======
    # To see if all letters are flagged green. If so, user has won!
>>>>>>> 5ca2c1f (Added github files)
    for check in range(0, len(word)):
        if (green_check[check] == 0):
            break
        if (check == len(word) - 1 and green_check[check] == 1):
            print()
            cprint(figlet_format('USER \(^_^)/ WON', font='starwars'), 'yellow', 'on_blue', attrs=['bold'])
            exit()
    print()
        
