import random

from engine.movables.movable import Square_Movable

COOLDOWN = 120
ENEMY_MOVE_SPEED = 0.25

class Enemy(Square_Movable):
    def __init__(self, screen_size, screen_location_x, screen_location_y, x_start: float, y_start: float, x_hitbox: float, y_hitbox: float, x_size: float, y_size: float, ignore_types=[]):
        super().__init__(screen_size, x_start, y_start, x_hitbox, y_hitbox, x_size, y_size, [Enemy]+ignore_types)
        self.screen_location_x = screen_location_x
        self.screen_location_y = screen_location_y
        self.move_frames = 0
        self.direction = None

    
    def calculate_move_logic(self, tile_map, other_objects, player):
            if self.move_frames == 0:
                self.direction = ["UP", "DOWN", "LEFT", "RIGHT"][random.randint(0, 3)]
                self.move_frames = COOLDOWN
            else:
                match self.direction:
                    case "UP":
                        if not self.check_collision(tile_map, other_objects, 0, -ENEMY_MOVE_SPEED) and not self.check_object_collision([player], 0, -ENEMY_MOVE_SPEED):
                            self.move(0, -ENEMY_MOVE_SPEED)
                    case "DOWN":
                        if not self.check_collision(tile_map, other_objects, 0, ENEMY_MOVE_SPEED) and not self.check_object_collision([player], 0, ENEMY_MOVE_SPEED):
                            self.move(0, ENEMY_MOVE_SPEED)
                    case "LEFT":
                        if not self.check_collision(tile_map, other_objects, -ENEMY_MOVE_SPEED, 0) and not self.check_object_collision([player], -ENEMY_MOVE_SPEED, 0):
                            self.move(-ENEMY_MOVE_SPEED, 0)
                    case "RIGHT":
                        if not self.check_collision(tile_map, other_objects, ENEMY_MOVE_SPEED, 0) and not self.check_object_collision([player], ENEMY_MOVE_SPEED, 0):
                            self.move(ENEMY_MOVE_SPEED, 0)
                
                self.move_frames -= 1


    def is_on_screen(self, current_screen_x, current_screen_y):
        return current_screen_x == self.screen_location_x and current_screen_y == self.screen_location_y