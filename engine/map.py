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
        self.prerender = self.render(start_index)


    def check_collision(self, movable, x_move, y_move):
        if x_move and y_move:
            raise ValueError("woah, you cant move diagonally")
        
        direction = ""
        if x_move == 0: # moving on the y_axis
            x_start = movable.x_hitbox_start / self.x_size # scaled to indexes on tile_map
            x_end = movable.x_hitbox_end / self.x_size # scaled to indexes on tile_map
            x_start_index = int(x_start)
            x_end_index = int(x_end)

            if y_move < 0: # up        
                y = (movable.y_hitbox_start+y_move) / self.y_size # scaled to indexes on tile_map
                y_index = int(y) - 1 # because the hitbox is on the other side
                direction = "UP"
        
            elif y_move > 0: # down
                y = (movable.y_hitbox_end+y_move) / self.y_size # scaled to indexes on tile_map
                y_index = int(y) 
                direction = "DOWN"
        
            if y == int(y): # check if on edge of block
                if not (y_index == -1 or y_index == len(self.prerender)): # make sure the hitbox is not on the edge of the screen
                    if self.prerender[y_index][x_start_index].collidable or self.prerender[y_index][x_end_index].collidable: # check if the block at [y][x] is actually collidable at both x indexes
                        return direction

            # print(f"{y} == {int(y)} = {y == int(y)}\t{x_end} == {int(x_end)} = {x_end == int(x_end)}")
            
        else: # moving on x_axis
            y_start = movable.y_hitbox_start / self.y_size # scaled to indexes on tile_map
            y_end = movable.y_hitbox_end / self.y_size  # scaled to indexes on tile_map
            y_start_index = int(y_start)
            y_end_index = int(y_end)

            if x_move < 0: # left
                x = (movable.x_hitbox_start+x_move) / self.x_size # scaled to indexes on tile_map
                x_index = int(x) - 1 # because the hitbox is on the other side
                direction = "LEFT"
            
            elif x_move > 0: # right
                x = (movable.x_hitbox_end+x_move) / self.x_size # scaled to indexes on tile_map
                x_index = int(x)
                direction = "RIGHT"
            
            if x == int(x): # check if on edge of block
                if not (x_index == -1 or x_index == len(self.prerender[0])): # make sure the hitbox is not on the edge of the screen
                    if self.prerender[y_start_index][x_index].collidable or self.prerender[y_end_index][x_index].collidable: # check if the block at [y][x] is actually collidable at both y indexes
                        return direction
            
        

    def __getitem__(self, index):
        return self.prerender[index]
    
    
    def __str__(self):
        map_string = ""
        for index, row in enumerate(self.tile_map):
            map_string += f"{row}\n" if (index < len(self.tile_map) - 1) else f"{row}"
        
        return f"x_size: {self.x_size}\ny_size: {self.y_size}\nmap(reversed):\n{map_string}"


    def replace_screen(self, coordinates: tuple):
        self.current_screen = self.screens[coordinates[1]][coordinates[0]]
        self.current_screen_index = coordinates
        self.prerender = self.render(coordinates)
        
    
    def render(self, coordinates: tuple):
        new_screen = self.screens[coordinates[1]][coordinates[0]]
        prerender = []

        # for prerendering the objects in the map
        for row_index in range(len(new_screen)):
            prerender_row = []
            for x_index in range(len(new_screen[row_index])):
                match new_screen[row_index][x_index]:
                    case 0: # Regular 
                        prerender_row.append(tile.Color_Tile((100, 100, 255), x_index, row_index, self.x_size, self.y_size))
                    case 1: # collidable
                        prerender_row.append(tile.Collidable_Color_Tile((100, 255, 100), x_index, row_index, self.x_size, self.y_size))
                    case 2: # Clear 
                        prerender_row.append(tile.Color_Tile("clear", x_index, row_index, self.x_size, self.y_size))
                    case _:
                        prerender_row.append(tile.Color_Tile((0, 0, 0), x_index, row_index, self.x_size, self.y_size))
            prerender.append(prerender_row)
        
        return prerender

