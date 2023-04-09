class Movable:
    def __init__(self, screen_size):
        self.screen_size = screen_size
 


class Square_Movable(Movable):
    def __init__(self, screen_size, x_start:float, y_start:float, x_hitbox:float, y_hitbox:float, x_size:float, y_size:float, ignore_types:list):
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

        self.ignore_types = ignore_types

    
    def move(self, x:float, y:float):
        """moves the object by changing the values"""
        self.x_start += x
        self.y_start += y
        
        self.x_end = self.x_start + self.x_hitbox
        self.y_end = self.y_start + self.y_hitbox

        self.x_hitbox_start = self.x_end - self.x_hitbox
        self.y_hitbox_start = self.y_end - self.y_hitbox

        self.x_hitbox_end = self.x_end
        self.y_hitbox_end = self.y_end


    def edges_touching(self):
        """checks if the object is touching an edge of the screen"""
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
    
    def check_map_collision(self, tile_map, x_move, y_move):
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


    def check_object_collision(self, other_objects, x_move, y_move):
        """finds all objects touching this one returns a list"""
        if x_move and y_move:
            raise ValueError("woah, cant move diagonally")

        touching = []
        x_start = self.x_hitbox_start+x_move
        x_end = self.x_hitbox_end+x_move
        y_start = self.y_hitbox_start+y_move
        y_end = self.y_hitbox_end+y_move

        for object in other_objects:
            if Square_Movable in type(object).__bases__ and not (type(object) in self.ignore_types):
                other_x_start = object.x_start
                other_x_end = object.x_end
                other_y_start = object.y_start
                other_y_end = object.y_end

                on_same_y_axis = (y_start < other_y_end and y_start > other_y_start) or (y_end > other_y_start and y_start < other_y_start) # in the y range
                on_same_x_axis = (x_start < other_x_end and x_start > other_x_start) or (x_end > other_x_start and x_start < other_x_start) # in the x range
                if on_same_x_axis and on_same_y_axis: # in both ranges
                    touching.append(object)
            
            elif Circle_Movable in type(object).__bases__ and not(type(object) in self.ignore_types): # do this later lol
                other_x_center = object.x_center
                other_y_center = object.y_center
                other_radius = object.radius
                close_to_x_axis = abs(x_start - other_x_center) <= other_radius or abs(x_end - other_x_center) <= other_radius
        
        return touching

    
    def check_collision(self, tile_map, other_objects, x_move, y_move):
        return self.check_map_collision(tile_map, x_move, y_move) or self.check_object_collision(other_objects, x_move, y_move)
class Circle_Movable(Movable):
    def __init__(self, screen_size, x_center:float, y_center:float, radius:float ):
        super().__init__(screen_size)
        
        self.x_center = x_center
        self.y_center = y_center

        self.radius = radius