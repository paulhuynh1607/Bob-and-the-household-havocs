import pygame, sys
from sys import exit
from setting import *
from Player import Player, Projectile
from scenes import  Scenes
from button import Button
from WashingMachine import WashingMachine, Bullet

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bob and The House Hold Havoc")
clock = pygame.time.Clock()
player = Player()
projectile = Projectile
scene = Scenes(screen)
washingMachine = WashingMachine(300, 50,  500)
scene_num = 0


BG = pygame.image.load("../assets/GUI/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../assets/GUI/font.ttf", size)


def play():
    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        scene.change_scene(player.update())
        player.draw_projectiles(screen, washingMachine)
        screen.blit(player.image, player.pos)

        if player.scene_num == 3:
            # Check for collisions between player projectiles and the boss's projectiles
            washingMachine.draw(screen)
            washingMachine.update()
            for boss_projectile in washingMachine.projectiles:
                if boss_projectile.hitbox.colliderect(player.hitbox_combat) or boss_projectile.hitbox.colliderect(player.hitbox):
                    # Deal damage to the player
                    player.health -= 10  # Example: player takes damage
                    # Remove the projectiles after collision
                    washingMachine.projectiles.remove(boss_projectile)
                    break  # Exit the loop after handling the collision
            player.draw_health_bar(screen)

            for bullet in player.bullets:
                if bullet.hitbox.colliderect(washingMachine.hitbox):
                    # Deal damage to the player
                    washingMachine.take_damage(10)  # Example: player takes damage
                    # Remove the projectiles after collision
                    player.bullets.remove(bullet)
                    break  # Exit the loop after handling the collision



        # Uncomment the following lines if you want to visualize hitboxes
        # pygame.draw.rect(screen, "yellow", DOWN_WALL, width=2)
        # pygame.draw.rect(screen, "yellow", KITCHEN_HITBOX, width=2)
        # pygame.draw.rect(screen, "yellow", player.hitbox, width=2)
        # pygame.draw.rect(screen, "red", player.hitbox_combat, width=2)
        # pygame.draw.rect(screen, "red", COUCH_HITBOX, width=2)
        # pygame.draw.rect(screen, "red", WALL_HITBOX, width=2)

        pygame.display.update()
        clock.tick(FPS)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(15).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 460),
                              text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()


        pygame.display.update()


def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Bob and the", True, "#90d5ff")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
        MENU_TEXT1 = get_font(50).render("Household Havoc", True, "#90d5ff")
        MENU_RECT1 = MENU_TEXT.get_rect(center=(315, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/GUI/Play Rect.png").convert_alpha(), pos=(400, 250),
                             text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("../assets/GUI/Options Rect.png").convert_alpha(), pos=(400, 375),
                                text_input="OPTIONS", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/GUI/Quit Rect.png").convert_alpha(), pos=(400, 500),
                             text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(MENU_TEXT1, MENU_RECT1)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()


