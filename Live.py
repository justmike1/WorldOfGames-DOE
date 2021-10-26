import logging
from MemoryGame import Game1
from GuessGame import Game2
from CurrencyRouletteGame import Game3

def MemoryGame(difficulty):     #Starts the game's script at requested difficulty
    print(f'Starting Memory Game with difficulty {difficulty}')
    Game1(difficulty)

def GuessGame(difficulty):      #Starts the game's script at requested difficulty
    print(f'Starting Guess Game with difficulty {difficulty}')
    Game2(difficulty)

def CurrencyRouletteGame(difficulty):       #Starts the game's script at requested difficulty
    print(f'Starting Currency Roulette Game with difficulty {difficulty}')
    Game3(difficulty)

def start_game(game_id, difficulty):        #game_id equals d['game'], vice versa about difficulty, look main() function
    if game_id == 1:
        MemoryGame(difficulty)
    elif game_id == 2:
        GuessGame(difficulty)
    elif game_id == 3:
        CurrencyRouletteGame(difficulty)

def load_game():
    # Has to start with an try exception to get through the ValueError (typing a letter string)
    name = input("Hello There! What is your name? ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play!")
    # The variable that saves the Game & Difficulty inputs (has to be the first in the block & empty dict)
    d = {}
    # First input the variable as a string, next validate its a digit, next convert it to an integer(!)
    d['Game'] = input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. Currency Roulette - try and guess the value of a random amount of USD to ILS. \n : ")
    while d['Game'].isdigit() == False:
        logging.error('num is invalid')
        return(main())
    d['Game'] = int(d['Game'])
    if d['Game'] not in range(1, 4):
        logging.error('num is invalid')
        return (main())
    d['Difficulty'] = input("Please choose game difficulty from 1 to 5: ")
    while d['Difficulty'].isdigit() == False:
        logging.error('num is invalid')
        return (main())
    d['Difficulty'] = int(d['Difficulty'])
    if d['Difficulty'] not in range(1, 6):
        logging.error('num is invalid')
        return (main())
    return (name, d)

def main():     #The main function which starts the whole process, after it starts load_game for user's inputs, it starts the chosen game at certain difficulty
    FORMAT = '%(message)s'
    logging.basicConfig(format=FORMAT)
    name, d = load_game()
    start_game(d["Game"], d["Difficulty"])

if __name__ == "__main__":
    main()
