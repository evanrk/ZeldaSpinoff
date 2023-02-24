import pygame

from engine.map import Map
from engine.player import Player
from engine.tile import Tile

SCROLLING_SPEED = 5
OVERWORLD_COLOR = (232, 217, 116)
DUNGEON_COLOR = (76, 91, 115)

class ZeldaEngine:
    def __init__(self, surface, screen_size, tile_map:Map, player:Player):
        self.tile_map = tile_map
        self.surface = surface
        self.player = player
        self.screen_size = screen_size
        self.pause = False
        self.overworld = True


    def run(self):
        run = True
        while run:
            self.fill_background(self.overworld) # CHANGE
            if not self.pause: # runs when not paused
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    if "UP" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[1] > 0:
                            self.animate_screen_switch("UP")
                    else:
                        self.player.move(0, 1)
                
                elif keys[pygame.K_DOWN]:
                    if "DOWN" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[1] < len(self.tile_map.screens)-1: # len is 1 greater than last index value
                            self.animate_screen_switch("DOWN")
                    else:
                        self.player.move(0, -1)

                elif keys[pygame.K_LEFT]:    
                    if "LEFT" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[0] > 0:
                            self.animate_screen_switch("LEFT")
                    else:
                        self.player.move(-1, 0)
                
                elif keys[pygame.K_RIGHT]:
                    if "RIGHT" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[0] < len(self.tile_map.screens[0])-1: # len is 1 greater than last index value
                            self.animate_screen_switch("RIGHT")
                    else:
                        self.player.move(1, 0)
                    
            # change screen
            # print(f"({player.x_start}, {player.y_start})")
            self.render_map(self.tile_map)
            self.render_player()
            pygame.display.update()

            for event in pygame.event.get():
                # quit!
                if event.type == pygame.QUIT:
                    run = False


    def render_map(self, tile_map, offset=0, direction="x", overworld=True):
        for row in tile_map:
            for tile in row:
                if direction == "x":
                    x_offset = offset
                    y_offset = 0
                elif direction == "y":
                    x_offset = 0
                    y_offset = offset
                else:
                    raise ValueError("not an axis")
                if tile.color == "clear":
                    continue
                # print(f"start: ({tile.x_start}, {tile.y_start}) end: ({tile.x_end}, {tile.y_end})")
                rectangle = pygame.Rect(tile.x_start+x_offset, tile.y_start+y_offset, tile.x_size, tile.y_size)
                pygame.draw.rect(self.surface, tile.color, rectangle)
    
    def render_player(self): # changing
        player_rect = pygame.Rect(self.player.x_start, self.player.y_start, self.player.x_hitbox, self.player.y_hitbox)
        pygame.draw.rect(self.surface, (255, 0, 0), player_rect)

    
    def animate_screen_switch(self, starting_direction):
        self.pause = True
        # starting_screen = self.tile_map.current_screen
        if starting_direction == "UP":
            direction = "y"
            max_offset = -self.screen_size[1]
            x = self.tile_map.current_screen_index[0]
            y = self.tile_map.current_screen_index[1] - 1
            ending_screen = self.tile_map.render((x, y))
        elif starting_direction == "DOWN":
            direction = "y"
            max_offset = self.screen_size[1]
            x = self.tile_map.current_screen_index[0]
            y = self.tile_map.current_screen_index[1] + 1
            ending_screen = self.tile_map.render((x, y))
        elif starting_direction == "LEFT":
            direction = "x"
            max_offset = -self.screen_size[0]
            x = self.tile_map.current_screen_index[0] - 1
            y = self.tile_map.current_screen_index[1]
            ending_screen = self.tile_map.render((x, y))
        elif starting_direction == "RIGHT":
            direction = "x"
            max_offset = self.screen_size[0]
            x = self.tile_map.current_screen_index[0] + 1
            y = self.tile_map.current_screen_index[1]
            ending_screen = self.tile_map.render((x, y))
        else:
            raise ValueError("ummm thats not a direction")
        
        negative = int(max_offset/abs(max_offset)) # whether the offset adds or subtracts to the max
        
        where_u_r_going = -negative*SCROLLING_SPEED
        for offset in range(max_offset, negative*1, where_u_r_going): # change is 1 or -1 based off of the starting direction
            self.fill_background(self.overworld)
            
            offset_for_old = offset-max_offset # the offset for the old map
            self.render_map(ending_screen, offset=offset, direction=direction) # renders the new map
            self.render_map(self.tile_map, offset=offset_for_old, direction=direction) # renders the old map


            # print(offset + self.player.x_size)            
            if direction == "x" and negative*offset > self.player.x_size: # if the offset is greater then the player size it will move the player, this prevents the player from going off the screen
                self.player.move(where_u_r_going, 0)
            elif direction == "y" and negative*offset > self.player.y_size: # same here but for y-axis
                self.player.move(0, -where_u_r_going) # position is negative on y-axis
            
            self.render_player()

            pygame.display.update()
        
        
        self.fill_background(self.overworld)
        self.tile_map.replace_screen((x, y))

        self.pause=False


    def fill_background(self, overworld):
        self.surface.fill(OVERWORLD_COLOR if overworld else DUNGEON_COLOR)
