import arcade
from helper import (GameState,
                    Screen)

class FadeScreen(Screen):
    def __init__(self, WindowSize):
        self.WindowSize = WindowSize
        self.speed = 7
        self.start_fade_out()

    def start_fade_in(self):
        self.alpha = 255
        self.fade_in = False

    def start_fade_out(self):
        self.alpha = 0
        self.fade_in = True

    def update(self, delta_time):
        if self.fade_in:
            self.alpha += self.speed
        else:
            self.alpha -= self.speed

        self.alpha = max(min(self.alpha, 255), 0)

        if self.fade_in and self.alpha >= 255:
            return GameState.FINISHED_STAGE
        if not self.fade_in and self.alpha <= 0:
            return GameState.FINISHED_STAGE

    def draw(self):
        color = [0, 0, 0, self.alpha]
        arcade.draw_lrtb_rectangle_filled(0, self.WindowSize[0], self.WindowSize[1], 0, color)
