import arcade
from helper import (flip_y,
                    Text,
                    GameState,
                    Screen)

class IntroScreen(Screen):
    def __init__(self, WindowSize):
        self.texts = [
            Text(WindowSize[0] / 2, flip_y(WindowSize, 110), "The source code for this presentation can be found at\nhttps://github.com/MrValdez/PyCon-APAC-2018"),
        ]

    def load(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.gameState = GameState.RUNNING

    def update(self, delta_time):
        return self.gameState

    def draw(self):
        for text in self.texts:
            text.draw()

    def on_key_press(self, key, modifiers):
        self.gameState = GameState.NEXT_STAGE