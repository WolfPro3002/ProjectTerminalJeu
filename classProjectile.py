import pygame
from classMonster import *
from math import sqrt

# Création class projectile :
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.monster = Monster(self)
        self.player = player
        self.velocity = 5
        self.time = 0
        self.image = pygame.image.load('Asset/dent vers droite.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        # Coordonnées placement du projectile :
        self.rect.x = player.rect.x + 20
        self.rect.y = player.rect.y + 20
        self.origin_image = self.image
        self.angle = 0

    # Effet de chute du projectile :
    def rotate(self):
        self.angle += -0.5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)

    # Enleve le projectile :
    def remove(self):
        self.player.all_projectiles.remove(self)

    # Animation projectile :
    def move(self):
        self.rect.x += self.velocity
        self.rect.y += 0.9
        self.rotate()
        self.time += 1

        # Collisions avec le monstre du projectile :
        for monster in self.player.rect_monstre():
            if not (self.rect.y >= monster['y'] + monster['height'] + self.velocity or self.rect.y + self.rect.height <= monster['y'] or self.rect.x + self.rect.width <= monster['x'] or self.rect.x >= monster['x'] + monster['width']):
                self.remove()

        # Degats monstre :
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            # Inflige des dégats :
            monster.damage(self.player.attack)

        # Collisions avec les objets du jeu :
        for obstacle in self.player.rect_obstacles():
            if not (self.rect.y >= obstacle['y']+obstacle['height'] or self.rect.y+self.rect.height <= obstacle['y'] or self.rect.x+self.rect.width <= obstacle['x']+self.velocity or self.rect.x >= obstacle['x']+obstacle['width']):
                self.remove()

        # verifier si notre projectile n'est plus présent sur l'écran :
        if self.rect.x > 1080:
            # Suprimme projectile :
            self.remove()

        elif self.time == 70:
            # Suprimme le projectile au bout de 10s :
            self.remove()