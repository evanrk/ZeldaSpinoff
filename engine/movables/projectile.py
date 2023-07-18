from engine.movables.movable import Square_Movable
from engine.models.vector import Vector2d
class Projectile(Square_Movable):
    def __init__(self, screen_size, x_start: float, y_start: float, x_hitbox: float, y_hitbox: float, x_size: float, y_size: float, direction:Vector2d, owner_type:type, attack_types:list, ignore_types=[]):
        super().__init__(screen_size, x_start, y_start, x_hitbox, y_hitbox, x_size, y_size, ignore_types + owner_type)
    
    def update(self, tile_map, other_objects, player):
        touch_directions, touch_objects, touch_types, touching_by_type = self.check_collision(tile_map, other_objects)
        

        # self.calculate_move_logic(touch_directions, touch_direction_player)