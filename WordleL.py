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

for element in range(0, len(word)):
    print(Fore.GREEN + word[element], end ="")
    
