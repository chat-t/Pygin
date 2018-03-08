from game_engine.component import Component


class TextMash(Component):

    def __init__(self, game_object, message, color, size, font):
        super(TextMash, self).__init__(game_object)
        self.message = message
        self.color = color
        self.size = size
        self.font = font