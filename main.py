import pygame

from engine.map import Map
from engine.player import Player
from engine.engine import ZeldaEngine

BACKGROUND = (150, 150, 150)
SCREEN_SIZE = (800, 600)
SCREEN_INDEX_SIZE = (8, 6)
PLAYER_HITBOX_X, PLAYER_HITBOX_Y = 40, 25
START = (1, 0)

# set dimensions of the screen
surface = pygame.display.set_mode(SCREEN_SIZE)

# caption
pygame.display.set_caption("Zelda?")

# change background color
surface.fill(BACKGROUND)
pygame.display.flip()

# 0 = Color <-- gotta change this lol
# 1 = Collidable_Color <-- this too
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

engine = ZeldaEngine(surface, SCREEN_SIZE, tile_map, player)
engine.run()