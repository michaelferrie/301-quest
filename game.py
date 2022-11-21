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
pygame.display.set_caption("301-QUEST")

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
# images
bg_img = pygame.image.load('assets/images/bg.png').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

main_menu_bg_img = pygame.image.load('assets/images/main_menu_base.png')
main_menu_bg_img = pygame.transform.scale(main_menu_bg_img, (MENU_WINDOW_WIDTH , MENU_WINDOW_HEIGHT))

map_img = pygame.image.load('assets/images/map.png').convert_alpha()
map_img = pygame.transform.scale(map_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

new_player_img = pygame.image.load('assets/images/new_player.png').convert_alpha()
new_player_img = pygame.transform.scale(new_player_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

settings_img = pygame.image.load('assets/images/game_settings.png').convert_alpha()
settings_img = pygame.transform.scale(settings_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

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
    
# draw map screen
def draw_map():
    window.blit(map_img, (0, 0))

# draw new player
def draw_player():
    window.blit(new_player_img, (0, 0))

# draw settings area
def draw_settings():
    window.blit(settings_img, (0, 0))

# function to draw menu title
def draw_menu():
    # main menu bg
    window.blit(main_menu_bg_img,
                ((WINDOW_WIDTH / 2) - (MENU_WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) - (MENU_WINDOW_HEIGHT / 2)))

    # main menu title
    menu_title = font.render("RPG GAME", True, TEXT_COLOUR)
    window.blit(menu_title, ((WINDOW_WIDTH / 2) - 51, (WINDOW_HEIGHT / 2) - 128))
   

    # continue button
    continue_btn = font.render("Continue (C)", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 160))
    window.blit(continue_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 21, 180))

    # new game button
    new_game_btn = font.render("New Quest (N)", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 210))
    window.blit(new_game_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 15, 230))

    # settings button
    settings_btn = font.render("Settings (S)", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 260))
    window.blit(settings_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 23, 280))

    # exit button
    exit_btn = font.render("Quit (Q)", True, TEXT_COLOUR)
    window.blit(main_menu_button, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2), 310))
    window.blit(exit_btn, ((WINDOW_WIDTH / 2) - (BTN_WIDTH / 2) + 50, 330))

# map area loop
def game_map():
    map_area = True
    while map_area:
        draw_map()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print('Quitting')
                    map = False
                    main_menu()

# new game area loop
def new_player():
    player_area = True
    while player_area:
        draw_player()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print('Quitting')
                    player_area = False
                    main_menu()
                    
# settings area loop
def settings():
    settings_area = True
    while settings_area:
        draw_settings()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print('Quitting')
                    settings_area = False
                    main_menu()
                    
# main menu loop
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
                    game_map()
                if event.key == pygame.K_n:
                    print('New Quest')
                    running = False
                    new_player()
                if event.key == pygame.K_s:
                    print('Settings')
                    running = False
                    settings()
                if event.key == pygame.K_q:
                    print('Quitting')
                    pygame.quit()

# main game loop
running = True
while running:
    main_menu()
    
pygame.quit()