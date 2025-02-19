import pygame
from sys import exit
import math
from pygame.locals import *
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_image = PLAYER_FRONT
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load(self.current_image).convert_alpha(), 0, PLAYER_SIZE)
        self.hitbox = pygame.Rect(self.pos[0] + 45, self.pos[1] + 80, 50, 30)
        self.hitbox_combat = (self.pos[0] + 45, self.pos[1] + 15, 50, 95)
        self.speed = PLAYER_SPEED
        self.velocity_x = 0
        self.velocity_y = 0
        self.scene_num = 0
        self.collide_list = COLLIDE_LIST_LIVING_ROOM

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()
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

    def move(self, collide_list):
        # Create a temporary hitbox for the next position
        temp_hitbox = self.hitbox.move(self.velocity_x, self.velocity_y)

        if temp_hitbox.colliderect(KITCHEN_HITBOX) and self.scene_num == 0:
            self.scene_num = 1
            self.pos = pygame.math.Vector2(20, self.pos.y)
            self.collide_list = COLLIDE_LIST_KITCHEN

        if temp_hitbox.colliderect(LIVING_ROOM_HITBOX) and self.scene_num == 1:
            self.scene_num = 0
            self.pos = pygame.math.Vector2(700, self.pos.y)
            self.collide_list = COLLIDE_LIST_LIVING_ROOM

        # Check for collisions with the collidable objects
        for cl in collide_list:
            if temp_hitbox.colliderect(cl):
                # Collision detected, do not move
                return

        # No collision, update position and hitbox
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
        self.hitbox.topleft = (self.pos[0] + 45, self.pos[1] + 80)
        self.hitbox_combat = (self.pos[0] + 45, self.pos[1] + 15, 50, 95)

    def update(self, scene_num):
        self.image = pygame.transform.rotozoom(pygame.image.load(self.current_image).convert_alpha(), 0, PLAYER_SIZE)
        self.user_input()
        self.move(self.collide_list)
        return self.scene_num

