import pygame
from sys import exit
from setting import *
from Player import Player
from scenes import  Scenes

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bob and The House Hold Havoc")
clock = pygame.time.Clock()
player = Player()
scene = Scenes(screen)


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    scene.change_scene(0)
    screen.blit(player.image, player.pos)
    # pygame.draw.rect(screen, "yellow", player.hitbox, width=2)
    # pygame.draw.rect(screen, "red", player.hitbox_combat, width=2)
    # pygame.draw.rect(screen, "red", COUCH_HITBOX, width=2)
    # pygame.draw.rect(screen, "red", WALL_HITBOX, width=2)

    player.update(COLLIDE_LIST)

    pygame.display.update()
    clock.tick(FPS)

