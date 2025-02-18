import math
import pygame
import random

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    TOP_PAD = 150
    SIDE_PAD = 100

    def __init__(self, width, height, lst):  # lst is the starting list we want to sort
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        # This basically works out how tall each block should be in proportion to other blocks
        self.block_height = round(
            (self.height - self.SIDE_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
