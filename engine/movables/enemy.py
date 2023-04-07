from engine.movables.movable import Square_Movable

class Enemy(Square_Movable):
    def __init__(self, screen_size, x_start: float, y_start: float, x_hitbox: float, y_hitbox: float, x_size: float, y_size: float, ignore_types):
        super().__init__(screen_size, x_start, y_start, x_hitbox, y_hitbox, x_size, y_size, ignore_types)

        