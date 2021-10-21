
name = input("Hello There! What is your name? ")

def welcome(name):
    return(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play!")
print(welcome(name))


def load_game():
        while True:
            Game = input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. Currency Roulette - try and guess the value of a random amount of USD to ILS. \n : ")
            if int(Game) < 4:
                while True:
                    Difficulty = input("Please choose game difficulty from 1 to 5: ")
                    if int(Difficulty) < 6:
                        return
                    else:
                        print("The number is invalid, try again!")
                return
            else:
                print("The number is invalid, try again!")

load_game()

