import yaml
import sys
import re

#load yaml stdin
ymldata = yaml.load(sys.stdin.read())
handlers = ymldata['handlers'] #list

#load input.txt
F = open('input.txt')
lines = F.read().strip().split('\n')
F.close()

for line in lines:
    max_match = ''
    script = ''
    for handler in handlers:
        if not('script' in handler):
            continue
        p = str(handler['url']) #url pattern
        match = re.match(p, line)
        if match:
            if len(match.group(0)) > len(max_match):
                max_match = match.group(0)
                script = handler['script']
    sys.stdout.write(str(script) + '\n')

