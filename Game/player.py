import pygame
from . import map

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.facing_dir = 0
        self.current_node = map.starting_node
        self.target_node = self.current_node
        self.velocity = 3
        self.velocity_vector = [0,0]
        self.is_moving = False
        self.score = 0
        self.is_dead = False
        self.ate_dot = False
        self.ate_fruit = False
        self.scary_mode = 0

        img = pygame.image.load("./Sprites/pacman0.png").convert_alpha()
        self.images.append(img)
        self.rect = self.images[0].get_rect()

        img = pygame.image.load("./Sprites/pacman1.png").convert_alpha()
        self.images.append(img)
        self.rect = self.images[1].get_rect()

        img = pygame.image.load("./Sprites/pacman2.png").convert_alpha()
        self.images.append(img)
        self.rect = self.images[2].get_rect()

        img = pygame.image.load("./Sprites/pacman3.png").convert_alpha()
        self.images.append(img)
        self.rect = self.images[3].get_rect()

        self.rect = self.rect.inflate(-self.rect.width // 2, -self.rect.height // 2) #halving player hitbox
        self.rect.x = map.starting_node.x
        self.rect.y = map.starting_node.y

    
    def draw(self,screen):
        screen.blit(self.images[self.facing_dir],self.rect)


    # When moving the player, if the player's x or y coordinate exceedes that of the target node, we manually
    # set the player's x or y to that of the target node.
    # When moving right or left, we add a boundary of 50 pixels (could be much smaller) so that we don't 
    # immediately change the player's coordinates when pacman is moving through the tunnel

    def move_right(self):
        self.rect.x += self.velocity
        self.velocity_vector = [self.velocity,0]
        if self.rect.x > (self.target_node.x):
            if self.rect.x < (self.target_node.x+50): 
                self.rect.x = self.target_node.x

        #checking if pacman goes through the tunnel
        if self.rect.x < -20:
            self.rect.x = 540

        if self.rect.x > 540:
            self.rect.x = -20

    def move_left(self):
        self.rect.x -= self.velocity
        self.velocity_vector = [-self.velocity,0]
        if self.rect.x < self.target_node.x:
            if self.rect.x > self.target_node.x -50:
                self.rect.x = self.target_node.x

        #checking if pacman goes through the tunnel
        if self.rect.x < -20:
            self.rect.x = 540

        if self.rect.x > 540:
            self.rect.x = -20
    
    def move_up(self):
        self.rect.y -= self.velocity
        self.velocity_vector = [0,-self.velocity]
        if self.rect.y < self.target_node.y:
            self.rect.y = self.target_node.y
    
    def move_down(self):
        self.rect.y += self.velocity
        self.velocity_vector = [0,self.velocity]
        if self.rect.y > self.target_node.y:
            self.rect.y = self.target_node.y

    def update_movement(self):
        if self.rect.x < self.target_node.x:
            if (self.current_node == map.c5 and self.target_node == map.h5):
                self.move_left()
            else:
                self.move_right()
        elif self.rect.x > self.target_node.x:
            if (self.current_node == map.h5 and self.target_node == map.c5):
                self.move_right()
            else:
                self.move_left()
        if self.rect.y < self.target_node.y:
            self.move_down()
        elif self.rect.y > self.target_node.y:
            self.move_up()

        #upon reaching the destination, update current node and stop moving
        if self.rect.x == self.target_node.x and self.rect.y == self.target_node.y: 
            self.is_moving = False
            self.velocity_vector = [0,0]
            self.current_node = self.target_node
