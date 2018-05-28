from helper import (flip_y,
                    Text,
                    SlideTemplate)

from hack import Image


class Stage1c(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 1"
        subtitle = "Who is MrValdez"

        slides = [
                  [Text(50, flip_y(WindowSize, 40), """- I'm a video game programming hobbyist
- Active board member at Python Philippines
- Use game programming to teach programming
- https://mrvaldez.ph
- https://github.com/mrvaldez
- @MrValdez
"""),
                   Image(650, flip_y(WindowSize, 30), "mrvaldez.png", scale=0.6),]
                  ]

        super().__init__(WindowSize, title, subtitle, slides)