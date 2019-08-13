import pygame
import random

pygame.init()

# Display Settings
width = 1600
height = 1000
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
        self.image.fill(b)
        self.rect = self.image.get_rect()
        self.x_vel = random.randrange(-5,5)
        self.y_vel = random.randrange(-5,5)
        self.id = Block.id
        Block.id += 1

    def reverse(self):
        self.x_vel *= -1
        self.y_vel *= -1

    def update(self):
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        if self.rect.x > width - 25 or self.rect.x < 0:
            self.x_vel *= -1
        if self.rect.y > height - 25 or self.rect.y < 0:
            self.y_vel *= -1

        for box in block_list:
            if self.id == box.id:
                continue

            collided = pygame.sprite.collide_rect(self, box)
            if collided:
                Block.reverse(self)
                Block.reverse(box)


all_sprites_list = pygame.sprite.Group()

# Creating blocks
block_list = pygame.sprite.Group()
for x in range(10):
    block = Block(b, 50, 50)
    block.rect.x = random.randrange(width - 25)
    block.rect.y = random.randrange(height - 25)
    block_list.add(block)
    all_sprites_list.add(block)

# Running the sim
on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    display.fill(w)
    block_list.update()
    all_sprites_list.draw(display)

    pygame.display.update()
    clock.tick(60)
