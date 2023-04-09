import pygame

from engine.map import Map
from engine.movables.player import Player
from engine.movables.enemy import Enemy
from engine.engine import ZeldaEngine

BACKGROUND = (150, 150, 150)
SCREEN_SIZE = (800, 600)
SCREEN_INDEX_SIZE = (8, 6)
PLAYER_HITBOX_X, PLAYER_HITBOX_Y = 40, 25
PLAYER_SIZE_X, PLAYER_SIZE_Y = 40, 25
START = (0, 0)
INVINCIBILITY_FRAMES = 120 # 2 seconds

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
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
[1, 0, 2, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
[1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

player = Player(SCREEN_SIZE, 100, 200, PLAYER_HITBOX_X, PLAYER_HITBOX_Y, PLAYER_SIZE_X, PLAYER_SIZE_Y, [Player], 60)

# enemy = Enemy(SCREEN_SIZE, 100, 100, PLAYER_HITBOX_X, PLAYER_HITBOX_Y, PLAYER_SIZE_X, PLAYER_SIZE_Y, [Player])

engine = ZeldaEngine(surface, SCREEN_SIZE, tile_map, player)
engine.run()


# fix enemy collision with player