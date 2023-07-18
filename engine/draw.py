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

    draw_image(heart, heart_data, x_offset, y_offset, size, size, surface) 

def draw_half_heart(x_offset, y_offset, size, surface, smiley=False, hole_color=(0, 0, 0), cut_vertical=True):
    if smiley:
        heart = smiley_heart_image
        heart_data = smiley_heart_image_data
    else:
        heart = boring_heart_image
        heart_data = boring_heart_image_data

    draw_half_image_with_hole(heart, heart_data, x_offset, y_offset, size/2, size, surface, hole_color=hole_color, cut_vertical=cut_vertical)


def draw_empty_heart(x_offset, y_offset, size, surface, hole_color=(0, 0, 0)):
    heart = boring_heart_image
    heart_data = boring_heart_image_data

    draw_image_with_hole(heart, heart_data, x_offset, y_offset, size, size, surface, hole_color=hole_color)

def draw_image(image:Image, image_data, x_offset:int, y_offset:int, size_x:int, size_y:int, surface):
    """draws an image in the spot you want; SIZE X AND Y MUST BE PROPORTIONAL TO THE ORIGINAL IMAGE SIZE BC OF PYGAME"""
    x_size = int(size_x/image.size[0])    
    y_size = int(size_y/image.size[1])

    for index, color in enumerate(image_data):
        if color[3] == 0:
            continue
        else:
            color = color[:3]

        x_start = (index % image.size[0])*x_size
        y_start = (index // image.size[1])*y_size

        rectangle = pygame.Rect(x_start+x_offset, y_start+y_offset, x_size, y_size)
        pygame.draw.rect(surface, color, rectangle)  

def draw_half_image(image:Image, image_data, x_offset:int, y_offset:int, size_x:int, size_y:int, surface, cut_vertical=True):
    """draws half an image obviously; look at draw full image"""

    x_size = int(size_x/image.size[0])*2
    y_size = int(size_y/image.size[1])

    for index, color in enumerate(image_data):
        if not cut_vertical and index > len(image_data)//2:
            break

        if color[3] == 0 or (cut_vertical and index % image.size[0] > (image.size[0]//2-1)):
            continue
        else:
            color = color[:3]

        x_start = (index % image.size[0])*x_size
        y_start = (index // image.size[1])*y_size

        rectangle = pygame.Rect(x_start+x_offset, y_start+y_offset, x_size, y_size)
        pygame.draw.rect(surface, color, rectangle)


def draw_half_image_with_hole(image:Image, image_data, x_offset:int, y_offset:int, size_x:int, size_y:int, surface, hole_color=(0, 0, 0), cut_vertical=True):
    """draws half an image obviously, but everything that is not white will be black; look at draw full image"""

    x_size = int(size_x/image.size[0])*2    
    y_size = int(size_y/image.size[1])

    for index, color in enumerate(image_data):
        is_white_ish = color[0] >= 240 and color[1] >= 240 and color[2] >= 240

        if color[3] == 0:
            continue
        elif cut_vertical and index % image.size[0] > (image.size[0]//2-1):
            if is_white_ish: # leave the border
                color = color[:3]
            else:
                color = hole_color
        elif not cut_vertical and index > len(image_data)//2:
          if is_white_ish:
              color = color[:3]
          else:
              color = hole_color
        else:
            color = color[:3]

        x_start = (index % image.size[0])*x_size
        y_start = (index // image.size[1])*y_size

        rectangle = pygame.Rect(x_start+x_offset, y_start+y_offset, x_size, y_size)
        pygame.draw.rect(surface, color, rectangle)

def draw_image_with_hole(image:Image, image_data, x_offset:int, y_offset:int, size_x:int, size_y:int, surface, hole_color=(0, 0, 0)):
    """draws an image in the spot you want, but everything that is not white will be black; SIZE X AND Y MUST BE PROPORTIONAL TO THE ORIGINAL IMAGE SIZE BC OF PYGAME"""
    x_size = int(size_x/image.size[0])    
    y_size = int(size_y/image.size[1])


    for index, color in enumerate(image_data):
        is_white_ish = color[0] >= 240 and color[1] >= 240 and color[2] >= 240
        
        if color[3] == 0:
            continue
        elif is_white_ish:
            color = color[:3]
        else:
            color = hole_color

        x_start = (index % image.size[0])*x_size
        y_start = (index // image.size[1])*y_size

        rectangle = pygame.Rect(x_start+x_offset, y_start+y_offset, x_size, y_size)
        pygame.draw.rect(surface, color, rectangle) 