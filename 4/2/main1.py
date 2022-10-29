from collections import Counter
from functools import reduce
import numpy as np
import heapq
from itertools import combinations,product,izip,ifilter,chain
import operator


def read_file(input_file):
    f = open(input_file)
    data = [item.strip() for item in f.readlines()]
    k, t = map(int, data[0].split(' '))
    f.close()
    return k, t, data[1:]


def correct(seq, k):
    return [seq[i:i + k] for i in range(len(seq) - k + 1)]


def all_kmers(k, Dna):
    return [correct(seq, k) for seq in Dna]


def profile_baseline_consensus(List, k, t):
    List = np.asarray([list(item) for item in List])
    i, baseline_score, consensus = 0, 0, ''
    pro = np.zeros(shape=(4, k))
    while i < k:
        d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        c = Counter(List[:, i])
        consensus += c.most_common(1)[0][0]
        baseline_score += t - c.most_common(1)[0][1]
        for kd, vd in d.iteritems():
            if kd in c.keys():
                d[kd] = (c[kd] + 1) / float(t + 1)
            else:
                d[kd] = 1 / float(t + 1)
        pro[:, i] = [d['A'], d['C'], d['G'], d['T']]
        i += 1
    return (consensus, baseline_score, pro)


def pmpkp(kmer, order, profile):
    c, i = [], 0
    while i < len(kmer):
        c.append(profile.item(order.index(kmer[i]), i))
        i += 1
    return reduce(operator.mul, c, 1)


def form_profile(iks, kmer_set, k, t):
    order = ['A', 'C', 'G', 'T']
    consensus, baseline, profile = profile_baseline_consensus(iks, k, t)
    intermediate = [(kmer, pmpkp(kmer, order, profile)) for kmer in kmer_set]
    iks.append(heapq.nlargest(1, intermediate, key=lambda x: x[1])[0][0])
    return iks


def loopover(iks, ksl, k, t):
    i = 0
    while i < len(ksl):
        iks = form_profile(iks, ksl[i], k, t)
        i += 1
    return iks


def best_motifs_collections(k, t, Dna):
    aksv = all_kmers(k, Dna)
    return [loopover([iks], aksv[1:], k, t) for iks in aksv[0]]


def greedy_motif_search(Dna, k, t):
    aksv = all_kmers(k, Dna)
    best_motifs = [dna[:k] for dna in Dna]
    baseline_score = profile_baseline_consensus(best_motifs, k, t)[1]
    bmcs = best_motifs_collections(k, t, Dna)
    for bmc in bmcs:
        pbc = profile_baseline_consensus(bmc, k, t)
        if pbc[1] < baseline_score:
            baseline_score = pbc[1]
            best_motifs = bmc
    return best_motifs


def result(filename):
    k, t, Dna = read_file(filename)
    return greedy_motif_search(Dna, k, t)


if __name__ == "__main__":
    results = result("input.txt")
    fw = open('output.txt', 'w')
    fw.write('\n'.join(results))
    fw.close()
