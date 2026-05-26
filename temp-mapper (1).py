#!/usr/bin/env python3

import sys

def mapper():
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 5:
            continue
        date = parts[2].split('_')[0]  # Extract the date part (YYYYMMDD)
        try:
            temp = float(parts[3])         # Extract the temperature
        except ValueError:
            continue
        print(f"{date}\t{temp}")

if __name__ == "__main__":
    mapper()
