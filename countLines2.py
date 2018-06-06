import sys 

try:
    F = open(sys.stdin.read().strip())
    lines = F.read().strip().split('\n')
    n = 1
    for line in lines:
        sys.stdout.write(str(n) + ': ' + str(line) + '\n')
        n += 1
    F.close()
except IOError:
    sys.stdout.write('ERROR\n')