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

class WoG(ABC):
    @abstractmethod
    pass

#game_1 = MemoryGame
class game_1(WoG):
    pass
    
#game_2 = GuessGame
class game_2(WoG):
    pass

#game_3 = CurrencyRouletteGame
class game_3(WoG):
    pass
