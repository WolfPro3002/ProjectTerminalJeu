import pygame

# Création class torche:
class Torche(pygame.sprite.Sprite):

     def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Asset/torche mur pas fini.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y