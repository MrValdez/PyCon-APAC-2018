import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate)


class Slide(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "What you need to know to program game"

        slides = [[],

                  [Text(50, flip_y(WindowSize, 70), "1. Game Library"),],
 
                  [Text(50, flip_y(WindowSize, 70), """1. Game Library
2, Game Programming Design Patterns: Game loop""")],

                  [Text(50, flip_y(WindowSize, 70), """1. Game Library
2. Game Programming Design Patterns: Game loop
3. Object Oriented Programming: Game objects""")],

                  [Text(50, flip_y(WindowSize, 70), """1. Game Library
2. Game Programming Design Patterns: Game loop
3. Object Oriented Programming: Game objects
4. Maths""")],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)