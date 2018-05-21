from helper import (flip_y,
                    Text,
                    Image,
                    SlideTemplate)


class Stage1c(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 1"
        subtitle = "Who is MrValdez"

        slides = [
                  [Text(50, flip_y(WindowSize, 70), """I'm a video game programming hobbyist

- Use game programming to teach programming
- 6 year Global Game Jam veteran
    - Make a game in ~48 hours
    - Every January
- Active board member at Python Philippines"""),],
                   [
                   Image(100, flip_y(WindowSize, 100), "crunch time.jpg", transition="left"),
                   Image(200, flip_y(WindowSize, 100), "Game Jam 2011.jpg", transition="right")]]

        super().__init__(WindowSize, title, subtitle, slides)