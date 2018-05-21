import arcade
from helper import (flip_y,
                    Text,
                    GameState,
                    Screen,
                    Avatar)

class Stage1(Screen):
    def __init__(self, WindowSize):
        self.texts = [
            Text(10, flip_y(WindowSize, 20), "Stage 1", {"font_name": "Georgia", "font_size": 40, "bold": True, "anchor_x": "left", "align": "left"}),
        ]
        self.WindowSize = WindowSize

        self.avatar = Avatar("crono_back.gif")
        self.avatar.center_x = WindowSize[0] / 2
        self.avatar.center_y = WindowSize[1] / 2
        self.sprites = arcade.SpriteList()
        self.sprites.append(self.avatar)

    def load(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.gameState = GameState.RUNNING

    def update(self, delta_time):
        self.sprites.update()
        return self.gameState

    def draw(self):
        self.sprites.draw()

        arcade.draw_lrtb_rectangle_filled(0, self.WindowSize[0], flip_y(self.WindowSize, 0), flip_y(self.WindowSize, 100), arcade.color.BLACK)

        for text in self.texts:
            text.draw()

    def on_key_press(self, key, modifiers):
        self.avatar.move(key, modifiers, keydown=True)

    def on_key_release(self, key, modifiers):
        self.avatar.move(key, modifiers, keydown=False)