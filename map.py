class Map:
    """Map is accessed by [x][y] instead of the normal [y][x] bc its easier"""
    def __init__(self, screen_size, map):
        self.map = []
        self.unreversed_map = map

        for x_index in range(len(map[0])):
            new_row = []
            for y_index in range(len(map)):
                # print(y_index)
                new_row.append(map[y_index][x_index])
            
            self.map.append(new_row)
    
        self.x_size = screen_size[0]/len(map) # gets the x_size of every block
        self.y_size = screen_size[1]/len(map[0]) # gets the y_size of every block

    def __getitem__(self, index):
        return self.map[index]
    
    def __str__(self):
        map_string = ""
        for index, row in enumerate(self.unreversed_map):
            map_string += f"{row}\n" if (index < len(self.unreversed_map) - 1) else f"{row}"
        
        return f"x_size: {self.x_size}\ny_size: {self.y_size}\nmap(reversed):\n{map_string}"
