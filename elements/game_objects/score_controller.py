from game_engine.game_object import GameObject
from elements.game_objects.game_objects.text import Text
from game_engine.game_object import GameObject
from game_engine.color import Color
from pygame.math import Vector2

class ScoreController(GameObject):

    def start(self):

        font_path = "assets/fonts/neuropolxrg.ttf"

        self.step_delta = 150  # Number of steps of the game required to update the score

        self.score = 0.0
        score_x = 10.0
        score_y = 5.0
        score_message = str(self.score)
        score_color = Color.white
        score_size = 15

        self.game_object_list = [
            Text(Vector2(score_x, score_y), score_message, score_color, score_size, font_path)
        ]

    def update(self):
        self.score = self.score + 1 / self.step_delta

        self.game_object_list[0].text_mesh.message = str(int(self.score))
