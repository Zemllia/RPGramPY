from core.MapObject import MapObject
from core.Position import Position


class Map():

    map = []
    map_objects_for_update = []
    size_x = 1
    size_y = 1
    size_z = 1

    def __init__(self, size_x, size_y, size_z):
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z
        for i in range(size_x):
            d2 = []
            for j in range(size_y):
                d3 = []
                d2.append(d3)
            self.map.append(d2)

    def get_object_by_position(self, position: Position = Position(0, 0, 0)):
        return self.map[position.x][position.y][position.z]

    def add_object(self, position: Position = Position(0, 0, 0), map_object: MapObject = None):
        self.map[position.x][position.y].append(map_object)

    def replace_object(self, position: Position = Position(0, 0, 0), map_object: MapObject = None):
        self.map[position.x][position.y][position.z] = map_object

    def remove_object(self, position: Position = Position(0, 0, 0)):
        self.map[position.x][position.y][position.z] = None
