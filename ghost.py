import pygame
class Ghost:
    def __init__(self, speed, ghost_x, ghost_y, ghost_direction, target, img, screen, level):
        self.speed = speed
        self.ghost_x = ghost_x
        self.ghost_y = ghost_y
        self.ghost_centre_x = self.ghost_x + 22
        self.ghost_centre_y = self.ghost_y + 22
        self.direction = ghost_direction
        self.target = target
        self.level = level
        self.turns = self.check_collisions()
        self.screen = screen
        self.img = img
        self.hitbox = self.draw()
       
    def move_ghost(self):
        #r, l, u, d
        #if going right and target is right, keep going if it can
        if self.direction == 0:
            if self.target[0] > self.ghost_x and self.turns[0]:
                self.ghost_x += self.speed
            #collision to right detected
            elif not self.turns[0]:
                #if target below ghost and it is able, turn down
                if self.target[1] > self.ghost_y and self.turns [3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                #if target is above ghost and it is able, turn up
                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                #if target is to left of ghost and it is able, turn left
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                #what to do if target is in direction it cant move
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[1]:
                    seld.direction = 1
                    self.ghost_x -= speed
            #can still go right but target isnt there
            elif self.turns[0]:
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                if self.target[1] > self.ghost_y and self.turns[2]:
                    self.direction = 3
                    self.ghost_y -= self.speed
                else:
                    self.ghost_x += self.speed
        
        #if going left and target is left, keep going if it can
        elif self.direction == 1:
            #if going left but can turn down to chase target, do so
            
            if self.target[1] > self.ghost_y and self.turns[3]:
                self.direction = 3
            #if current direction beneficial, keep going
            elif self.target[0] < self.ghost_x and self.turns[1]:
                self.ghost_x -= self.speed
            #collision to left detected
            elif not self.turns[1]:
                #if target below ghost and it is able, turn down
                if self.target[1] > self.ghost_y and self.turns [3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                #if target is above ghost and it is able, turn up
                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                #if target is to right of ghost and it is able, turn right
                elif self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                #what to do if target is in direction it cant move
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[0]:
                    seld.direction = 0
                    self.ghost_x += speed
            #can still go right but target isnt there
            elif self.turns[1]:
                if self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                if self.target[1] > self.ghost_y and self.turns[2]:
                    self.direction = 3
                    self.ghost_y -= self.speed
                else:
                    self.ghost_x -= self.speed
                    
        #if going up and target is up, keep going if it can
        elif self.direction == 2:
            #if going up but can turn left to chase target, do so           
            if self.target[0] < self.ghost_x and self.turns[1]:
                self.direction = 1
                self.ghost_x -= self.speed
            #if current direction beneficial, keep going
            elif self.target[1] < self.ghost_y and self.turns[2]:
                self.ghost_y -= self.speed
            #collision to left detected
            elif not self.turns[2]:
                #if target to right of ghost and it is able, turn right
                if self.target[0] > self.ghost_x and self.turns [0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                #if target is to left of ghost and it is able, turn left
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                #if target is below ghost and it is able, turn down
                elif self.target[1] > self.ghost_y and self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                #what to do if target is in direction it cant move
                elif self.turns[3]:
                    self.direction = 3
                    self.ghost_y += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[0]:
                    seld.direction = 0
                    self.ghost_x += speed
            #can still go up but target isnt there
            elif self.turns[2]:
                if self.target[0] > self.ghost_x and self.turns [0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                else:
                    self.ghost_y -= self.speed

        #if going down and target is below, keep going if it can
        elif self.direction == 3:
            #if current direction beneficial, keep going
            if self.target[1] > self.ghost_y and self.turns[3]:
                self.ghost_y += self.speed
            #collision below detected
            elif not self.turns[3]:
                #if target to right of ghost and it is able, turn right          
                if self.target[0] > self.ghost_x and self.turns[0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                #if target is to left of ghost and it is able, turn left
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                #if target is above ghost and it is able, turn up
                elif self.target[1] < self.ghost_y and self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                #what to do if target is in direction it cant move
                elif self.turns[2]:
                    self.direction = 2
                    self.ghost_y -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                elif self.turns[0]:
                    seld.direction = 0
                    self.ghost_x += speed                    
            #can still go down but target isnt there
            elif self.turns[3]:
                if self.target[0] > self.ghost_x and self.turns [0]:
                    self.direction = 0
                    self.ghost_x += self.speed
                elif self.target[0] < self.ghost_x and self.turns[1]:
                    self.direction = 1
                    self.ghost_x -= self.speed
                else:
                    self.ghost_y += self.speed
        #allow ghosts to move off screen and come back other side
        if self.ghost_x < -30:
            self.ghost_x = 900
        elif self.ghost_x > 900:
            self.ghost_x - 30

        return self.ghost_x, self.ghost_y, self.direction
                
                
        

    def draw(self):
        self.screen.blit(self.img, (self.ghost_x, self.ghost_y))
        ghost_rect = pygame.rect.Rect((self.ghost_centre_x - 18, self.ghost_centre_y - 18), (36, 36))
        return ghost_rect

    def check_collisions(self):
        space_height = ((950 - 50) // 32)
        space_width = (900 // 30)
        num3 = 15
        #R,L,U,D
        self.turns = [False, False, False, False]
        #check ghost is on legitimate square
        if self.ghost_centre_x // 30 < 29:
            #checks that ghost can go in the opposite direction to where it is going
            if self.level[self.ghost_centre_y // space_height][(self.ghost_centre_x - num3)//space_width] < 3:
                self.turns[1] = True
            if self.level[self.ghost_centre_y // space_height][(self.ghost_centre_x + num3)//space_width] < 3:
                self.turns[0] = True
            if self.level[(self.ghost_centre_y + num3) // space_height][self.ghost_centre_x //space_width] < 3:
                self.turns[3] = True
            if self.level[(self.ghost_centre_y - num3) // space_height][self.ghost_centre_x //space_width] < 3:
                self.turns[2] = True
                
            #while moveing up or down checks you can go left or right
            if self.direction == 2 or self.direction == 3:
                #checks ghost is roughly in the middle of the square
                if 12<= self.ghost_centre_x % space_width <= 18:
                    if self.level[(self.ghost_centre_y + num3) // space_height][self.ghost_centre_x // space_width] < 3:
                        self.turns[3] = True
                    if self.level[(self.ghost_centre_y - num3) // space_height][self.ghost_centre_x // space_width] < 3:
                        self.turns[2] = True

                if 12<= self.ghost_centre_y % space_height <= 18:
                    if self.level[self.ghost_centre_y // space_height][(self.ghost_centre_x - space_width) // space_width] < 3:
                        self.turns[1] = True
                    if self.level[self.ghost_centre_y // space_height][(self.ghost_centre_x + space_width) // space_width] < 3:
                        self.turns[0] = True

            #while moving left or right checks you can go up or down
            if self.direction == 0 or self.direction == 1:
                #checks ghost is roughly in the middle of the square
                if 12<= self.ghost_centre_x % space_width <= 18:
                    if self.level[(self.ghost_centre_y + num3) // space_height][self.ghost_centre_x // space_width] < 3:
                        self.turns[3] = True
                    if self.level[(self.ghost_centre_y - num3) // space_height][self.ghost_centre_x // space_width] < 3:
                        self.turns[2] = True

                if 12<= self.ghost_centre_y % space_height <= 18:
                    if self.level[self.ghost_centre_y // space_height][(self.ghost_centre_x - num3) // space_width] < 3:
                        self.turns[1] = True
                    if self.level[self.ghost_centre_y // space_height][(self.ghost_centre_x + num3) // space_width] < 3:
                        self.turns[0] = True

            else:
                self.turns[0] = True
                self.turns[1] = True
            
                
        return self.turns

    
