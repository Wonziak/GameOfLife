import pygame
import copy
from cell_class import *

vec = pygame.math.Vector2


class Game_window:
    def __init__(self, screen, x, y, window_width=800, window_height=800):
        self.screen = screen
        self.pos = vec(x, y)
        self.width, self.height = window_width-200, window_height-200
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rows = self.height//20
        self.cols = self.width//20
        self.grid = [[Cell(self.image, x, y, self.rows, self.cols) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbours(self.grid)

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((255, 255, 255))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y, self.rows, self.cols) for x in range(self.cols)] for y in range(self.rows)]

    def evaluate(self):
        new_grid = copy.copy(self.grid)

        for row in self.grid:
            for cell in row:
                cell.live_neighbours() # zlicz żywych sąsiadów każdej komórki

        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbours == 2 or cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True
                    if cell.alive_neighbours < 2:
                        new_grid[yidx][xidx].alive = False
                    if  cell.alive_neighbours > 3:
                        new_grid[yidx][xidx].alive = False
                else:
                    if cell.alive_neighbours == 3:
                        new_grid[yidx][xidx].alive = True
        self.grid = new_grid
