import pygame

from PIL import Image


full_heart_image = Image.open("engine/sprites/smiley_heart.png")
full_heart_image_data = full_heart_image.getdata()


def draw_full_heart(x_offset, y_offset, size, surface):
    x_size = int(size/full_heart_image.size[0])    
    y_size = int(size/full_heart_image.size[1])

    for index, color in enumerate(full_heart_image_data):
        if color[3] == 0:
            continue
        else:
            color = color[:3]

        x_start = (index % full_heart_image.size[0])*x_size
        y_start = (index // full_heart_image.size[1])*y_size

        rectangle = pygame.Rect(x_start+x_offset, y_start+y_offset, x_size, y_size)
        pygame.draw.rect(surface, color, rectangle)  

