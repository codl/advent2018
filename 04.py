import re
from collections import defaultdict


def run(_in):
    entries = _in.split('\n')
    entries.sort()

    current_guard = None
    asleep_per_guard_and_minute = defaultdict(lambda:
            defaultdict(lambda: 0))
    asleep_per_guard = defaultdict(lambda: 0)
    fall_asleep_minute = None

    for entry in entries:
        result = re.match('''
                \[.*:([0-9]{2})\]\ (
                    Guard\ \#([0-9]+)\ begins\ shift
                  | .*
                )''', entry, re.VERBOSE)
        minute = int(result.group(1))
        action = result.group(2)
        guard = result.group(3)
        if action == 'falls asleep':
            fall_asleep_minute = minute
        elif action == 'wakes up':
            for asleep_minute in range(fall_asleep_minute, minute):
                asleep_per_guard_and_minute[current_guard][asleep_minute] += 1
                asleep_per_guard[current_guard] += 1
        elif result.group(3):
            current_guard = int(result.group(3))
            continue
        else:
            raise Exception('now you fucked up!!!!')

    def strat1():

        max_minutes = 0
        worst_guard = None
        for guard in asleep_per_guard.keys():
            if asleep_per_guard[guard] > max_minutes:
                worst_guard = guard
                max_minutes = asleep_per_guard[guard]

        guard_minutes = asleep_per_guard_and_minute[worst_guard]
        max_minutes = 0
        worst_minute = None

        for (minute, count) in guard_minutes.items():
            if count > max_minutes:
                worst_minute = minute
                max_minutes = count

        return worst_guard * worst_minute

    def strat2():

        max_minutes = 0
        worst_minute = None
        worst_guard = None
        for guard in asleep_per_guard_and_minute.keys():
            minutes = asleep_per_guard_and_minute[guard]
            for minute in minutes.keys():
                if minutes[minute] > max_minutes:
                    max_minutes = minutes[minute]
                    worst_minute = minute
                    worst_guard = guard

        return worst_guard * worst_minute

    return (strat1(), strat2())




if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
