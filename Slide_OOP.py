import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate)


class Slide(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "Game Objects"

        slides = [[Text(50, flip_y(WindowSize, 70), """- It is useful to use OOP for Game objects
- Game objects have functions for updating and drawing
- Every frame, the game will update and draw game objects."""),
                    Text(50, flip_y(WindowSize, 70), """class GameObject:
Position
Sprite
"""),
                    Text(50, flip_y(WindowSize, 70), """class Monster(GameObject):
def update(self):
    pass

def draw(self):
    pass""")],

                 ]

        super().__init__(WindowSize, title, subtitle, slides)


class Slide2(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "Game Object Containers"

        slides = [[Text(50, flip_y(WindowSize, 70), """New instances of game objects are added to a container. This makes it easier to manage all the game objects in a game
                  - Every frame, we call the update and draw functions of all the game objects inside a container"""),
                    Text(50, flip_y(WindowSize, 70), """monsters = []
for monster in monsters:
    monster.update()
for monster in monsters:
    monster.draw()
""")
],

                 ]

        super().__init__(WindowSize, title, subtitle, slides)