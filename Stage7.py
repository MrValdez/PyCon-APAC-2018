import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate)


class Stage7(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 7"
        subtitle = "Live coding"
        slides = []

        super().__init__(WindowSize, title, subtitle, slides)

        self.text = Text(WindowSize[0] / 2, WindowSize[1] / 2, "Let's make a game",
                         kwargs={"font_name": "Impact",
                                 "color": arcade.color.BLACK,
                                 "bold": True})

    def draw(self):
        super().draw()

        self.text.draw()

    def update(self, delta_time):
        self.text.kwargs["font_size"] = min(self.text.kwargs["font_size"] + 0.9, 80)
        
        return self.gameState