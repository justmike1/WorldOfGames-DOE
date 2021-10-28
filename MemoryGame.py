import random
import time

class Game1:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def generate_sequence(self):
        res = random.sample(range(1, 101), self.Difficulty)
        res_str = f"Random number list is {res}"
        print(res_str, flush=True, end='\r')
        time.sleep(3)
        print('    '*len(res_str))




    def get_list_from_user(self):
        self.user_res = random.sample(range(int(input(''))))


    def play(self):
        self.generate_sequence()
        self.get_list_from_user()
       # return self.is_list_equal

'''
    def is_list_equal(self):
        i = 1
        UserWins = False
        while i < 3:
            if self.User_Guess == self.secret_number:
                print('Correct, You made it!')
                UserWins = True
                break
            else:
                print('The number you guessed is incorrect')
                i += 1
                self.get_guess_from_user()
        return UserWins
'''



