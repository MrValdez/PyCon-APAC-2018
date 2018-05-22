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
                    Text(150, flip_y(WindowSize, 200), """@dataclass
class GameObject:
    x: int
    y: int
    image: Image 
"""),
                    Text(500, flip_y(WindowSize, 200), """class Monster(GameObject):
    def update(self):
        pass

    def draw(self):
        pass""")],

                 ]

        super().__init__(WindowSize, title, subtitle, slides)

    def draw(self):
        if self.currentSlide == 0:
            # border for class code
            class_pos = [[self.slides[0][1].kwargs["start_x"], 250, self.slides[0][1].kwargs["start_y"], 200],
                         [self.slides[0][2].kwargs["start_x"], 380, self.slides[0][2].kwargs["start_y"], 200],]  # manually created

            for left, width, top, height in class_pos:
                left -= 10
                right = left + width
                bottom = top - height
                arcade.draw_lrtb_rectangle_outline(left, right,
                                      top, bottom,
                                      arcade.color.BLACK)

        super().draw()

class Slide2(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 2"
        subtitle = "Game Object Containers"

        slides = [[Text(50, flip_y(WindowSize, 50), """- New instances of game objects are added to a container. This makes it
easier to manage all the game objects in a game

- Every frame, we call the update and draw functions of all the game objects
inside a container""", {"font_size": 18}),
                    Text(250, flip_y(WindowSize, 230), """monsters = []

for monster in monsters:
    monster.update()
for monster in monsters:
    monster.draw()
""")
],

                 ]

        super().__init__(WindowSize, title, subtitle, slides)

    def draw(self):
        # border for class code
        left, width, top, height = self.slides[0][1].kwargs["start_x"], 350, self.slides[0][1].kwargs["start_y"], 200
        left -= 30
        right = left + width
        bottom = top - height
        arcade.draw_lrtb_rectangle_outline(left, right,
                              top, bottom,
                              arcade.color.BLACK)

        super().draw()
