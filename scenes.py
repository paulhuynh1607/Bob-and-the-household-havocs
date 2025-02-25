
import pygame
from setting import *

class Scenes:
    def __init__(self, screen):
        self.current_scene = 0
        self.screen = screen
        self.isChemical = True

    def living_room(self):
        background = pygame.transform.scale(pygame.image.load(FLOOR).convert(), (WIDTH, HEIGHT))
        wall = pygame.transform.scale(pygame.image.load(WALL).convert(), (WIDTH, 100))
        couch = pygame.transform.scale(pygame.image.load(COUCH).convert_alpha(), (138, 266))
        door = pygame.transform.scale(pygame.image.load(DOOR_TO_BASEMENT).convert_alpha(), (29, 252))
        tv_table = pygame.transform.scale(pygame.image.load(TV_TABLE).convert_alpha(), (85, 155))
        tv = pygame.transform.scale(pygame.image.load(TV).convert_alpha(), (47, 160))

        self.screen.blit(background, (0, 0))
        self.screen.blit(wall, (0, 0))
        self.screen.blit(couch, (COUCH_X, COUCH_Y))
        self.screen.blit(door, (DOOR_TO_BASEMENT_X, DOOR_TO_BASEMENT_Y))
        self.screen.blit(tv_table, (TV_TABLE_X, TV_TABLE_Y))
        self.screen.blit(tv, (TV_X, TV_Y))

    def kitchen(self):
        floor = pygame.transform.scale(pygame.image.load(K_FLOOR).convert(), (WIDTH, HEIGHT))
        wall = pygame.transform.scale(pygame.image.load(WALL).convert(), (WIDTH, 100))
        wall2 = pygame.transform.scale(pygame.image.load(KITCHEN_WALL).convert(), (WIDTH, 100))
        dining_chair = pygame.transform.scale(pygame.image.load(DINING_CHAIR).convert_alpha(), (75, 109))
        dining_chair1 = pygame.transform.scale(pygame.image.load(DINING_CHAIR1).convert_alpha(), (75, 109))
        dining_table = pygame.transform.scale(pygame.image.load(DINING_TABLE).convert_alpha(), (152, 109))
        normal_fridge = pygame.transform.scale(pygame.image.load(NORMAL_FRIDGE).convert_alpha(), (113, 176))
        stove = pygame.transform.scale(pygame.image.load(STOVE).convert_alpha(), (155, 369))
        sink = pygame.transform.scale(pygame.image.load(SINK).convert_alpha(), (152, 160))
        spray = pygame.transform.scale(pygame.image.load(Spray).convert_alpha(), (64, 56))
        purpleGooBucket = pygame.transform.scale(pygame.image.load(PurpleGooBucket).convert_alpha(), (56, 56))

        self.screen.blit(floor, (0, 0))
        self.screen.blit(wall, (0, 0))
        self.screen.blit(wall2, (225, 0))
        self.screen.blit(dining_chair, (DINING_CHAIR_X, DINING_CHAIR_Y))
        self.screen.blit(dining_chair1, (DINING_CHAIR_X1, DINING_CHAIR_Y1))
        self.screen.blit(dining_table, (DINING_TABLE_X, DINING_TABLE_Y))
        self.screen.blit(normal_fridge, (FRIDGE_X, FRIDGE_Y))
        self.screen.blit(stove, (STOVE_X, STOVE_Y))
        self.screen.blit(sink, (SINK_X, SINK_Y))
        if self.isChemical:

            self.screen.blit(spray, (Spray_X, Spray_Y))
            self.screen.blit(purpleGooBucket, (PurpleGooBucket_X, PurpleGooBucket_Y))

    def basement(self): # I added this one for the basement - Benedict
        floor = pygame.transform.scale(pygame.image.load(BASEMENT_FLOOR).convert(), (WIDTH, HEIGHT)) # I used the kitchen floor as placeholder -Benedict
        stairs = pygame.transform.scale(pygame.image.load(STAIRS).convert(), (208, 368))
        railings = pygame.transform.scale(pygame.image.load(RAILINGS).convert(), (48, 368))
        shelf = pygame.transform.scale(pygame.image.load(SHELF).convert_alpha(), (128, 224))
        washing_machine = pygame.transform.scale(pygame.image.load(WASHING_MACHINE).convert_alpha(), (160, 240))

        self.screen.blit(floor, (0, 0))
        self.screen.blit(stairs, (STAIRS_X, STAIRS_Y))
        self.screen.blit(railings, (RAILINGS_X, RAILINGS_Y))
        self.screen.blit(shelf, (SHELF_X, SHELF_Y))
        self.screen.blit(washing_machine, (WASHING_MACHINE_X, WASHING_MACHINE_Y))


    def combat_scene(self):
        floor = pygame.transform.scale(pygame.image.load(BASEMENT_FLOOR).convert(), (WIDTH, HEIGHT)) # I used the kitchen floor as placeholder -Benedict
        self.screen.blit(floor, (0, 0))


    def change_scene(self, current_scene_num):
        self.current_scene = current_scene_num
        match self.current_scene:
            case 0:
                self.living_room()
            case 1:
                self.kitchen()
            case 2:
                if self.isChemical:
                    self.basement()
                else:
                    self.combat_scene()



