__author__ = 'heziresheff'

import json

DEFAULT_IN = 'C:\\Users\\t-yeresh\\Downloads\\test\\graph.log'
DEFAULT_OUT = 'graph.json'


def log2graph(in_log):
    E = []
    V = []
    log = open(DEFAULT_IN, 'r')

    # Skip header
    while log.readline()[0] != "=":
        pass

    # People
    while True:
        row = log.readline()
        if row[0] == '=':
            break
        V.append(row.replace("\n", ""))

    # Friends
    for i, person in enumerate(V):
        print(i)
        log.readline()
        log.readline()
        while True:
            row = log.readline()
            if row.startswith("->End Person"):
                break
            row = row.split("?")[0]
            if row in V:
                j = V.index(row)
                E.append([i, j])

    return V, E


if __name__ == "__main__":
    # command line tool
    V, E = log2graph(DEFAULT_IN)
    json.dump({"V": V, "E": E}, open(DEFAULT_OUT, 'w'), indent=4)
