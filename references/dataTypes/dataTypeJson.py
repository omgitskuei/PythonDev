import json

json.dumps([1, 'simple', 'list']) #'[1, "simple", "list"]'

x = [1, 'simple', 'list']
f = open('testFile', 'r+')

json.dump(x, f)

x = json.load(f)
