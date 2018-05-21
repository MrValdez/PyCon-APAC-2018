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

    def update(self, delta_time):
        pass

    def draw(self):
        pass

    def on_key_press(self,key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
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


class SlideTemplate(Screen):
    def __init__(self, WindowSize, title, subtitle, slides):
        self.header = [
            Text(10, flip_y(WindowSize, 20), title, {"font_name": "Georgia", "font_size": 40, "bold": True, "anchor_x": "left", "align": "left"}),
            Text(30, flip_y(WindowSize, 90), subtitle, {"font_name": "Georgia", "font_size": 20, "italic": True, "anchor_x": "left", "align": "left"}),
            
        ]

        self.WindowSize = WindowSize
        self.slides = slides

        self.header_height = 150

        # adjust all y coordinates of text in slides to below the header
        for slide in self.slides:
            for element in slide:
                element.kwargs["start_y"] -= self.header_height
                element.kwargs["align"] = "left"
                element.kwargs["anchor_x"] = "left"
                element.kwargs["color"] = arcade.color.BLACK

    def load(self):
        self.currentSlide = 0
        self.gameState = GameState.RUNNING
        arcade.set_background_color(arcade.color.WHITE)

    def update(self, delta_time):
        return self.gameState

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(0, self.WindowSize[0], flip_y(self.WindowSize, 0), flip_y(self.WindowSize, self.header_height), arcade.color.BLACK)

        for text in self.header:
            text.draw()

        for text in self.slides[self.currentSlide]:
            text.draw()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.currentSlide = max(self.currentSlide - 1, 0)
        else:
            # default, move to the next slide on any keypress
            self.currentSlide += 1

        if self.currentSlide >= len(self.slides):
            self.gameState = GameState.NEXT_STAGE
            self.currentSlide = len(self.slides) - 1
