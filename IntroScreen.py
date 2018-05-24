import arcade
from helper import (flip_y,
                    Text,
                    GameState,
                    Screen)

class IntroScreen(Screen):
    def __init__(self, WindowSize):
        self.texts = [
            Text(WindowSize[0] / 2, flip_y(WindowSize, 110), "The source code for this presentation can be found at\nhttps://github.com/MrValdez/PyCon-APAC-2018"),
            Text(WindowSize[0] / 2, 0, """Anyone can make a game...

It just take a lot of effort.

In this talk, MrValdez will be introducing the basics of Game Programming.

By the end, we would have enough to make a simple game.




But he can't do it alone.

He'll need your help.




3 volunteers from the audience to help:



Two artists.    One player.



This is the one hour story of how PyCon APAC 2018 made a game.
"""),
        ]
        self.WindowSize = WindowSize

        artist1 = arcade.Sprite("crono_back.gif")
        artist1.center_x = 375
        artist1.center_y = -660
        
        artist2 = arcade.Sprite("crono_back.gif")
        artist2.center_x = 475
        artist2.center_y = -660
        
        tester = arcade.Sprite("crono_back.gif")
        tester.center_x = 600
        tester.center_y = -660

        self.sprites = arcade.SpriteList()
        self.sprites.append(artist1)
        self.sprites.append(artist2)
        self.sprites.append(tester)

    def load(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.gameState = GameState.RUNNING
        self.scroll = 0
        self.start_timer = 4
        self.scroll_speed = 1
        self.end_timer = 3

        #debug values:
        #self.start_timer = 0
        #self.scroll_speed = 3

    def update(self, delta_time):
        if self.start_timer > 0:
            # wait for timer to clear to start scrolling
            self.start_timer -= delta_time
            return

        left = 0
        right = self.WindowSize[0]
        bottom = 0
        top = self.WindowSize[1]

        self.scroll += self.scroll_speed
        bottom -= self.scroll
        top -= self.scroll

        if bottom > -1000:
            arcade.set_viewport(left, right, bottom, top)
        else:
            # we reached the end of the scrolling. start a timer to end the intro screen
            self.end_timer -= delta_time
            if self.end_timer < 0:
                return GameState.NEXT_STAGE

        return self.gameState

    def draw(self):
        for text in self.texts:
            text.draw()

        self.sprites.draw()