import sys
sys.setrecursionlimit(4000)


def make_graph(sequence, DBJ_edges, k, length):
    count = -1
    for i in range(len(DBJ_edges)):
        selection = sequence[1 - k:]
        if DBJ_edges[i][0] == selection:
            count = i
    if count == -1:
        if len(DBJ_edges):
            print()
            return []
        else:
            selection = sequence[:length]
            print(selection)
            return [sequence]

    i = count
    first_line = sequence + DBJ_edges[i][1][-1]
    edges = DBJ_edges[:i] + DBJ_edges[i + 1:]
    return make_graph(first_line, edges, k, length)


def de_bruijn_graph(strings):
    length = len(strings[0])
    size = len(strings)
    DBJ_edges = []
    for kmer in strings:
        a = kmer[0:length - 1]
        b = kmer[1:length]
        DBJ_edges.append([a, b])
    make_graph(strings[0], DBJ_edges, length, size)


strings = []
input = open("input.txt", 'r')
lines = input.readlines()
for line in lines:
    if line[-1] == "\n":
        line = line[:-1]
    strings.append(line)

output = open("output.txt", 'w')

de_bruijn_graph(strings)
