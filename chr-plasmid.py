import re
import sys

data = sys.stdin.read()
#data=">YPL187W MF(ALPHA)1 SGDID:S000006108, Chr XVI from 193648-194145, Genome Release 64-2-1, Verified ORF, Mating pheromone alpha-factor, made by alpha cells; interacts with mating type a cells to induce cell cycle arrest and other responses leading to mating; also encoded by MF(ALPHA)2, although MF(ALPHA)1 produces most alpha-factor; MF(ALPHA)1 has a paralog, MF(ALPHA)2, that arose from the whole genome duplication"
#f=open("orf_coding.fasta")
#data = f.read()
p = re.compile(">(.*) (.*) (\w*):(\w*), .*(Chr \w*|plasmid) (from)")
r = p.finditer(data)

for it in r:
    #print it.group(2),",",it.group(5)
    sys.stdout.write(it.group(2))
    sys.stdout.write(",")
    sys.stdout.write(it.group(5))
    sys.stdout.write("\n")

