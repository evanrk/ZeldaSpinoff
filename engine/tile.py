class Tile:
    def __init__(self, start_x, start_y, x_size, y_size):
        self.start_x = start_x
        self.start_y = start_y

        self.end_x = start_x + x_size
        self.end_y = start_y + y_size

class Collidable_Tile(Tile):
    def __init__(self, start_x, start_y, x_size, y_size):
        super().__init__(start_x, start_y, x_size, y_size)
