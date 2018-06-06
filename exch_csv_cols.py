import csv
import sys

orig_data=sys.stdin.read()

lines = orig_data.splitlines()
cola = int(lines[0])-1
colb = int(lines[1])-1
data = lines[2:]

reader = csv.reader(data, delimiter=',')
for row in reader:
    row[cola], row[colb] = row[colb], row[cola]
    for i in range(0,len(row)):
        sys.stdout.write(row[i])
        if i < len(row) - 1:
            sys.stdout.write(",")
    sys.stdout.write("\n")

