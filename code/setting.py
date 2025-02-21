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

SIDE_RIGHT_WALL = Rect(WIDTH-10, 0, 10, HEIGHT)
SIDE_LEFT_WALL = Rect(10, 0, 10, HEIGHT)
DOWN_WALL = Rect(0, HEIGHT-10, WIDTH, 10)


# Living Room Scene
FLOOR = "../assets/background/LivingRoomFloorWithCarpet.png"
WALL = "../assets/background/WallLivingRoomGreen.png"
WALL_HITBOX = Rect(0, 0, WIDTH, 100)
KITCHEN_HITBOX = Rect(WIDTH-10, 0, 10, HEIGHT)
COUCH = "../assets/Entities/furniture/sofaGreen.png"
COUCH_X = 150
COUCH_Y = 200
COUCH_HITBOX = Rect(COUCH_X, COUCH_Y, 138, 266)

COLLIDE_LIST_LIVING_ROOM = [COUCH_HITBOX, WALL_HITBOX, SIDE_LEFT_WALL, DOWN_WALL]

# Kitchen Scene
K_FLOOR = "../assets/background/KitchenFloor.png"
KITCHEN_WALL = "../assets/background/KitchenWall.png"
LIVING_ROOM_HITBOX = Rect(10, 0, 10, HEIGHT)

DINING_CHAIR = "../assets/Entities/furniture/ChairDining.png"
DINING_CHAIR_X, DINING_CHAIR_Y = 220, 400
DINING_CHAIR_HITBOX = Rect(DINING_CHAIR_X, DINING_CHAIR_Y, 75, 109)

DINING_CHAIR1 = "../assets/Entities/furniture/FlipChairDining.png"
DINING_CHAIR_X1, DINING_CHAIR_Y1 = 460, 400
DINING_CHAIR_HITBOX1 = Rect(DINING_CHAIR_X1, DINING_CHAIR_Y1, 75, 109)

DINING_TABLE = "../assets/Entities/furniture/DiningTable.png"
DINING_TABLE_X, DINING_TABLE_Y = 300, 400
DINING_TABLE_HITBOX = Rect(DINING_TABLE_X, DINING_TABLE_Y, 152, 109)

NORMAL_FRIDGE = "../assets/Entities/furniture/FridgeNormal.png"
FRIDGE_X, FRIDGE_Y = 310, 20
FRIDGE_HITBOX = Rect(FRIDGE_X, FRIDGE_Y, 113, 176)

COLLIDE_LIST_KITCHEN = [WALL_HITBOX, SIDE_RIGHT_WALL, DOWN_WALL, DINING_TABLE_HITBOX, DINING_CHAIR_HITBOX, DINING_CHAIR_HITBOX1, FRIDGE_HITBOX]

