import sys

lines = open('test.txt')

num_lines = sum(1 for line in lines)

print(num_lines)

lines.close()