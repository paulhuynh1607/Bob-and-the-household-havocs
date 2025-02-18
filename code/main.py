import pygame
from sys import exit
import math
from setting import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bob and The House Hold Havoc")
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load(FLOOR).convert(), (WIDTH, HEIGHT))
wall = pygame.transform.scale(pygame.image.load(WALL).convert(), (WIDTH, 100))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_image = PLAYER_FRONT
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load(self.current_image).convert_alpha(), 0, PLAYER_SIZE)
        self.base_player_image = self.image
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.speed = PLAYER_SPEED


    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.speed = PLAYER_SPEED * 2
        else:
            self.speed = PLAYER_SPEED
        if keys[pygame.K_w]:
        if keys[pygame.K_w]:
            self.current_image = PLAYER_DOWN
            self.velocity_y = -self.speed
        elif keys[pygame.K_s]:
            self.current_image = PLAYER_FRONT
            self.velocity_y = self.speed
        elif keys[pygame.K_a]:
            self.current_image = PLAYER_LEFT
            self.velocity_x = -self.speed
        elif keys[pygame.K_d]:
            self.current_image = PLAYER_RIGHT
            self.velocity_x = self.speed

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center

    def update(self):
        self.image = pygame.transform.rotozoom(pygame.image.load(self.current_image).convert_alpha(), 0, PLAYER_SIZE)
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
    screen.blit(wall, (0, 0))
    screen.blit(player.image, player.rect)
    player.update()
    pygame.draw.rect(screen, "red", player.hitbox_rect, width=2)

    pygame.display.update()
    clock.tick(FPS)

