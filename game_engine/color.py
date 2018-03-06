import random

class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    @classmethod
    def random_color(cls):
        """
        :return: a random color
        """
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
