class Map:
    """Map is accessed by [x][y] instead of the normal [y][x] bc its easier"""
    def __init__(self, screen_size, map):
        self.map = map
        self.prerender = []

        # for column in 

        self.x_size = screen_size[0]/len(map) # gets the x_size of every block
        self.y_size = screen_size[1]/len(map[0]) # gets the y_size of every block

    def __getitem__(self, index):
        return self.prerender[index]
    
    def __str__(self):
        map_string = ""
        for index, row in enumerate(self.map):
            map_string += f"{row}\n" if (index < len(self.map) - 1) else f"{row}"
        
        return f"x_size: {self.x_size}\ny_size: {self.y_size}\nmap(reversed):\n{map_string}"
