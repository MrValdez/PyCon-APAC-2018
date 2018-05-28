import arcade
from helper import (flip_y,
                    Text,
                    SlideTemplate,
                    GameState,
                    Avatar)

from hack import Image

"""
collision = (box1_pos[0] + box1_size[0] > box2_pos[0] and
             box1_pos[0] < box2_pos[0] + box2_size[0] and
             box1_pos[1] + box1_size[1] > box2_pos[1] and
             box1_pos[1] < box2_pos[1] + box2_size[1])
"""

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

        self.animations = [self.animation1_draw, self.animation2_draw, self.animation3_draw,
                           self.animation4_draw, self.animation5_draw, self.animation6_draw]

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
        self.monitor = Image(0, 0, "monitor.png", scale=0.8)

        animation5_text = """Some game libraries (such as Arcade) have their
Y axis origin at the bottom left.

The maths to flip the y-coordinates is just (height - y)"""
        kwargs = {"color": arcade.color.GRAY, "align": "left", "anchor_x": "left", "font_size": 15}
        self.coordinate_note = Text(400, 400, animation5_text, kwargs=kwargs)

        self.resolution_text = Text(370, 330, "640 x 480\n800 x 600\n1024 x 768")

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

    def _draw_point(self, x, y, reverse_y_axis=False):
        offset = 10
        pixel_x, pixel_y = self._get_pos_in_coord(x, y)

        if reverse_y_axis:
            text = "({}, {})".format(x, y)
        else:
            text = "({}, {})".format(x, 10 - y)

        arcade.draw_commands.draw_circle_filled(pixel_x, pixel_y, 5, arcade.color.BLACK)
        arcade.draw_text(text, pixel_x, pixel_y + offset,
                         font_size=16, color=arcade.color.BLACK, anchor_x="center", align="center", anchor_y="bottom")

    def animation3_draw(self):
        self._draw_graph()

        self._draw_point(1, 10)
        self._draw_point(5, 6)
        self._draw_point(14, 3)

    def _draw_sprite(self, sprite, x, y, reverse_y_axis=False):
        offset = 10
        self._draw_point(x, y, reverse_y_axis)
        pixel_x, pixel_y = self._get_pos_in_coord(x, y)
        sprite.left, sprite.top = pixel_x - offset, pixel_y + offset
        sprite.draw()

    def animation4_draw(self):
        self._draw_graph()

        self._draw_sprite(self.mario_sprite, 14, 3)
        self._draw_sprite(self.mario_box, 5, 6)
        self._draw_sprite(self.mario_score, 1, 10)

    def animation5_draw(self):
        self._draw_graph()

        self._draw_sprite(self.mario_sprite, 14, 3, reverse_y_axis=True)
        self._draw_sprite(self.mario_box, 5, 6, reverse_y_axis=True)
        self._draw_sprite(self.mario_score, 1, 10, reverse_y_axis=True)

        self.coordinate_note.draw()

    def animation6_draw(self):
        self.monitor.left, self.monitor.top = 120, 400

        self.monitor.draw()
        self._draw_graph()
        self.resolution_text.draw()

