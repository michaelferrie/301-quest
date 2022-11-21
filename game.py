# import libraries
import pygame
from pygame.locals import *
from pygame import mixer

# initialise game
pygame.init()

# define window size
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# window name
pygame.display.set_caption("301-QUEST")


# define fonts
# returns the font with the desired size
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


# define text colour (white)
TEXT_COLOUR_WHITE = (255, 255, 255)

# define menu window size
MENU_WINDOW_WIDTH = 400
MENU_WINDOW_HEIGHT = 620

# define menu buttons size
BTN_WIDTH = 150
BTN_HEIGHT = 55

# images
BG_IMG = pygame.image.load('assets/images/bg.png').convert_alpha()
BG_IMG = pygame.transform.scale(BG_IMG, (WINDOW_WIDTH, WINDOW_HEIGHT))

MAIN_MENU_BG_IMG = pygame.image.load('assets/images/main_menu_base.png')
MAIN_MENU_BG_IMG = pygame.transform.scale(MAIN_MENU_BG_IMG, (MENU_WINDOW_WIDTH, MENU_WINDOW_HEIGHT))

MAP_IMG = pygame.image.load('assets/images/map.png').convert_alpha()
MAP_IMG = pygame.transform.scale(MAP_IMG, (WINDOW_WIDTH, WINDOW_HEIGHT))

NEW_PLAYER_IMG = pygame.image.load('assets/images/new_player.png').convert_alpha()
NEW_PLAYER_IMG = pygame.transform.scale(NEW_PLAYER_IMG, (WINDOW_WIDTH, WINDOW_HEIGHT))

SETTINGS_IMG = pygame.image.load('assets/images/game_settings.png').convert_alpha()
SETTINGS_IMG = pygame.transform.scale(SETTINGS_IMG, (WINDOW_WIDTH, WINDOW_HEIGHT))

# main menu buttons
MAIN_MENU_BTN = pygame.image.load('assets/images/button.png')
MAIN_MENU_BTN  = pygame.transform.scale(MAIN_MENU_BTN, (BTN_WIDTH, BTN_HEIGHT))

# music - make a music selector function later
mixer.init()
mixer.music.load('assets/music/RVW_S6_Moderato.mp3')
mixer.music.play()


# draw functions - combine these into a single function later
# function to draw background
def draw_bg():
    GAME_DISPLAY.blit(BG_IMG, (0, 0))


# draw map screen
def draw_map():
    GAME_DISPLAY.blit(MAP_IMG, (0, 0))


# draw new player
def draw_player():
    GAME_DISPLAY.blit(NEW_PLAYER_IMG, (0, 0))


# draw settings area
def draw_settings():
    GAME_DISPLAY.blit(SETTINGS_IMG, (0, 0))


# function to draw menu title
# sorry, broke some of the positioning of this mr jorge
def draw_menu():
    # main menu bg
    GAME_DISPLAY.blit(MAIN_MENU_BG_IMG,
                ((WINDOW_WIDTH / 2) - (MENU_WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) - (MENU_WINDOW_HEIGHT / 2)))

    # main menu title
    menu_title = get_font(18).render("301-QUEST", True, TEXT_COLOUR_WHITE)
    GAME_DISPLAY.blit(menu_title, ((WINDOW_WIDTH / 2) - 51, (WINDOW_HEIGHT / 2) - 128))

    # continue button
    continue_btn = get_font(18).render("Continue (C)", True, TEXT_COLOUR_WHITE)
    GAME_DISPLAY.blit(MAIN_MENU_BTN , ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 160))
    GAME_DISPLAY.blit(continue_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 21, 180))

    # new game button
    new_game_btn = get_font(18).render("New Quest (N)", True, TEXT_COLOUR_WHITE)
    GAME_DISPLAY.blit(MAIN_MENU_BTN , ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 210))
    GAME_DISPLAY.blit(new_game_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 15, 230))

    # settings button
    settings_btn = get_font(18).render("Settings (S)", True, TEXT_COLOUR_WHITE)
    GAME_DISPLAY.blit(MAIN_MENU_BTN , ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 260))
    GAME_DISPLAY.blit(settings_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 23, 280))

    # exit button
    exit_btn = get_font(18).render("Quit (Q)", True, TEXT_COLOUR_WHITE)
    GAME_DISPLAY.blit(MAIN_MENU_BTN, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 310))
    GAME_DISPLAY.blit(exit_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 50, 330))


# exit area back to main menu
def exit_area():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or pygame.K_ESCAPE:
                print('Quitting')
                map = False
                main_menu()


# change game area
def change_area(zone):
    set_area = True
    selected_area = zone
    while set_area:
        selected_area()
        pygame.display.flip()
        exit_area()


# main menu
def main_menu():
    main_menu = True
    while main_menu:
        draw_bg()
        draw_menu()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    print('Continue')
                    running = False
                    change_area(draw_map)
                if event.key == pygame.K_n:
                    print('New Quest')
                    running = False
                    change_area(draw_player)
                if event.key == pygame.K_s:
                    print('Settings')
                    running = False
                    change_area(draw_settings)
                if event.key == pygame.K_q or pygame.K_ESCAPE:
                    print('Quitting')
                    pygame.quit()

# main game loop
running = True
while running:
    main_menu()
    
pygame.quit()
