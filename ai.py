import keyboard

class Ai():
    def __init__(self,ypos,xpos):
        self.ypos = ypos
        self.xpos = xpos

    def update_ai(self,game_map):
        if keyboard.is_pressed("UP") and game_map[self.ypos -3][self.xpos] != "@":
            self.ypos -= 1
        if keyboard.is_pressed("DOWN") and game_map[self.ypos +3][self.xpos] != "@":
            self.ypos += 1