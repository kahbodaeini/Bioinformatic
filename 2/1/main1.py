class Node:
    def __init__(self, kmer):
        self.kmer = kmer
        self.edges = []


def k_mers(m, string):
    kmers_arr = []
    size = len(string) + 1
    for i in range(size - m):
        kmers_arr.append(string[i: i + m])
    return kmers_arr


def de_Bruijn_graph(DNA_arr):
    nodes = {}
    a = []
    b = []
    size = len(DNA_arr[0])
    for DNA in DNA_arr:
        last_node = None
        for kmer in k_mers(size - 1, DNA):
            if kmer not in nodes:
                nodes[kmer] = Node(kmer)
            if last_node:
                if nodes[kmer] not in last_node.edges:
                    last_node.edges.append(nodes[kmer])
            last_node = nodes[kmer]
    for kmer, node in sorted(nodes.items()):
        for edge in node.edges:
            a.append(kmer), b.append(edge.kmer)
    return a, b


def calculate_complement(DNA_strand):
    complement = []
    transforms = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'T'}
    DNA_arr = list(DNA_strand)
    DNA_arr.reverse()
    DNA_strand = ''.join(DNA_arr)
    for DNA in DNA_strand:
        complement.append(transforms[DNA])
    string = ''.join(complement)
    return string


file = open("input.txt", 'r')
strings = file.read().splitlines()
file.close()

strings += [calculate_complement(string) for string in strings]

a, b = de_Bruijn_graph(strings)

output = open("output.txt", 'w')

for i in range(len(a)):
    output.write(f'({a[i]}, {b[i]})')
    output.write('\n')