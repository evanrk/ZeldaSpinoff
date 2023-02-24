class Player:
    def __init__(self, SCREEN_SIZE, x_start:float, y_start:float, x_hitbox:float, y_hitbox:float, x_size:float, y_size:float):
        self.screen_size = SCREEN_SIZE
        
        self.x_size = x_size
        self.y_size = y_size
        
        self.x_start = x_start
        self.y_start = y_start
        
        self.x_end = x_start + x_size
        self.y_end = y_start + y_size
        
        self.x_hitbox_start = self.x_end - x_hitbox
        self.y_hitbox_start = self.y_end - y_hitbox
        
        self.x_hitbox = x_hitbox
        self.y_hitbox = y_hitbox
        

    def __str__(self):
        return f"current_pos: ({self.x_current}, {self.y_current})\nhitbox_x: {self.x_hitbox}\nhitbox_y: {self.y_hitbox}"

    def move(self, x:float, y:float):
        self.x_start += x
        self.y_start -= y
        self.x_end = self.x_start + self.x_hitbox
        self.y_end = self.y_start + self.y_hitbox

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