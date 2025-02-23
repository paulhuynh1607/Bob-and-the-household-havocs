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
COUCH_X = 170
COUCH_Y = 250
COUCH_HITBOX = Rect(COUCH_X, COUCH_Y, 138, 266)
DOOR_TO_BASEMENT = "../assets/Entities/furniture/DoorInLivingRoom.png"
DOOR_TO_BASEMENT_X = 0
DOOR_TO_BASEMENT_Y = 0
DOOR_TO_BASEMENT_HITBOX = Rect(DOOR_TO_BASEMENT_X, DOOR_TO_BASEMENT_Y, 29, 252)
TV_TABLE = "../assets/Entities/furniture/TVTable.png"
TV_TABLE_X = -10
TV_TABLE_Y = 310
TV_TABLE_HITBOX = Rect(TV_TABLE_X, TV_TABLE_Y, 85, 155)
TV = "../assets/Entities/furniture/TV.png"
TV_X = 10
TV_Y = 260
TV_HITBOX = Rect(TV_X, TV_Y, 47, 160)
COLLIDE_LIST_LIVING_ROOM = [COUCH_HITBOX, WALL_HITBOX, SIDE_LEFT_WALL, DOWN_WALL,
                            DOOR_TO_BASEMENT_HITBOX, TV_TABLE_HITBOX, TV_HITBOX]
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

STOVE = "../assets/Entities/furniture/Stove.png"
STOVE_X, STOVE_Y = 650, 25
STOVE_HITBOX = Rect(STOVE_X, STOVE_Y, 155, 369)

NORMAL_FRIDGE = "../assets/Entities/furniture/Fridge/FridgeNormal.png" # Changed the file directory because jino made the animation for the fridge
FRIDGE_X, FRIDGE_Y = 310, 20
FRIDGE_HITBOX = Rect(FRIDGE_X, FRIDGE_Y, 113, 176)

COLLIDE_LIST_KITCHEN = [WALL_HITBOX, SIDE_RIGHT_WALL, DOWN_WALL, DINING_TABLE_HITBOX, DINING_CHAIR_HITBOX, DINING_CHAIR_HITBOX1, FRIDGE_HITBOX, STOVE_HITBOX]

#Basement scene
#Basement scene
PLAYER_START_BASEMENT_X = 550
PLAYER_START_BASEMENT_Y = 20
BASEMENT_FLOOR = "../assets/background/BasementFloor.png"
STAIRS = "../assets/Entities/furniture/Stairs.png"
STAIRS_X = 592
STAIRS_Y = 0
RAILINGS = "../assets/Entities/furniture/StairRailing.png"
RAILINGS_X = 544
RAILINGS_Y = 0
RAILINGS_HITBOX = Rect(RAILINGS_X, RAILINGS_Y, 48, 368)
WASHING_MACHINE = ""
WASHING_MACHINE_X = ""
WASHING_MACHINE_Y = ""
WASHING_MACHINE_HITBOX = Rect(FRIDGE_X, FRIDGE_Y, 113, 176)
SHELF = "../assets/Entities/furniture/Shelf.png"
SHELF_X = 200
SHELF_Y = 0
SHELF_HITBOX = Rect(SHELF_X, SHELF_Y, 128, 224)
COLLIDE_LIST_BASEMENT = [WALL_HITBOX, SIDE_RIGHT_WALL, SIDE_LEFT_WALL, DOWN_WALL,
                         RAILINGS_HITBOX, SHELF_HITBOX]


# Combat scene
COMBAT_FLOOR = "../assets/background/LivingRoomFloorNoCarpet.png"
COLLIDE_LIST_COMBAT = [SIDE_LEFT_WALL, SIDE_RIGHT_WALL]
