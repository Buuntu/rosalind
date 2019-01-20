#!/usr/bin/env python3

import sys

def main():
    sequence = sys.argv[1]
    sequence = sequence.replace('T','U')
    print(sequence)

if __name__ == "__main__":
    main()
