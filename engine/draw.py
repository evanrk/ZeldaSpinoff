import pygame

from PIL import Image


boring_heart_image = Image.open("engine/sprites/full_heart_img.png")
boring_heart_image_data = boring_heart_image.getdata()

smiley_heart_image = Image.open("engine/sprites/smiley_heart.png")
smiley_heart_image_data = smiley_heart_image.getdata()

def draw_full_heart(x_offset, y_offset, size, surface, smiley=False):
    if smiley:
        heart = smiley_heart_image
        heart_data = smiley_heart_image_data
    else:
        heart = boring_heart_image
        heart_data = boring_heart_image_data

    x_size = int(size/heart.size[0])    
    y_size = int(size/heart.size[1])

    for index, color in enumerate(heart_data):
        if color[3] == 0:
            continue
        else:
            color = color[:3]

        x_start = (index % heart.size[0])*x_size
        y_start = (index // heart.size[1])*y_size

        rectangle = pygame.Rect(x_start+x_offset, y_start+y_offset, x_size, y_size)
        pygame.draw.rect(surface, color, rectangle)  

