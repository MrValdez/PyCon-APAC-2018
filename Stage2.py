import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate)


class Stage2(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "What knowledge do we need for game programming?"

        slides = [[Text(10, flip_y(WindowSize, 20), "Slide 1"),
                   Text(10, flip_y(WindowSize, 50), "Slide 1")],
                   
                  [Text(10, flip_y(WindowSize, 0), "Slide 2")],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)