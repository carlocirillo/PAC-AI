import pygame
from pygame.locals import *
from . import map
from . player import Player
from . import dots
from . import fruits
from . import ghosts
from . import nodes
import numpy as np
from math import sqrt

#defining constants
SCREEN_WIDTH = 540
SCREEN_HEIGHT = 640
max_dist = sqrt(pow(SCREEN_HEIGHT,2)+pow(SCREEN_WIDTH,2))

pygame.init()
 
pygame.font.init()
font = pygame.font.Font("./Sprites/ByteBounce.ttf",36) #FONT

clock = pygame.time.Clock()

#LOADING SPRITES
background_image = pygame.image.load("./Sprites/map.png")
pacman_sprites = pygame.image.load("./Sprites/pacman0.png")

#WINDOW SETTINGS
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pac-Man')
pygame.display.set_icon(pacman_sprites)

#INITIALIZING PLAYER
player = Player()
player.current_node = map.starting_node

#TIME SETTINGS
start_time = pygame.time.get_ticks()
scary_mode_start_time = 0
current_ticks = 0

#REFRESHING SCREEN
def refresh_screen():
    screen.fill("black")
    screen.blit(background_image, (0, 0)) #drawing the background
    dots.dots_group.draw(screen) #drawing the dots
    fruits.fruits_group.draw(screen) #drawing the fruits
    player.draw(screen) #drawing the player
    for ghost in ghosts.ghosts_group: #drawing every ghost
        ghost.draw(screen)
    score_text = font.render(f"SCORE: {player.score}", True, (255, 255, 255)) #drawing the score
    screen.blit(score_text, (20, 600))
    pygame.display.flip()  # refresh on-screen display
 
 
if __name__ == "__main__":
    #GAME LOOP
    game = True
    while game:

        current_time = pygame.time.get_ticks() #get the current time

        #player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        #logical updates
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.current_node.left_node and player.is_moving == False:
            player.target_node = player.current_node.left_node
            player.is_moving = True
            player.facing_dir = 2

        if keys[pygame.K_RIGHT] and player.current_node.right_node and player.is_moving == False:
            player.target_node = player.current_node.right_node
            player.is_moving = True
            player.facing_dir = 0
    
        if keys[pygame.K_UP] and player.current_node.up_node and player.is_moving == False:
            player.target_node = player.current_node.up_node
            player.is_moving = True
            player.facing_dir = 1

        if keys[pygame.K_DOWN] and player.current_node.down_node and player.is_moving == False:
            player.target_node = player.current_node.down_node
            player.is_moving = True
            player.facing_dir = 3

        #releasing ghosts

        if current_time - start_time < 13000:
            if (current_time - start_time > 2000):
                ghosts.release(ghosts.red_ghost,player)
            if (current_time - start_time > 4000): 
                ghosts.release(ghosts.orange_ghost,player)
            if (current_time - start_time > 6000):
                ghosts.release(ghosts.blue_ghost,player)
            if (current_time - start_time > 8000):
                ghosts.release(ghosts.pink_ghost,player)

        #player movement updates
        player.update_movement()
    

        #update ghosts movement
        for ghost in ghosts.ghosts_group:
            if (abs(ghost.rect.x - ghost.target_node.x) < 1 and abs(ghost.rect.y - ghost.target_node.y) < 1):
                ghost.current_node = ghost.target_node
                if(ghost.released):
                    if not ghost.is_scared: #check if player isn't in scary mode
                        ghost.path_to_pacman = nodes.bfs_shortest_path(ghost.current_node, player.target_node)
                    else:
                        if(ghost.rect.x <= player.rect.x and ghost.rect.y <= player.rect.y):
                            ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.a1)
                        elif(ghost.rect.x > player.rect.x and ghost.rect.y <= player.rect.y):
                            ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.j1)
                        elif(ghost.rect.x <= player.rect.x and ghost.rect.y > player.rect.y):
                            ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.a10)
                        elif(ghost.rect.x > player.rect.x and ghost.rect.y > player.rect.y):
                            ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.j10)
            ghost.update_movement()




        #kill the dots on collision
        collided_dots = pygame.sprite.spritecollide(player, dots.dots_group, dokill=True) 
        if collided_dots:
            player.score += 10*len(collided_dots)
        if not dots.dots_group:
            print("you won!")
            game = False

        #kill the fruits on collision
        collided_fruits = pygame.sprite.spritecollide(player, fruits.fruits_group, dokill=True) 
        if collided_fruits:
            player.score += 50*len(collided_fruits)
            #enter scary mode
            for ghost in ghosts.ghosts_group:
                ghost.is_scared = True
            scary_mode_start_time = pygame.time.get_ticks()
        if (current_time - scary_mode_start_time) > 3000: #for 3 seconds player enters scary mode
            scary_mode_start_time = 0 #after 3 seconds set timer back to zero and exit scary mode
            for ghost in ghosts.ghosts_group:
                ghost.is_scared = False

        #lose the game upon colliding with ghost
        collided_ghosts = pygame.sprite.spritecollide(player, ghosts.ghosts_group,dokill = False)
        if collided_ghosts:
            print("You lost!")
            game = False


        refresh_screen()

        clock.tick(60)        
