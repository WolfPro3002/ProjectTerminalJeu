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

# Modification bannierre pour l'accueille :
banner = pygame.image.load('Asset/BannierreJeu.png').convert_alpha()
banner = pygame.transform.scale(banner, (300, 300))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2.90)
banner_rect.y = math.ceil(screen.get_height() / 3)

# Musique bouton :
music_bouton = mixer.Sound('Asset/Bruitages/cercueille.wav')

# Crétion du jeu :
game = Game()

# Lancement musique de fond d'accueille :
game.musique_acueille()

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
        screen.blit(game.play_button, game.play_button_rect)
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

            # Si espace est toucher le projectile se lance :
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        # Clavier qui n'est plus touché :
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # Si le boutton play est touché le jeu se lance :
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer :
            if game.play_button_rect.collidepoint(event.pos):
                game.stop_musique()
                # mettre le jeu en marche:
                game.is_playing = True
                game.start()
                # Lancement musique de fond :
                game.music_jeu()
                # Bruitage du click du boutton
                music_bouton.play()
                # Deplace le bouton de lancement du jeu :
                game.play_button_rect.x = 1200
                game.play_button_rect.y = 780