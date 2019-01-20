#!/usr/bin/env python3

import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def main():
    sequence = Seq(sys.argv[1], generic_dna)
    print(str(sequence.reverse_complement()))

if __name__ == "__main__":
    main()
