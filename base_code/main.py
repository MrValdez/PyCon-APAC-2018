import pygame
import random
#import android


class Entity:
    def __init__(self, image, pos):
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey([255, 255, 255])
        self.pos = list(pos)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.pos)

class cPlayer(Entity):
    def __init__(self):
        Entity.__init__(self, "player.png", [0, 0])

class cEnemy(Entity):
    def __init__(self):
        pos = [random.randint(600, 2000), random.randint(0, 300)]
        Entity.__init__(self, "enemy.png", pos)

    def update(self):
        self.pos[0] -= 1

class cBullet(Entity):
    def __init__(self, pos):
        Entity.__init__(self, "shot.png", pos)

    def update(self):
        self.pos[0] += 10


# pygame setup
pygame.init()
pygame.display.set_caption("Game Programming with Python")

resolution = [640, 480]
screen = pygame.display.set_mode(resolution)
time = pygame.time.Clock()

fontpath = pygame.font.get_default_font()
font = pygame.font.Font(fontpath, 12)

useJoystick = False

if useJoystick:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

#if joystick.get_axis(0) < -0.2:
#if hatposition=joystick.get_hat(0) == -1:
#    joystick.get_button(0)
keystate = pygame.key.get_pressed()
isRunning = True

# setup game objects
player = cPlayer()

enemyList = []
numberOfEnemies = 4

for i in range(numberofEnemies):
    newEnemy = cEnemy()
    enemyList.append(newEnemy)

bulletList = []

sfx = pygame.mixer.Sound('example.wav')
sfx.play()

# game loop
while isRunning:
    screen.fill([128, 128, 128])

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False

    #if android.check_pause():
    #    android.wait_for_resume()

    # inputs
    prevKeystate = keystate
    keystate = pygame.key.get_pressed()
    
    if keystate[pygame.K_ESCAPE]:
        isRunning = False

    if useJoystick:
        if pygame.joystick.Joystick(1).get_button(0):
            joy_x = pygame.joystick.Joystick(1).get_axis(0) * 32768
            joy_y = pygame.joystick.Joystick(1).get_axis(1) * 32768
            
            if joy_y < 480 / 2:
                player.pos[1] -= 1
            if joy_y > 480 / 2:
                player.pos[1] += 1

    if keystate[pygame.K_UP]:
        player.pos[1] -= 1
    if keystate[pygame.K_DOWN]:
        player.pos[1] += 1
    if keystate[pygame.K_SPACE] and not prevKeystate[pygame.K_SPACE]:
        newBullet = cBullet(player.pos)
        bulletList.append(newBullet)

    # collisions
    for bullet in bulletList:
        for enemy in enemyList:
            box1_pos = bullet.pos
            box1_size = bullet.image.get_size()
            box2_pos = enemy.pos
            box2_size = enemy.image.get_size()

            collision = (box1_pos[0] + box1_size[0] > box2_pos[0] and
                         box1_pos[0] < box2_pos[0] + box2_size[0] and
                         box1_pos[1] + box1_size[1] > box2_pos[1] and
                         box1_pos[1] < box2_pos[1] + box2_size[1])

            if collision:
                enemyList.remove(enemy)
                bulletList.remove(bullet)

    # updates
    player.update()
    
    for enemy in enemyList:
        enemy.update()
    for bullet in bulletList:
        bullet.update()

    # draws
    player.draw(screen)
    
    for enemy in enemyList:
        enemy.draw(screen)
    for bullet in bulletList:
        bullet.draw(screen)

    text = font.render("Hello World", True, [255, 255, 255])
    screen.blit(text, [0, 0])
    
    pygame.display.update()
    time.tick(60)

pygame.quit()
