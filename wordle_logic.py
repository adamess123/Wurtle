import sys
from termcolor import cprint
from pyfiglet import figlet_format
from api_request import fetch_random_word
from word_coloring import word_coloring
from colorama import init

api_url = 'https://api.api-ninjas.com/v1/randomword'
api_key = '5mZJECPTxfUjrteYfn47zg==qRVV0l9npNg4rL9p'


def run_wordle_game():
    init(strip=not sys.stdout.isatty())     # Initializes color management system

    cprint(figlet_format('W U R T L E', font='larry3d'),
                         'yellow', attrs=['bold'])

    word = fetch_random_word(api_url, api_key) 

    word_coloring(word)
