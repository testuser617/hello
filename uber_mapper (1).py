import sys
import csv

def mapper():
    for line in sys.stdin:
        line = line.strip()
        data = list(csv.reader([line]))[0]

        # Skip lines that don't have the expected number of columns
        if len(data) < 4:
            continue
        
        # Skip header row
        if data[0].lower() == 'date/time':
            continue
        
        # Extract the date part from the Date/Time column
        date_time = data[0]
        date = date_time.split(' ')[0]  # Get the date part (before the space)
        
        print(f"{date}\t1")

if __name__ == "__main__":
    mapper()

