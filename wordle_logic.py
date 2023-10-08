import sys
import shutil
from termcolor import cprint
from pyfiglet import figlet_format
from api_request import fetch_random_word
from word_coloring import word_coloring
from colorama import init

api_url = 'https://api.api-ninjas.com/v1/randomword'
api_key = '5mZJECPTxfUjrteYfn47zg==qRVV0l9npNg4rL9p'

def custom_print(text, color, on_color, attrs):
    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Calculate the number of spaces to add before and after the text
    padding = (terminal_width - len(text)) // 2

    # Construct the padded text
    padded_text = ' ' * padding + text + ' ' * padding

    # Print the padded text with termcolor
    cprint(padded_text, color, on_color, attrs=attrs)

def run_wordle_game():
    init(strip=not sys.stdout.isatty())
    custom_print(figlet_format('W O R D L E', font='larry3d'), 'yellow', 'on_blue', attrs=['bold'])
    word = fetch_random_word(api_url, api_key)

    print("Given Word: " + word)

    word_coloring(word)



    # Every time a green letter is flagged, check entire green_check list
    # To see if all letters are flagged green. If so, user has won.

