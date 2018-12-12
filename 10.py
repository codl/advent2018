import re
from math import inf
from collections import defaultdict
from itertools import count

class Star(object):
    def __init__(self, posx, posy, velx, vely):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely

    def step(self):
        return Star(self.posx + self.velx, self.posy + self.vely, self.velx, self.vely)

def boundaries(stars):
    max_x = max(stars, key=lambda star: star.posx).posx
    min_x = min(stars, key=lambda star: star.posx).posx
    max_y = max(stars, key=lambda star: star.posy).posy
    min_y = min(stars, key=lambda star: star.posy).posy
    width = max_x - min_x
    height = max_y - min_y
    del stars
    return locals()

def pprint_field(stars):
    b = boundaries(stars)
    field = dict()
    result = ""
    for star in stars:
        field[(star.posx, star.posy)] = True
    for y in range(b['min_y'], b['max_y'] + 1):
        for x in range(b['min_x'], b['max_x'] + 1):
            if field.get((x, y)):
                result += '*'
            else:
                result += '.'
        result += '\n'

    return result

def run(_in):
    stars = list()
    for line in _in.split('\n'):
        result = re.match('position=< *([-0-9]+), *([-0-9]+)> velocity=< *([-0-9]+), *([-0-9]+)>', line)
        stars.append(Star(*(int(group) for group in result.groups())))

    min_width = inf
    min_height = inf

    prev_stars = None

    for i in count():
        prev_stars = stars
        stars = list()
        for star in prev_stars:
            stars.append(star.step())
        b = boundaries(stars)
        if min_width > b['width']:
            min_width = b['width']
        if min_height > b['height']:
            min_height = b['height']
        if min_width < b['width'] and min_height < b['height']:
            return pprint_field(prev_stars)+ "Time: {}\n".format(i)





if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
