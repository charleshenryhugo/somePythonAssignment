import sys
import csv

orig_data = sys.stdin.read()
lines = orig_data.splitlines()

reader = csv.reader(lines, delimiter=",")

for row in reader:
    for i in range(0, len(row)):
        sys.stdout.write(row[i])
        if i < len(row) - 1:
            sys.stdout.write("\t")
    sys.stdout.write("\n")
