import json
import pandas as pd

def next_level():
    print('This is what you chose:')
    print(pd.read_json('input_data.json'))

def load_game():
    name = input("Hello There! What is your name? ")
    print(f"Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play!")
    d =  {}
    while True:
        d['Game'] = input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. Currency Roulette - try and guess the value of a random amount of USD to ILS. \n : ")
        if int(d['Game']) > 3:
            print('num is invalid')
            break
        elif int(d['Game']) < 1:
            print('num is invalid')
            break
        d['Difficulty'] = input("Please choose game difficulty from 1 to 5: ")
        if int(d['Difficulty']) > 5:
            print('num is invalid')
            break
        elif int(d['Difficulty']) < 1:
            print('num is invalid')
            break
        else:
            next_level()
            return(name,d)
            #next_level()

out = {}

while True:
    exit = input('Are you sure you want to play (y/n)? ')
    if exit.lower() == 'n':
        break
    elif exit.lower() != 'y':
        print("Try again")
        break
    else:
        name, d = load_game()
        out[name] = d


# I made a json to save input data
with open('input_data.json', 'w') as f:
    json.dump(out, f, indent=2)



'''
    while True:
        Game = input("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. Currency Roulette - try and guess the value of a random amount of USD to ILS. \n : ")
        if Game.lower() == '1':
            break
        elif Game
            while True:
                Difficulty = input("Please choose game difficulty from 1 to 5: ")
                if int(Difficulty) < 6:
                    return(Difficulty,d)
                else:
                    print("The number is invalid, try again!")
            return(Game,d)
        else:
            print("The number is invalid, try again!")
'''

