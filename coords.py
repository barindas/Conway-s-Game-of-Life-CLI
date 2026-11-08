import config


def make_coord_array(size):
    return [[config.none_icon for x in range(size[0])] for y in range(size[-1])]


class Node:
    def __init__(self, coord_sys, x, y):
        self.coord_sys = coord_sys
        self.x = y
        self.y = x
        
        self.neighbors = list()


    def make_once(self):
        self.coord_sys[self.x][self.y] = config.alive_icon
    def kill(self):
        self.coord_sys[self.x][self.y] = config.none_icon
     

    def get_neighbors(self):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):

                if dr == 0 and dc == 0:
                    continue

                r,c = self.x + dr, self.y + dc
                rows, cols = len(self.coord_sys), len(self.coord_sys[0])

                if 0 <= r < rows and 0 <= c < cols:
                    self.neighbors.append(self.coord_sys[r][c])

        return self.neighbors
    
    def count_neighbors(self):
        count = 0
        for neighbor in self.neighbors:
            if neighbor == config.alive_icon:
                count += 1
        return count



