import random
import requests
import json

class Game3:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def get_money_interval(self):
        url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=3eee6e211600d6203628"
        response = requests.get(url)
        data = response.text
        parsed = json.loads(data)
        self.USD_ILS = float(parsed["USD_ILS"])
        self.random_number = random.randint(1, 101)
        self.generated_number = str(round(self.random_number * self.USD_ILS)

    def get_guess_from_user(self):
        self.User_Guess = input(f'Guess a the value of USD\ILS ')
        i = 1
        UserWins = False
        while i < 3:  # the user gets 3 tries
            if self.User_Guess == str(self.secret_number):
                print(f'Congrats, You made it! Secret number was {self.secret_number}!')
                UserWins = True
                break
            else:
                print('The number you guessed is incorrect')
                i += 1
                self.get_guess_from_user()
        return UserWins

    def play(self):
        self.get_money_interval()
        return self.get_guess_from_user()



