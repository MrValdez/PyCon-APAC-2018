import arcade

SIZE = (800, 600)

def flip_y(y):
    return SIZE[1] - y

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


class Text:
    """ Helper class to have text with a default kwargs for this project """

    def __init__(self, x, y, text, kwargs=None):
        self.kwargs = {"color": arcade.color.WHITE,
                       "font_name": ("Arial"),
                       "font_size": 20,
                       "anchor_x": "center",
                       "anchor_y": "top",
                       "align": "center",
                       }

        self.kwargs["text"] = text
        self.kwargs["start_x"] = x
        self.kwargs["start_y"] = y

        if kwargs:
            self.kwargs.update(kwargs)

    def draw(self):
        arcade.draw_text(**self.kwargs)


class TitleScreen:
    def __init__(self):
        self.texts = [
            Text(SIZE[0] / 2, flip_y(110), "MrValdez", {"font_size": 60, "font_name": "Armalite Rifle"}),
            Text(SIZE[0] / 2, flip_y(190), "Game Programming with Python", {"font_size": 30}),
            Text(SIZE[0] / 2, flip_y(500), "Difficulty: Intermediate", {"italic": True}),
        ]

        self.start_text = Text(SIZE[0] / 2, flip_y(400), "Press any key")
        self.blink_time = 0.75
        self.blink = self.blink_time
        self.start_text_visible = True

    def update(self, delta_time):
        self.blink -= delta_time
        if self.blink < 0:
            self.blink += self.blink_time
            self.start_text_visible = not self.start_text_visible

    def draw(self):
        Text(SIZE[0] / 2, flip_y(400), "Difficulty: Intermediate"),

        for text in self.texts:
            text.draw()

        if self.start_text_visible:
            self.start_text.draw()


class Engine(arcade.Window):
    def __init__(self):
        super().__init__(*SIZE, title = "PYCON APAC 2018")
        self.set_location(5, 30)
        arcade.set_background_color(arcade.color.AMAZON)

        self.currentStage = TitleScreen()

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