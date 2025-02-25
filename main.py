import asyncio
import pygame
import sys
from setting import *
from Player import Player
from scenes import Scenes
from button import Button
from WashingMachine import WashingMachine

pygame.init()

# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bob and The House Hold Havoc")
clock = pygame.time.Clock()

# Initialize game objects
scene = Scenes(screen)
player = Player(scene)
washingMachine = WashingMachine(300, 50, 500)

# Load background
BG = pygame.image.load("assets/GUI/Background.png")

# Define game states
MAIN_MENU = 0
PLAYING = 1
WINNING = 2
LOSING = 3
OPTIONS = 4
current_state = MAIN_MENU


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/GUI/font.ttf", size)


def draw_winning_scene():
    screen.fill((0, 0, 0))  # Fill the screen with black
    text = get_font(50).render("You Win!", True, (0, 255, 0))  # Render the "You Win!" text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # Center the text

    restart_text = get_font(15).render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    member1_text = get_font(20).render("Programming: Paulhuynh1607", True, (255, 255, 255))
    member1_rect = member1_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    member2_text = get_font(20).render("Music/Assistant art and programing:", True, (255, 255, 255))
    member2_rect = member2_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
    member2_text1 = get_font(20).render("BennyMcleany", True, (255, 255, 255))
    member2_rect1 = member2_text.get_rect(center=(WIDTH // 2+225, HEIGHT // 2 + 160))

    member3_text = get_font(20).render("Art & Graphics: XYRzppI", True, (255, 255, 255))
    member3_rect = member3_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 190))

    # Draw the credits
    screen.blit(member1_text, member1_rect)
    screen.blit(member2_text, member2_rect)
    screen.blit(member2_text1, member2_rect1)
    screen.blit(member3_text, member3_rect)

    # Draw the text
    screen.blit(text, text_rect)
    screen.blit(restart_text, restart_rect)


def draw_losing_scene():
    screen.fill((0, 0, 0))  # Fill the screen with black
    text = get_font(50).render("Game Over", True, (255, 0, 0))  # Render the "Game Over" text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # Center the text

    restart_text = get_font(15).render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    # Draw the text
    screen.blit(text, text_rect)
    screen.blit(restart_text, restart_rect)


def draw_main_menu():
    screen.blit(BG, (0, 0))
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(50).render("Bob and the", True, "#90d5ff")
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
    MENU_TEXT1 = get_font(50).render("Household Havoc", True, "#90d5ff")
    MENU_RECT1 = MENU_TEXT.get_rect(center=(315, 150))

    PLAY_BUTTON = Button(image=pygame.image.load("assets/GUI/Play Rect.png").convert_alpha(), pos=(400, 250),
                         text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
    OPTIONS_BUTTON = Button(image=pygame.image.load("assets/GUI/Options Rect.png").convert_alpha(), pos=(400, 375),
                            text_input="OPTIONS", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/GUI/Quit Rect.png").convert_alpha(), pos=(400, 500),
                         text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

    screen.blit(MENU_TEXT, MENU_RECT)
    screen.blit(MENU_TEXT1, MENU_RECT1)

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)

    return PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON


class Slider:
    def __init__(self, x, y, width, height, min_value=0, max_value=1, initial_value=0.5):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.handle_rect = pygame.Rect(x + (width * initial_value) - (height // 2), y, height, height)

    def draw(self, screen):
        # Draw the slider background
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        # Draw the slider handle
        pygame.draw.rect(screen, (100, 100, 100), self.handle_rect)

    def update(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:  # If mouse is pressed
            # Update the handle position
            self.handle_rect.x = max(self.rect.x, min(mouse_pos[0] - self.handle_rect.width // 2, self.rect.x + self.rect.width - self.handle_rect.width))
            # Calculate the new volume value
            self.value = (self.handle_rect.x - self.rect.x) / self.rect.width
            pygame.mixer.music.set_volume(self.value)  # Set the volume


def draw_options_menu():
    screen.fill((0, 0, 0))  # Fill the screen with black
    text = get_font(50).render("Options", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    text1 = get_font(30).render("Music", True, (255, 255, 255))
    text_rect1 = text.get_rect(center=(WIDTH // 2 + 90, HEIGHT // 2 + 80))
    screen.blit(text1, text_rect1)

    volume_slider.draw(screen)  # Draw the volume slider

    back_text = get_font(15).render("Press B to go back", True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 ))
    screen.blit(back_text, back_rect)


# Initialize the slider
volume_slider = Slider(200, 400, 400, 20)

# Main game loop
async def main():
    pygame.mixer.init()
    game_snd = pygame.mixer.Sound("assets/music/Joyful.ogg")
    boss_fight_snd = pygame.mixer.Sound("assets/music/Pagaway2.ogg")
    end_theme_snd = pygame.mixer.Sound("assets/music/EndTheme.ogg")
    while True:
        global current_state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if current_state == MAIN_MENU:
            end_theme_snd.stop()
            PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON = draw_main_menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    current_state = PLAYING
                if OPTIONS_BUTTON.checkForInput(mouse_pos):
                    current_state = OPTIONS  # Switch to options state
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        elif current_state == OPTIONS:
            draw_options_menu()
            volume_slider.update(mouse_pos, mouse_pressed)  # Update the slider

            keys = pygame.key.get_pressed()
            if keys[pygame.K_b]:  # Go back to the main menu
                current_state = MAIN_MENU

        elif current_state == PLAYING:
            scene.change_scene(player.update())
            player.draw_projectiles(screen, washingMachine)
            screen.blit(player.image, player.pos)
            game_snd.play()

            if player.scene_num == 2 and not scene.isChemical:
                game_snd.stop()
                boss_fight_snd.play()
                boss_fight_snd.set_volume(volume_slider.value)
                washingMachine.draw(screen)
                washingMachine.update()
                player.draw_health_bar(screen)

                # Check for collisions between boss projectiles and the player's hitbox
                for boss_bullet in washingMachine.projectiles:
                    if boss_bullet.hitbox.colliderect(player.hitbox_combat) or boss_bullet.hitbox.colliderect(player.hitbox):
                        player.health -= 10  # Player takes damage
                        washingMachine.projectiles.remove(boss_bullet)  # Remove the bullet after collision
                        break

                # Check for collisions between player bullets and the washing machine
                for bullet in player.bullets:
                    if bullet.hitbox.colliderect(washingMachine.hitbox):
                        washingMachine.take_damage(10)  # Deal damage to the washing machine
                        player.bullets.remove(bullet)  # Remove the player's bullet after collision
                        break

                # Check for winning condition
                if washingMachine.health <= 0:
                    current_state = WINNING  # Switch to winning state

            # Check for losing condition
            if player.health <= 0:
                current_state = LOSING  # Switch to losing state

        elif current_state == WINNING:
            boss_fight_snd.stop()
            end_theme_snd.play()
            draw_winning_scene()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                player.health = 100
                washingMachine.health = 500  # Reset boss health
                scene.isChemical = True
                current_state = MAIN_MENU  # Restart the game by going back to the main menu
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        elif current_state == LOSING:
            draw_losing_scene()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                player.health = 100
                washingMachine.health = 500
                current_state = MAIN_MENU  # Restart the game by going back to the main menu
                scene.isChemical = True
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)
        await asyncio.sleep(0)

asyncio.run(main())
