import pygame

from engine.map import Map
from engine.player import Player
from engine.tile import Tile

SCROLLING_SPEED = 2

class ZeldaEngine:
    def __init__(self, surface, screen_size, tile_map:Map, player:Player):
        self.tile_map = tile_map
        self.surface = surface
        self.player = player
        self.screen_size = screen_size
        self.pause = False

    def run(self):
        run = True
        while run:
            if not self.pause: # runs when not paused
                keys = pygame.key.get_pressed()
                if not self.player.edges_touching():
                    if keys[pygame.K_UP]:
                        self.player.move(0, 1)
                    elif keys[pygame.K_DOWN]:
                        self.player.move(0, -1)
                    elif keys[pygame.K_LEFT]:
                        self.player.move(-1, 0)
                    elif keys[pygame.K_RIGHT]:
                        self.player.move(1, 0)
                else:
                    if "UP" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[1] > 0:
                            self.animate_screen_switch("UP")
                    elif "DOWN" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[1] < len(self.tile_map[:]):
                            self.animate_screen_switch("DOWN")
                    elif "LEFT" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[0] > 0:
                            self.animate_screen_switch("LEFT")
                    elif "RIGHT" in self.player.edges_touching():
                        if self.tile_map.current_screen_index[0] < len(self.tile_map[0]):
                            self.animate_screen_switch("RIGHT")
                    # if "UP" in self.player.edges_touching():
                    #     if self.tile_map.current_screen_index[1] != 0:
                    #         self.tile_map.replace_screen((self.tile_map.current_screen_index[0], self.tile_map.current_screen_index[1]-1)) # move screen up
                    # elif "DOWN" in self.player.edges_touching():
                    #     if self.tile_map.current_screen_index[1] + 1 != len(self.tile_map):
                    #         self.tile_map.replace_screen((self.tile_map.current_screen_index[0], self.tile_map.current_screen_index[1]+1)) # move screen down
                    # elif "LEFT" in self.player.edges_touching():
                    #     if self.tile_map.current_screen_index[0] != 0:
                    #         self.tile_map.replace_screen((self.tile_map.current_screen_index[0]-1, self.tile_map.current_screen_index[1])) # move screen left
                    # elif "RIGHT" in self.player.edges_touching():
                    #     if self.tile_map.current_screen_index[0] + 1 == len(self.tile_map[0]):
                    #         self.tile_map.replace_screen((self.tile_map.current_screen_index[0]+1, self.tile_map.current_screen_index[1])) # move screen right
                    
            # change screen
            # print(f"({player.x_start}, {player.y_start})")
            self.render_map(self.tile_map)
            self.render_player()
            pygame.display.update()

            for event in pygame.event.get():
                # quit!
                if event.type == pygame.QUIT:
                    run = False


    def render_map(self, tile_map, offset=0, direction="x"):
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
        
        negative = int(max_offset/abs(max_offset))
        # if max_offset >= 1:
        for offset in range(max_offset, negative*1, -negative*SCROLLING_SPEED): # change is 1 or -1 based off of the starting direction
            offset_for_old = offset-max_offset
            self.surface.fill((125, 125, 125))
            self.render_map(ending_screen, offset=offset, direction=direction)
            self.render_map(self.tile_map, offset=offset_for_old, direction=direction)
            pygame.display.update()
        # elif max_offset <= -1:
        #     for offset in range(max_offset, -1, SCROLLING_SPEED): # change is 1 or -1 based off of the starting direction
        #         offset_for_old = offset-max_offset
        #         self.surface.fill((125, 125, 125))
        #         self.render_map(ending_screen, offset=offset, direction=direction)
        #         self.render_map(self.tile_map, offset=offset_for_old, direction=direction)
        #         pygame.display.update()
        # else:
        #     print("wtf")
        
        self.tile_map.replace_screen((x, y))

        pause=True

        self.tile_map
        self.screen_size
