import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate,
                    GameState)

from hack import Image

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

        self.animations = [self.animation4_draw]
        self.animations = [self.animation1_draw, self.animation2_draw, self.animation3_draw, self.animation4_draw]

        super().__init__(WindowSize, title, subtitle, slides)

    def load(self):
        super().load()
        self.currentAnimation = 0
        self.resetAnimation()

        self.tick_step = 30
        self.axis_size = 10

        # variables for y and x axis
        self.y_axis = [100, 100 - 5, 100, 400 - 4]
        self.x_axis = [100, 100, 600 + 10, 100]

        self.mario_sprite = Image(0, 0, "mario_sprite.png", scale=2.3)
        self.mario_box = Image(0, 0, "mario_box.png", scale=2.3)
        self.mario_score = Image(0, 0, "mario_score.png", scale=2.3)

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
        start_x, start_y = 100, 100 - 5     # -5 from (border_width / 2)
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

    def _draw_graph(self):
        # y axis
        start_x, start_y, end_x, end_y = self.y_axis
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)

        for y in range(start_y + self.tick_step, end_y, self.tick_step):
            arcade.draw_commands.draw_line(start_x - self.axis_size, y, start_x + self.axis_size, y,
                                           arcade.color.GRAY, border_width=4)

        # x axis
        start_x, start_y, end_x, end_y = self.x_axis
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)

        for x in range(start_x + self.tick_step, end_x + self.tick_step, self.tick_step):
            arcade.draw_commands.draw_line(x, start_y - self.axis_size, x, start_y + self.axis_size,
                                           arcade.color.GRAY, border_width=4)

    def animation2_draw(self):
        # y axis
        start_x, start_y = 100, 100 - 5
        end_x, end_y = 100, 400 - 4         # simple hack to put the last tick end at the edge
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)

        def is_within_delta_percentage(start, current, end):
            # animation for stepping
            per = (current - start) / (end - start)
            return per > self.currentDelta / self.targetDelta

        for y in range(start_y + self.tick_step, end_y, self.tick_step):
            if is_within_delta_percentage(start_y, y, end_y):
                break
            arcade.draw_commands.draw_line(start_x - self.axis_size, y, start_x + self.axis_size, y,
                                           arcade.color.GRAY, border_width=4)

        # x axis
        start_x, start_y = 100, 100
        end_x, end_y = 600 + 10, 100        # simple hack to put the last tick end at the edge
        arcade.draw_commands.draw_line(start_x, start_y, end_x, end_y,
                                       arcade.color.BLACK, border_width=10)

        for x in range(start_x + self.tick_step, end_x + self.tick_step, self.tick_step):
            if is_within_delta_percentage(start_x, x, end_x):
                break

            arcade.draw_commands.draw_line(x, start_y - self.axis_size, x, start_y + self.axis_size,
                                           arcade.color.GRAY, border_width=4)

        self.currentDelta += 0.1
        self.currentDelta = min(self.currentDelta, self.targetDelta)

    def _get_pos_in_coord(self, x, y):
        return (self.x_axis[0] + (x * self.tick_step),
                self.y_axis[1] + (y * self.tick_step))

    def _draw_point(self, x, y):
        offset = 10
        pixel_x, pixel_y = self._get_pos_in_coord(x, y)

        text = "({}, {})".format(x, 10 - y)
        arcade.draw_commands.draw_circle_filled(pixel_x, pixel_y, 5, arcade.color.BLACK)
        arcade.draw_text(text, pixel_x, pixel_y + offset,
                         font_size=16, color=arcade.color.BLACK, anchor_x="center", align="center", anchor_y="bottom")

    def animation3_draw(self):
        self._draw_graph()

        self._draw_point(1, 10)
        self._draw_point(5, 5)
        self._draw_point(14, 3)

    def animation4_draw(self):
        self._draw_graph()

        def draw_sprite(sprite, x, y):
            offset = 10
            self._draw_point(x, y)
            pixel_x, pixel_y = self._get_pos_in_coord(x, y)
            sprite.left, sprite.top = pixel_x - offset, pixel_y + offset
            sprite.draw()

        draw_sprite(self.mario_sprite, 14, 3)
        draw_sprite(self.mario_box, 5, 5)
        draw_sprite(self.mario_score, 1, 10)


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
