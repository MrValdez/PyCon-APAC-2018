import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate)


class Stage2(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "What knowledge are needed for game programming?"

        slides = [[],

                  [Text(50, flip_y(WindowSize, 70), "1. Object Oriented Programming"),],
 
                  [Text(50, flip_y(WindowSize, 70), """1. Object Oriented Programming
2. Maths""")],

                  [Text(50, flip_y(WindowSize, 70), """1. Object Oriented Programming
2. Maths
3. Game loop""")],

                  [Text(50, flip_y(WindowSize, 70), """1. Object Oriented Programming
2. Maths
3. Game loop
4. Game library""")],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)