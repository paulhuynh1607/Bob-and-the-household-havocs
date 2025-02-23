import pygame
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
        self.images = {
            'back': [PLAYER_DOWN, PLAYER_DOWN1, PLAYER_DOWN2, PLAYER_DOWN3, PLAYER_DOWN4] ,  # Add your images for moving down
            'left': [PLAYER_LEFT, PLAYER_LEFT1, PLAYER_LEFT2, PLAYER_LEFT3, PLAYER_LEFT4],   # Add your images for moving left
            'right': [PLAYER_RIGHT, PLAYER_RIGHT1, PLAYER_RIGHT2, PLAYER_RIGHT3, PLAYER_RIGHT4], # Add your images for moving right
            'front': [PLAYER_FRONT, PLAYER_FRONT1, PLAYER_FRONT2, PLAYER_FRONT3, PLAYER_FRONT4] # Add your images for moving up
        }
        self.current_image = self.images['front'][0]  # Start with the first image for moving down
        self.image_index = 0  # Index for the current image
        self.health = 100
        self.max_health = 100
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load(self.current_image).convert_alpha(), 0, PLAYER_SIZE)
        self.hitbox = pygame.Rect(self.pos[0] + 45, self.pos[1] + 80, 50, 30)
        self.hitbox_combat = (self.pos[0] + 45, self.pos[1] + 15, 50, 95)
        self.hitbox_combat = (self.pos[0] + 45, self.pos[1], 50, 95)
        self.speed = PLAYER_SPEED
        self.velocity_x = 0
        self.velocity_y = 0
        self.scene_num = 0
        self.collide_list = COLLIDE_LIST_LIVING_ROOM
        self.water_radius = 6
        self.bullets = []
        self.last_shot_time = 0
        self.shoot_delay = 500
        self.player_state = "front"

        # Animation variables
        self.animation_timer = 0
        self.animation_delay = 200  # Time in milliseconds to switch images
        self.is_moving = False  # Track if the player is moving

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0
        keys = pygame.key.get_pressed()

        if self.scene_num != 3:
            if keys[pygame.K_w]:
                self.velocity_y = -self.speed
                self.player_state = "back"
                self.is_moving = True
            elif keys[pygame.K_s]:
                self.velocity_y = self.speed
                self.player_state = "front"
                self.is_moving = True
            elif keys[pygame.K_a]:
                self.velocity_x = -self.speed
                self.player_state = "left"
                self.is_moving = True
            elif keys[pygame.K_d]:
                self.velocity_x = self.speed
                self.player_state = "right"
                self.is_moving = True
            else:
                self.is_moving = False  # Not moving

        else:
            if keys[pygame.K_a]:
                self.velocity_x = -self.speed
                self.player_state = "back"
                self.is_moving = True
            elif keys[pygame.K_d]:
                self.velocity_x = self.speed
                self.player_state = "back"
                self.is_moving = True
            if keys[pygame.K_e]:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_shot_time >= self.shoot_delay:
                    new_projectile = Projectile(self.pos.x + 75, self.pos.y, self.water_radius, (0, 0, 255))
                    self.bullets.append(new_projectile)
                    self.last_shot_time = current_time


    def draw_health_bar(self, screen):
        if self.scene_num == 3:
            # Draw the health bar background
            pygame.draw.rect(screen, (255, 0, 0), (self.pos.x + 20, self.pos.y - 20, 100, 10))  # Red background
            # Draw the current health
            health_width = (self.health / self.max_health) * 100  # Calculate health width
            pygame.draw.rect(screen, (0, 255, 0), (self.pos.x + 20, self.pos.y - 20, health_width, 10))  # Green health



    def move(self, collide_list):
        # Create a temporary hitbox for the next position
        temp_hitbox = self.hitbox.move(self.velocity_x, self.velocity_y)

        if temp_hitbox.colliderect(DOOR_TO_BASEMENT_HITBOX) and self.scene_num == 0: # This is what I put
            print(self.scene_num)
            self.scene_num = 2
            self.pos = pygame.math.Vector2(700, self.pos.y)
            self.collide_list = COLLIDE_LIST_BASEMENT

        if temp_hitbox.colliderect(KITCHEN_HITBOX) and self.scene_num == 0:
            self.scene_num = 1
            self.pos = pygame.math.Vector2(20, self.pos.y)
            self.collide_list = COLLIDE_LIST_KITCHEN

        if temp_hitbox.colliderect(LIVING_ROOM_HITBOX) and self.scene_num == 1:
            self.scene_num = 0
            self.pos = pygame.math.Vector2(700, self.pos.y)
            self.collide_list = COLLIDE_LIST_LIVING_ROOM



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

    def update(self):
        self.user_input()
        self.move(self.collide_list)

        # Update projectiles
        for bullet in self.bullets:
            bullet.update()  # Move the projectile upwards

        # Handle animation
        if self.is_moving:
            current_time = pygame.time.get_ticks()
            if current_time - self.animation_timer >= self.animation_delay:
                if not len(self.images[self.player_state]) - 1 == self.image_index:
                    self.image_index = (self.image_index + 1)  # Cycle through images
                    self.animation_timer = current_time  # Reset the timer
                else:
                    self.image_index = 0
        else:
            self.image_index = 0  # Reset to the first image when not moving

        self.current_image = self.images[self.player_state][self.image_index]
        self.image = pygame.transform.rotozoom(pygame.image.load(self.current_image).convert_alpha(), 0, PLAYER_SIZE)

        return self.scene_num

    def draw_projectiles(self, screen, boss):
        for bullet in self.bullets:
            bullet.draw(screen)  # Draw each projectile on the screen
            # Check for collisions with boss projectiles
            for boss_projectile in boss.projectiles:
                if bullet.hitbox.colliderect(boss_projectile.hitbox):
                    # Deal damage or perform any action on collision
                    self.health -= 10  # Example: player takes damage
                    boss_projectile.y = 600  # Move the boss projectile off-screen
                    self.bullets.remove(bullet)  # Remove the player's bullet after collision
                    break  # Exit the loop after handling the collision
