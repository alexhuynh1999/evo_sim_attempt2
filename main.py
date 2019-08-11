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

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(b)
        self.rect = self.image.get_rect()
        self.x_vel = 5
        self.y_vel = 5

    def update(self):
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        if self.rect.y > height or self.rect.y < 0:
            self.y_vel = -self.y_vel
        if self.rect.x > width or self.rect.x < 0:
            self.x_vel = -self.x_vel


block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Creating blocks
for x in range(10):
    block = Block(b, 50, 50)
    block.rect.x = random.randrange(width)
    block.rect.y = random.randrange(height)
    block_list.add(block)
    all_sprites_list.add(block)


# Running the game
on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    display.fill(w)
    #print(event)
    block_list.update()
    all_sprites_list.draw(display)

    pygame.display.update()
    clock.tick(60)
