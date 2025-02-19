from pygame.locals import *
# Game Setup
WIDTH = 800
HEIGHT = 600
FPS = 60

# Player setting
PLAYER_START_X = 300
PLAYER_START_Y = 300

PLAYER_SPEED = 3
PLAYER_SIZE = 1

PLAYER_FRONT = "../assets/Entities/Bob/BobFront.png"
PLAYER_LEFT = "../assets/Entities/Bob/BobLeft.png"
PLAYER_RIGHT = "../assets/Entities/Bob/BobRight.png"
PLAYER_DOWN = "../assets/Entities/Bob/BobBack.png"

# Living Room Scene
FLOOR = "../assets/background/LivingRoomFloorWithCarpet.png"
WALL = "../assets/background/WallLivingRoomGreen.png"
WALL_HITBOX = Rect(0, 0, WIDTH, 100)
COUCH = "../assets/Entities/furniture/sofaGreen.png"
COUCH_X = 150
COUCH_Y = 200
COUCH_HITBOX = Rect(COUCH_X, COUCH_Y, 138, 266)
COLLIDE_LIST = [COUCH_HITBOX, WALL_HITBOX]
# I added this part for the invisible rect (it's not invisible as of feb 18 11:01) these are the properties of the rect
ENTER_KITCHEN_X = 798
ENTER_KITCHEN_Y = 0
ENTER_KITCHEN_HITBOX = Rect(ENTER_KITCHEN_X, ENTER_KITCHEN_Y, 2, HEIGHT)
ENTER_KITCHEN_HEIGHT = 800
ENTER_KITCHEN_WIDTH = 2

