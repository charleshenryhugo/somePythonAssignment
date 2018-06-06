import csv
import sys

orig_data=sys.stdin.read()

lines = orig_data.splitlines()
tgtcol = int(lines[0])-1
tgtval = str(lines[1])
head = lines[2].split(",")
data = lines[3:]

reader = csv.reader(data, delimiter=',')

#write the head line
for i in range(0, len(head)):
    sys.stdout.write(head[i])
    if i < len(head) - 1:
        sys.stdout.write(",")
sys.stdout.write("\n")

for row in reader:
    if tgtcol < len(row) and row[tgtcol] != tgtval:
        continue
    for i in range(0, len(row)):
        sys.stdout.write(row[i])
        if i < len(row) - 1:
            sys.stdout.write(",")
    sys.stdout.write("\n")