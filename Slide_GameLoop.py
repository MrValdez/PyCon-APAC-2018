from helper import (flip_y,
                    Text,
                    SlideTemplate)

from hack import Image

class Slide(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 1"
        subtitle = "Game Loop"

        slides = [

                  [Text(50, flip_y(WindowSize, 70), """- The basic code for all games
- Infinite loop
- Runs after game world setup
- Each iteration is called a "frame" """),
                   Image(500, flip_y(WindowSize, 70), "game_loop.png", scale=1.2)],

                  ]

        super().__init__(WindowSize, title, subtitle, slides)