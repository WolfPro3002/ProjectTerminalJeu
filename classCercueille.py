import pygame

# Création d'une classe cercueille :
class Cercueille(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Asset/Ancien Cercueil2.png')
        self.rect = self.image.get_rect()
        # Placement au milieu de l'écran :
        self.rect.x = x # 540
        self.rect.y = y # 378