from collections import defaultdict
import itertools

def run(input_):
    boxes = input_.split('\n')
    twos = 0
    threes = 0
    common_id = None

    for i, box in zip(itertools.count(), boxes):
        # part 1 stuff
        two = False
        three = False
        letter_counts = defaultdict(lambda: 0)
        for letter in box:
            letter_counts[letter] += 1
        for count in letter_counts.values():
            if count == 2:
                two = True
            if count == 3:
                three = True
        if two:
            twos += 1
        if three:
            threes += 1

        # part 2 stuff
        rest = boxes[i+1:]

        for other_box in rest:
            differing = 0
            same_letters = list()
            for j in range(len(box)):
                if box[j] != other_box[j]:
                    differing += 1
                else:
                    same_letters.append(box[j])
                if differing >= 2:
                    break
            if differing == 1:
                common_id = ''.join(same_letters)


    checksum = twos * threes

    return checksum, common_id


if __name__ == '__main__':
    with open('02-1.example.input') as f:
        print(run(f.read().strip())[0])
    with open('02-2.example.input') as f:
        print(run(f.read().strip())[1])
    with open('02.input') as f:
        print(run(f.read().strip()))
