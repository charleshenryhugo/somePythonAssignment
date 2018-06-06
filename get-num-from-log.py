import re
import sys

data = sys.stdin.read()

p = re.compile("added (\d*) sequences in (\d*[.]*\d*) seconds.")
r = p.search(data)
if r != None:
    print(r.group(1))