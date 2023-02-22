class Tile:
    def __init__(self, x_index:int, y_index:int, x_size:float, y_size:float):
        self.start_x = x_index*x_size
        self.start_y = y_index*y_size

        self.x_size = x_size
        self.y_size = y_size

        self.end_x = self.start_x + x_size
        self.end_y = self.start_y + y_size
        self.collidable = False

class Collidable_Tile(Tile):
    def __init__(self, x_index:int, y_index:int, x_size:float, y_size:float):
        super().__init__(x_index, y_index, x_size, y_size)
        self.collidable = True

class Color_Tile(Tile):
    def __init__(self, color, x_index:int, y_index:int, x_size:float, y_size:float):
        super().__init__(x_index, y_index, x_size, y_size)
        
        self.color = color

class Collidable_Color_Tile(Collidable_Tile):
    def __init__(self, color, x_index:int, y_index:int, x_size:float, y_size:float):
        super().__init__(x_index, y_index, x_size, y_size)

        self.color = color