#END OF PLAYABLE GAME









#DEFINING FUNCIONS FOR THE AGENT BELOW

def get_distance_to_dot(dot):
    dist = abs(player.rect.x-dot.rect.x)+abs(player.rect.y-dot.rect.y)
    return dist

def get_distance_to_closest_dot():
    min_dist = float('inf')
    for dot in dots.dots_group:
        dist = get_distance_to_dot(dot)
        if dist < min_dist:
            min_dist = dist
    return min_dist if min_dist != float('inf') else 0


def relative_velocity_from_ghost_n(player,ghost):
    vector = [(player.velocity_vector[0] - ghost.velocity_vector[0])/6, (player.velocity_vector[1] - ghost.velocity_vector[1])/6]
    return vector

def get_observation():
    #pacman_x_n = player.rect.x/SCREEN_WIDTH #normalize dimensions
    #pacman_y_n = player.rect.y/SCREEN_HEIGHT
    closest_dist = 100
    dist_from_closest_ghost = []
    rel_vel_from_closest_ghost = []

    for ghost in ghosts.ghosts_group:
        delta_x_n = abs(ghost.rect.x/SCREEN_WIDTH -  player.rect.x/SCREEN_WIDTH)
        delta_y_n = abs(ghost.rect.y/SCREEN_HEIGHT - player.rect.y/SCREEN_HEIGHT)
        if delta_x_n + delta_y_n < closest_dist:
            closest_dist = delta_x_n + delta_y_n
            dist_from_closest_ghost = [delta_x_n, delta_y_n]
            rel_vel_from_closest_ghost = relative_velocity_from_ghost_n(player,ghost)


    #scary_mode = player.scary_mode

    #dist_to_dot_n = (get_distance_to_closest_dot())/max_dist


    obs = dist_from_closest_ghost + rel_vel_from_closest_ghost + [player.rect.x,player.rect.y]# + [dist_to_dot_n] #+ [scary_mode]
    
    return np.array(obs, dtype=np.float32)

