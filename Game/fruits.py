import pygame
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./Sprites/fruit2.png")
        self.rect = self.image.get_rect()

rows = [60,447]
cols = [23,506]

fruits_group = pygame.sprite.Group()
def reset_all():
    for i in range (2):
        for j in range (2):
            fruit = Fruit()
            fruit.rect = fruit.image.get_rect()
            fruit.rect.x = cols[j]
            fruit.rect.y = rows[i]
            fruits_group.add(fruit)
reset_all()