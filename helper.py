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


class Image(arcade.Sprite):
    """ 
    Helper class to make the code consistent with Text element
    
    transitions: left, right, bottom
    """
    
    def __init__(self, left, top, filename, transition=None, border=0):
        super().__init__(filename)
        self.border = border
        self._init_transition(left, top, transition)

    def _init_transition(self, left, top, transition):
        self.target_position = [left, top]

        if transition == "left":
            self.left = left - 1000     # todo: it would be nice to soft code this to the window's width
        elif transition == "right":
            self.left = left + 1000     # todo: it would be nice to soft code this to the window's position
        else:
            self.left = left

        if transition == "bottom":
            self.top = top - 1000
        else:
            self.top = top

    def update(self):
        speed = 30
        if self.left < self.target_position[0]:
            self.left += speed
            self.left = min(self.left, self.target_position[0])     # prevent overshoot
        if self.left > self.target_position[0]:
            self.left -= speed
            self.left = max(self.left, self.target_position[0])     # prevent overshoot
        if self.top < self.target_position[1]:
            self.top += speed
            self.top = min(self.top, self.target_position[1])     # prevent overshoot

        super().update()

    def draw(self):
        if self.border:
            arcade.draw_lrtb_rectangle_filled(self.left - self.border, self.right + self.border,
                                              self.top + self.border, self.bottom - self.border,
                                              arcade.color.BLACK)
        super().draw()

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
                if type(element) is Text:
                    element.kwargs["start_y"] -= self.header_height
                    element.kwargs["align"] = "left"
                    element.kwargs["anchor_x"] = "left"
                    element.kwargs["color"] = arcade.color.BLACK
                if issubclass(type(element), arcade.Sprite):
                    element.top -= self.header_height
                    element.target_position[1] -= self.header_height

    def load(self):
        self.currentSlide = 0
        self.gameState = GameState.RUNNING
        arcade.set_background_color(arcade.color.WHITE)

    def update(self, delta_time):
        if self.slides:
            for element in self.slides[self.currentSlide]:
                if issubclass(type(element), Image):
                    element.update()

        return self.gameState

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(0, self.WindowSize[0], flip_y(self.WindowSize, 0), flip_y(self.WindowSize, self.header_height), arcade.color.BLACK)

        for text in self.header:
            text.draw()

        if self.slides:
            for element in self.slides[self.currentSlide]:
                element.draw()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.currentSlide = max(self.currentSlide - 1, 0)
        else:
            # default, move to the next slide on any keypress
            self.currentSlide += 1

        if self.currentSlide >= len(self.slides):
            self.gameState = GameState.FINISHED_STAGE
            self.currentSlide = len(self.slides) - 1
