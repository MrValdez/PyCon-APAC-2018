import arcade
from helper import (flip_y,
                    Text,
                    GameState)
from TitleScreen import TitleScreen
from FadeScreen import FadeScreen
from IntroScreen import IntroScreen

WindowSize = (1024, 600)

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
        self.currentStage = self.stages[1]
        self.currentStage.load()
        self.fade = FadeScreen(WindowSize)
        self.gameState = GameState.RUNNING

        self.debug = True

    def setup(self):
        self.avatar = Avatar("crono_back.gif")
        self.avatar.center_x = WindowSize[0] / 2
        self.avatar.center_y = WindowSize[1] / 2

    def on_draw(self):
        arcade.start_render()

        self.currentStage.draw()
        
        if self.debug:
            self.avatar.draw()
            print(self.avatar.position)     # used to check coordinate position. useful in placing elements for slides

        if self.gameState == GameState.NEXT_STAGE:
            self.fade.draw()

    def update(self, delta_time):
        if self.gameState == GameState.RUNNING:
            returned_game_state = self.currentStage.update(delta_time)
            if returned_game_state in GameState:
                self.gameState = returned_game_state

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
                self.change_stage(new_stage)

    def change_stage(self, new_stage_index):
        self.currentStage = self.stages[new_stage_index]
        self.currentStage.load()

        arcade.set_viewport(0, WindowSize[0], 0, WindowSize[1])
    
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