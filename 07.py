import re
from collections import defaultdict
import string
from math import inf

def part1(requirements):
    parents, children, tasks = graph_from_requirements(requirements)

    task_list = list()
    while tasks:
        available_tasks = [task for task in tasks if not parents.get(task)]
        available_tasks.sort()
        next_task = available_tasks[0]
        for child in children[next_task]:
            parents[child].remove(next_task)

        del children[next_task]
        tasks.remove(next_task)

        task_list.append(next_task)

    return ''.join(task_list)

def part2(requirements, base_time, worker_count):
    parents, children, tasks = graph_from_requirements(requirements)

    task_lengths = {task: string.ascii_uppercase.find(task)+1 + base_time
            for task in tasks}

    print(children)

    t = 0
    worker_task = defaultdict(lambda: None)
    worker_time_remaining = defaultdict(lambda: 0)
    while tasks or any((worker_task[i] for i in range(worker_count))):
        t+=1
        for i in range(worker_count):
            worker_time_remaining[i] -= 1
            if worker_time_remaining[i] <= 0:
                if worker_task[i]:
                    task = worker_task[i]
                    worker_task[i] = None
                    for child in children[task]:
                        try:
                            parents[child].remove(task)
                        except Exception as e:
                            print(task)
                            print(children)
                            print(parents)
                            raise e
                    del children[task]

        for i in range(worker_count):
            if not worker_task[i]:
                available_tasks = [task for task in tasks if not parents.get(task)]
                available_tasks.sort()
                if available_tasks:
                    next_task = available_tasks.pop(0)
                    worker_task[i] = next_task
                    worker_time_remaining[i] = task_lengths[next_task]
                    tasks.remove(next_task)

        # debug ouput
        if False:
            print(t, end="\t")
            for i in range(worker_count):
                print('{}:{}'.format(worker_task[i], worker_time_remaining[i]), end='\t')
            print(''.join(tasks))

    return t-1

def graph_from_requirements(requirements):
    parents = defaultdict(lambda: set())
    children = defaultdict(lambda: set())
    tasks = set()

    for parent, child in requirements:
        parents[child].add(parent)
        children[parent].add(child)
        tasks = tasks | set((parent, child))

    return parents, children, tasks

def run(_in, base_time, worker_count):
    requirements = list()
    for line in _in.split('\n'):
        result = re.match("Step ([A-Z]) must be finished before step ([A-Z]) can begin\.", line.strip())
        requirements.append((result[1], result[2]))


    return (
        part1(requirements),
        part2(requirements, base_time, worker_count))





if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip(), 0, 2))
    with open(day + '.input') as f:
        print(run(f.read().strip(), 60, 5))
