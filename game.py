# import libraries
import pygame
from pygame.locals import *
from pygame import mixer

# initialise game
pygame.init()

# define window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# window name
pygame.display.set_caption("RPG GAME")

# define fonts
font = pygame.font.Font("assets/fonts/Cardinal-Alternate.ttf", 18)

# define text colour (white)
TEXT_COLOUR = (255, 255, 255)

# define menu window size
MENU_WINDOW_WIDTH = 500
MENU_WINDOW_HEIGHT = 300

# define menu buttons size
BTN_WIDTH = 150
BTN_HEIGHT = 55

# set game attributes
# bg
bg_img = pygame.image.load('assets/images/bg.png')
bg_img = pygame.transform.scale(bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

# main menu bg
main_menu_bg_img = pygame.image.load('assets/images/main_menu_base.png')
main_menu_bg_img = pygame.transform.scale(main_menu_bg_img, (MENU_WINDOW_WIDTH , MENU_WINDOW_HEIGHT))

# main menu buttons
main_menu_button = pygame.image.load('assets/images/button.png')
main_menu_button = pygame.transform.scale(main_menu_button, (BTN_WIDTH, BTN_HEIGHT))

# music
mixer.init()
mixer.music.load('assets/music/RVW_S6_Moderato.mp3')
mixer.music.play()


# function to draw background
def draw_bg():
    window.blit(bg_img, (0, 0))


# function to draw menu title
def draw_menu():
    # main menu bg
    window.blit(main_menu_bg_img,
                ((WINDOW_WIDTH / 2) - (MENU_WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) - (MENU_WINDOW_HEIGHT / 2)))

    # main menu title
    menu_title = font.render("RPG GAME", True, TEXT_COLOUR)
    window.blit(menu_title, ((WINDOW_WIDTH / 2) - 51, (WINDOW_HEIGHT / 2) - 128))

    # continue button
    continue_btn = font.render("CONTINUE", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 160))
    window.blit(continue_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 21, 180))

    # new game button
    new_game_btn = font.render("NEW GAME", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 210))
    window.blit(new_game_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 15, 230))

    # settings button
    settings_btn = font.render("SETTINGS", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 260))
    window.blit(settings_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 23, 280))

    # exit button
    exit_btn = font.render("EXIT", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 310))
    window.blit(exit_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 50, 330))

# main game loop
running = True
while running:

    draw_bg()
    draw_menu()

    # event handler to quit the game
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()
