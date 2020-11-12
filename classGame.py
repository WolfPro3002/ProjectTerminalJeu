import pygame
from classPlayer import *
from classCercueille import *
from classMonster import *

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
        self.pressed = {}
        self.spawn_cercueille()
        self.spawn_monster()

    # Chargement du jeu quand elle est lancer :
    def uptdate(self, screen):
        # Icone jeu :
        icon_32x32 = pygame.image.load('Asset/IconeJeu.png')
        pygame.display.set_icon(icon_32x32)

        # Charger le joueur :
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # Recupere les monstres de notre jeu :
        for monster in self.all_monster:
            monster.foward()
            monster.update_health_bar(screen)

        # Charger le cercueille :
        self.all_objects.draw(screen)

        # Charger les monstres :
        self.all_monster.draw(screen)

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
    def spawn_cercueille(self):
        # Apparition cercueille :
        cercueille = Cercueille()
        self.all_objects.add(cercueille)

    # Création du spawn des monstres :
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)