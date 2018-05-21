import arcade
from helper import (flip_y,
                    Text,
                    GameState,
                    Avatar)
from TitleScreen import TitleScreen
from FadeScreen import FadeScreen
from IntroScreen import IntroScreen
from Stage1 import Stage1
from Stage2 import Stage2

WindowSize = (1024, 600)


class Engine(arcade.Window):
    def __init__(self):
        super().__init__(*WindowSize, title = "PYCON APAC 2018")
        self.set_location(5, 30)
        arcade.set_background_color(arcade.color.AMAZON)

        self.stages = [TitleScreen(WindowSize),
                       IntroScreen(WindowSize),
                       Stage1(WindowSize),
                       Stage2(WindowSize)]

        self.WindowSize = WindowSize
        self.currentStage = self.stages[0]
        self.currentStage = self.stages[3]      # debugging
        self.currentStage.load()
        self.fade = FadeScreen(WindowSize)
        self.gameState = GameState.RUNNING

        self.debug = False

    def setup(self):
        # This avatar is useful for debugging purposes.
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
        self.currentStage.on_key_release(key, modifiers)
        self.avatar.move(key, modifiers, keydown=False)

def main():
    game = Engine()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()