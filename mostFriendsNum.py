import sys

inputs=sys.stdin.read().split("\n")

dic={} #name:friend_num

i = 0
while True:
    if inputs[i] == 'END' and inputs[i+1] == 'END':
        break
    if inputs[i] in dic:
        dic[inputs[i]] += 1
    else:
        dic[inputs[i]] = 1
    if inputs[i+1] in dic:
        dic[inputs[i+1]] += 1
    else:
        dic[inputs[i+1]] = 1
    i += 2

Na = ""
Mf = 0
for k in dic.keys():
    if dic[k] >= Mf:
        Mf = dic[k]
        Na = k

sys.stdout.write(Na + ' ' + str(Mf) + '\n')