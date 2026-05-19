import random

class Ball():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos
        self.yDir = random.randint(-1,1)
        self.xDir = random.randint(1,2)
        self.counter = 0

    def update_ball(self,game_map,player,ai,game_height,game_width):

        if self.counter %2 == 0:
            # Resets Ball 
            if self.xpos < player.xpos or self.xpos > ai.xpos:
                self.xpos = game_width//2
                self.ypos = game_height//2
                self.yDir = random.randint(-1,1)
                self.xDir = random.randint(1,2)
            
            # Hit Left Paddle
            if abs(self.ypos - player.ypos) < 3 and abs(self.xpos - player.xpos) < 1:
                self.xDir = 2
                if abs(self.ypos - player.ypos) > 0 and abs(self.ypos - player.ypos) < 3:
                    self.yDir = -1
                elif abs(self.ypos - player.ypos) < 0 and abs(self.ypos - player.ypos) > -3:
                    self.yDir = 1
                
            # Hit Right Paddle
            if abs(self.ypos - ai.ypos) < 3 and abs(self.xpos - ai.xpos) < 1:
                self.xDir = 1
                if abs(self.ypos - ai.ypos) > 0 and abs(self.ypos - ai.ypos) < 3:
                    self.yDir = -1
                elif abs(self.ypos - ai.ypos) < 0 and abs(self.ypos - ai.ypos) > -3:
                    self.yDir = 1
            
            # Hit Wall
            if game_map[self.ypos][self.xpos] == "@":
                if self.yDir == -1:
                    self.yDir = 1
                elif self.yDir == 1:
                    self.yDir = -1

            # Left Right
            if self.xDir == 1:
               self.xpos -= 1
            elif self.xDir == 2:
                self.xpos +=1

            # Up Down
            if self.yDir != 0:
                if self.yDir == -1:
                    self.ypos -=1
                elif self.yDir == 1:
                    self.ypos +=1
                
        self.counter += 1
