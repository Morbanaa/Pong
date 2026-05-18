import random

class Ball():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos
        self.yDir = random.randint(-2,2)
        self.xDir = random.randint(0,1)
        self.counter = 0

    def update_ball(self,game_map):

        if self.counter %2 == 0:
            if self.xDir == 1:
               self.xpos += 1
            elif self.xDir == 0:
                self.xpos -=1

            if self.yDir != 0:
                if self.yDir == -2:
                    self.ypos -=2
                elif self.yDir == -1:
                    self.ypos -=1
                elif self.yDir == 1:
                    self.ypos +=1
                elif self.yDir == 2:
                    self.ypos += 2

        self.counter += 1
         