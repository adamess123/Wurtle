import requests
import json
from colorama import Fore, Back, Style

# While loop and Api call until 5 letter word is obtained.
# while (len(word) != 5)
api_url = 'https://api.api-ninjas.com/v1/randomword'
response = requests.get(api_url, headers = {
    'X-Api-Key': '5mZJECPTxfUjrteYfn47zg==qRVV0l9npNg4rL9p'
}). json()

print(response)

# toLower the word

# ===================================================
word = "test"

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
    # To see if all letters are flagged green. If so, user has won.
    for check in range(0, len(word)):
        if (green_check[check] == 0):
            break
        if (check == len(word) - 1 and green_check[check] == 1):
            print()
            print(Fore.WHITE + "User has won")
            exit()
        
