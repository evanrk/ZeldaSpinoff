import math

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
    
    def check_map_collision(self, tile_map, debug=False):
        # old detection just in case
        
        directions = []

        x_start = self.x_hitbox_start / tile_map.x_size # scaled to indexes on tile_map
        x_end = self.x_hitbox_end / tile_map.x_size # scaled to indexes on tile_map
        x_start_index = int(x_start)
        x_end_index = int(x_end)


        y_start = (self.y_hitbox_start) / tile_map.y_size # scaled to indexes on tile_map
        y_start_index = int(y_start)
        y_end = (self.y_hitbox_end) / tile_map.y_size # scaled to indexes on tile_map
        y_end_index = int(y_end)

    
        if y_start == int(y_start): # check if the top edge of the movable is on the edge of a block
            if debug: print(f"UP:    (({x_start_index}, {x_end_index}), {y_start_index})")
            y_start_index -= 1 # because the hitbox is on the other side
            x_end_index = math.ceil(x_end - 1) # if touching an edge, make sure its checking on the block the movable is on rn
            if not (y_start_index == -1 or y_start_index == len(tile_map.prerender)): # make sure the hitbox is not on the edge of the screen
                if tile_map.prerender[y_start_index][x_start_index].collidable or tile_map.prerender[y_start_index][x_end_index].collidable: # check if the block at the [y][x] values above the hitbox is actually collidable at both sides of the hitbox
                    directions.append("UP")

        if y_end == int(y_end): # check if the bottom edge of the movable is on an edge of a block
            x_end_index = math.ceil(x_end - 1) # if touching an edge, make sure its checking on the block the movable is on rn
            if debug: print(f"DOWN:  (({x_start_index}, {x_end_index}), {y_end_index})")
            if not (y_end_index == -1 or y_end_index == len(tile_map.prerender)): # make sure the hitbox is not on the edge of the screen
                if tile_map.prerender[y_end_index][x_start_index].collidable or tile_map.prerender[y_end_index][x_end_index].collidable: # check if the block at [y][x] is actually collidable at both x indexes
                    directions.append("DOWN")

        if x_start == int(x_start): # check if the left edge of the movable is on the edge of block
            x_start_index -= 1 # because the hitbox in on the other side
            if y_start == int(y_start): y_start_index += 1 # if touching an edge, make sure its checking on the block the movable is on rn
            if y_end == int(y_end): y_end_index -= 1 # same thing here but on the other side
            if debug: print(f"LEFT: ({x_start_index}, ({y_start_index}, {y_end_index}))")
            if not (x_start_index == -1 or x_start_index == len(tile_map.prerender[0])): # make sure the hitbox is not on the edge of the screen
                if tile_map.prerender[y_start_index][x_start_index].collidable or tile_map.prerender[y_end_index][x_start_index].collidable: # check if the block at [y][x] is actually collidable at both y indexes
                    directions.append("LEFT")

        if x_end == int(x_end): # check if the right edge of the movable is on the edge of block
            if y_start == int(y_start) or y_end == int(y_end): x_end_index += 1 # idk it just works
            if y_start == int(y_start): y_start_index += 1 # if touching an edge, make sure its checking on the block the movable is on rn
            if y_end == int(y_end): y_end_index -= 1 # same thing here but on the other side
            if debug: print(f"RIGHT: ({x_end_index}, ({y_start_index}, {y_end_index}))")
            if not (x_end_index == -1 or x_end_index == len(tile_map.prerender[0])): # make sure the hitbox is not on the edge of the screen
                if tile_map.prerender[y_start_index][x_end_index].collidable or tile_map.prerender[y_end_index][x_end_index].collidable: # check if the block at [y][x] is actually collidable at both y indexes
                    directions.append("RIGHT")

        return directions

        # direction = ""
        # if x_move == 0: # moving on the y_axis
        #     x_start = self.x_hitbox_start / tile_map.x_size # scaled to indexes on tile_map
        #     x_end = self.x_hitbox_end / tile_map.x_size # scaled to indexes on tile_map
        #     x_start_index = int(x_start)
        #     x_end_index = int(x_end)

        #     if y_move < 0: # up    
        #         y = (self.y_hitbox_start+y_move) / tile_map.y_size # scaled to indexes on tile_map
        #         y_index = int(y) - 1 # because the hitbox is on the other side
        #         direction = "UP"
        
        #     elif y_move > 0: # down
        #         y = (self.y_hitbox_end+y_move) / tile_map.y_size # scaled to indexes on tile_map
        #         y_index = int(y) 
        #         direction = "DOWN"
        
        #     if y == int(y): # check if on edge of block
        #         if not (y_index == -1 or y_index == len(tile_map.prerender)): # make sure the hitbox is not on the edge of the screen
        #             if tile_map.prerender[y_index][x_start_index].collidable or tile_map.prerender[y_index][x_end_index].collidable: # check if the block at [y][x] is actually collidable at both x indexes
        #                 return direction

        #     # print(f"{y} == {int(y)} = {y == int(y)}\t{x_end} == {int(x_end)} = {x_end == int(x_end)}")
            
        # else: # moving on x_axis
        #     y_start = self.y_hitbox_start / tile_map.y_size # scaled to indexes on tile_map
        #     y_end = self.y_hitbox_end / tile_map.y_size  # scaled to indexes on tile_map
        #     y_start_index = int(y_start)
        #     y_end_index = int(y_end)

        #     if x_move < 0: # left
        #         x = (self.x_hitbox_start+x_move) / tile_map.x_size # scaled to indexes on tile_map
        #         x_index = int(x) - 1 # because the hitbox is on the other side
        #         direction = "LEFT"
            
        #     elif x_move > 0: # right
        #         x = (self.x_hitbox_end+x_move) / tile_map.x_size # scaled to indexes on tile_map
        #         x_index = int(x)
        #         direction = "RIGHT"
            
        #     if x == int(x): # check if on edge of block
        #         if not (x_index == -1 or x_index == len(tile_map.prerender[0])): # make sure the hitbox is not on the edge of the screen
        #             if tile_map.prerender[y_start_index][x_index].collidable or tile_map.prerender[y_end_index][x_index].collidable: # check if the block at [y][x] is actually collidable at both y indexes
        #                 return direction

            # if y_start == int(y_start): # check if on edge of block
            #     print(f"({x_start_index}, {y_start_index}){tile_map.prerender[y_start_index][x_start_index].collidable}")
            #     if not (y_start_index == -1 or y_start_index == len(tile_map.prerender)): # make sure the hitbox is not on the edge of the screen
            #         if tile_map.prerender[y_start_index][x_start_index].collidable or tile_map.prerender[y_start_index][x_end_index].collidable: # check if the block at [y][x] is actually collidable at both x indexes
            #             return "UP"
            
            # if y_end == int(y_end): # check if on edge of block
            #     if not (y_end_index == -1 or y_end_index == len(tile_map.prerender)): # make sure the hitbox is not on the edge of the screen
            #         if tile_map.prerender[y_end_index][x_start_index].collidable or tile_map.prerender[y_end_index][x_end_index].collidable: # check if the block at [y][x] is actually collidable at both x indexes
            #             return True

            # print(f"{y} == {int(y)} = {y == int(y)}\t{x_end} == {int(x_end)} = {x_end == int(x_end)}")
            
        # else: # moving on x_axis
        #     y_start = self.y_hitbox_start / tile_map.y_size # scaled to indexes on tile_map
        #     y_end = self.y_hitbox_end / tile_map.y_size  # scaled to indexes on tile_map
        #     y_start_index = int(y_start)
        #     y_end_index = int(y_end)

        #     if x_move < 0: # left
        #         x = (self.x_hitbox_start) / tile_map.x_size # scaled to indexes on tile_map
        #         x_index = int(x) - 1 # because the hitbox is on the other side
                
            
        #     elif x_move > 0: # right
        #         x = (self.x_hitbox_end) / tile_map.x_size # scaled to indexes on tile_map
        #         x_index = int(x)
        #         "
            
        #     if x == int(x): # check if on edge of block
        #         if not (x_index == -1 or x_index == len(tile_map.prerender[0])): # make sure the hitbox is not on the edge of the screen
        #             if tile_map.prerender[y_start_index][x_index].collidable or tile_map.prerender[y_end_index][x_index].collidable: # check if the block at [y][x] is actually collidable at both y indexes
        #                 return direction


    def check_object_collision2(self, other_objects, x_move, y_move):
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

                on_same_y_axis = (y_start <= other_y_end and y_start >= other_y_start) or (y_end >= other_y_start and y_start <= other_y_start) # in the y range
                on_same_x_axis = (x_start <= other_x_end and x_start >= other_x_start) or (x_end >= other_x_start and x_start <= other_x_start) # in the x range
                if on_same_x_axis and on_same_y_axis: # in both ranges
                    touching.append(object)
            
            elif Circle_Movable in type(object).__bases__ and not(type(object) in self.ignore_types): # do this later lol
                other_x_center = object.x_center
                other_y_center = object.y_center
                other_radius = object.radius
                close_to_x_axis = abs(x_start - other_x_center) <= other_radius or abs(x_end - other_x_center) <= other_radius
        
        return touching
    
    def check_object_collision(self, other_objects):
        """finds all objects touching this one returns a list"""
        directions = []
        touching = {"UP": [], "DOWN": [], "LEFT": [], "RIGHT": []}
        
        x_start = self.x_hitbox_start
        x_end = self.x_hitbox_end
        y_start = self.y_hitbox_start
        y_end = self.y_hitbox_end

        
        for object in other_objects:
            if Square_Movable in type(object).__bases__ and not (type(object) in self.ignore_types):
                other_x_start = object.x_start
                other_x_end = object.x_end
                other_y_start = object.y_start
                other_y_end = object.y_end


                on_same_y_axis = (y_start <= other_y_end and y_start >= other_y_start) or (y_end >= other_y_start and y_start <= other_y_start) # in the y range
                on_same_x_axis = (x_start <= other_x_end and x_start >= other_x_start) or (x_end >= other_x_start and x_start <= other_x_start) # in the x range


                if on_same_x_axis and (y_start <= other_y_end and y_start >= other_y_start): # up?
                    if x_start - other_x_end != 0 and x_end - other_x_start != 0:
                        directions.append("UP")
                        touching["UP"].append(object)
                
                if on_same_x_axis and (y_end >= other_y_start and y_start <= other_y_start): # down? idk lmao
                    if x_start - other_x_end != 0 and x_end - other_x_start != 0:
                        directions.append("DOWN")
                        touching["DOWN"].append(object)

                if on_same_y_axis and (x_start <= other_x_end and x_start >= other_x_start): # left?
                    if y_start - other_y_end != 0 and y_end - other_y_start != 0:
                        directions.append("LEFT")
                        touching["LEFT"].append(object)

                if on_same_y_axis and (x_end >= other_x_start and x_start <= other_x_start): # right?
                    if y_start - other_y_end != 0 and y_end - other_y_start != 0:
                        directions.append("RIGHT")
                        touching["RIGHT"].append(object)
            
            # elif Circle_Movable in type(object).__bases__ and not(type(object) in self.ignore_types): # do this later lol
            #     other_x_center = object.x_center
            #     other_y_center = object.y_center
            #     other_radius = object.radius
            #     close_to_x_axis = abs(x_start - other_x_center) <= other_radius or abs(x_end - other_x_center) <= other_radius
        
        types_touching = []
        for object in touching:
            types_touching.append(type(touching))

        return directions, touching, set(types_touching)

    
    def check_collision(self, tile_map, other_objects):
        map_touching_direction = self.check_map_collision(tile_map)
        object_touching_direction, objects_touching, types_touching = self.check_object_collision(other_objects)
        
        return set(map_touching_direction + object_touching_direction), objects_touching, types_touching


class Circle_Movable(Movable):
    def __init__(self, screen_size, x_center:float, y_center:float, radius:float ):
        super().__init__(screen_size)
        
        self.x_center = x_center
        self.y_center = y_center

        self.radius = radius