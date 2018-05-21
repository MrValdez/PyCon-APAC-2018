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
                       "font_name": "Arial",
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


class Avatar(arcade.Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 10

    def update(self):
        super().update()

    def move(self, key, modifier, keydown):
        speed = self.speed
        if not keydown:
            speed *= -1

        if key == arcade.key.UP:
            self.change_y += speed
        if key == arcade.key.DOWN:
            self.change_y += -speed
        if key == arcade.key.LEFT:
            self.change_x += -speed
        if key == arcade.key.RIGHT:
            self.change_x += speed
