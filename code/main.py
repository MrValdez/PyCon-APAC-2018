import pygame
import dataclasses
import random

resolution = [800, 600]
screen = pygame.display.set_mode(resolution)
isRunning = True

hero = pygame.image.load("hero.png")
hero.set_colorkey([255, 128, 128])
hero_pos = [0, 0]

@dataclasses.dataclass
class GameObject:
    x: int
    y: int
    image: pygame.Surface

class Villain(GameObject):
    def __init__(self, x, y):
        self.image = pygame.image.load("villain.png").convert()
        self.image.set_colorkey([255, 128, 128])
        self.x = x
        self.y = y
        self.speed = random.randint(3, 5)

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

villains = []
for i in range(100):
    x = random.randint(500, 2000)
    y = random.randint(0, 500)
    villains.append(Villain(x, y))

#sfx_collision = pygame.mixer.Sound("sfx.wav")

while isRunning:
    screen.fill([255, 0, 128])
    screen.fill([0xFF, 0xFF, 0x7F])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    speed = 10
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        hero_pos[0] += speed
    if keys[pygame.K_UP]:
        hero_pos[1] -= speed
    if keys[pygame.K_DOWN]:
        hero_pos[1] += speed

    for villain in villains:
        box1_pos = hero_pos
        box1_size = hero.get_size()
        box2_pos = [villain.x, villain.y]
        box2_size = villain.image.get_size()

        collision = (box1_pos[0] + box1_size[0] > box2_pos[0] and
                         box1_pos[0] < box2_pos[0] + box2_size[0] and
                         box1_pos[1] + box1_size[1] > box2_pos[1] and
                         box1_pos[1] < box2_pos[1] + box2_size[1])

        if collision:
            villains.remove(villain)
            #sfX_collision.play()

    for villain in villains:
        villain.update()

    screen.blit(hero, hero_pos)

    for villain in villains:
        villain.draw(screen)

    pygame.display.update()