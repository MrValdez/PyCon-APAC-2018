import arcade
import random
from helper import (flip_y,
                    Text,
                    GameState,
                    Screen,
                    Avatar)

# Assets taken from:
#  https://opengameart.org/content/lpc-cliffsmountains-with-grass-top-and-more
#  (Lanea Zimmerman ("Sharm"), Daniel Eddeland, and Wiliam Thompson)

class Stage1(Screen):
    def __init__(self, WindowSize):
        self.texts = [
            Text(10, flip_y(WindowSize, 20), "Stage 1", {"font_name": "Georgia", "font_size": 40, "bold": True, "anchor_x": "left", "align": "left"}),
        ]
        self.WindowSize = WindowSize

        self.avatar = Avatar("crono_back.gif")
        self.avatar.center_x = 860
        self.avatar.center_y = 120

        self.sprites = arcade.SpriteList()
        self.sprites.append(self.avatar)

        self.walls = arcade.SpriteList()

        top_row = list(zip(range(20, 1024, 90), [500] * 15))
        for i in range(len(top_row)):
            left = top_row[i][0]
            top = top_row[i][1] + random.randint(-10, 10)
            top_row[i] = (left, top)
        for pos in top_row:
            wall = arcade.Sprite("LPC_cliffs_grass.png", image_x=15, image_y=288 - 175 - 100, image_width=65, image_height=120, scale=1.6)
            wall.left = pos[0] 
            wall.top = pos[1]
            self.walls.append(wall)


        right_row = [[903, 410], 
                     #[920, 410 - 240 + 20]
                     ]
        for pos in right_row:
            wall = arcade.Sprite("LPC_cliffs_grass.png", image_x=95, image_y=288 - 130 - 150, image_width=75, image_height=120, scale=2.2)
            wall.left = pos[0]
            wall.top = pos[1]
            self.walls.append(wall)

        bottom_row = list(zip(range(20, 1024, 90), [50] * 15))
        left_row = list(zip([10] * 15, range(50, 500, 200)))
        left_row.reverse()

        for pos in left_row + bottom_row:
            wall = arcade.Sprite("LPC_cliffs_grass.png", image_x=174, image_y=288 - 175 - 100, image_width=80, image_height=140, scale=2)
            wall.left = pos[0]
            wall.top = pos[1]
            self.walls.append(wall)

        self.physics = arcade.PhysicsEngineSimple(self.avatar, self.walls)

        self.floor = arcade.SpriteList()
        cave = arcade.Sprite("LPC_cliffs_grass.png", image_x=1, image_y=288 - 140, image_width=30, image_height=45, scale=2.4)
        target_cliff = top_row[3]
        cave.left = target_cliff[0] + 14
        cave.top = target_cliff[1] - 83
        self.floor.append(cave)

    def load(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.gameState = GameState.RUNNING

    def update(self, delta_time):
#        self.sprites.update()
        self.physics.update()
        return self.gameState

    def draw(self):
        self.walls.draw()
        self.sprites.draw()
        self.floor.draw()

        arcade.draw_lrtb_rectangle_filled(0, self.WindowSize[0], flip_y(self.WindowSize, 0), flip_y(self.WindowSize, 100), arcade.color.BLACK)

        for text in self.texts:
            text.draw()

    def on_key_press(self, key, modifiers):
        self.avatar.move(key, modifiers, keydown=True)

    def on_key_release(self, key, modifiers):
        self.avatar.move(key, modifiers, keydown=False)