class Tile:
    def __init__(self, x_index:int, y_index:int, x_size:float, y_size:float):
        self.x_start = x_index*x_size
        self.y_start = y_index*y_size

        self.x_size = x_size
        self.y_size = y_size

        self.x_end = self.x_start + x_size
        self.y_end = self.y_start + y_size
        self.collidable = False

class Collidable_Tile(Tile):
    def __init__(self, x_index:int, y_index:int, x_size:float, y_size:float):
        super().__init__(x_index, y_index, x_size, y_size)
        self.collidable = True

class Color_Tile(Tile):
    def __init__(self, color, x_index:int, y_index:int, x_size:float, y_size:float):
        super().__init__(x_index, y_index, x_size, y_size)
        
        self.color = color
    
    def __str__(self):
        return f"Color_Tile: Rect({self.x_start}, {self.y_start}, {self.x_end}, {self.y_end})"

class Collidable_Color_Tile(Collidable_Tile):
    def __init__(self, color, x_index:int, y_index:int, x_size:float, y_size:float):
        super().__init__(x_index, y_index, x_size, y_size)

        self.color = color

    def __str__(self):
        return f"Collidable: Rect({self.x_start}, {self.y_start}, {self.x_end}, {self.y_end})"