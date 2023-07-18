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
            

    def __getitem__(self, index):
        return self.prerender[index]
    
    
    def __str__(self):
        """returns a formatted string of the map's important values"""
        map_string = ""
        for index, row in enumerate(self.tile_map):
            map_string += f"{row}\n" if (index < len(self.tile_map) - 1) else f"{row}"
        
        return f"x_size: {self.x_size}\ny_size: {self.y_size}\nmap(reversed):\n{map_string}"


    def replace_screen(self, coordinates: tuple):
        """changes the screen"""
        self.current_screen = self.screens[coordinates[1]][coordinates[0]]
        self.current_screen_index = coordinates
        self.prerender = self.render(coordinates)
        
    
    def render(self, coordinates: tuple):
        """converts numbers into Tile objects"""
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

