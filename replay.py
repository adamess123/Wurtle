def replay():
    retry = input("Play again? ")#cprint(figlet_format('PLAY AGAIN? ', font='starwars'), 'yellow', 'on_blue'))
    if retry.lower == 'yes' or 'y':
       return True
    elif retry.lower == 'n' or 'n':
       return False
    else:
        exit()