import pygame
import random

pygame.init()

# Display Settings
width = 1600
height = 900
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Evolution Simulator Attempt 2')
clock = pygame.time.Clock()
# Color
b = (0, 0, 0)
w = (255, 255, 255)


class Block(pygame.sprite.Sprite):
    id = 0

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([25,25])
        self.image.fill(
            (random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255))
        )
        self.rect = self.image.get_rect()
        self.x_vel = random.randrange(-10, 10)
        self.y_vel = random.randrange(-10,10)
        self.id = Block.id
        Block.id += 1

    # Fun buggy physics, but not particularly useful for what I want to do.
    # def hascollided(self, box):
    #     # Collisions in the x-direction
    #     if (self.x_vel > 0 and box.x_vel < 0) or (self.x_vel < 0 and box.x_vel > 0):
    #         self.x_vel *= -1
    #         box.x_vel *= -1
    #     # Wonky physics, but at least the momentum is conserved
    #     xp = self.x_vel + box.x_vel
    #     if self.x_vel > 0 and box.x_vel > 0:
    #         if self.x_vel > box.x_vel:
    #             box.x_vel = 0.75 * xp
    #             self.x_vel = 0.25 * xp
    #         else:
    #             box.x_vel = 0.25 * xp
    #             self.x_vel = 0.75 * xp
    #     if self.x_vel < 0 and box.x_vel < 0:
    #         if self.x_vel > box.x_vel:
    #             box.x_vel = 0.25 * xp
    #             self.x_vel = 0.75 * xp
    #         else:
    #             box.x_vel = 0.75 * xp
    #             self.x_vel = 0.25 * xp
    #
    #     if self.y_vel > 0 and box.y_vel < 0 or self.y_vel < 0 and box.y_vel > 0:
    #         self.y_vel *= -1
    #         box.y_vel *= -1
    #     yp = self.y_vel + box.y_vel
    #     if self.y_vel > 0 and box.y_vel > 0:
    #         if self.y_vel > box.y_vel:
    #             box.y_vel = 0.75 * yp
    #             self.y_vel = 0.25 * yp
    #         else:
    #             box.y_vel = 0.25 * yp
    #             self.y_vel = 0.75 * yp
    #     if self.y_vel < 0 and box.y_vel < 0:
    #         if self.y_vel > box.y_vel:
    #             box.y_vel = 0.25 * yp
    #             self.y_vel = 0.75 * yp
    #         else:
    #             box.y_vel = 0.75 * yp
    #             self.y_vel = 0.25 * yp

    def update(self):
        # for box in block_list:
        #     if self.id == box.id:
        #         continue
        #
        #     collided = pygame.sprite.collide_rect(self, box)
        #     if collided:
        #       Block.hascollided(self, box)
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        if self.rect.x > width - 25 or self.rect.x < 0:
            self.x_vel *= -1
        if self.rect.y > height - 25 or self.rect.y < 0:
            self.y_vel *= -1


class Food(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([25,25])
        self.image.fill((139,69,19))
        self.rect = self.image.get_rect()

    def update(self):
        pygame.sprite.spritecollide(self,block_list, True)


all_sprites_list = pygame.sprite.Group()

# Creating blocks
block_list = pygame.sprite.Group()
for x in range(10):
    block = Block(b, 50, 50)
    block.rect.x = random.randrange(width - 25)
    block.rect.y = random.randrange(height - 25)
    block_list.add(block)
    all_sprites_list.add(block)
# Creating food
food_list = pygame.sprite.Group()
for x in range(25):
    food = Food(b, 50, 50)
    food.rect.x = random.randrange(width - 25)
    food.rect.y = random.randrange(height - 25)
    food_list.add(food)
    all_sprites_list.add(food)

# Running the sim
on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    display.fill(w)
    block_list.update()
    food_list.update()
    all_sprites_list.draw(display)

    pygame.display.update()
    clock.tick(60)
