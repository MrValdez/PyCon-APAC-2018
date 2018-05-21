import arcade
from enum import Enum, auto

def flip_y(SIZE, y):
    return SIZE[1] - y

class GameState(Enum):
    RUNNING = auto()
    NEXT_STAGE = auto()
    FINISHED_STAGE = auto()

class Screen:
    def load(self):
        pass

class Text:
    """ Helper class to have text with a default kwargs for this project """

    def __init__(self, x, y, text, kwargs=None):
        self.kwargs = {"color": arcade.color.WHITE,
                       "font_name": ("Arial"),
                       "font_size": 20,
                       "anchor_x": "center",
                       "anchor_y": "top",
                       "align": "center",
                       }

        self.kwargs["text"] = text
        self.kwargs["start_x"] = x
        self.kwargs["start_y"] = y

        if kwargs:
            self.kwargs.update(kwargs)

    def draw(self):
        arcade.draw_text(**self.kwargs)