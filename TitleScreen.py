from helper import (flip_y,
                    Text)

class TitleScreen:
    def __init__(self, WindowSize):
        self.texts = [
            Text(WindowSize[0] / 2, flip_y(WindowSize, 110), "MrValdez", {"font_size": 60, "font_name": "Armalite Rifle"}),
            Text(WindowSize[0] / 2, flip_y(WindowSize, 190), "Game Programming with Python", {"font_size": 30}),
            Text(WindowSize[0] / 2, flip_y(WindowSize, 500), "Difficulty: Intermediate", {"italic": True}),
        ]

        self.start_text = Text(WindowSize[0] / 2, flip_y(WindowSize, 400), "Press any key")
        self.blink_time = 0.75
        self.blink = self.blink_time
        self.start_text_visible = True

    def update(self, delta_time):
        self.blink -= delta_time
        if self.blink < 0:
            self.blink += self.blink_time
            self.start_text_visible = not self.start_text_visible

    def draw(self):
        for text in self.texts:
            text.draw()

        if self.start_text_visible:
            self.start_text.draw()