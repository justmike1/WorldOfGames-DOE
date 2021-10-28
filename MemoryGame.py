import random
import time

class Game1:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def generate_sequence(self):
        self.res = random.sample(range(1, 101), self.Difficulty)
        print("Random number list is: " + str(self.res), end='\r')
        time.sleep(1)
        print('')



    def get_list_from_user(self):
        self.user_res = random.sample(range(int(input(''))))


    def play(self):
        self.generate_sequence()
        self.get_list_from_user()
       # return self.is_list_equal





