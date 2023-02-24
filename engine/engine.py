import pygame

from engine.map import Map
from engine.player import Player
from engine.tile import Tile

class ZeldaEngine:
    def __init__(self, surface, tile_map:Map, player:Player):
        self.tile_map = tile_map
        self.surface = surface
        self.player = player

    def run(self):
        run = True
        while run:
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
                    if self.tile_map.current_screen_index[1] != 0:
                        self.tile_map.replace_screen((self.tile_map.current_screen_index[0], self.tile_map.current_screen_index[1]-1)) # move screen up
                elif "DOWN" in self.player.edges_touching():
                    if self.tile_map.current_screen_index[1] + 1 != len(self.tile_map):
                        self.tile_map.replace_screen((self.tile_map.current_screen_index[0], self.tile_map.current_screen_index[1]+1)) # move screen down
                elif "LEFT" in self.player.edges_touching():
                    if self.tile_map.current_screen_index[0] != 0:
                        self.tile_map.replace_screen((self.tile_map.current_screen_index[0]-1, self.tile_map.current_screen_index[1])) # move screen left
                elif "RIGHT" in self.player.edges_touching():
                    if self.tile_map.current_screen_index[0] + 1 == len(self.tile_map[0]):
                        self.tile_map.replace_screen((self.tile_map.current_screen_index[0]+1, self.tile_map.current_screen_index[1])) # move screen right
                
            # change screen
            # print(f"({player.x_start}, {player.y_start})")
            self.render_map()
            self.render_player()
            pygame.display.update()

            for event in pygame.event.get():
                # quit!
                if event.type == pygame.QUIT:
                    run = False


    def render_map(self):
        for row in self.tile_map:
            for tile in row:
                # print(f"start: ({tile.x_start}, {tile.y_start}) end: ({tile.x_end}, {tile.y_end})")
                rectangle = pygame.Rect(tile.x_start, tile.y_start, tile.x_size, tile.y_size)
                pygame.draw.rect(self.surface, tile.color, rectangle)
    

    def render_player(self): # changing
        player_rect = pygame.Rect(self.player.x_start, self.player.y_start, self.player.x_hitbox, self.player.y_hitbox)
        pygame.draw.rect(self.surface, (255, 0, 0), player_rect)