import pygame

from code.main import scene
from setting import *

class Projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = -5  # Speed of the projectile moving upwards
        self.hitbox = pygame.Rect(x, y, radius * 2, radius * 2)  # Create a square hitbox

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.y += self.speed  # Move the projectile upwards
        self.hitbox.topleft = (self.x - self.radius, self.y - self.radius)  # Update hitbox position

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_image = PLAYER_FRONT
        self.health = 100
        self.max_health = 100  # Maximum health
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load(self.current_image).convert_alpha(), 0, PLAYER_SIZE)
        self.hitbox = pygame.Rect(self.pos[0] + 45, self.pos[1] + 80, 50, 30)
        self.hitbox_combat = (self.pos[0] + 45, self.pos[1] + 15, 50, 95)
        self.speed = PLAYER_SPEED
        self.velocity_x = 0
        self.velocity_y = 0
        self.scene_num = 0
        self.collide_list = COLLIDE_LIST_LIVING_ROOM
        self.water_radius = 6
        self.bullets = []
        self.last_shot_time = 0  # Time of the last shot
        self.shoot_delay = 500  # Delay in milliseconds

    def draw_health_bar(self, screen):
        if scene == 3:
            # Draw the health bar background
            pygame.draw.rect(screen, (255, 0, 0), (self.pos.x + 20, self.pos.y - 20, 100, 10))  # Red background
            # Draw the current health
            health_width = (self.health / self.max_health) * 100  # Calculate health width
            pygame.draw.rect(screen, (0, 255, 0), (self.pos.x + 20, self.pos.y - 20, health_width, 10))  # Green health

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()
        if self.scene_num != 3:
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
        else:
            if keys[pygame.K_a]:
                self.velocity_x = -self.speed
            elif keys[pygame.K_d]:
                self.velocity_x = self.speed
            if keys[pygame.K_e]:
                current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
                if current_time - self.last_shot_time >= self.shoot_delay:  # Check if enough time has passed
                    # Create a new projectile at the player's position
                    new_projectile = Projectile(self.pos.x + 75, self.pos.y, self.water_radius, (0, 0, 255))  # Blue color
                    self.bullets.append(new_projectile)
                    self.last_shot_time = current_time  # Update the last shot time

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

        if temp_hitbox.colliderect(DOOR_TO_BASEMENT_HITBOX) and self.scene_num == 0: # This is what I put
            self.scene_num = 2
            self.pos = pygame.math.Vector2(700, self.pos.y)
            self.collide_list = COLLIDE_LIST_BASEMENT

        if self.scene_num == 2:
            self.pos

        if self.scene_num == 3:
            self.pos.y = 400
            self.current_image = PLAYER_DOWN
            self.collide_list = COLLIDE_LIST_COMBAT

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

        # Update projectiles
        for bullet in self.bullets:
            bullet.update()  # Move the projectile upwards

        return self.scene_num

    def draw_projectiles(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)  # Draw each projectile on the screen
            # pygame.draw.rect(screen, "red", bullet.hitbox, width=1)  # Draw the hitbox for each projectile
