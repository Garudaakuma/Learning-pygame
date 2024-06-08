# imports
import pygame

NEIGHBOR_OFFSET = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'stone', 'grass'}


class tile_map:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tile_map = {}
        self.offgrid_tiles = []

        def create_map(i:int,x_index:int,fix_xindex:bool,y_index:int,fix_yindex:bool,type_:str,varient:int):
            x_index = x_index if fix_xindex else x_index + i
            y_index = y_index if fix_yindex else y_index + i
            
            self.tile_map[f"{x_index};{y_index}"] = {'type': type_,'variant': varient,'pos': (x_index,y_index)}
        for i in range(10):
            if i == 0:
                for j in range(3): create_map(i,12 + j,True,2,False,'stone',j)
                
                self.tile_map[f"{3 + i};10"] = {'type': 'grass', 'variant': 0, 'pos': (3 + i, 10)}
            elif i == 9:
                for j in range(3): create_map(i,12 + j,True,2,False,'stone',6 - j)
                
                self.tile_map[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 2, 'pos': (3 + i, 10)}
            else:
                create_map(i,12,True,2,False,'stone',7)
                create_map(i,13,True,2,False,'stone',8)
                create_map(i,14,True,2,False,'stone',3)
                
                self.tile_map[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}

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
