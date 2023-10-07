import requests
import json
from colorama import Fore, Back, Style
import sys
from colorama import init

init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('WORDLE', font='starwars'), 'yellow', 'on_blue', attrs=['bold'])

api_url = 'https://api.api-ninjas.com/v1/randomword'

word = None

while True:
    response = requests.get(api_url, headers={
        'X-Api-Key': '5mZJECPTxfUjrteYfn47zg==qRVV0l9npNg4rL9p'
    }).json()

    if len(response["word"]) == 5:
        word = response["word"].lower()
        break
# ===================================================

print("Given Word: " + word)

for element in range(0, 6):

    print(Fore.WHITE)

    green_check = []
    for x in range(0, len(word)):
        green_check.append(0)

    res = {}

    for keys in word:
        res[keys] = res.get(keys, 0) + 1

    print("Count of chars:\n" + str(res))

    val = input("Enter word attempt: ")
    print("Attempted Word is: " + val)

    # Pre check count decrease before printing
    for element in range(0, len(word)):
        if (word[element] == val[element]):
            res[val[element]] -= 1

    for element in range(0, len(word)):

        yellow = 0

        # If letter lines up in the same place, print green.
        if (word[element] == val[element]):
            green_check[element] = 1
            print(Fore.GREEN + val[element], end="")

        else:
            if (res.get(val[element], 0) == 0):
                print(Fore.WHITE + val[element], end="")
            # Nested for-loop to check for yellow color coding.
            elif (res[val[element]] >= 1):
                print(Fore.YELLOW + val[element], end="")
            # If yellow is not flagged, then only other option must be white/incorrect letter.
            else:
                print(Fore.WHITE + val[element], end="")

    # Every time a green letter is flagged, check entire green_check list
    # To see if all letters are flagged green. If so, user has won.
    for check in range(0, len(word)):
        if (green_check[check] == 0):
            break
        if (check == len(word) - 1 and green_check[check] == 1):
            print()
            cprint(figlet_format('USER \(^_^)/ WON', font='starwars'), 'yellow', 'on_blue', attrs=['bold'])
            exit()
    print()