import random
import requests
import json

class Game3:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def get_money_interval(self):
        url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=3eee6e211600d6203628" #  the free API
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        self.USD_ILS = float(parsed["USD_ILS"])     #get the value
        self.random_number = random.randint(1, 101)     #generate random number
        self.gen_number = round(self.random_number * self.USD_ILS)     # round it to integer
        self.gen_list = list(range(self.gen_number-self.Difficulty, self.gen_number+self.Difficulty)) #generate a list in the range of difficulty
        print(f'{self.gen_list}')

    def get_guess_from_user(self):
        self.User_Guess = input(f'Guess the number generated: ')
        i = 1
        UserWins = False
        while i < 3:  # the user gets 3 tries
            if self.User_Guess not in self.gen_list:
                print('The number you guessed is incorrect')
                i += 1
                self.get_guess_from_user()
            else:
                print(f'Congrats, You made it! Generated number was {self.gen_number}!')
                UserWins = True
                break
        return UserWins

    def play(self):
        self.get_money_interval()
        return self.get_guess_from_user()



