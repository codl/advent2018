def run(input_):
    changes = tuple(map(lambda x: int(x), input_.split('\n')))

    frequency = 0
    first_loop_end = None
    repeated = None
    reached = set((0,))

    while repeated is None:
        for change in changes:
            frequency += change
            if frequency in reached and repeated is None:
                repeated = frequency
            reached |= set((frequency,))
        if first_loop_end is None:
            first_loop_end = frequency

    return first_loop_end, repeated


if __name__ == '__main__':
    with open('01.example.input') as f:
        print(run(f.read().strip()))
    with open('01.input') as f:
        print(run(f.read().strip()))
