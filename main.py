import pygame

import engine.tile as map_tile
from engine.map import Map
from engine.player import Player
from engine.engine import ZeldaEngine

BACKGROUND = (150, 150, 150)
SCREEN_SIZE = (800, 600)
SCREEN_INDEX_SIZE = (8, 6)
PLAYER_HITBOX_X, PLAYER_HITBOX_Y = 40, 25
START = (1, 1)

# set dimensions of the screen
surface = pygame.display.set_mode(SCREEN_SIZE)

# caption
pygame.display.set_caption("Zelda?")

# change background color
surface.fill(BACKGROUND)
pygame.display.flip()

# 0 = Color <-- gotta change this lol
# 1 = Collidable_Color <-- this too

# x:y = 4:3
# screen1 = Map(SCREEN_SIZE, [
# [1, 0, 0, 1, 1, 0, 0, 1],
# [1, 0, 0, 1, 1, 0, 0, 1],
# [1, 0, 1, 1, 1, 1, 0, 1],
# [1, 0, 1, 1, 1, 1, 0, 1],
# [1, 0, 0, 1, 1, 0, 0, 1],
# [1, 0, 0, 1, 1, 0, 0, 1]
# ])


tile_map = Map(SCREEN_SIZE, SCREEN_INDEX_SIZE, START, [
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
])

player = Player(SCREEN_SIZE, 100, 100, PLAYER_HITBOX_X, PLAYER_HITBOX_Y)

engine = ZeldaEngine(surface, tile_map, player)
engine.run()

# def render_map(map: Map):
#     for row in map:
#         for tile in row:
#             # print(f"start: ({tile.x_start}, {tile.y_start}) end: ({tile.x_end}, {tile.y_end})")
#             rectangle = pygame.Rect(tile.x_start, tile.y_start, tile.x_size, tile.y_size)
#             pygame.draw.rect(surface, tile.color, rectangle)

# def render_player(player: Player): # changing
#     player_rect = pygame.Rect(player.x_start, player.y_start, player.x_hitbox, player.y_hitbox)
#     pygame.draw.rect(surface, (255, 0, 0), player_rect)

# render_map(tile_map)
# pygame.display.update()



# render_player(player)


# run = True
# while run:
#     keys = pygame.key.get_pressed()
#     if not player.edges_touching():
#         if keys[pygame.K_UP]:
#             player.move(0, 1)
#         elif keys[pygame.K_DOWN]:
#             player.move(0, -1)
#         elif keys[pygame.K_LEFT]:
#             player.move(-1, 0)
#         elif keys[pygame.K_RIGHT]:
#             player.move(1, 0)
#     else:
#         if "UP" in player.edges_touching():
#             if tile_map.current_screen_index[1] != 0:
#                 tile_map.replace_screen((tile_map.current_screen_index[0], tile_map.current_screen_index[1]-1)) # move screen up
#         elif "DOWN" in player.edges_touching():
#             if tile_map.current_screen_index[1] + 1 != len(tile_map):
#                 tile_map.replace_screen((tile_map.current_screen_index[0], tile_map.current_screen_index[1]+1)) # move screen down
#         elif "LEFT" in player.edges_touching():
#             if tile_map.current_screen_index[0] != 0:
#                 tile_map.replace_screen((tile_map.current_screen_index[0]-1, tile_map.current_screen_index[1])) # move screen left
#         elif "RIGHT" in player.edges_touching():
#             if tile_map.current_screen_index[0] + 1 == len(tile_map[0]):
#                 tile_map.replace_screen((tile_map.current_screen_index[0]+1, tile_map.current_screen_index[1])) # move screen right
        
#          # change screen

#     # print(f"({player.x_start}, {player.y_start})")
#     render_map(tile_map)
#     render_player(player)
#     pygame.display.update()

#     # print(player.edges_touching())

#     for event in pygame.event.get():
#         # quit!
#         if event.type == pygame.QUIT:
#             run = False