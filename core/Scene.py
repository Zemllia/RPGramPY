import threading
import time


class Scene:

    update_time = 1

    def __init__(self):
        t1 = threading.Thread(target=self.time_line)
        t1.start()

    def time_line(self):
        while True:
            self.on_update()
            time.sleep(self.update_time)

    # Call every update time (should be overrided)
    def on_update(self):
        print('update')

    scene_objects = {}
