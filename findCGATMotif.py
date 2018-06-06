import sys

#TAAAAACAATA

lines = sys.stdin.read().strip().split('\n')
#lines = open('seqs.txt').read().splitlines()
motif = lines[0]

#print out the name of first seq
if lines[1][0] == '>':
    lnspls = lines[1].split(' ')
    seqname = lnspls[0][1:]
    sys.stdout.write(seqname+': ')


tempSeq = ''
count = 0
for line in lines[2:]:
    #if we meet the beginning of next seq, we count the motif
    if line[0] == '>':
        #Now the tempSeq represents the previous seq.
        for i in range(0, len(tempSeq) - len(motif) + 1):
            if tempSeq[i:i+len(motif)] == motif: 
                count += 1
        #output the count of motif in the last seq
        sys.stdout.write(str(count)+'\n')

        #reset the tempSeq and count
        tempSeq = ''
        count = 0

        #After counting the target motif, let's print out the name of next seq first
        lnspls = line.split(' ')
        seqname = lnspls[0][1:]
        sys.stdout.write(seqname+': ')

    else:
        tempSeq += line.strip()

#We still need to count the notif of the last seq
#Now the tempSeq represents the last seq.
for i in range(0, len(tempSeq) - len(motif) + 1):
    if tempSeq[i:i+len(motif)] == motif: 
        count += 1
#output the count of motif in the last seq
sys.stdout.write(str(count)+'\n')