from termcolor import cprint
from pyfiglet import figlet_format

# prompts user if they want to replay the game
def replay():
    cprint(figlet_format('   PLAY AGAIN?', font='starwars'), 'yellow')
    cprint(figlet_format('  Y / N', font='starwars'), 'yellow')
    retry = input("")
    return retry.lower() in ['y', 'yes']
