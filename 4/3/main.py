import random

def randomized_motif_search(DNA, k, t):
    m = random_motifs(DNA, k, t)
    best_founded_motifs = m
    while True:
        profile = create_profile(m)
        m = generate_motifs(profile, DNA)
        if calculate_score(m) < calculate_score(best_founded_motifs):
            best_founded_motifs = m
        else:
            return best_founded_motifs


def random_motifs(DNA, k, t):
    random_motifs = []
    for i in range(t):
        random_numb = random.randint(0, t)
        random_motifs.append(DNA[i][random_numb:random_numb + k])
    return random_motifs


def generate_motifs(profile, DNA):
    motifs = []
    t = len(DNA)
    k = len(profile['A'])
    for i in range(t):
        motifs.append(profile_most_probable_kmer(DNA[i], k, profile))
    return motifs


def profile_most_probable_kmer(text, k, profile):
    most_probable_value = -1
    most_probable_kmer = ''
    for i in range(0, 1 + len(text) - k):
        kmer = text[i:i + k]
        probKmerVal = calculate_probability(kmer, profile)
        if probKmerVal > most_probable_value:
            most_probable_value = probKmerVal
            most_probable_kmer = kmer
    return most_probable_kmer


def calculate_probability(text, profile):
    p = 1
    for i in range(len(text)):
        p = p * profile[text[i]][i]
    return p


def create_profile(motifs):
    profile = dict()
    motif_len = len(motifs[0])
    length = len(motifs)
    size = motif_len
    profile['A'] = [1 for i in range(size)]
    profile['C'] = [1 for i in range(size)]
    profile['G'] = [1 for i in range(size)]
    profile['T'] = [1 for i in range(size)]
    for i in range(length):
        for j in range(size):
            profile[motifs[i][j]][j] += 1
    return profile


def calculate_counts(motifs):
    count = {}
    pseudocounts = {}
    t = len(motifs)
    k = len(motifs[0])
    for symbol in 'GACT':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    for symbol in 'GACT':
        pseudocounts[symbol] = []
    for c in count:
        for y in count[c]:
            z = y + 1
            pseudocounts[c].append(z)
    return pseudocounts


def get_consensus(motifs):
    k = len(motifs[0])
    count = calculate_counts(motifs)
    consensus = ''
    for j in range(k):
        m = 0
        most_used_symbol = ''
        for symbol in 'ACGT':
            if count[symbol][j] > m:
                m = count[symbol][j]
                most_used_symbol = symbol
        consensus += most_used_symbol
    return consensus


def calculate_hamming_distance(str_one, str_two):
    length = len(str_one)
    distances = 0
    for i in range(length):
        if str_one[i] != str_two[i]:
            distances += 1
    return distances


def calculate_score(motifs):
    score = 0
    consensus = get_consensus(motifs)
    for motif in motifs:
        score += calculate_hamming_distance(consensus, motif)
    return score


input_file = open("input.txt", 'r')
lines = input_file.read().splitlines()

k, t = lines[0].split()
k, t = int(k), int(t)
DNA = [lines[i] for i in range(1, len(lines))]

number_of_iterations = 1000
randomized_motif_search(DNA, k, t)
m = randomized_motif_search(DNA, k, t)
best_gained_motifs = m
for i in range(number_of_iterations + 1):
    m = randomized_motif_search(DNA, k, t)
    if calculate_score(m) < calculate_score(best_gained_motifs):
        best_gained_motifs = m
    else:
        best_founded_motifs = best_gained_motifs

print('\n'.join(best_founded_motifs))