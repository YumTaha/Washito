import pygame
from tiles import Tile
from player import Player
from settings import tile_size

class Level:
    def __init__(self, level_data, *args, **kwargs):

        # level setup
        self.display_surface = pygame.display.get_surface()
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif col == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Player((x, y), tile_size)
                    self.tiles.add(tile)
    
    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

