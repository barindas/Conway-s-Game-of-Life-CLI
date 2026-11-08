import coords
import config
import engine
import time
import os

coord_array = coords.make_coord_array(config.aspect)
running = True

for node in config.alive_at_start:
    foo = coords.Node(coord_array,
        node[0] + config.offset_at_start,
        node[-1] + config.offset_at_start)
    foo.make_once()

while running:
    os.system('clear')

    engine.frame(coord_array, engine.calculate(coord_array))
    time.sleep(1/config.fps)




