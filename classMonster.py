import pygame
from pygame import mixer

# Création de la classe monstre :
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.velocity = 2
        self.bruitage_mort_monstre = mixer.Sound('Asset/Bruitages/mort du monstre.mp3')
        self.image = pygame.image.load('Asset/Pers_Face_Static1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1080
        self.rect.y = 500

    # Création dégats du monstre :
    def damage(self, amount):
        # Infliger les dégats:
        self.health -= amount

        # Verifie si la vie du monstre est égal a zéro :
        if self.health <= 0:
            # Réaparraitre :
            self.rect.x = 1080
            self.health = self.max_health
            # Bruitages mort :
            pygame.mixer.Channel(0).play(self.bruitage_mort_monstre)

    # Création d'une méthode qui permet d'afficher la barre de vie du monstre :
    def update_health_bar(self, surface):
        # Couleur pour jauge de vie (vert) :
        bar_color = (111, 210, 46)
        # Couleur pour l'arrière plan de la jauge :
        back_bar_color = (60, 63, 60)
        # Position de la jauge de vie ainsi sa largeur et son épesseur :
        bar_position = [self.rect.x - 20, self.rect.y - 10, self.health, 5]
        # Position de l'arrière plan de notre jauge de vie :
        back_bar_position = [self.rect.x - 20, self.rect.y - 10, self.max_health, 5]
        # Création barre de vie :
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    # Instanciation de l'obstacle joueur :
    def rect_obstacles(self):
        return [{'x':self.game.all_player.sprites()[i].rect.x, 'y':self.game.all_player.sprites()[i].rect.y, 'width':self.game.all_player.sprites()[i].rect.width, 'height':self.game.all_player.sprites()[i].rect.height} for i in range(len(self.game.all_player))]

    # Initiation de l'obstacle projectile :
    def rect_projectiles(self):
        return [{'x':self.game.player.all_projectiles.sprites()[i].rect.x, 'y':self.game.player.all_projectiles.sprites()[i].rect.y, 'width':self.game.player.all_projectiles.sprites()[i].rect.width, 'height':self.game.player.all_projectiles.sprites()[i].rect.height} for i in range(len(self.game.player.all_projectiles))]

    # Création d'une méthode pour faire avancer le monstre :
    def foward(self):
        # Si le monstre est en collision avec le joueur :
        deplacement = True
        for obstacle in self.rect_obstacles():
            if not (self.rect.y >= obstacle['y'] + obstacle['height'] or self.rect.y + self.rect.height <= obstacle['y'] or self.rect.x + self.rect.width <= obstacle['x'] + self.velocity or self.rect.x >= obstacle['x'] +obstacle['width']):
                deplacement = False

        if deplacement:
            self.rect.x -= self.velocity

        # Dégats monstre au joueur :
        for monster in self.game.check_collision(self, self.game.all_player):
            monster.damage(self.attack)