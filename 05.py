import string

def react(polymer):
    polymer = tuple(polymer)

    i = 0
    while i < len(polymer) - 1:
        unit = polymer[i]
        unit2 = polymer[i+1]
        if unit == unit2.swapcase():
            reacted = True
            polymer = polymer[:i] + polymer[i+2:]
            i -= 2
        i += 1
        if i < 0:
            i = 0
    return ''.join(polymer)


def run(_in):
    polymer = _in

    plain_length = len(react(polymer))

    shortest_length = plain_length
    for unit_type in string.ascii_lowercase:
        improved_polymer = polymer.replace(unit_type, '')\
                                  .replace(unit_type.swapcase(), '')
        length = len(react(improved_polymer))
        if length < shortest_length:
            shortest_length = length

    return plain_length, shortest_length



    return len(polymer)




if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
