
# -1 0 1 → (x, y)
NEIGHBOR_OFFSET = []
for i in [-1, 0, 1]:
    for j in [1, 0, -1]:
        NEIGHBOR_OFFSET.append((i,j))
# NEIGHBOR_OFFSET = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

class Tile_map:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(3 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
            
    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])
            
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            x_pos, y_pos = tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size
            surf.blit(self.game.assets[tile['type']][tile['variant']], (x_pos, y_pos))
