from engine import draw
import pygame

class Hearts_Ui():
    def __init__(self, screen_size, surface, max_hearts=3, heart_size=48, heart_buffer=10, edge_buffer_x=10, edge_buffer_y=10):
        """Its gonna round to the nearest number of pixels bc pygame sucks"""
        self.max_hearts = max_hearts
        self.heart_size = heart_size
        self.heart_buffer = heart_buffer
        self.edge_buffer_x = edge_buffer_x
        self.edge_buffer_y = edge_buffer_y
        self.screen_size_x = screen_size[0]
        self.screen_size_y = screen_size[1]
        self.surface = surface

        self.update_hearts(max_hearts)

    def update_hearts(self, num_hearts, smiley=False):
        y_offset = self.edge_buffer_y
        
        start=0

        if num_hearts - int(num_hearts) == 0.5:
            x_offset = self.screen_size_x - self.edge_buffer_x - self.heart_size
            start = 1
            draw.draw_half_heart(x_offset, y_offset, self.heart_size, self.surface, hole_color=(0, 0, 0))

        for index in range(start, int(num_hearts+start)):
            x_offset = self.screen_size_x - self.edge_buffer_x - index*(self.heart_buffer + self.heart_size) - self.heart_size
            
            draw.draw_full_heart(x_offset, y_offset, self.heart_size, self.surface)
            # draw.draw_half_heart(x_offset, y_offset, self.heart_size, self.surface, cut_vertical=True)
        

    # def update_max_hearts(hearts):
        