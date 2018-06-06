import json

a = []
a.append('airplane')
a.append('car')
a.append('bike')

a = [4, 9, 2]
a.append(3)

a = {}
a['John'] = 1234
a['Jeff'] = 9999

b = json.dumps(a)
print(b)

