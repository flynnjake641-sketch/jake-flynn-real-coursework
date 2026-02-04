from ghost import Ghost
from grid import grids
import pygame

#This is to set up the screen, along with a clock system to cap fps
pygame.init()
WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MAZEGAME")
clock = pygame.time.Clock()
running = True
level = grids
player_images=[]

for i in range(1,5):
    player_images.append(pygame.transform.scale(pygame.image.load(f"sprites/{i}.png"), (45, 45)))

enemy_img = pygame.transform.scale(pygame.image.load(f"sprites/ghost.png"), (45, 45))

player_x = 450
player_y = 663
direction = 0
counter = 0
#Right, Left, Up, Down
turn_valid =[False, False, False, False]
direction_command = 0
player_speed = 2
score = 0
target = (player_x, player_y)


#Checks if the player is colliding with a dot,
#and increases score then removes the dot if that is the case
def check_collisions(score):
    space_height = (HEIGHT - 50) // 32
    space_width = WIDTH // 30
    if 0 < player_x < 870:
        if level[centre_y // space_height][centre_x // space_width] == 1:
            level[centre_y // space_height][centre_x // space_width] = 0
            score += 10
        elif level[centre_y // space_height][centre_x // space_width] == 2:
                level[centre_y // space_height][centre_x // space_width] = 0
                score += 50

    return score


    
#draws each section of the grid, creating the maze.
def draw_grid():
    space_height = ((HEIGHT - 50) // 32)
    space_width = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, "white", (j * space_width + (0.5*space_width), i*space_height + (0.5*space_height)),4)
            elif level[i][j] == 2:
                pygame.draw.circle(screen, "red", (j * space_width + (0.5*space_width), i*space_height + (0.5*space_height)), 8)
            elif level[i][j] == 3:
                pygame.draw.line(screen, "blue", (j * space_width + (0.5*space_width), i*space_height), (j * space_width + (0.5*space_width), (i+1)*space_height),8)
            elif level[i][j] == 4:
                pygame.draw.line(screen, "blue", (j * space_width, i * space_height + (0.5 * space_height)), ((j+1) * space_width, i * space_height + (0.5 * space_height)), 8)
            elif level[i][j] == 5:
                pygame.draw.line(screen, "blue", (j * space_width, i * space_height + (0.5 * space_height)), (j * space_width + (0.5*space_width), (i+1)*space_height) , 8)
            elif level[i][j] == 6:
                pygame.draw.line(screen, "blue", (j * space_width + (0.5*space_width), (i+1)*space_height), ((j+1) * space_width, i * space_height + (0.5 * space_height)), 8)
            elif level[i][j] == 7:
                pygame.draw.line(screen, "blue", (j * space_width + (0.5*space_width), i*space_height), ((j+1) * space_width, i * space_height + (0.5 * space_height)), 8)
            elif level[i][j] ==8:
                pygame.draw.line(screen, "blue", (j * space_width, i * space_height + (0.5 * space_height)),  (j * space_width + (0.5*space_width), i*space_height), 8)


    
#class player:

    #def __init__(self, speed,):
        
        
def draw_player():
    #0-right, 1-left, 2-up, 3-down
    if direction == 0:
        screen.blit(player_images[counter// 5], (player_x, player_y))
    elif direction == 1:
        screen.blit(pygame.transform.flip(player_images[counter// 5],True, False), (player_x, player_y))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(player_images[counter// 5], 90), (player_x, player_y))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(player_images[counter// 5], 270), (player_x, player_y))    

def check_position(centrex, centrey):
    #Right, Left, Up, Down
    turns = [False, False, False, False]
    space_height = ((HEIGHT - 50) // 32)
    space_width = (WIDTH // 30)
    num3 = 15
    #check collisions based on centre x and centre y of player + or - num3
    if centrex //30 < 29:
        #checks if you can turn in the direction opposite to where you are currently going
        if direction == 0: 
            if level[centrey//space_height][(centrex - num3)//space_width] < 3:
                turns[1] = True
        elif direction == 1: 
            if level[centrey//space_height][(centrex + num3)//space_width] < 3:
                turns[0] = True
        elif direction == 2: 
            if level[(centrey + num3)//space_height][centrex//space_width] < 3:
                turns[3] = True
        elif direction == 3: 
            if level[(centrey - num3)//space_height][centrex//space_width] < 3:
                turns[2] = True

         # checks 
        if direction == 2 or direction == 3:
            #checks your around the midpoint of square
            if 12 <= centrex % space_width <= 18:
                if level[(centrey + num3) // space_height][centrex // space_width] <3:
                    turns[3] = True
                if level[(centrey - num3) // space_height][centrex // space_width] <3:
                    turns[2] = True
            if 12 <= centrey % space_height <= 18:
                if level[centrey // space_height][(centrex - space_width) // space_width] <3:
                    turns[1] = True
                if level[centrey// space_height][(centrex + space_width) // space_width] <3:
                    turns[0] = True
        # checks           
        if direction == 0 or direction == 1:
            #checks your around the midpoint of square
            if 12 <= centrex % space_width <= 18:
                if level[(centrey + space_height) // space_height][centrex // space_width] <3:
                    turns[3] = True
                if level[(centrey - space_height) // space_height][centrex // space_width] <3:
                    turns[2] = True
            if 12 <= centrey % space_height <= 18:
                if level[centrey // space_height][(centrex - num3) // space_width] <3:
                    turns[1] = True
                if level[centrey// space_height][(centrex + num3) // space_width] <3:
                    turns[0] = True         

    else:
        turns[0] = True
        turns[1] = True
        

    
    return turns

def move_player(play_x, play_y):
    #r, l, u, d
    if direction == 0 and turn_valid[0]:
        play_x += player_speed
    elif direction == 1 and turn_valid[1]:
        play_x -= player_speed
    elif direction == 2 and turn_valid[2]:
        play_y -= player_speed
    elif direction == 3 and turn_valid[3]:
        play_y += player_speed

    return play_x, play_y    
    
#sets the characters position to a premade point
character_pos = pygame.Vector2(500, 500)

#create objects of the ghost class
turns = Ghost.check_collisions()
ghost1 = Ghost(2, 440, 388, 2, target, enemy_img, screen, level, turns)
ghost2 = Ghost(2, 440, 438, 2, target, enemy_img, screen, level, turns)
ghost3 = Ghost(2, 440, 438, 2, target, enemy_img, screen, level, turns)


#main game loop
while running:
    clock.tick(60)
    if counter < 19:
        counter += 1
    else:
        counter = 0
#change the screen to purple
    screen.fill("#CC6CE7")    
    draw_grid()
    draw_player()
    Ghost.draw(ghost1)
    Ghost.draw(ghost2)
    Ghost.draw(ghost3)
    centre_x = player_x + 23
    centre_y = player_y + 23
    turn_valid = check_position(centre_x, centre_y)
    player_x, player_y = move_player(player_x, player_y)
    turns = ghost1.check_collisions()
    ghost1.move_ghost()
    score = check_collisions(score)
    print(score)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                direction_command = 0
            elif event.key == pygame.K_a:
                direction_command = 1
            elif event.key == pygame.K_w:
                direction_command = 2
            elif event.key == pygame.K_s:
                direction_command = 3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d and direction_command == 0:
            direction_command = direction
        elif event.key == pygame.K_a and direction_command == 1:
            direction_command = direction
        elif event.key == pygame.K_w and direction_command == 2:
            direction_command = direction
        elif event.key == pygame.K_s and direction_command == 3:
            direction_command = direction

    for i in range(4):
        if direction_command == i and turn_valid[i]:
            direction = i

    if player_x>900:
        player_x = -47
    elif player_x < -50:
        player_x = 897

    



            
    pygame.display.flip()


pygame.quit() 
