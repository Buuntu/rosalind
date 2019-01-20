#!/usr/bin/env python3

import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC
from Bio import SeqIO

def main():
    file = sys.argv[1]
    with open(file, "r") as handle:
        sequences = list(SeqIO.parse(handle, "fasta"))
        highest_gc = (GC(sequences[0].seq), sequences[0])
        for record in sequences[1:]:
            gc = GC(record.seq)
            if gc > highest_gc[0]:
                highest_gc = (gc, record)

    print(highest_gc[1].id)
    print(highest_gc[0])

if __name__ == "__main__":
    main()
