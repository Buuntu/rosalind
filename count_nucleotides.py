#!/usr/bin/env python3

import sys
from Bio.Seq import Seq

def main():
    sequence = sys.argv[1]
    count_a = sequence.count('A')
    count_c = sequence.count('C')
    count_g = sequence.count('G')
    count_t = sequence.count('T')

    print(count_a, count_c, count_g, count_t)

if __name__ == "__main__":
    main()
