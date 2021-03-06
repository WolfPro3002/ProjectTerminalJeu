import pygame
import math
from classPlayer import *
from classCercueille import *
from classMonster import *
from classTorche import *


# Création d'une classe Game :
class Game:

    def __init__(self):
        # Commencement jeu :
        self.is_playing = False
        # Joueur :
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        # Monsters :
        self.all_monster = pygame.sprite.Group()
        # Objets piece :
        self.all_objects = pygame.sprite.Group()
        # Bouton lancement jeu :
        self.play_button = pygame.image.load('Asset/button.png')
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 330
        self.play_button_rect.y = 250
        self.pressed = {}

    # Spawn des objets quand le jeu est lancé :
    def start(self):
        self.spawn_cercueille(540, 378)
        # Torche du haut :
        self.spawn_torche(540, 0)
        # Torche du bas :
        self.spawn_torche(540, 700)
        # Torche de droite :
        self.spawn_torche(0, 378)
        # Torche de gauche :
        self.spawn_torche(1030, 378)
        self.spawn_monster()

    # Fin du jeu :
    def game_over(self):
        # Remettre le jeu a neuf :
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.all_monster = pygame.sprite.Group()
        self.player._health = self.player._maxHealth
        self.is_playing = False
        self.stop_musique()
        self.musique_acueille()
        self.play_button_rect.x = 330
        self.play_button_rect.y = 250

    # Musique accueille :
    def music_jeu(self):
        mixer.music.load('Asset/Bruitages/jeu vidéo 2.wav')
        mixer.music.play(-1, 0, 20000)
        mixer.music.set_volume(0.3)

    # Musique Game over :
    def musique_acueille(self):
        mixer.music.load('Asset/Bruitages/music accueille.mp3')
        mixer.music.play(-1)

    # Stop la musique :
    def stop_musique(self):
        mixer.music.stop()

    # Chargement du jeu quand elle est lancer :
    def uptdate(self, screen):
        # Icone jeu :
        icon_32x32 = pygame.image.load('Asset/IconeJeu.png')
        pygame.display.set_icon(icon_32x32)

        # Charger le joueur :
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # Charger les monstres :
        self.all_monster.draw(screen)

        # Récupere les projectiles :
        for projectile in self.player.all_projectiles:
            projectile.move()

        # L'ensemble des projectiles :
        self.player.all_projectiles.draw(screen)

        # Recupere les monstres de notre jeu :
        for monster in self.all_monster:
            monster.foward()
            monster.update_health_bar(screen)

        # Charger le cercueille :
        self.all_objects.draw(screen)

        # Mettre a jour la fenetre :
        pygame.display.flip()

        # Verification du deplacement du joueur bordures a gauche ou a droite :
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.moveRigth()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 1:
            self.player.moveLef()

        # Verification du déplacement du joueur bordures du haut en bas :
        elif self.pressed.get(pygame.K_z) and self.player.rect.y > 1:
            self.player.moveUp()
        elif self.pressed.get(pygame.K_s) and self.player.rect.y + self.player.rect.height < screen.get_height():
            self.player.moveDown()

    # Création collision :
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)

    # Création du cercueille :
    def spawn_cercueille(self, x, y):
        # Apparition cercueille :
        cercueille = Cercueille(x, y)
        self.all_objects.add(cercueille)

    # Création de la torche :
    def spawn_torche(self, x, y):
        torche = Torche(x, y)
        self.all_objects.add(torche)

    # Création du spawn des monstres :
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)