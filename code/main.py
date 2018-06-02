import pygame
import random

screen_resolution = [1050, 500]
display = pygame.display.set_mode(screen_resolution)
isRunning = True

clock = pygame.time.Clock()

hero = pygame.image.load("hero.png")
hero.set_colorkey([255, 128, 128])
hero_pos = [0, 0]
hero_unhappy = pygame.image.load("unhappy-hero.png")
hero_unhappy.set_colorkey([255, 128, 128])
hero_is_alive = True

class GameObject:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.image.convert()
        self.image.set_colorkey([255, 128, 128])

    def update(self):
        pass
    
    def draw(self, display):
        display.blit(self.image, [self.x, self.y]) 

class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, "enemy.png")
        self.speed = 10

    def update(self):
        self.x -= self.speed

enemies = []
for i in range(10):
    new_enemy = Enemy(random.randint(1000, 5000), random.randint(0, 500))
    enemies.append(new_enemy)

while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False

    display.fill([0, 0, 0])

    keys = pygame.key.get_pressed()
    
    if hero_is_alive:
        speed = 3
        if keys[pygame.K_LEFT]:
            hero_pos[0] -= speed
        if keys[pygame.K_RIGHT]:
            hero_pos[0] += speed
        if keys[pygame.K_DOWN]:
            hero_pos[1] += speed
        if keys[pygame.K_UP]:
            hero_pos[1] -= speed
    
    hero_pos[0] = max(0, hero_pos[0])
    hero_pos[1] = max(0, hero_pos[1])
    hero_pos[0] = min(screen_resolution[0] - hero.get_width(), hero_pos[0])
    hero_pos[1] = min(screen_resolution[1] - hero.get_height(), hero_pos[1])
    
    for enemy in enemies:
        box1_pos = hero_pos
        box1_size = hero.get_size()
        box2_pos = enemy.x, enemy.y
        box2_size = enemy.image.get_size()
        
        collision = (box1_pos[0] + box1_size[0] > box2_pos[0] and
                     box1_pos[0] < box2_pos[0] + box2_size[0] and
                     box1_pos[1] + box1_size[1] > box2_pos[1] and
                     box1_pos[1] < box2_pos[1] + box2_size[1])
        if collision:
            # enemies.remove(enemy)
            hero_is_alive = False
            continue

    for enemy in enemies:
        enemy.update()
    
    if hero_is_alive:
        display.blit(hero, hero_pos)
    else:
        display.blit(hero_unhappy, hero_pos)
    
    for enemy in enemies:
        enemy.draw(display)
        
    
    pygame.display.update()
    clock.tick(120)

pygame.quit()