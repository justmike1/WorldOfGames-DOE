from MainGame import *
import random
import requests
import json
import os
from dotenv import load_dotenv


class Game3(WoG, Scores):
    def generate(self):
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        for key in API_KEY:
            if key == '':
                logging.error("Your .env is empty")
                break
            else:
                continue
        url = f"https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey={API_KEY}" #  the free API
        res = requests.get(url)
        if res.status_code != 200:
            logging.warning("Check your API")
            return -1
        else:
            data = res.text
            parsed = json.loads(data)
            self.USD_ILS = float(parsed["USD_ILS"])     #get the value
            self.random_number = random.randint(1, 101)     #generate random number
            print(f'{self.random_number} USD')
            self.gen_number = round(self.random_number//self.USD_ILS)     # round it to integer
            self.gen_list = list(range(self.gen_number-self.Difficulty, self.gen_number+self.Difficulty)) #generate a list in the range of difficulty
            #print(f'{self.gen_list}') #Delete the sharp symbol when you want to test

    def get_input_from_user(self):
        self.User_Guess = int(input(f'Guess the number in ILS: '))

    def compare_results(self):
        i = 1
        while i < 4:  # the user gets 3 tries
            if self.User_Guess not in self.gen_list:
                i += 1
                logging.warning('\nThe number you guessed is incorrect, try again: ')
                self.get_input_from_user()
            else:
                logging.info(f'Congrats, You made it! Generated number was {self.gen_number}!')
                self.add_score()
                break






