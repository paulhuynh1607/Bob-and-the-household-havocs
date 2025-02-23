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
        self.shoot_delay = 1000  # Time in milliseconds between shots
        self.last_shot_time = pygame.time.get_ticks()  # Track the last shot time
        self.teleport_delay = 3000  # Time in milliseconds between teleports
        self.last_teleport_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_health_bar(screen)

        for projectile in self.projectiles:
            projectile.draw(screen)

    def draw_health_bar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x-20, self.y - 20, self.max_health/10, 10))  # Red background
        health_width = (self.health / self.max_health) * self.max_health
        pygame.draw.rect(screen, (0, 255, 0), (self.x-20, self.y - 20, health_width/10, 10))  # Green health

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            projectile = Bullet(self.x + self.image.get_width() // 2, self.y + self.image.get_height(), 5,
                                    (255, 0, 0))  # Red color
            self.projectiles.append(projectile)
            self.last_shot_time = current_time  # Update the last shot time

    def teleport(self):
        # Generate a random x-coordinate within the screen width
        self.x = random.randint(0, 800 - self.image.get_width())  # Assuming screen width is 800
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
        self.projectiles = [p for p in self.projectiles if p.y < 600]

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
        self.hitbox = pygame.Rect(x, y, radius * 2, radius * 2)  # Create a square hitbox

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x-50, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x+50, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x-250, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x+250, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x-350, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x+350, self.y), self.radius)

    def update(self):
        self.y += self.speed  # Move the projectile downwards
        self.hitbox.topleft = (self.x - self.radius, self.y - self.radius)  # Update hitbox position