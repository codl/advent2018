from functools import reduce

class Node(object):
    def __init__(self, parent, child_count, meta_count):
        self.parent = parent
        self.metadata = list()
        self.children = list()
        self.child_count = child_count
        self.meta_count = meta_count
        self.__checksum2 = None

    def checksum(self):
        s = reduce(lambda a, b: a+b, self.metadata, 0)
        s += reduce(lambda acc, child: acc + child.checksum(), self.children, 0)
        return s

    def checksum2(self):
        if not self.__checksum2:
            c = 0
            if self.children:
                for meta in self.metadata:
                    if meta < 1 or meta > len(self.children):
                        continue
                    c += self.children[meta-1].checksum2()
            else:
                c = sum(self.metadata, 0)

            self.__checksum2 = c

        return self.__checksum2


def parse_node(parent, numbers):
    child_count, meta_count = numbers[0:2]
    node = Node(parent, child_count, meta_count)
    numbers = numbers[2:]
    for i in range(child_count):
        child, numbers = parse_node(node, numbers)
        node.children.append(child)
    node.metadata = numbers[:meta_count]
    numbers = numbers[meta_count:]

    return node, numbers


def run(_in):
    numbers = [int(s) for s in _in.split(' ')]

    tree, nothing = parse_node(None, numbers)

    return tree.checksum(), tree.checksum2()



if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
