from helper import (flip_y,
                    Text,
                    SlideTemplate)

from hack import Image


class Stage1b(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 1"
        subtitle = ""

        slides = [
                  [Text(50, flip_y(WindowSize, 40), "Who here play video games?")],

                  [Text(50, flip_y(WindowSize, 40), "Who here play video games?"),
                   Image(100, flip_y(WindowSize, 100), "video_game1.png", scale=1.4, transition="left")],

                  [Text(50, flip_y(WindowSize, 40), "Who here play video games?"),
                   Image(100, flip_y(WindowSize, 100), "video_game1.png", scale=1.4),
                   Image(360, flip_y(WindowSize, 70), "video_game2.png", scale=0.5, transition="right")],

                  [Text(50, flip_y(WindowSize, 40), "Who here play video games?"),
                   Image(100, flip_y(WindowSize, 100), "video_game1.png", scale=1.4),
                   Image(360, flip_y(WindowSize, 70), "video_game2.png", scale=0.5),
                   Image(250, flip_y(WindowSize, 80), "video_game3.png", scale=0.75, transition="bottom")],

                  ]

        super().__init__(WindowSize, title, subtitle, slides)