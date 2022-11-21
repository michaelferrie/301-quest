# import libraries
import pygame
from pygame.locals import *
from pygame import mixer

# initialise game
pygame.init()

# define window size
window_width = 1280
window_height = 720
game_display = pygame.display.set_mode((window_width, window_height))

# window name
pygame.display.set_caption("301-QUEST")

# define fonts
font = pygame.font.Font("assets/fonts/Cardinal-Alternate.ttf", 18)

# define text colour (white)
text_colour = (255, 255, 255)

# define menu window size
menu_window_width = 400
menu_window_height = 620

# define menu buttons size
btn_width = 150
btn_height = 55

# images
bg_img = pygame.image.load('assets/images/bg.png').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (window_width, window_height))

main_menu_bg_img = pygame.image.load('assets/images/main_menu_base.png')
main_menu_bg_img = pygame.transform.scale(main_menu_bg_img, (menu_window_width , menu_window_height))

map_img = pygame.image.load('assets/images/map.png').convert_alpha()
map_img = pygame.transform.scale(map_img, (window_width, window_height))

new_player_img = pygame.image.load('assets/images/new_player.png').convert_alpha()
new_player_img = pygame.transform.scale(new_player_img, (window_width, window_height))

settings_img = pygame.image.load('assets/images/game_settings.png').convert_alpha()
settings_img = pygame.transform.scale(settings_img, (window_width, window_height))

# main menu buttons
main_menu_button = pygame.image.load('assets/images/button.png')
main_menu_button = pygame.transform.scale(main_menu_button, (btn_width, btn_height))

# music - make a music selector function later
mixer.init()
mixer.music.load('assets/music/RVW_S6_Moderato.mp3')
mixer.music.play()

# draw functions - combine these into a single function later
# function to draw background
def draw_bg():
    game_display.blit(bg_img, (0, 0))
 
# draw map screen
def draw_map():
    game_display.blit(map_img, (0, 0))

# draw new player
def draw_player():
    game_display.blit(new_player_img, (0, 0))

# draw settings area
def draw_settings():
    game_display.blit(settings_img, (0, 0))

# function to draw menu title
# sorry, broke some of the positioning of this mr jorge
def draw_menu():
    # main menu bg
    game_display.blit(main_menu_bg_img,
                ((window_width / 2) - (menu_window_width / 2), (window_height / 2) - (menu_window_height / 2)))

    # main menu title
    menu_title = font.render("301-QUEST", True, text_colour)
    game_display.blit(menu_title, ((window_width / 2) - 51, (window_height / 2) - 128))
   

    # continue button
    continue_btn = font.render("Continue (C)", True, text_colour)
    game_display.blit(main_menu_button, ((window_width / 2) - (btn_width / 2), 160))
    game_display.blit(continue_btn, ((window_width / 2) - (btn_width / 2) + 21, 180))

    # new game button
    new_game_btn = font.render("New Quest (N)", True, text_colour)
    game_display.blit(main_menu_button, ((window_width / 2) - (btn_width / 2), 210))
    game_display.blit(new_game_btn, ((window_width / 2) - (btn_width / 2) + 15, 230))

    # settings button
    settings_btn = font.render("Settings (S)", True, text_colour)
    game_display.blit(main_menu_button, ((window_width / 2) - (btn_width / 2), 260))
    game_display.blit(settings_btn, ((window_width / 2) - (btn_width / 2) + 23, 280))

    # exit button
    exit_btn = font.render("Quit (Q)", True, text_colour)
    game_display.blit(main_menu_button, ((window_width / 2) - (btn_width / 2), 310))
    game_display.blit(exit_btn, ((window_width / 2) - (btn_width / 2) + 50, 330))


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