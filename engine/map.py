import math
import engine.tile as tile

class Map:
    """Map [y][x]!!"""
    def __init__(self, screen_size, map):
        self.map = map
        self.prerender = []

        self.x_size = screen_size[0]/(len(map[0])) # gets the x_size of every block
        self.y_size = screen_size[1]/(len(map)) # gets the y_size of every block

        # prerendering the objects in the map
        for row_index in range(len(map)):
            prerender_row = []
            for x_index in range(len(map[row_index])):
                match map[row_index][x_index]:
                    case 0: # Regular 
                        prerender_row.append(tile.Color_Tile((100, 100, 255), x_index, row_index, self.x_size, self.y_size))
                    case 1: # collidable
                        prerender_row.append(tile.Collidable_Color_Tile((100, 255, 100), x_index, row_index, self.x_size, self.y_size))
                    case _:
                        prerender_row.append(tile.Color_Tile((0, 0, 0), x_index, row_index, self.x_size, self.y_size))


            self.prerender.append(prerender_row)

    def check_collision(self, moveable, x_move, y_move):
        if x_move and y_move:
            raise ValueError("woah, you cant move diagonally")
        
        if y_move > 0: # up
            pass
        elif y_move < 0: # down
            pass
        elif x_move < 0: # left
            pass
        elif x_move > 0: # right
            pass


    def __getitem__(self, index):
        return self.prerender[index]
    
    def __str__(self):
        map_string = ""
        for index, row in enumerate(self.map):
            map_string += f"{row}\n" if (index < len(self.map) - 1) else f"{row}"
        
        return f"x_size: {self.x_size}\ny_size: {self.y_size}\nmap(reversed):\n{map_string}"