from core.Map import Map
from PIL import Image


class SymbolRenderer:

    def render_map(self, map: Map, fov: int, centerPosition):
        final_map = "My position is: x {}, y {}, z {} \n". format(centerPosition.x, centerPosition.y, centerPosition.z)
        for i in range(centerPosition.x + fov * -1, centerPosition.x + fov + 1):
            for j in range(centerPosition.y + fov * -1, centerPosition.y + fov + 1):
                if i < 0 or j < 0:
                    final_map += '# '
                elif i >= len(map.map) or j >= len(map.map[0]):
                    final_map += '# '
                else:
                    cur_object = map.map[i][j][len(map.map[i][j])-1]
                    if cur_object is None:
                        cur_object = map.map[i][j][len(map.map[i][j])-2]
                    final_map += (cur_object.map_symbol + ' ')
            final_map += "\n"
        print(final_map)
        return final_map


class ImageRenderer:

    def render_map(self, map, fov, centerPosition):
            img = Image.new('RGB', (32*fov, 32*fov))
            fog_img = Image.open('Textures/fog.png')
            ground_img = Image.open('Textures/GroundTile.png')
            player_img = Image.open('Textures/Player.png')

            for i in range(centerPosition.x + fov * -1, centerPosition.x + fov + 1):
                for j in range(centerPosition.y + fov * -1, centerPosition.y + fov + 1):
                    if i < 0 or j < 0:
                        img.paste(fog_img, (32*j, 32*i))
                    elif i >= len(map.map) or j >= len(map.map[0]):
                        img.paste(fog_img, (32*j, 32*i))
                    else:
                        cur_object = map.map[i][j][len(map.map[i][j]) - 1]
                        cur_z = len(map.map[i][j]) - 1
                        if cur_object is None:
                            for k in range(len(map.map[i][j]) - 1):
                                cur_object = map.map[i][j][cur_z]
                                if cur_object is not None:
                                    break
                                cur_z = cur_z - k
                            if cur_object is None:
                                img.paste(fog_img, (32 * j, 32 * i))
                            else:
                                img.paste(Image.open(cur_object.map_image), (32 * j, 32 * i))
                        else:
                            if cur_object.is_not_tile:
                                img.paste(ground_img, (32 * j, 32 * i))
                            img.paste(Image.open(cur_object.map_image), (32 * j, 32 * i))

            return img
