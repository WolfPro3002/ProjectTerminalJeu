import pygame
import os
from classPlayer import *
from classGame import *
import math
from pygame import mixer

pygame.init()

# Icone jeu :
icon_32x32 = pygame.image.load('Asset/IconeJeu.png')
pygame.display.set_icon(icon_32x32)

# Ouverture de la fenêtre du jeu :
pygame.display.set_caption('Projet jeu terminal')
screen = pygame.display.set_mode((1080, 756))
Run = True

# Création du background :
background = pygame.image.load('Asset/parquet2.png')

# Lancement musique de fond d'accueille :
mixer.music.load('Asset/Bruitages/music accueille.mp3')
mixer.music.play(-1)

# Modification bannierre pour l'accueille :
banner = pygame.image.load('Asset/BannierreJeu.png').convert_alpha()
banner = pygame.transform.scale(banner, (300, 300))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2.90)
banner_rect.y = math.ceil(screen.get_height() / 3)

# Création d'un boutoun :
play_button = pygame.image.load('Asset/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 3)

# Musique bouton :
music_bouton = mixer.Sound('Asset/Bruitages/cercueille.wav')


# Crétion du jeu :
game = Game()

# Boucle ouverture de la fenêtre et du jeu :
while Run:

    # Appliquer le background :
    screen.blit(background, (0, 0))

    # Jeu commence ou non :
    if game.is_playing:
        # Déclanche les instructions:
        game.uptdate(screen)
    # Si le jeu n'a pas commencer
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mettre a jour la fenetre :
    pygame.display.flip()

    # Fermeture fenêtre :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            pygame.quit()
            print('Fermeture du jeu')

        # Déplacements quand le clavier est touché pour fluidité déplacement :
        # Clavier qui est touché :
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        # Clavier qui n'est plus touché :
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # Si le boutton play est touché le jeu se lance :
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer :
            if play_button_rect.collidepoint(event.pos):
                mixer.music.stop()
                # mettre le jeu en marche:
                game.is_playing = True
                # Lancement musique de fond :
                mixer.music.load('Asset/Bruitages/jeu vidéo 2.wav')
                mixer.music.play(-1, 0, 20000)
                mixer.music.set_volume(0.3)
                # Bruitage du click du boutton
                music_bouton.play()