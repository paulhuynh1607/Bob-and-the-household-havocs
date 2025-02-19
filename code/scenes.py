import pygame
from setting import *

class Scenes:
    def __init__(self, screen):
        self.current_scene = 0
        self.screen = screen

    def living_room(self):
        background = pygame.transform.scale(pygame.image.load(FLOOR).convert(), (WIDTH, HEIGHT))
        wall = pygame.transform.scale(pygame.image.load(WALL).convert(), (WIDTH, 100))
        couch = pygame.transform.scale(pygame.image.load(COUCH).convert_alpha(), (138, 266))

        self.screen.blit(background, (0, 0))
        self.screen.blit(wall, (0, 0))
        self.screen.blit(couch, (COUCH_X, COUCH_Y))


    def change_scene(self, current_scene_num):
        self.current_scene = current_scene_num
        match self.current_scene:
            case 0:
                self.living_room()

