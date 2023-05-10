import pygame
from sys import exit

# SET UP
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# state of the game
game_active = True

# Importing, rendering and drawing a text surface
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render('Pygame', False, (64, 64, 64))
text_rectangle = text_surface.get_rect(center=(400, 50))

# importing the sky surface and ground surface
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

# importing and drawing the enemy surface
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(800, 300))

# importing and drawing the main character
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

player_gravity = 2

# game loop
while True:

    # Events - user input
    for event in pygame.event.get():

        # if player clicks the x button, close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # check if player presses a key dow
        # check if key is space bar and player character is positioned above 300
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                player_gravity = 2
            player_rectangle.y =- player_gravity

        # check if player presses key down and game is over
        if event.type == pygame.KEYDOWN and game_active==False:
            game_active = True
            player_rectangle.bottom = 300
            snail_rectangle.left = 800

    # if-else statement for Game state
    # game on
    if game_active:

        # Place sky and ground rectangles on the display screen
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Place enemy on the display screen
        screen.blit(snail_surface, snail_rectangle)

        # draws a rectangle around the "pygame" text, adjusts size, sets color and border radius
        pygame.draw.rect(screen, '#c0e5ac', text_rectangle.inflate(10, 10), border_radius=10)

        # place the "pygame" text on the display screen
        screen.blit(text_surface, text_rectangle)

        # player's gravity
        player_gravity += 0.3
        player_rectangle.y += player_gravity

        # re-position player after jump
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300

        # place player on the display screen
        screen.blit(player_surface, player_rectangle)

        # check if there is collision between enemy and player
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False

        # move enemy to the left
        snail_rectangle.left -= 6

        # check if enemy character goes too far to the left - reposition
        if snail_rectangle.left < -100:
            snail_rectangle.left = 800

    # Game over
    else:
        screen.fill('grey')

        # render, draw and display game over message
        gameOver_text_surface = test_font.render('Game Over', False, (64, 64, 64))
        gameOver_text_rect = gameOver_text_surface.get_rect(center=(400, 50))
        screen.blit(gameOver_text_surface, gameOver_text_rect)

        # render, draw and display character image
        player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
        player_stand_scaled = pygame.transform.rotozoom(player_stand, 0.5, 1.5)
        player_stand_rect = player_stand_scaled.get_rect(center=(400, 200))
        screen.blit(player_stand_scaled, player_stand_rect)

        # render, draw and display user prompt message
        startAgain_text_surface = test_font.render('Press Space to start again', False, (64, 64, 64))
        startAgain_text_rect = startAgain_text_surface.get_rect(center=(400, 330))
        screen.blit(startAgain_text_surface, startAgain_text_rect)

    pygame.display.update()
    clock.tick(60)
