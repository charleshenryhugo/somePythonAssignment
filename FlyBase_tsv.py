import sys
import csv

orig_data = sys.stdin.read() #read from stdin
#orig_data = open("dmel-all-r6.10.gtf").read() #read from file
lines = orig_data.splitlines()

reader = csv.reader(lines, delimiter="\t")

lres = ["Chromosome", "Gene Count", "Avg Size"]

#a dictionary for all chromosomes {chromosome-ID: [count, total-size]}
dic = {}

for row in reader:
    chID = row[0]
    if chID.find("211")!=-1 or chID.find("Unmapped")!=-1:
        continue
    if row[2] != "gene":
        continue
    if (chID in dic.keys()):
        dic[chID][0] += 1
        dic[chID][1] += int(row[4]) - int(row[3])
    else:
        dic[chID] = [int(1), int(row[4]) - int(row[3])]


sys.stdout.write("Chromosome,")
sys.stdout.write("Gene Count,")
sys.stdout.write("Avg Size\n")

#dic.keys().sort()
for key in sorted(dic.keys()):
    dic[key][1] =  dic[key][1] / dic[key][0] + 1
    sys.stdout.write(key)
    sys.stdout.write("\t")
    sys.stdout.write(str(dic[key][0]))
    sys.stdout.write("\t")
    sys.stdout.write(str(dic[key][1]))
    sys.stdout.write("\n")
