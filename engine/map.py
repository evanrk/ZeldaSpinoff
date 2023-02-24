import math
import engine.tile as tile

class Map:
    """Map [y][x]!!"""
    def __init__(self, screen_size, screen_size_index, start_index, tile_map):
        self.tile_map = tile_map
        self.screens = []
        self.current_screen_index = start_index

        self.x_size = screen_size[0]/(screen_size_index[0]) # gets the x_size of every block
        self.y_size = screen_size[1]/(screen_size_index[1]) # gets the y_size of every block


        # convert map into each screen based on screen_size_index
        for start_y_index in range(0, len(tile_map), screen_size_index[1]):
            mini = []
            for x_index in range(0, len(tile_map[0]), screen_size_index[0]):
                individual = []
                for y_index in range(start_y_index, start_y_index + screen_size_index[1]):
                    individual.append(tile_map[y_index][x_index:x_index+screen_size_index[0]])
                mini.append(individual)
            self.screens.append(mini)

        self.current_screen = self.screens[start_index[1]][start_index[0]]
        self.prerender = [] # a prerender of the current screen

        
        # prerendering the objects in the map
        for row_index in range(len(self.current_screen)):
            prerender_row = []
            for x_index in range(len(self.current_screen[row_index])):
                match self.current_screen[row_index][x_index]:
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
        for index, row in enumerate(self.tile_map):
            map_string += f"{row}\n" if (index < len(self.tile_map) - 1) else f"{row}"
        
        return f"x_size: {self.x_size}\ny_size: {self.y_size}\nmap(reversed):\n{map_string}"


    def replace_screen(self, coordinates: tuple):
        self.current_screen = self.screens[coordinates[1]][coordinates[0]]
        self.prerender = []

        # prerendering the objects in the map
        for row_index in range(len(self.current_screen)):
            prerender_row = []
            for x_index in range(len(self.current_screen[row_index])):
                match self.current_screen[row_index][x_index]:
                    case 0: # Regular 
                        prerender_row.append(tile.Color_Tile((100, 100, 255), x_index, row_index, self.x_size, self.y_size))
                    case 1: # collidable
                        prerender_row.append(tile.Collidable_Color_Tile((100, 255, 100), x_index, row_index, self.x_size, self.y_size))
                    case _:
                        prerender_row.append(tile.Color_Tile((0, 0, 0), x_index, row_index, self.x_size, self.y_size))


            self.prerender.append(prerender_row)