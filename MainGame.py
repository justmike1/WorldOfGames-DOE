from Live import main
import logging
from abc import ABC, abstractmethod

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

'''''
class WoG(ABC):
    @abstractmethod
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()
'''