class Slide3(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics - Collision Detection"

        slides = [[
                   Image(620, flip_y(WindowSize, 130), "mario_monster.jpg", scale=0.7),
                   Image(100, flip_y(WindowSize, 170), "mario_sprite.jpg", scale=0.45),
                   Text(50, flip_y(WindowSize, 70), """- Collision Detection is the algorithm used to see if two sprites intersects
- A sprite is an image of a game object"""),
                   ],
                  [
                   Image(620, flip_y(WindowSize, 130), "mario_monster.jpg", scale=0.7),
                   Image(100, flip_y(WindowSize, 170), "mario_sprite.jpg", scale=0.45),
                   Text(50, flip_y(WindowSize, 70), """- Are these two sprites touching?
- How can the computer tell that these sprites are touching?"""),],
                  [
                   Image(620, flip_y(WindowSize, 130), "mario_monster.jpg", scale=0.7),
                   Image(100, flip_y(WindowSize, 170), "mario_sprite.jpg", scale=0.45),
                   Text(50, flip_y(WindowSize, 70), """- Are these two sprites touching?
- How can the computer tell that these sprites are touching?
- We can use maths to detect if they touched. """),],
                  [Image(620, flip_y(WindowSize, 130), "mario_monster.jpg", scale=0.7, border=1),
                   Image(100, flip_y(WindowSize, 170), "mario_sprite.jpg", scale=0.45, border=1),
                   Text(50, flip_y(WindowSize, 70), """- To simplify the maths, sprites are represented by the computer as rectangles"""),],
                  [Image(620, flip_y(WindowSize, 130), "mario_monster.jpg", scale=0.7, border=1),
                   Image(600, flip_y(WindowSize, 170), "mario_sprite.jpg", scale=0.45, border=1, transition="left", transition_distance=500),
                   Text(50, flip_y(WindowSize, 70), """- If the rectangle overlaps, it means there is a collision. An event is triggered
- Events are anything that can affect the game state"""),],
                  [Image(620, flip_y(WindowSize, 130), "mario_monster.jpg", scale=0.7),
                   Image(530, flip_y(WindowSize, 160), "mario_lose.png", scale=3),
                   Text(50, flip_y(WindowSize, 70), """- The event here, according to the game rules, is that Mario loses."""),],
                  [Text(50, flip_y(WindowSize, 70), """- The formula to check if two rectangles have collided is:"""),],
                  [Text(50, flip_y(WindowSize, 70), """- The formula to check if two rectangles have collided is:"""),
                   Text(55, flip_y(WindowSize, 70), """
(box1.x + box1.width >= box2.x and
 box1.x <= box2.x + box2.width and
 box1.y + box1.height >= box2.y and
 box1.y <= box2.y + box2.height)
""", kwargs={"font_size": 30, "font_name": "consolas"})],
                  [Text(50, flip_y(WindowSize, 70), """- The formula to check if two rectangles have collided is:"""),
                   Text(55, flip_y(WindowSize, 70), """
(box1.x + box1.width >= box2.x and
 box1.x <= box2.x + box2.width and
 box1.y + box1.height >= box2.y and
 box1.y <= box2.y + box2.height)
""", kwargs={"font_size": 30, "font_name": "consolas"}),
                   Text(50, flip_y(WindowSize, 350), """- Note that this formula is when (0, 0) is at top-left.""", kwargs={"italic": True})],
                 [Text(50, flip_y(WindowSize, 70), """- If (0, 0) is at lower-left, use this formula:"""),
                   Text(55, flip_y(WindowSize, 70), """
(box1.x + box1.width >= box2.x and
 box1.x <= box2.x + box2.width and
 box1.y - box1.height <= box2.y and
 box1.y >= box2.y - box2.height)
""", kwargs={"font_size": 30, "font_name": "consolas"}),]
                 ]

        super().__init__(WindowSize, title, subtitle, slides)


class Slide4(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics - Collision Detection - DEMO"
        slides = []

        super().__init__(WindowSize, title, subtitle, slides)

    def load(self):
        super().load()

        formula_text  = """(box1.x + box1.width >= box2.x and

 box1.x <= box2.x + box2.width and

 box1.y + box1.height >= box2.y and

 box1.y <= box2.y + box2.height)"""
        kwargs = {"font_size": 20, "font_name": "consolas", "color": arcade.color.BLACK, "align": "left", "anchor_x": "left", }
        self.formula = Text(105, flip_y(self.WindowSize, 170), formula_text, kwargs=kwargs)

        kwargs = {"font_size": 12, "color": arcade.color.BLACK, "align": "left", "anchor_x": "left", }
        self.instruction = Text(305, flip_y(self.WindowSize, 150), "Move using WASD and arrow keys. SPACE to go to next slide", kwargs=kwargs)

        self.check1 = Text(75, flip_y(self.WindowSize, 200), "\N{heavy check mark}", kwargs=kwargs)
        self.check2 = Text(75, flip_y(self.WindowSize, 260), "\N{heavy check mark}", kwargs=kwargs)
        self.check3 = Text(75, flip_y(self.WindowSize, 320), "\N{heavy check mark}", kwargs=kwargs)
        self.check4 = Text(75, flip_y(self.WindowSize, 380), "\N{heavy check mark}", kwargs=kwargs)

        self.mario = Avatar("mario_sprite.jpg", 0.45)
        self.mario.left = 300
        self.mario.top = 130
        self.bowser = Avatar("mario_monster.jpg", 0.7)
        self.bowser.left = 700
        self.bowser.top = 300

    def draw(self):
        super().draw()

        self.instruction.draw()

        border = 1
        for sprite in [self.bowser, self.mario]:
            arcade.draw_lrtb_rectangle_filled(sprite.left - border, sprite.right + border,
                                              sprite.top + border, sprite.bottom - border,
                                              arcade.color.BLACK)
            sprite.draw()

        self.formula.draw()

        data = (self.mario.left, self.mario.width, self.bowser.left,
                self.mario.left, self.bowser.left, self.bowser.width,
                flip_y(self.WindowSize, self.mario.top), self.mario.height, flip_y(self.WindowSize, self.bowser.top),
                flip_y(self.WindowSize, self.mario.top), flip_y(self.WindowSize, self.bowser.top), self.bowser.height,)
        introspection_text = """ {:^6}   {:^10}    {:^6}

 {:^6}    {:^6}   {:^10}

 {:^6}  {:^11}     {:^6}

 {:^6}    {:^6}   {:^12}""".format(*data)
        kwargs = {"font_size": 20, "font_name": "consolas", "color": arcade.color.BLUE, "align": "left", "anchor_x": "left", }
        introspection = Text(105, flip_y(self.WindowSize, 195), introspection_text, kwargs=kwargs)
        introspection.draw()

        if self.mario.left + self.mario.width >= self.bowser.left:
            self.check1.draw()
        if self.mario.left <= self.bowser.left + self.bowser.width:
            self.check2.draw()
        if flip_y(self.WindowSize, self.mario.top) + self.mario.height >= flip_y(self.WindowSize, self.bowser.top):
#        if self.mario.top - self.mario.height <= self.bowser.top:
            self.check3.draw()
        if flip_y(self.WindowSize, self.mario.top) <= flip_y(self.WindowSize, self.bowser.top) + self.bowser.height:
#        if self.mario.top >= self.bowser.top - self.bowser.height:
            self.check4.draw()

    def update(self, delta_time):
        self.mario.update()
        self.bowser.update()

        return self.gameState

    def on_key_press(self, key, modifiers):
        self.mario.move_WASD(key, modifiers, keydown=True)
        self.bowser.move(key, modifiers, keydown=True)

    def on_key_release(self, key, modifiers):
        self.mario.move_WASD(key, modifiers, keydown=False)
        self.bowser.move(key, modifiers, keydown=False)

        if key == arcade.key.SPACE:
            # we put this here to prevent skipping the next slide (if this was in on_key_press)
            self.gameState = GameState.FINISHED_STAGE

class Slide5(SlideTemplate):
    def __init__(self, WindowSize):
        title = "Stage 4"
        subtitle = "Mathematics - Collision Detection"
        slides = [
                    [Text(50, flip_y(WindowSize, 10), """- A key factor in good game design is to realize that you can use multiple collision boxes""", {"font_size": 15}),
                     Image(100, flip_y(WindowSize, 60), "hitbox1.jpg", scale=0.7),
                     Text(50, flip_y(WindowSize, 400), """Source: https://twitter.com/al_rikir/status/996638753241423872?s=21""", {"font_size": 10, "italic": True})],
                    [Text(50, flip_y(WindowSize, 10), """- A key factor in good game design is to realize that you can use multiple collision boxes""", {"font_size": 15}),
                     Image(100, flip_y(WindowSize, 60), "hitbox2.jpg", scale=1),
                     Text(50, flip_y(WindowSize, 400), """Source: https://twitter.com/al_rikir/status/996638753241423872?s=21""", {"font_size": 10, "italic": True})],
                    [Text(50, flip_y(WindowSize, 10), """- You can also make some collision boxes differently sized from the sprite to make
the game much more enjoyable.""", {"font_size": 15}),
                     Image(140, flip_y(WindowSize, 80), "mario_hitbox.png", scale=1.5),
                     Text(50, flip_y(WindowSize, 410), """Source: https://gamedev.stackexchange.com/a/57006/614""", {"font_size": 10, "italic": True})],
                 ]

        super().__init__(WindowSize, title, subtitle, slides)
