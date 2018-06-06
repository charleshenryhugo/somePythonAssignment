import sys

#read input.txt, search_string, outout.txt
lines = sys.stdin.read().split('\n')
inputFile = lines[0]
outputFile = lines[2]
srhStr = lines[1]

#read the content of input.txt
lines = open(inputFile, 'r')
outputFile = open(outputFile, 'w')
n = 1
hitn = 0
for line in lines:
    if line.find(srhStr) != -1:
        hitn += 1
        outputFile.write('line ' + str(n) + ', hit #' + str(hitn) + ': ' + line)
    n += 1

lines.close()
outputFile.close()