from core.Position import Position


class Creature:
    id = 0
    name = "Creature"
    fov = 10
    level = 1
    xp = 0
    on_kill_xp = 5
    HP = 100
    energy = 100
    hunger = 100
    thirst = 100
    inventory = []
    position = Position(0, 0, 0)
    cur_map = None
