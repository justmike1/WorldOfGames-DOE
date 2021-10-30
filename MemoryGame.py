import random
import time

class Game1:
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def generate_sequence(self):
        self.res = random.sample(range(1, 101), self.Difficulty)
        res_str = f"Random number list is {self.res}"
        print(res_str, flush=True, end='\r')
        time.sleep(3)
        print('    ' * len(res_str))

    def get_list_from_user(self):
        self.user_res = random.sample(range(int(input('Guess the generated list: '))))

    def compare_results(self):
        i = 1
        while i < 3:  # the user gets 3 tries
            if self.user_res not in self.res:
                print('The number you guessed is incorrect')
                i += 1
                self.get_list_from_user()
            else:
                print(f'Congrats, You made it! Generated list was {self.res}!')
                break

    def play(self):
        self.generate_sequence()
        self.get_list_from_user()
        return self.compare_results()
