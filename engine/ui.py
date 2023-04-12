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

    def update_hearts(self, hearts, smiley=False):
        y_offset = self.edge_buffer_y
        for heart_num in range(hearts):
            x_offset = self.screen_size_x - self.edge_buffer_x - heart_num*(self.heart_buffer + self.heart_size) - self.heart_size
            
            draw.draw_full_heart(x_offset, y_offset, self.heart_size, self.surface)

    # def update_max_hearts(hearts):
        