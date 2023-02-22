import pygame

import engine.tile as tile
from engine.map import Map

BACKGROUND = (150, 150, 150)

# set dimensions of the screen
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# caption
pygame.display.set_caption("Zelda?")

# change background color
screen.fill(BACKGROUND)
pygame.display.flip()

# 0 = Color <-- gotta change this lol
# 1 = Collidable_Color <-- this too

# x:y = 4:3
map = Map(SCREEN_SIZE, [
[1, 0, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 1]
])

run = True
while run:
    for event in pygame.event.get():
        
        
        # quit!
        if event.type == pygame.QUIT:
            run = False