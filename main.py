import arcade
from helper import (flip_y,
                    Text)
from TitleScreen import TitleScreen

SIZE = (800, 600)

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
        super().__init__(*SIZE, title = "PYCON APAC 2018")
        self.set_location(5, 30)
        arcade.set_background_color(arcade.color.AMAZON)

        self.currentStage = TitleScreen(SIZE)

    def setup(self):
        self.avatar = Avatar("crono_back.gif")
        self.avatar.center_x = SIZE[0] / 2
        self.avatar.center_y = SIZE[1] / 2
#        self.avatars = arcade.SpriteList()
#        self.avatars.append(self.avatar)

    def on_draw(self):
        arcade.start_render()

        self.currentStage.draw()
        self.avatar.draw()

    def update(self, delta_time):
        self.currentStage.update(delta_time)
        self.avatar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.close()

        self.avatar.move(key, modifiers, keydown=True)

    def on_key_release(self, key, modifiers):
        self.avatar.move(key, modifiers, keydown=False)

def main():
    game = Engine()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()