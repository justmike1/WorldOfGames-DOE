from abc import ABC
import logging


class WoG(ABC):
    FORMAT = '%(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def play(self):
        self.generate()
        self.get_input_from_user()
        return self.compare_results()

class Scores:
    def add_score(self):
        self.scores_file = open("Scores.txt", "a")
        self.points_of_winning = (self.Difficulty*3)+5
        self.scores_file.write(f"\n{str(self.points_of_winning)}")
        self.scores_file.close()
