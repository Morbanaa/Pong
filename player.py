import keyboard

class Player():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

    def update_player(self,game_map):
        if keyboard.is_pressed("W") and game_map[self.ypos -3][self.xpos] != "@":
            self.ypos -= 1
        if keyboard.is_pressed("S") and game_map[self.ypos +3][self.xpos] != "@":
            self.ypos += 1