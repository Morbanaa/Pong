# Teddy Rodd
# Morbanaa Studios
# Pong

import sys
from player import Player
from ai import Ai
from ball import Ball

# Colors
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY  = '\033[90m'
# Reset Color
RESET = '\033[0m'

class Game_Manger():
    def __init__(self,game_height,game_width):
        self.game_height = game_height
        self.game_width = game_width
        self.game_map = []

        # Creates Player Object
        self.player = Player(self.game_height//2,3)

        # Creates Ai Object
        self.ai = Ai(self.game_height//2,self.game_width-3)

        # Creates Ball Object
        self.ball = Ball(self.game_height//2,self.game_width//2)

    def world_gen(self):
        for y in range(self.game_height):
            row = []
            for x in range(self.game_width):
                if y == 0 or y == self.game_height -1 or x == 0 or x == self.game_width -1:
                    row.append("@")
                else:
                    row.append(" ")
            self.game_map.append(row)
    
    def update_objects(self):
        self.player.update_player(self.game_map)
        self.ai.update_ai(self.game_map)
        self.ball.update_ball(self.game_map,self.player,self.ai,self.game_height,self.game_width)

    def update_map(self):

        for i in range(-2,3):
            
            self.game_map[self.player.ypos + i][self.player.xpos] = "|"
            self.game_map[self.ai.ypos + i][self.ai.xpos] = "|"

        if self.game_map[self.player.ypos-3][self.player.xpos] != "@":
            self.game_map[self.player.ypos -3][self.player.xpos] = " "
        if self.game_map[self.player.ypos+3][self.player.xpos] != "@":
            self.game_map[self.player.ypos +3][self.player.xpos] = " "

        if self.game_map[self.ai.ypos-3][self.ai.xpos] != "@":
            self.game_map[self.ai.ypos -3][self.ai.xpos] = " "
        if self.game_map[self.ai.ypos+3][self.ai.xpos] != "@":
            self.game_map[self.ai.ypos +3][self.ai.xpos] = " "

    def render_world(self):
        for y in range(self.game_height):
            for x in range(self.game_width):
                if self.game_map[y][x] == "|":
                    print(f"{GREEN}|{RESET}",end="")
                elif y == self.ball.ypos and x == self.ball.xpos:
                    print(f"{RED}o{RESET}",end="")
                else:
                    print(f"{DARK_GRAY}{self.game_map[y][x]}{RESET}",end="")
            print()

    def clear_move_cursor(self):
        sys.stdout.write("\033[H")
        sys.stdout.flush()

