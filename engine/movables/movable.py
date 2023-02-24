class Movable:
    def __init__(self, screen_size):
        self.screen_size = screen_size
    

    def __str__(self):
        return f"current_pos: ({self.x_current}, {self.y_current})\nhitbox_x: {self.x_hitbox}\nhitbox_y: {self.y_hitbox}"
 


class Square_Movable(Movable):
    def __init__(self, screen_size, x_start:float, y_start:float, x_hitbox:float, y_hitbox:float, x_size:float, y_size:float):
        super().__init__(screen_size)
        
        self.x_size = x_size
        self.y_size = y_size
        
        self.x_start = x_start
        self.y_start = y_start
        
        self.x_end = x_start + x_size
        self.y_end = y_start + y_size
        
        self.x_hitbox = x_hitbox
        self.y_hitbox = y_hitbox
        
        self.x_hitbox_start = self.x_end - self.x_hitbox
        self.y_hitbox_start = self.y_end - self.y_hitbox
        
        self.x_hitbox_end = self.x_end
        self.y_hitbox_end = self.y_end

    
    def move(self, x:float, y:float):
        self.x_start += x
        self.y_start += y
        
        self.x_end = self.x_start + self.x_hitbox
        self.y_end = self.y_start + self.y_hitbox

        self.x_hitbox_start = self.x_end - self.x_hitbox
        self.y_hitbox_start = self.y_end - self.y_hitbox

        self.x_hitbox_end = self.x_end
        self.y_hitbox_end = self.y_end


    def edges_touching(self):
        edges = []
        if self.y_start == 0:
            edges.append("UP")
        if self.y_end == self.screen_size[1]:
            edges.append("DOWN")
        if self.x_start == 0:
            edges.append("LEFT")
        if self.x_end == self.screen_size[0]:
            edges.append("RIGHT")
        return edges
    
    def check_collision(self, tile_map, x_move, y_move):
        if x_move and y_move:
            raise ValueError("woah, you cant move diagonally")
        
        direction = ""
        if x_move == 0: # moving on the y_axis
            x_start = self.x_hitbox_start / tile_map.x_size # scaled to indexes on tile_map
            x_end = self.x_hitbox_end / tile_map.x_size # scaled to indexes on tile_map
            x_start_index = int(x_start)
            x_end_index = int(x_end)

            if y_move < 0: # up        
                y = (self.y_hitbox_start+y_move) / tile_map.y_size # scaled to indexes on tile_map
                y_index = int(y) - 1 # because the hitbox is on the other side
                direction = "UP"
        
            elif y_move > 0: # down
                y = (self.y_hitbox_end+y_move) / tile_map.y_size # scaled to indexes on tile_map
                y_index = int(y) 
                direction = "DOWN"
        
            if y == int(y): # check if on edge of block
                if not (y_index == -1 or y_index == len(tile_map.prerender)): # make sure the hitbox is not on the edge of the screen
                    if tile_map.prerender[y_index][x_start_index].collidable or tile_map.prerender[y_index][x_end_index].collidable: # check if the block at [y][x] is actually collidable at both x indexes
                        return direction

            # print(f"{y} == {int(y)} = {y == int(y)}\t{x_end} == {int(x_end)} = {x_end == int(x_end)}")
            
        else: # moving on x_axis
            y_start = self.y_hitbox_start / tile_map.y_size # scaled to indexes on tile_map
            y_end = self.y_hitbox_end / tile_map.y_size  # scaled to indexes on tile_map
            y_start_index = int(y_start)
            y_end_index = int(y_end)

            if x_move < 0: # left
                x = (self.x_hitbox_start+x_move) / tile_map.x_size # scaled to indexes on tile_map
                x_index = int(x) - 1 # because the hitbox is on the other side
                direction = "LEFT"
            
            elif x_move > 0: # right
                x = (self.x_hitbox_end+x_move) / tile_map.x_size # scaled to indexes on tile_map
                x_index = int(x)
                direction = "RIGHT"
            
            if x == int(x): # check if on edge of block
                if not (x_index == -1 or x_index == len(tile_map.prerender[0])): # make sure the hitbox is not on the edge of the screen
                    if tile_map.prerender[y_start_index][x_index].collidable or tile_map.prerender[y_end_index][x_index].collidable: # check if the block at [y][x] is actually collidable at both y indexes
                        return direction



class Circle_Movable(Movable):
    def __init__(self, screen_size, x_center:float, y_center:float, radius:float ):
        super().__init__(screen_size)
        
        self.x_center = x_center
        self.y_center = y_center

        self.radius = radius