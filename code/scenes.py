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

    def kitchen(self):
        floor = pygame.transform.scale(pygame.image.load(K_FLOOR).convert(), (WIDTH, HEIGHT))
        wall = pygame.transform.scale(pygame.image.load(WALL).convert(), (WIDTH, 100))
        wall2 = pygame.transform.scale(pygame.image.load(KITCHEN_WALL).convert(), (WIDTH, 100))
        dining_chair = pygame.transform.scale(pygame.image.load(DINING_CHAIR).convert_alpha(), (75, 109))
        dining_chair1 = pygame.transform.scale(pygame.image.load(DINING_CHAIR1).convert_alpha(), (75, 109))
        dining_table = pygame.transform.scale(pygame.image.load(DINING_TABLE).convert_alpha(), (152, 109))
        normal_fridge = pygame.transform.scale(pygame.image.load(NORMAL_FRIDGE).convert_alpha(), (113, 176))

        self.screen.blit(floor, (0, 0))
        self.screen.blit(wall, (0, 0))
        self.screen.blit(wall2, (225, 0))
        self.screen.blit(dining_chair, (DINING_CHAIR_X, DINING_CHAIR_Y))
        self.screen.blit(dining_chair1, (DINING_CHAIR_X1, DINING_CHAIR_Y1))
        self.screen.blit(dining_table, (DINING_TABLE_X, DINING_TABLE_Y))
        self.screen.blit(normal_fridge, (FRIDGE_X, FRIDGE_Y))

    def change_scene(self, current_scene_num):
        self.current_scene = current_scene_num
        match self.current_scene:
            case 0:
                self.living_room()
            case 1:
                self.kitchen()


