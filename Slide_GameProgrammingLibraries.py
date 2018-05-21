import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate)


class Slide(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 6"
        subtitle = "Python game programming libraries"

        slides = [[Text(50, flip_y(WindowSize, 70), """Game programming libraries
  - Pygame
  - Arcade
  - Ren'py
  - many more"""),
                   Text(600, flip_y(WindowSize, 70), """Platforms
  - PC
  - Mac
  - iOS
  - Android""")],
                 [Text(50, flip_y(WindowSize, 70),  """Libraries that can also be used for games
  - Kivy
  - Django / Flask
  - Curses
  - many more""")]]

        super().__init__(WindowSize, title, subtitle, slides)