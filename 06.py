import re
from math import inf
from collections import defaultdict


def run(_in, safe_area_distance):
    lines = _in.split('\n')
    coordinates = list()
    for line in lines:
        match = re.match('([0-9]+), ([0-9]+)', line)
        coordinates.append((int(match[1]), int(match[2])))

    left_boundary = coordinates[0][0]
    right_boundary = coordinates[0][0]
    top_boundary = coordinates[0][1]
    bottom_boundary = coordinates[0][1]

    for coordinate in coordinates:
        if coordinate[0] > right_boundary:
            right_boundary = coordinate[0]
        if coordinate[0] < left_boundary:
            left_boundary = coordinate[0]
        if coordinate[1] > bottom_boundary:
            bottom_boundary = coordinate[1]
        if coordinate[1] < top_boundary:
            top_boundary = coordinate[1]

    areas = defaultdict(lambda: 0)
    safe_area = 0

    for x in range(left_boundary, right_boundary + 1):
        for y in range(top_boundary, bottom_boundary + 1):
            shortest_distance = inf
            closest_index = None
            cumulative_distance = 0
            for index in range(len(coordinates)):
                xx, yy = coordinates[index]
                distance = abs(x - xx) + abs(y - yy)
                cumulative_distance += distance
                if distance < shortest_distance:
                    closest_index = index
                    shortest_distance = distance
                elif distance == shortest_distance:
                    closest_index = None
            if (x in (left_boundary, right_boundary)\
                    or y in (top_boundary, bottom_boundary))\
                    and closest_index:
                        areas[closest_index] = inf
            elif closest_index:
                areas[closest_index] += 1
            if cumulative_distance < safe_area_distance:
                safe_area += 1
            #    print('X', end='')
            #else:
            #    print('.', end='')
        #print('')
        ##  yea we demoscene now

    return max((value for value in areas.values() if value != inf)), safe_area


if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip(), 32))
    with open(day + '.input') as f:
        print(run(f.read().strip(), 10000))
