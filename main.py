import pygame
import random
import math
import numpy as np

pygame.init()

# Display Settings
width = 800
height = 600
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
        self.x_vel = random.randrange(1, 10)
        self.y_vel = random.randrange(1, 10)
        self.vision = random.randrange(50, 250)
        self.id = Block.id
        Block.id += 1
        self.fitness = 0

    def update(self):
        fed = pygame.sprite.spritecollide(self, food_list, True)
        if fed:
            self.fitness += 1

        if self.rect.x > width - 25 or self.rect.x < 0:
            self.x_vel *= -1
        if self.rect.y > height - 25 or self.rect.y < 0:
            self.y_vel *= -1

        pygame.draw.circle(display,(255,0,0), (self.rect.x, self.rect.y), self.vision, 4)

        closest_food = []
        for food in food_list:
            x = food.rect.x
            y = food.rect.y
            d_x = self.rect.x - x
            d_y = self.rect.y - y
            dist = math.sqrt(d_x ** 2 + d_y ** 2)
            if dist < self.vision:
                closest_food.append((food, dist, d_x, d_y))
        closest_food.sort(key=sortSecond)
        projection = [self.x_vel, self.y_vel]
        if len(closest_food) >= 1:
            x, y = closest_food[0][2], closest_food[0][3]
            length = closest_food[0][1]
            norm = (x / length, y / length)
            speed = (self.x_vel, self.y_vel)
            dot = round(np.dot(norm, speed))
            if dot == 0:
                projection[0] = 0
            elif dot == 1:
                projection[1] = 0
            else:
                projection = [norm[0] * dot + 1 * np.sign(norm[0] * dot), norm[1] * dot + 1 * np.sign(norm[1] * dot)]

        self.rect.x += projection[0]
        self.rect.y += projection[1]


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
