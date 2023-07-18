import random

from engine.models.vector import Vector2d
from engine.movables.movable import Square_Movable

# constants
COOLDOWN = 120
ENEMY_MOVE_SPEED = 0.25


class Enemy(Square_Movable):
    def __init__(self, screen_size, screen_location_x, screen_location_y, x_start: float, y_start: float, x_hitbox: float, y_hitbox: float, x_size: float, y_size: float, ignore_types=[]):
        super().__init__(screen_size, x_start, y_start, x_hitbox, y_hitbox, x_size, y_size, [Enemy]+ignore_types)
        self.screen_location_x = screen_location_x
        self.screen_location_y = screen_location_y
        self.move_frames = 0
        self.chosen_direction = None

    
    def update(self, tile_map, other_objects, player):
        touch_directions, touch_objects, types_touching = self.check_collision(tile_map, other_objects)
        touch_direction_player, _, _ = self.check_object_collision([player])

        self.calculate_move_logic(touch_directions, touch_direction_player)


    def calculate_move_logic(self, touch_directions, touch_direction_player):
            if self.move_frames == 0:
                self.chosen_direction = ["UP", "DOWN", "LEFT", "RIGHT"][random.randint(0, 3)]
                self.move_frames = COOLDOWN
            else:

                match self.chosen_direction:
                    case "UP":
                        if not "UP" in touch_directions and not "UP" in touch_direction_player: # up
                            self.move(Vector2d(0, -ENEMY_MOVE_SPEED))
                    case "DOWN":
                        if not "DOWN" in touch_directions and not "DOWN" in touch_direction_player: # down
                            self.move(Vector2d(0, ENEMY_MOVE_SPEED))
                    case "LEFT":
                        if not "LEFT" in touch_directions and not "LEFT" in touch_direction_player: # left
                            self.move(Vector2d(-ENEMY_MOVE_SPEED, 0))
                    case "RIGHT":
                        if not "RIGHT" in touch_directions and not "RIGHT" in touch_direction_player: # right
                            self.move(Vector2d(ENEMY_MOVE_SPEED, 0))
                
                self.move_frames -= 1


    def is_on_screen(self, current_screen_x, current_screen_y):
        return current_screen_x == self.screen_location_x and current_screen_y == self.screen_location_y