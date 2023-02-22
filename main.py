import pygame

import engine.tile as map_tile
from engine.map import Map
from engine.player import Player

BACKGROUND = (150, 150, 150)

# set dimensions of the screen
SCREEN_SIZE = (800, 600)
surface = pygame.display.set_mode(SCREEN_SIZE)

# caption
pygame.display.set_caption("Zelda?")

# change background color
surface.fill(BACKGROUND)
pygame.display.flip()

# 0 = Color <-- gotta change this lol
# 1 = Collidable_Color <-- this too

# x:y = 4:3
screen1 = Map(SCREEN_SIZE, [
[1, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 0, 0, 1],
[1, 0, 0, 1, 1, 0, 0, 1]
])

screen2 = Map(SCREEN_SIZE, [
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
])

START = (1, 2)

screens = [
[screen1, screen2, screen1],
[screen2, screen1, screen2],
[screen1, screen2, screen1],
]

def render_map(map: Map):
    for row in map:
        for tile in row:
            # print(f"start: ({tile.x_start}, {tile.y_start}) end: ({tile.x_end}, {tile.y_end})")
            rectangle = pygame.Rect(tile.x_start, tile.y_start, tile.x_size, tile.y_size)
            pygame.draw.rect(surface, tile.color, rectangle)

def render_player(player: Player): # changing
    player_rect = pygame.Rect(player.x_start, player.y_start, player.x_hitbox, player.y_hitbox)
    pygame.draw.rect(surface, (255, 0, 0), player_rect)

render_map(screen2)
pygame.display.update()



player = Player(100, 100, 40, 20)
render_player(player)


run = True
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(0, 1)
    elif keys[pygame.K_DOWN]:
        player.move(0, -1)
    elif keys[pygame.K_LEFT]:
        player.move(-1, 0)
    elif keys[pygame.K_RIGHT]:
        player.move(1, 0)

    render_map(screen2)
    render_player(player)
    pygame.display.update()

    for event in pygame.event.get():
        # quit!
        if event.type == pygame.QUIT:
            run = False