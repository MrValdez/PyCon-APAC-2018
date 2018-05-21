import arcade
from helper import (flip_y,
                    Text,
                    GameState)
from TitleScreen import TitleScreen
from FadeScreen import FadeScreen
from IntroScreen import IntroScreen

WindowSize = (800, 600)

class Avatar(arcade.Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 10

    def update(self):
        super().update()

    def move(self, key, modifier, keydown):
        speed = self.speed
        if not keydown:
            speed *= -1

        if key == arcade.key.UP:
            self.change_y += speed
        if key == arcade.key.DOWN:
            self.change_y += -speed
        if key == arcade.key.LEFT:
            self.change_x += -speed
        if key == arcade.key.RIGHT:
            self.change_x += speed


class Engine(arcade.Window):
    def __init__(self):
        super().__init__(*WindowSize, title = "PYCON APAC 2018")
        self.set_location(5, 30)
        arcade.set_background_color(arcade.color.AMAZON)

        self.stages = [TitleScreen(WindowSize),
                       IntroScreen(WindowSize)]

        self.WindowSize = WindowSize
        self.currentStage = self.stages[0]
        self.currentStage.load()
        self.fade = FadeScreen(WindowSize)
        self.gameState = GameState.RUNNING

    def setup(self):
        self.avatar = Avatar("crono_back.gif")
        self.avatar.center_x = WindowSize[0] / 2
        self.avatar.center_y = WindowSize[1] / 2
#        self.avatars = arcade.SpriteList()
#        self.avatars.append(self.avatar)

    def on_draw(self):
        arcade.start_render()

        self.currentStage.draw()
        self.avatar.draw()

        if self.gameState == GameState.NEXT_STAGE:
            self.fade.draw()

    def update(self, delta_time):
        if self.gameState == GameState.RUNNING:
            self.gameState = self.currentStage.update(delta_time)

            if self.gameState == GameState.NEXT_STAGE:
                # Start transition to fade out 
                self.fade.start_fade_out()

        self.avatar.update()
        
        if self.gameState == GameState.NEXT_STAGE:
            state = self.fade.update(delta_time)
            if state == GameState.FINISHED_STAGE:
                self.gameState = GameState.RUNNING
                new_stage = self.stages.index(self.currentStage) + 1
                new_stage %= len(self.stages)
                self.currentStage = self.stages[new_stage]
                self.currentStage.load()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.close()

        self.currentStage.on_key_press(key, modifiers)
        self.avatar.move(key, modifiers, keydown=True)

    def on_key_release(self, key, modifiers):
        self.avatar.move(key, modifiers, keydown=False)

def main():
    game = Engine()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()