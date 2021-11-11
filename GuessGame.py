from MainGame import *
import random

class Game2(WoG):
    def generate(self):
        self.secret_number = random.randint(1, self.Difficulty)

    def get_input_from_user(self):
        self.User_Guess = input(f'Guess a number between 1 to {self.Difficulty}: ')

    def compare_results(self):
        i = 1
        UserWins = False
        while i < 3:        # the user gets 3 tries
            if self.User_Guess == str(self.secret_number):
                print(f'Congrats, You made it! Secret number was {self.secret_number}!')
                UserWins = True
                break
            else:
                print('The number you guessed is incorrect')
                i += 1
                self.get_input_from_user()
        return UserWins





