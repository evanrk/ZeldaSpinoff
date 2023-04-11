from engine.movables.movable import Square_Movable

class Player(Square_Movable):
    def __init__(self, screen_size, x_start:float, y_start:float, x_hitbox:float, y_hitbox:float, x_size:float, y_size:float, ignore_types, invincibility_frames):
        super().__init__(screen_size, x_start, y_start, x_hitbox, y_hitbox, x_size, y_size, ignore_types)

        self.invincibility_frames = invincibility_frames

        self.inventory = {}
        self.max_health = 3
        self.current_health = self.max_health
        self.invincible = False
    
    def loose_health(self, hit_points):
        """takes away health"""
        if not self.invincible:
            self.current_health -= hit_points # subtracts health but cant go below 0 health
            if self.current_health < 0:
                self.current_health = 0
            return self.current_health
    
    def heal(self, hit_points): # adds health but cant go over max health
        """adds health"""
        self.health += hit_points
        if self.health > self.max_health:
            self.health = self.max_health
        return self.health
    
    def __getitem__(self, key):
        return self.inventory[key]
    
    def update(self, tile_map, other_objects, move_direction=None):
        touching_direction, objects_touching = self.check_collision(tile_map, other_objects)

        match move_direction:
            case "UP":
                if not "UP" in touching_direction:
                    self.move(0, -1)
            
            case "DOWN":
                if not "DOWN" in touching_direction:
                    self.move(0, 1)
            
            case "LEFT":
                if not "LEFT" in touching_direction:
                    self.move(-1, 0)
            
            case "RIGHT":
                if not "RIGHT" in touching_direction:
                    self.move(1, 0)

        return touching_direction, objects_touching