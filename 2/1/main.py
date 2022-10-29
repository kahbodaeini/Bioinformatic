def reverse(string):
    reverse = ""
    for ch in string[::-1]:
        if ch == 'A':
            reverse += 'T'
        elif ch == 'T':
            reverse += 'A'
        elif ch == 'C':
            reverse += 'G'
        elif ch == 'G':
            reverse += 'C'
    return reverse


def de_bruijn_graph(nodes):

    edges = []
    for string in nodes:
        if (string[0: -1], string[1:]) not in edges:
            edges.append((string[0: -1], string[1:]))
    return edges


file = open("input.txt", 'r')
strings = file.readlines()

# nodes = []
# 
# for string in strings:
#     if string not in nodes:
#         nodes.append(string)
# 
#     rev_str = reverse(string)
#     if rev_str not in nodes:
#         nodes.append(rev_str)

nodes = []
reverse_complement_strings = [reverse(string) for string in strings]
for string in strings:
    if string not in nodes:
        nodes.append(string)
for string in reverse_complement_strings:
    if string not in nodes:
        nodes.append(string)

edges = de_bruijn_graph(nodes)

output = open("output.txt", 'w')
for edge in edges:
    output.write(f'({str(edge[0])}, {str(edge[1])})')
    output.write('\n')
