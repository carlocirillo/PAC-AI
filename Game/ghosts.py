import pygame
from . import map
from . import nodes


SCREEN_WIDTH = 540
SCREEN_HEIGHT = 640

class Ghost(pygame.sprite.Sprite):
    def __init__(self,id):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.images = []
        self.facing_dir = 0
        self.current_node = map.ghosts_starting_node
        self.target_node = map.ghosts_starting_node
        self.velocity = 2
        self.velocity_vector = [0,0]
        self.is_moving = False
        self.is_scared = False
        self.released = 0
        
        self.images.append(pygame.image.load(("./Sprites/Fantasmi/Spaventato.png")))
        self.rect = self.images[0].get_rect()
        self.image = self.images[self.facing_dir]

        self.path_to_pacman = []
        self.path_away_from_pacman = []
    
    def __repr__(self):
        return f"{self.id}_ghost"

    def draw(self,screen):
        if not self.is_scared:
            screen.blit(self.images[self.facing_dir],self.rect)
        else:
            screen.blit(self.images[0],self.rect)

    def move_right(self):
        if self.released:
            self.facing_dir = 1
            self.rect.x += self.velocity
            self.velocity_vector = [self.velocity,0]
            if (self.rect.x > self.target_node.x and self.rect.x < self.target_node.x + 50):
                self.rect.x = self.target_node.x
                #self.current_node = self.target_node
        if self.rect.x < -20:
            self.rect.x = 540

        if self.rect.x > 540:
            self.rect.x = -20

    def move_left(self):
        if self.released:
            self.facing_dir = 3
            self.rect.x -= self.velocity
            self.velocity_vector = [-self.velocity,0]
            if (self.rect.x < self.target_node.x and self.rect.x > self.target_node.x -50):
                self.rect.x = self.target_node.x
                #self.current_node = self.target_node
        if self.rect.x < -20:
            self.rect.x = 540

        if self.rect.x > 540:
            self.rect.x = -20

    def move_up(self):
        if self.released:
            self.facing_dir = 2
            self.rect.y -= self.velocity
            self.velocity_vector = [0,-self.velocity]
            if self.rect.y < self.target_node.y:
                self.rect.y = self.target_node.y
                #self.current_node = self.target_node
    
    def move_down(self):
        if self.released:
            self.facing_dir = 4
            self.rect.y += self.velocity
            self.velocity_vector = [0,self.velocity]
            if self.rect.y > self.target_node.y:
                self.rect.y = self.target_node.y
                #self.current_node = self.target_node

    def update_movement(self):
        if (not self.released):
            return
        if self.is_scared:
            self.velocity = 1
        else:
            self.velocity = 2
        #update to next target node when target node is reached
        if (self.current_node == self.target_node):
            if (not self.is_scared and self.path_to_pacman):
                self.target_node = self.path_to_pacman.pop(0)
            elif (self.is_scared and self.path_away_from_pacman):
                self.target_node = self.path_away_from_pacman.pop(0)

        #move toward target node
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
        elif self.rect.y < self.target_node.y:
            self.move_down()
        elif self.rect.y > self.target_node.y:
            self.move_up()

    def get_mode(self):
        if(self.is_scared):
            return 1
        return 0
        

red_ghost = Ghost("red")
red_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosso/Rosso1.png")))
red_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosso/Rosso2.png")))
red_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosso/Rosso3.png")))
red_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosso/Rosso4.png")))
red_ghost.rect.x = SCREEN_WIDTH/2 - 2*(red_ghost.rect.width)
red_ghost.rect.y = SCREEN_HEIGHT/2 -55
red_ghost.facing_dir = 1

pink_ghost = Ghost("pink")
pink_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosa/Rosa1.png")))
pink_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosa/Rosa4.png")))
pink_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosa/Rosa2.png")))
pink_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Rosa/Rosa3.png")))
pink_ghost.rect.x = SCREEN_WIDTH/2 - (pink_ghost.rect.width)
pink_ghost.rect.y = SCREEN_HEIGHT/2 -55
pink_ghost.facing_dir = 1


blue_ghost = Ghost("blue")
blue_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Blu/Blu1.png")))
blue_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Blu/Blu2.png")))
blue_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Blu/Blu3.png")))
blue_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Blu/Blu4.png")))
blue_ghost.rect.x = SCREEN_WIDTH/2 
blue_ghost.rect.y = SCREEN_HEIGHT/2 -55
blue_ghost.facing_dir = 3


orange_ghost = Ghost("orange")
orange_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Arancione/Arancione1.png")))
orange_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Arancione/Arancione2.png")))
orange_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Arancione/Arancione3.png")))
orange_ghost.images.append(pygame.image.load(("./Sprites/Fantasmi/Arancione/Arancione4.png")))
orange_ghost.rect.x = SCREEN_WIDTH/2 + (orange_ghost.rect.width)
orange_ghost.rect.y = SCREEN_HEIGHT/2 -55
orange_ghost.facing_dir = 3


ghosts_group = pygame.sprite.Group()
ghosts_group.add(red_ghost)
ghosts_group.add(pink_ghost)
ghosts_group.add(blue_ghost)
ghosts_group.add(orange_ghost)


def release(ghost,player):
    if ghost.target_node == map.ghosts_starting_node:
        if ghost.rect.x<map.ghosts_starting_node.x:
            ghost.rect.x += ghost.velocity

        elif ghost.rect.x>map.ghosts_starting_node.x:
            ghost.rect.x -= ghost.velocity

        if (ghost.rect.x>map.ghosts_starting_node.x-2 and ghost.rect.x<map.ghosts_starting_node.x+2):
            ghost.rect.x = map.ghosts_starting_node.x
            if(ghost.rect.y > map.ghosts_starting_node.y):
                ghost.rect.y -= ghost.velocity
            else: 
                ghost.rect.y = map.ghosts_starting_node.y
                ghost.released += 1
                ghost.path_to_pacman = nodes.bfs_shortest_path(map.ghosts_starting_node,player.current_node)
