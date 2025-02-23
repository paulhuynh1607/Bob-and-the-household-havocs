import pygame
import random
from setting import *

class WashingMachine:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.image = pygame.image.load(EVIL_WASHING_MACHINE).convert_alpha()  # Load your boss image
        self.hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.projectiles = []
        self.shoot_delay = 2000  # Time in milliseconds between shots
        self.last_shot_time = pygame.time.get_ticks()  # Track the last shot time
        self.teleport_delay = 3000  # Time in milliseconds between teleports
        self.last_teleport_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_health_bar(screen)

        for projectile in self.projectiles:
            projectile.draw(screen)

    def draw_health_bar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x - 40, self.y - 20, self.max_health/2, 10))  # Red background
        health_width = (self.health / self.max_health) * self.max_health
        pygame.draw.rect(screen, (0, 255, 0), (self.x - 40, self.y - 20, health_width/2, 10))  # Green health

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            # Create multiple bullets with offsets
            for offset in range(-50, 51, 50):  # Adjust the range and step for bullet spread
                projectile = Bullet(self.x + self.image.get_width() // 2 + offset,
                                    self.y + self.image.get_height(),
                                    5, (255, 0, 0))  # Red color
                self.projectiles.append(projectile)
            self.last_shot_time = current_time  # Update the last shot time

    def teleport(self):
        # Generate a random x-coordinate within the screen width
        self.x = random.randint(0, WIDTH - self.image.get_width())  # Assuming WIDTH is defined in setting
        self.hitbox.topleft = (self.x, self.y)  # Update hitbox position

    def update(self):
        self.shoot()  # Check if the boss should shoot
        current_time = pygame.time.get_ticks()
        if current_time - self.last_teleport_time >= self.teleport_delay:
            self.teleport()  # Teleport to a new random x-coordinate
            self.last_teleport_time = current_time  # Update the last teleport time

        # Update projectiles
        for projectile in self.projectiles:
            projectile.update()  # Move the projectile downwards

        # Remove projectiles that are off-screen
        self.projectiles = [p for p in self.projectiles if p.y < HEIGHT]  # Assuming HEIGHT is defined in setting

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0  # Prevent negative health


class Bullet:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5  # Speed of the projectile moving downwards
        self.hitbox = pygame.Rect(x - radius, y, radius * 2, radius * 2)  # Create a square hitbox

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.y += self.speed  # Move the projectile downwards
        self.hitbox.topleft = (self.x - self.radius, self.y)  # Update hitbox position
