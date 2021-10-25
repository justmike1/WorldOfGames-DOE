def MemoryGame(difficulty):
    print("Starting Memory Game with difficulty", difficulty)

def GuessGame(difficulty):
    print("Starting Guess Game with difficulty", difficulty)

def CurrencyRouletteGame(difficulty):
    print("Starting Currency Roulette Game with difficulty", difficulty)

def start_game(game_id, difficulty):
    if game_id == 1:
        MemoryGame(difficulty)
    elif game_id == 2:
        GuessGame(difficulty)
    elif game_id == 3:
        CurrencyRouletteGame(difficulty)

def load_game():
    name = input("Hello There! What is your name? ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play!")
    d = {}
    d['Game'] = int(input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. Currency Roulette - try and guess the value of a random amount of USD to ILS. \n : "))
    if d['Game'] not in range(1, 4):
        print('num is invalid')
        return (main())
    d['Difficulty'] = int(input("Please choose game difficulty from 1 to 5: "))
    if d['Difficulty'] not in range(1, 6):
        print('num is invalid')
        return (main())
    return (name, d)

def main():
    name, d = load_game()
    start_game(d["Game"], d["Difficulty"])

main()
