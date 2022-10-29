def ham_dis(str1, str2):
    n = len(str1)
    ham = 0

    for i in range(n):
        if str1[i] == str2[i]:
            continue
        ham += 1

    return ham


def score(motifs):
    score = 0
    for i in range(len(motifs[0])):
        motif = ''.join([motifs[j][i] for j in range(len(motifs))])
        score += min([ham_dis(motif, homogeneous * len(motif)) for homogeneous in 'ACGT'])
    return score


def profile(motifs):
    prof = []
    for i in range(len(motifs[0])):
        col = ''.join([motifs[j][i] for j in range(len(motifs))])
        prof.append([float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'])
    return prof


def profile_most_probable_kmer(dna, k, prof):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    max_prob = [-1, None]
    for i in range(len(dna) - k + 1):
        current_prob = 1
        for j, nucleotide in enumerate(dna[i:i + k]):
            current_prob *= prof[j][nuc_loc[nucleotide]]
        if current_prob > max_prob[0]:
            max_prob = [current_prob, dna[i:i + k]]

    return max_prob[1]


with open('input.txt') as input_data:
    k, t = map(int, input_data.readline().split())
    dna_list = [line.strip() for line in input_data.readlines()]

best_score = [t * k, None]

for i in range(len(dna_list[0]) - k + 1):
    motifs = [dna_list[0][i:i + k]]
    current_profile = profile(motifs)

    for j in range(1, t):
        motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))
        current_profile = profile(motifs)

    current_score = score(motifs)
    if current_score < best_score[0]:
        best_score = [current_score, motifs]

print('\n'.join(best_score[1]))
with open('output.txt', 'w') as output_data:
    output_data.write('\n'.join(best_score[1]))
