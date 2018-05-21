import arcade
from helper import (flip_y,
                    Text,
                    GameState,
                    Screen,
                    Avatar)

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

class Stage2(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "What knowledge do we need for game programming?"
        slides = [[Text(10, flip_y(WindowSize, 20), "Slide 1"),
                   Text(10, flip_y(WindowSize, 50), "Slide 1")],
                   
                  [Text(10, flip_y(WindowSize, 0), "Slide 2")],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)