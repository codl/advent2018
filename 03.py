import re
from collections import defaultdict

def cross(a, b):
    for aa in a:
        for bb in b:
            yield (aa, bb)

class Claim(object):
    def __init__(self, definition):
        result = re.match(
                "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)",
                definition)
        self.id = int(result.group(1))
        self.xpos = int(result.group(2))
        self.ypos = int(result.group(3))
        self.xsize = int(result.group(4))
        self.ysize = int(result.group(5))
        self.double_claimed = False

    def __repr__(self):
        return "<Claim {}: {}x{} at {},{}>".format(
                self.id, self.xsize, self.ysize,
                self.xpos, self.ypos)



def run(_in):
    claims = _in.split('\n')
    claims = tuple(map(lambda x: Claim(x), claims))

    claim_counts = defaultdict(lambda: 0)

    for claim in claims:
        for x in range(claim.xpos, claim.xpos + claim.xsize):
            for y in range(claim.ypos, claim.ypos + claim.ysize):
                claim_counts[(x, y)] += 1
                if claim_counts[(x, y)] > 1:
                    claim.double_claimed = True

    double_claimed = 0

    for claim_count in claim_counts.values():
        if claim_count > 1:
            double_claimed += 1

    claim_with_no_overlap = None
    for claim in claims:
        if claim.double_claimed:
            continue
        found_double_claim = False
        for pos in cross(
                range(claim.xpos, claim.xpos + claim.xsize),
                range(claim.ypos, claim.ypos + claim.ysize)):
            if claim_counts[pos] > 1:
                found_double_claim = True
                break
        if not found_double_claim:
            claim_with_no_overlap = claim
            break

    return double_claimed, claim_with_no_overlap




if __name__ == '__main__':
    import sys
    import os
    day = os.path.basename(sys.argv[0]).split('.')[0]
    with open(day + '.example.input') as f:
        print(run(f.read().strip()))
    with open(day + '.input') as f:
        print(run(f.read().strip()))
