import pygame
import random

pygame.init()

# Display Settings
width = 1600
height = 900
display = pygame.display.set_mode((width, height))
day = 0
pygame.display.set_caption('Evolution Simulator | Day ' + str(day))
clock = pygame.time.Clock()
# Color
b = (0, 0, 0)
w = (255, 255, 255)


class Block(pygame.sprite.Sprite):
    id = 0

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(
            (random.randrange(0, 255),
             random.randrange(0, 255),
             random.randrange(0, 255))
        )
        self.rect = self.image.get_rect()
        self.x_vel = random.randrange(-10, 10)
        self.y_vel = random.randrange(-10, 10)
        self.id = Block.id
        Block.id += 1
        self.fitness = 0

    def update(self):
        fed = pygame.sprite.spritecollide(self, food_list, True)
        if fed:
            self.fitness += 1

        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        if self.rect.x > width - 25 or self.rect.x < 0:
            self.x_vel *= -1
        if self.rect.y > height - 25 or self.rect.y < 0:
            self.y_vel *= -1


class Food(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()


all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
food_list = pygame.sprite.Group()


def createFood(amount):
    for x in range(amount):
        food = Food(b, 50, 50)
        food.rect.x = random.randrange(width - 25)
        food.rect.y = random.randrange(height - 25)
        food_list.add(food)
        all_sprites_list.add(food)


# Creating blocks
for x in range(10):
    block = Block(b, 50, 50)
    block.rect.x = random.randrange(width - 25)
    block.rect.y = random.randrange(height - 25)
    block_list.add(block)
    all_sprites_list.add(block)
# Creating food
createFood(25)


def sortSecond(val):
    return val[1]


def thanos():
    fitnessgram = []
    for block in block_list:
        fitnessgram.append([block.id, block.fitness])
    fitnessgram.sort(key=sortSecond)
    dead = fitnessgram[:len(fitnessgram)//2]
    alive = fitnessgram[len(fitnessgram)//2:]
    dead_id = [id[0] for id in dead]
    for block in block_list:
        if block.id in dead_id:
            block.kill()


# Running the sim
on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    if len(food_list) == 0:
        thanos()
        createFood(25)
        day += 1
        pygame.display.set_caption('Evolution Simulator | Day ' + str(day))

    display.fill(w)
    block_list.update()
    all_sprites_list.draw(display)
    pygame.display.update()
    clock.tick(60)
