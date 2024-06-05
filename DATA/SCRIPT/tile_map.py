# imports
import pygame

NEIGHBOR_OFFSET = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}


class tile_map:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tile_map = {}
        self.offgrid_tiles = []

        for i in range(10):
            if i == 0:
                self.tile_map[f"{3 + i};10"] = {'type': 'grass', 'variant': 0, 'pos': (3 + i, 10)}
                
                self.tile_map[f"12;{8 + i}"] = {'type': 'stone', 'variant': 0, 'pos': (12, 8 + i)}
                self.tile_map[f"13;{8 + i}"] = {'type': 'stone', 'variant': 1, 'pos': (13, 8 + i)}
                self.tile_map[f"14;{8 + i}"] = {'type': 'stone', 'variant': 2, 'pos': (14, 8 + i)}
            elif i == 9:
                self.tile_map[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 2, 'pos': (3 + i, 10)}
                
                self.tile_map[f"12;{8 + i}"] = {'type': 'stone', 'variant': 6, 'pos': (12, 8 + i)}
                self.tile_map[f"13;{8 + i}"] = {'type': 'stone', 'variant': 5, 'pos': (13, 8 + i)}
                self.tile_map[f"14;{8 + i}"] = {'type': 'stone', 'variant': 4, 'pos': (14, 8 + i)}
            else:
                self.tile_map[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
                
                self.tile_map[f"12;{8 + i}"] = {'type': 'stone', 'variant': 3, 'pos': (12, 8 + i)} 
                self.tile_map[f"13;{8 + i}"] = {'type': 'stone', 'variant': 8, 'pos': (13, 8 + i)} 
                self.tile_map[f"14;{8 + i}"] = {'type': 'stone', 'variant': 7, 'pos': (14, 8 + i)}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))  # x, y
        for offset in NEIGHBOR_OFFSET:
            check_loc = f"{tile_loc[0] + offset[0]};{tile_loc[1] + offset[1]}"
            if check_loc in self.tile_map:
                tiles.append(self.tile_map[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        tile_lamb = lambda x_y: tile['pos'][x_y] * self.tile_size
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile_lamb(0), tile_lamb(1), self.tile_size, self.tile_size))
        return rects

    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tile_map:
            tile = self.tile_map[loc]
            x_pos, y_pos = tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size
            surf.blit(self.game.assets[tile['type']][tile['variant']], (x_pos, y_pos))
