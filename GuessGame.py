import random
from abc import ABC, abstractmethod


class GuessGame:
    def __init__(self, Difficulty, Secret_number):
        self.Difficulty = Difficulty
        self.Secret_number = Secret_number

    @classmethod
    def generate_number(self):
        Secret_number = random.randint(1, 5)
        print(Secret_number)

    @classmethod
    def get_guess_from_user(self):
        target_num, guess_num = random.randint(1, self.Difficulty), 0
        while target_num != guess_num:
            pass

    @classmethod
    def compare_results(self):

    @classmethod
    def play(self):
        pass


