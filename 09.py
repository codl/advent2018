import re

def run(_in):
    results = list()
    for line in _in.split('\n'):
        res = re.match('([0-9]+) players; last marble is worth ([0-9]+) points', line)
        player_count = int(res[1])
        marble_limit = int(res[2])

        player_scores = [0] * player_count
        marbles = [0]
        cursor = 0

        value = 0
        player = -1

        #for marble_limit2 in (marble_limit, marble_limit * 100):

            while value < marble_limit2:
                value += 1
                player = (player + 1) % player_count
                if value % 23 == 0:
                    player_scores[player] += value
                    cursor = (cursor - 7) % len(marbles)
                    player_scores[player] += marbles.pop(cursor)
                    cursor = cursor % len(marbles)
                else:
                    cursor = (cursor + 2) % len(marbles)
                    marbles.insert(cursor, value)

                if False:
                    print('[{}]'.format(player), end=' ')
                    for i in range(len(marbles)):
                        marble = marbles[i]
                        if i == cursor:
                            print('*{}'.format(marble), end='')
                        else:
                            print(' {}'.format(marble), end='')
                    print('')

            results.append(max(player_scores))

    return results



if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
