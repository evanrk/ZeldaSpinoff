import pygame

import map
import block

BACKGROUND = (150, 150, 150)

# set dimensions of the screen
screen = pygame.display.set_mode((800, 600))

# caption
pygame.display.set_caption("Zelda?")

# change background color
screen.fill(BACKGROUND)
pygame.display.flip()


# x:y = 4:3
map = map.Map([
[1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1]
])


# run = True
# while run:
#     for event in pygame.event.get():
        
        
#         # quit!
#         if event.type == pygame.QUIT:
#             run = False