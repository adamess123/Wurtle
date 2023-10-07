from termcolor import cprint
from pyfiglet import figlet_format
from api_request import fetch_random_word
from word_coloring import word_coloring
import sys
from colorama import init
from replay import replay

api_url = 'https://api.api-ninjas.com/v1/randomword'
api_key = '5mZJECPTxfUjrteYfn47zg==qRVV0l9npNg4rL9p'


def run_wordle_game():
    init(strip=not sys.stdout.isatty())
    cprint(figlet_format('WORDLE', font='starwars'), 'yellow', 'on_blue', attrs=['bold'])

    word = fetch_random_word(api_url, api_key)

    print("Given Word: " + word)

    if (word_coloring(word) == True):

        while (replay()):
            run_wordle_game()


    # Every time a green letter is flagged, check entire green_check list
    # To see if all letters are flagged green. If so, user has won.

