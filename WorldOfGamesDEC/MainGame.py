from abc import ABC, abstractmethod

class WoG(ABC):
    def __init__(self, difficulty):
        self.Difficulty = difficulty
        self.play()

    def play(self):
        self.generate()
        self.get_input_from_user()
        return self.compare_results()
