import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate)


class Slide(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "What knowledge are needed for game programming?"

        slides = [[],

                  [Text(50, flip_y(WindowSize, 70), "1. Game Library"),],
 
                  [Text(50, flip_y(WindowSize, 70), """1. Game Library
2, Game loop""")],

                  [Text(50, flip_y(WindowSize, 70), """1. Game Library
2. Game loop
3. Object Oriented Programming""")],

                  [Text(50, flip_y(WindowSize, 70), """1. Game Library
2. Game loop
3. Object Oriented Programming
4. Maths""")],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)