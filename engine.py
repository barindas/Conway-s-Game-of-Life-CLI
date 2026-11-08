import coords
import config



def calculate(coordsys):

    usable_nodes = set()
    unusable_nodes = set()

    for y in range(config.aspect[-1]):
        for x in range(config.aspect[0]):
            node = coords.Node(coordsys, x, y)
            node.get_neighbors()
            
            coords_tuple = x, y

            if 1 < node.count_neighbors() < 4 and coordsys[y][x] == config.alive_icon:
                usable_nodes.add(coords_tuple)

            elif node.count_neighbors() == 3 and coordsys[y][x] == config.none_icon:
                usable_nodes.add(coords_tuple)

            else:
                unusable_nodes.add(coords_tuple)

    return unusable_nodes, usable_nodes

def frame(coordsys, calculated_tuple):
    
    for y in coordsys:
        print(''.join(y))

    for node in calculated_tuple[0]:
        coordsys[node[-1]][node[0]] = config.none_icon
    for node in calculated_tuple[-1]:
        coordsys[node[-1]][node[0]] = config.alive_icon

    


            

