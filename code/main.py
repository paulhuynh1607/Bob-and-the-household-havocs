import pygame
from sys import exit
import math
from setting import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bob and The House Hold Havoc")
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("assets/background/streetOne.png").convert(), (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load("assets/Entities/bob.png").convert_alpha(), 0, PLAYER_SIZE)
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.speed = PLAYER_SPEED

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        elif keys[pygame.K_s]:
            self.velocity_y = self.speed
        elif keys[pygame.K_a]:
            self.velocity_x = -self.speed
        elif keys[pygame.K_d]:
            self.velocity_x = self.speed

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)

    def update(self):
        self.user_input()
        self.move()

player = Player()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(player.image, player.pos)
    player.update()

    pygame.display.update()
    clock.tick(FPS)

