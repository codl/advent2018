import re

class LLinkedList(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left or self
        self.right = right or self

    def insert(self, value):
        other = LLinkedList(value, self.left, self)
        self.left.right = other
        self.left = other
        return other

    def remove(self):
        self.right.left = self.left
        self.left.right = self.right
        return self.right

    def move(self, count):
        if(count == 0):
            return self
        elif(count > 0):
            return self.right.move(count-1)
        elif(count < 0):
            return self.left.move(count+1)




def run(_in):
    results = list()
    for line in _in.split('\n'):
        res = re.match('([0-9]+) players; last marble is worth ([0-9]+) points', line)
        player_count = int(res[1])
        marble_limit = int(res[2])

        player_scores = [0] * player_count
        marbles = LLinkedList(0)

        value = 0
        player = -1

        for marble_limit2 in (marble_limit, marble_limit * 100):

            while value < marble_limit2:
                value += 1
                player = (player + 1) % player_count
                if value % 23 == 0:
                    player_scores[player] += value
                    marbles = marbles.move(-7)
                    player_scores[player] += marbles.value
                    marbles = marbles.remove()
                else:
                    marbles = marbles.move(2)
                    marbles = marbles.insert(value)


            results.append(max(player_scores))

    return results



if __name__ == '__main__':
    import sys
    import os
    day = '09'
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
