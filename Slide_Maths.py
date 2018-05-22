import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate,
                    GameState)


class Slide1(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics"

        slides = [[Text(50, flip_y(WindowSize, 70), "1. Coordinate System\n2. Collision Detection"),],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)


def compute_linear_interpolation(start, target, currentDelta, targetDelta):
    """ Helper function to interpolate between two points. """
    return start + ((target - start) * (currentDelta / targetDelta))


class Slide2(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics - Coordinate System"

        slides = []

        self.animations = [self.animation1_draw, self.animation2_draw]

        super().__init__(WindowSize, title, subtitle, slides)

    def load(self):
        super().load()
        self.currentAnimation = 0
        self.resetAnimation()

    def resetAnimation(self):
        self.targetDelta = 10
        self.currentDelta = 0

    def draw(self):
        super().draw()
        self.animations[self.currentAnimation]()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.currentAnimation = max(self.currentAnimation - 1, 0)
        else:
            self.currentAnimation += 1

        self.resetAnimation()

        if self.currentAnimation >= len(self.animations):
            self.gameState = GameState.FINISHED_STAGE
            self.currentAnimation = len(self.animations) - 1

    def animation1_draw(self):
        # y axis
        start_x, start_y = 100, 100
        end_x, target_y = 100, 400

        end_y = compute_linear_interpolation(start_y, target_y, self.currentDelta, self.targetDelta)
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)

        # x axis
        start_x, start_y = 100, 100
        target_x, end_y = 600, 100

        end_x = compute_linear_interpolation(start_x, target_x, self.currentDelta, self.targetDelta)
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)


        self.currentDelta += 0.1
        self.currentDelta = min(self.currentDelta, self.targetDelta)

    def animation2_draw(self):
        # y axis
        start_x, start_y = 100, 100
        end_x, end_y = 100, 400
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)

        # x axis
        start_x, start_y = 100, 100
        end_x, end_y = 600, 100
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)


        self.currentDelta += 0.1
        self.currentDelta = min(self.currentDelta, self.targetDelta)

class Slide3(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics - Collision Detection"

        slides = [[Text(50, flip_y(WindowSize, 70), """- Collision Detection is the algorithm used to see if two sprites intersects
- A sprite is an image of a game object"""),],
                  [Text(50, flip_y(WindowSize, 70), """- Are these two sprites touching?
- How can the computer tell that these sprites are touching?"""),],
                  [Text(50, flip_y(WindowSize, 70), """- Are these two sprites touching?
- How can the computer tell that these sprites are touching?
- We can use maths to detect if they touched. """),],
                  [Text(50, flip_y(WindowSize, 70), """- To simplify the maths, sprites are represented by the computer as rectangles"""),],
                  [Text(50, flip_y(WindowSize, 70), """- If the rectangle overlaps, it means there is a collision. An event is triggered
- Events are anything that can affect the game state"""),],
                  [Text(50, flip_y(WindowSize, 70), """- The event here, according to the game rules, is that Mario loses."""),],
                  [Text(50, flip_y(WindowSize, 70), """- The formula to check if two rectangles have collided is:"""),],
                  [Text(50, flip_y(WindowSize, 70), """- The formula to check if two rectangles have collided is:

(box1.x + box1.width >= box2.x and
 box1.x <= box2.x + box2.width and
 box1.y + box1.height >= box2.y and
 box1.y <= box2.y + box2.height)
"""),],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)

class Slide4(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics - Collision Detection - DEMO"
        slides = []

        super().__init__(WindowSize, title, subtitle, slides)

class Slide5(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics - Collision Detection"
        slides = [[Text(50, flip_y(WindowSize, 70), """- A key factor in good game design is to realize that you can use multiple collision boxes
- You can also make some collision boxes differently sized from the sprite to make the game more enjoyable"""),]]

        super().__init__(WindowSize, title, subtitle, slides)
