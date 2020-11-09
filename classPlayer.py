import pygame
from pygame import mixer

# Création de la classe Player :
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self._health = 100
        self._maxHealth = 100
        self.attack = 10
        self.velocity = 2
        self.marche = mixer.Sound('Asset/Bruitages/marcheParquet.wav')
        self.image = pygame.image.load('Asset/AidenLoaw1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 300

    # Instantiation des obstacles objets :
    def rect_obstacles(self):
        return [{'x':self.game.all_objects.sprites()[i].rect.x, 'y':self.game.all_objects.sprites()[i].rect.y, 'width':self.game.all_objects.sprites()[i].rect.width, 'height':self.game.all_objects.sprites()[i].rect.height} for i in range(len(self.game.all_objects))]

    # Instantiation de l'obstacle monstre :
    def rect_monstre(self):
        return [{'x':self.game.all_monster.sprites()[i].rect.x, 'y':self.game.all_monster.sprites()[i].rect.y, 'width':self.game.all_monster.sprites()[i].rect.width, 'height':self.game.all_monster.sprites()[i].rect.height} for i in range(len(self.game.all_monster))]


    # Méthode qui permet de faire bouger le joueur a droite :
    def moveRigth(self):
        deplacement = True
        # Si le joueur est en collision avec le cercueille :
        for obstacle in self.rect_obstacles():
            if not (self.rect.y >= obstacle['y']+obstacle['height'] or self.rect.y+self.rect.height <= obstacle['y'] or self.rect.x+self.rect.width <= obstacle['x'] or self.rect.x >= obstacle['x']+obstacle['width']-self.velocity):
                deplacement = False
        # Si le joueur est en collision avec le monstre :
        for monster in self.rect_monstre():
            if not (self.rect.y >= monster['y'] + monster['height'] + self.velocity or self.rect.y + self.rect.height <= monster['y'] or self.rect.x + self.rect.width <= monster['x'] or self.rect.x >= monster['x'] +monster['width']):
                deplacement = False
        if deplacement:
            self.rect.x += self.velocity
            self.marche.play()

    # Méthode qui permet de faire bouger le joueur a gauche :
    def moveLef(self):
        deplacement = True
        # Si le joueur est en collision avec le cercueille :
        for obstacle in self.rect_obstacles():
            if not (self.rect.y >= obstacle['y']+obstacle['height'] or self.rect.y+self.rect.height <= obstacle['y'] or self.rect.x+self.rect.width <= obstacle['x']+self.velocity or self.rect.x >= obstacle['x']+obstacle['width']):
                deplacement = False
        # Si le joueur est en collision avec le monstre :
        for monster in self.rect_monstre():
            if not (self.rect.y >= monster['y'] + monster['height'] + self.velocity or self.rect.y + self.rect.height <= monster['y'] or self.rect.x + self.rect.width <= monster['x'] or self.rect.x >= monster['x'] + monster['width']):
                deplacement = False
        if deplacement:
            self.rect.x -= self.velocity
            self.marche.play()

    # Méthode qui permet de faire bouger le joueur en haut :
    def moveUp(self):
        deplacement = True
        # Si le joueur est en collision avec le cercueille :
        for obstacle in self.rect_obstacles():
            if not (self.rect.y >= obstacle['y'] + obstacle['height'] + self.velocity or self.rect.y + self.rect.height <= obstacle['y'] or self.rect.x + self.rect.width <= obstacle['x'] or self.rect.x >= obstacle['x'] + obstacle['width']):
                deplacement = False
        # Si le joueur est en collision avec le monstre :
        for monster in self.rect_monstre():
            if not (self.rect.y >= monster['y'] + monster['height'] + self.velocity or self.rect.y + self.rect.height <= monster['y'] or self.rect.x + self.rect.width <= monster['x'] or self.rect.x >= monster['x'] + monster['width']):
                deplacement = False
        if deplacement:
            self.rect.y -= self.velocity
            self.marche.play()

    # Méthode qui permet de faire bouger le joueur en bas:
    def moveDown(self):
        deplacement = True
        # Si le joueur est en collision avec le cercueille :
        for obstacle in self.rect_obstacles():
            if not (self.rect.y >= obstacle['y'] + obstacle['height'] or self.rect.y + self.rect.height <= obstacle['y'] - self.velocity or self.rect.x + self.rect.width <= obstacle['x'] or self.rect.x >= obstacle['x'] + obstacle['width']):
                deplacement = False
        # Si le joueur est en collision avec le monstre :
        for monster in self.rect_monstre():
            if not (self.rect.y >= monster['y'] + monster['height'] + self.velocity or self.rect.y + self.rect.height <= monster['y'] or self.rect.x + self.rect.width <= monster['x'] or self.rect.x >= monster['x'] +monster['width']):
                deplacement = False
        if deplacement:
            self.rect.y += self.velocity
            self.marche.play()

        # Création d'une méthode qui permet d'afficher la barre de vie du joueur :
    def update_health_bar(self, surface):
        # Couleur pour jauge de vie (vert) :
        bar_color = (111, 210, 46)
        # Couleur pour l'arrière plan de la jauge :
        back_bar_color = (60, 63, 60)
        # Position de la jauge de vie ainsi sa largeur et son épesseur :
        bar_position = [self.rect.x - 20, self.rect.y - 10, self._health, 5]
        # Position de l'arrière plan de notre jauge de vie :
        back_bar_position = [self.rect.x - 20, self.rect.y - 10, self._maxHealth, 5]
        # Création barre de vie :
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
