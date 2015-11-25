__author__ = 'heziresheff'

import json

data = log = open("people.txt", 'r')
data.readline()

d = dict()
while True:
    row = data.readline()
    if row[0] == "=":
        break
    handle, name = row.split(" : ")
    d[handle] = name.replace('\n', '')

json.dump(d, open("people.json", 'w'), indent=4)



