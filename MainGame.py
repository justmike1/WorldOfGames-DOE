from Live import main
import logging

FORMAT = '%(message)s'
logging.basicConfig(format=FORMAT)

while True:
    exit = input('Are you sure you want to play? (y/n): ')
    if exit.lower() == 'n':
        break
    elif exit.lower() != 'y':
        logging.warning('\ninput is invalid, try again: ')
    else:
        main()
        break

