from Blocks.GrassBlock import GrassBlock
from core.Map import Map
from core.Player import Player
from core.Position import Position
from core.Renderers import SymbolRenderer, ImageRenderer
from core.Scene import Scene


class Scene1(Scene):
    update_time = 10

    world_map = None

    def on_update(self):
        pass

    def generate_map(self):
        self.world_map = Map(10, 10, 4)

        for i in range(10):
            for j in range(10):
                for k in range(3):
                    grass_block = GrassBlock()
                    self.world_map.add_object(Position(i, j, k), grass_block)

        for i in range(10):
            for j in range(10):
                self.world_map.add_object(Position(i, j, 3), None)
