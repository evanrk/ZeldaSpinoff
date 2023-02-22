class Map:
    """Map is accessed by [x][y] instead of the normal [y][x] bc its easier"""
    def __init__(self, map):
        self.map = []

        for x_index in range(len(map[0])):
            new_row = []
            for y_index in range(len(map)):
                # print(y_index)
                new_row.append(map[y_index][x_index])
            
            self.map.append(new_row)
    
    def __getitem__(self, index):
        return self.map[index]
