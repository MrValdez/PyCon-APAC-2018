from helper import (flip_y,
                    Text,
                    Image,
                    SlideTemplate)


class Stage1b(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 1"
        subtitle = ""

        slides = [
                  [Text(50, flip_y(WindowSize, 70), "Who here play video games?")],

                  [Text(50, flip_y(WindowSize, 70), "Who here play video games?"),
                   Image(100, flip_y(WindowSize, 100), "mario.png", transition="left")],

                  [Text(50, flip_y(WindowSize, 70), "Who here play video games?"),
                   Image(100, flip_y(WindowSize, 100), "mario.png"),
                   Image(200, flip_y(WindowSize, 100), "mario.png", transition="right")],

                  [Text(50, flip_y(WindowSize, 70), "Who here play video games?"),
                   Image(100, flip_y(WindowSize, 100), "mario.png"),
                   Image(200, flip_y(WindowSize, 100), "mario.png"),
                   Image(150, flip_y(WindowSize, 100), "mario.png", transition="bottom")],

                  ]

        super().__init__(WindowSize, title, subtitle, slides)