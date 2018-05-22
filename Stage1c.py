from helper import (flip_y,
                    Text,
                    SlideTemplate)

from hack import Image


class Stage1c(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 1"
        subtitle = "Who is MrValdez"

        slides = [
                  [Text(50, flip_y(WindowSize, 40), """I'm a video game programming hobbyist

- Use game programming to teach programming
- 6 year Global Game Jam veteran
    - Make a game in ~48 hours
    - Every January
"""),
                   Image(600, flip_y(WindowSize, 150), "crunch time.jpg", scale=0.8),
                   ],
                  [Text(50, flip_y(WindowSize, 40), """I'm a video game programming hobbyist

- Use game programming to teach programming
- 6 year Global Game Jam veteran
    - Make a game in ~48 hours
    - Every January
"""),
                   Image(600, flip_y(WindowSize, 150), "crunch time.jpg", scale=0.8),
                   Image(580, flip_y(WindowSize, 10), "Game Jam 2011.jpg", transition="right", scale=0.8)],
                  [Text(50, flip_y(WindowSize, 40), """I'm a video game programming hobbyist

- Active board member at Python Philippines
- https://mrvaldez.ph
- https://github.com/mrvaldez
- @MrValdez
"""),]]

        super().__init__(WindowSize, title, subtitle, slides)