import sys

def reducer():
    current_date = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        date, count = line.split('\t')

        try:
            count = int(count)
        except ValueError:
            continue

        if current_date == date:
            current_count += count
        else:
            if current_date is not None:
                print(f"{current_date}\t{current_count}")
            current_date = date
            current_count = count

    # Output the count for the last date
    if current_date is not None:
        print(f"{current_date}\t{current_count}")

if __name__ == "__main__":
    reducer()