def step_game(action):
    current_time = pygame.time.get_ticks()
    global current_ticks
    current_ticks += 1
    # Mappa l'azione dell'agente alla direzione (come facevi coi tasti)
    if action == 0 and player.current_node.right_node and not player.is_moving:
        player.target_node = player.current_node.right_node
        player.is_moving = True
        player.facing_dir = 0
    elif action == 1 and player.current_node.up_node and not player.is_moving:
        player.target_node = player.current_node.up_node
        player.is_moving = True
        player.facing_dir = 1
    elif action == 2 and player.current_node.left_node and not player.is_moving:
        player.target_node = player.current_node.left_node
        player.is_moving = True
        player.facing_dir = 2
    elif action == 3 and player.current_node.down_node and not player.is_moving:
        player.target_node = player.current_node.down_node
        player.is_moving = True
        player.facing_dir = 3

    # Movimento Pacman
    player.update_movement()
    player.ate_dot = False
    player.ate_fruit = False

    # Releasing ghosts
    if current_ticks < 780:
        if (current_ticks > 120):
            ghosts.release(ghosts.red_ghost,player)
        if (current_ticks > 240): 
            ghosts.release(ghosts.orange_ghost,player)
        if (current_ticks > 360):
            ghosts.release(ghosts.blue_ghost,player)
        if (current_ticks > 480):
            ghosts.release(ghosts.pink_ghost,player)


    # Movimento dei fantasmi
    for ghost in ghosts.ghosts_group:
        if (abs(ghost.rect.x - ghost.target_node.x) < 1 and abs(ghost.rect.y - ghost.target_node.y) < 1):
            ghost.current_node = ghost.target_node
            if ghost.released:
                if not ghost.is_scared:
                    ghost.path_to_pacman = nodes.bfs_shortest_path(ghost.current_node, player.target_node)
                else:
                    if(ghost.rect.x <= player.rect.x and ghost.rect.y <= player.rect.y):
                        ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.a1)
                    elif(ghost.rect.x > player.rect.x and ghost.rect.y <= player.rect.y):
                        ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.j1)
                    elif(ghost.rect.x <= player.rect.x and ghost.rect.y > player.rect.y):
                        ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.a10)
                    elif(ghost.rect.x > player.rect.x and ghost.rect.y > player.rect.y):
                        ghost.path_away_from_pacman = nodes.bfs_shortest_path(ghost.current_node, map.j10)
        ghost.update_movement()

    # Collisioni con i dots
    collided_dots = pygame.sprite.spritecollide(player, dots.dots_group, dokill=True)
    if collided_dots:
        player.score += 10 * len(collided_dots)
        player.ate_dot = True
    if not dots.dots_group:
        print("you won!")

    #collisioni con i fruits
    collided_fruits = pygame.sprite.spritecollide(player, fruits.fruits_group, dokill=True) 
    global scary_mode_start_time
    if collided_fruits:
        player.score += 50*len(collided_fruits)
        player.ate_fruit = True
        #enter scary mode
        player.scary_mode = 1
        for ghost in ghosts.ghosts_group:
            ghost.is_scared = True
        scary_mode_start_time = pygame.time.get_ticks()

    if (current_time - scary_mode_start_time) > 3000: #for 3 seconds player enters scary mode
        scary_mode_start_time = 0 #after 3 seconds set timer back to zero and exit scary mode
        player.scary_mode = 0
        for ghost in ghosts.ghosts_group:
            ghost.is_scared = False

    # Controllo collisione con fantasmi
    collided_ghosts = pygame.sprite.spritecollide(player, ghosts.ghosts_group,dokill = False)
    if collided_ghosts:
        print("You lost!")
        player.is_dead = True

def is_done():
    # Caso 1: il giocatore è morto (devi settare questa flag in step_game quando collide con un fantasma)
    if player.is_dead:
        #print(f"Episode reward: {episode_reward}")
        return True

    # Caso 2: tutti i dots sono stati mangiati
    if not dots.dots_group:  # gruppo vuoto
        return True

    return False

def get_reward():
    reward = 0.0

    if player.ate_dot:
        reward += 10.0

    if player.ate_fruit:
        reward += 10.0

    if player.is_dead:
        reward -= 50.0

    # penalità piccola per stimolare l’azione
    if not player.is_moving:
        reward -= 0.5  # ~ -3 al secondo
    else:
        reward += 0.5
    return reward

def reset_game():
    # Reset del giocatore
    global player
    player = Player()

    # Reset dei fantasmi
    for ghost in ghosts.ghosts_group:
        ghost.facing_dir = 0
        ghost.current_node = map.ghosts_starting_node
        ghost.target_node = map.ghosts_starting_node
        ghost.velocity = 2
        ghost.is_scared = False
        ghost.is_moving = False
        ghost.released = False
        ghost.rect = ghost.images[0].get_rect()
        ghost.path_to_pacman = []
        ghost.path_away_from_pacman = []
        ghost.rect.x = SCREEN_WIDTH/2 - (ghost.rect.width)
        ghost.rect.y = SCREEN_HEIGHT/2 -55

    # Reset dei dots e frutti
    dots.reset_all()      # Ricrea tutti i dots
    fruits.reset_all()    # Ricrea tutti i frutti

    # Reset del tempo
    global start_time, scary_mode_start_time, current_ticks
    start_time = pygame.time.get_ticks()
    scary_mode_start_time = 0
    current_ticks = 0


    # Ritorna la prima osservazione
    return get_observation()
