import math
import pygame
import random

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont("comicsans", 20)
    LARGE_FONT = pygame.font.SysFont("comicsans", 30)
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
        self.block_height = math.floor(
            (self.height - self.SIDE_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
    draw_info.window.blit(
        title, (draw_info.width/2 - title.get_width()/2, 5))

    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 45))

    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, draw_info.BLACK)
    draw_info.window.blit(
        sorting, (draw_info.width/2 - sorting.get_width()/2, 75))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, colour_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height)
        pygame.draw.rect(
            draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * \
            draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        if i in colour_positions:
            color = colour_positions[i]
        pygame.draw.rect(draw_info.window, color,
                         (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        value = random.randint(min_val, max_val)
        lst.append(value)

    return lst


def main():
    run = True
    clock = pygame.time.Clock()
    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(
        800, 600, lst)
    sorting = False
    ascending = True

    from algorithms.bubbleSort import bubbleSortAlgorithm
    from algorithms.insertionSort import insertionSortAlgorithm
    from algorithms.selectionSort import selectionSortAlgorithm

    sorting_algorithm = bubbleSortAlgorithm
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algorithm_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(
                        draw_info, ascending)
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False
                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = insertionSortAlgorithm
                    sorting_algorithm_name = "Insertion Sort"
                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubbleSortAlgorithm
                    sorting_algorithm_name = "Bubble Sort"
                elif event.key == pygame.K_s and not sorting:
                    sorting_algorithm = selectionSortAlgorithm
                    sorting_algorithm_name = "Selection Sort"


if __name__ == "__main__":
    main()
