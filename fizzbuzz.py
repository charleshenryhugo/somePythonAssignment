import sys

i = int(raw_input())
j = int(raw_input())

for k in range(i,j+1):
    if k % 5 == 0 and k % 3 == 0:
        sys.stdout.write("Fizz Buzz\n")
    elif k % 5 == 0:
        sys.stdout.write("Buzz\n")
    elif k % 3 == 0:
        sys.stdout.write("Fizz\n")
    else:
        sys.stdout.write(str(k)+"\n")