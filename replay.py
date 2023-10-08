from wordle_logic import run_wordle_game
from termcolor import cprint
from pyfiglet import figlet_format

def replay():
    cprint(figlet_format('PLAY AGAIN?', font='starwars'), 'yellow')
    retry = input("")
    return retry.lower() in ['y', 'yes']
