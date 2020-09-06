from Items.GrassItem import GrassItem
from core.MapObject import MapObject


class GrassBlock(MapObject):
    id = 0
    drop_item = GrassItem
    hardness = 1
    map_symbol = '+'
    map_image = 'Textures/GroundTile.png'
