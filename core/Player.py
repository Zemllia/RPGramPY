from core.Creature import Creature
from core.MapObject import MapObject
from core.Position import Position


class Player(Creature):

    def __init__(self, name, cur_map):
        self.name = name
        self.cur_map = cur_map
        self.player_on_map = self.PlayerOnMap(name)

    class PlayerOnMap(MapObject):
        map_symbol = '@'
        map_image = 'Textures/Player.png'
        is_not_tile = True

        def __init__(self, player_name):
            self.map_symbol = player_name[0]

    def move(self, direction):
        if direction == "UP":
            if self.position.x - 1 < 0:
                return
            self.cur_map.map[self.position.x][self.position.y][self.position.z] = None
            self.cur_map.map[self.position.x - 1][self.position.y][self.position.z] = self.player_on_map
            self.position.x -= 1

        if direction == "DOWN":
            if self.position.x + 1 > len(self.cur_map.map) - 1:
                return
            self.cur_map.map[self.position.x][self.position.y][self.position.z] = None
            self.cur_map.map[self.position.x + 1][self.position.y][self.position.z] = self.player_on_map
            self.position.x += 1

        if direction == "LEFT":
            if self.position.y - 1 < 0:
                return
            self.cur_map.map[self.position.x][self.position.y][self.position.z] = None
            self.cur_map.map[self.position.x][self.position.y - 1][self.position.z] = self.player_on_map
            self.position.y -= 1

        if direction == "RIGHT":
            if self.position.y + 1 > len(self.cur_map.map[0]) - 1:
                return
            self.cur_map.map[self.position.x][self.position.y][self.position.z] = None
            self.cur_map.map[self.position.x][self.position.y + 1][self.position.z] = self.player_on_map
            self.position.y += 1

    def spawn(self, spawn_position):
        self.cur_map.map[spawn_position.x][spawn_position.y][spawn_position.z] = self.player_on_map
        self.position = Position(spawn_position.x, spawn_position.y, spawn_position.z)
