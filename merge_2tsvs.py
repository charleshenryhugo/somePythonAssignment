import csv
import sys

files = sys.stdin.read().splitlines()

tsv1 = open(files[0])
tsv2 = open(files[1])

tsv1 = csv.reader(tsv1, delimiter = "\t")
tsv2 = csv.reader(tsv2, delimiter = "\t")

dic_tsv1 = {}

header = next(tsv1)
for row in tsv1:
    dic_tsv1[row[0]] = row[1]

sys.stdout.write("StudentID\t")
sys.stdout.write("Class\t")
sys.stdout.write("Grade\t")
sys.stdout.write("Name\n")

header = next(tsv2)
for row in tsv2:
    for i in range(0, len(row)):
        sys.stdout.write(row[i])
        sys.stdout.write("\t")
    sys.stdout.write(dic_tsv1[row[0]])
    sys.stdout.write("\n")

    