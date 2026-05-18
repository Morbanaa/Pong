# Teddy Rodd
# Morbanaa Studios
# Pong

from game_manager import Game_Manger
import time

def main():
    game_manager = Game_Manger(25,80) # height then width
    GAME_SPEED = .05

    game_manager.world_gen()
    while True:
        # Update
        game_manager.update_objects() # Needs to be before update map
        game_manager.update_map()

        # Render
        game_manager.render_world()

        # Util
        time.sleep(GAME_SPEED)
        game_manager.clear_move_cursor()


if __name__ == "__main__":
    main()