#!/usr/bin/env python3

import sys
from collections import defaultdict

def reducer():
    current_key = None
    max_temp = float('-inf')

    for line in sys.stdin:
        key, temp = line.strip().split('\t')
        temp = float(temp)

        if key != current_key:
            if current_key:
                print(f"{current_key}\t{max_temp}")
            current_key = key
            max_temp = temp
        else:
            max_temp = max(max_temp, temp)

    if current_key:
        print(f"{current_key}\t{max_temp}")

if __name__ == "__main__":
    reducer()
