from wordle_logic import run_wordle_game
from termcolor import cprint
from pyfiglet import figlet_format
from replay import replay

if __name__ == "__main__":
    while True:
        run_wordle_game()
        if not replay():
            cprint(figlet_format('BYE ', font='starwars'), 'yellow', 'on_blue')
            exit()
