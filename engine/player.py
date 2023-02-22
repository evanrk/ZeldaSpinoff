class Player:
    def __init__(self, x_start:float, y_start:float, x_hitbox:float, y_hitbox:float):
        self.x_start = x_start
        self.y_start = y_start
        self.x_hitbox = x_hitbox
        self.y_hitbox = y_hitbox
        self.x_end = x_start + x_hitbox
        self.y_end = y_start + y_hitbox

    def __str__(self):
        return f"current_pos: ({self.x_current}, {self.y_current})\nhitbox_x: {self.x_hitbox}\nhitbox_y: {self.y_hitbox}"

    def move(self, x:float, y:float):
        self.x_start += x
        self.y_start -= y
        self.x_end = self.x_start + self.x_hitbox
        self.y_end = self.y_start + self.y_hitbox