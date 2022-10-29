def pattern_to_number(motif):
    dictionary = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if len(motif) == 0:
        return 0
    symbol = motif[-1:]
    new_pattern = pattern_to_number(motif[0:-1])
    new_pattern = new_pattern * 4
    value = new_pattern + dictionary[symbol]
    return value


def gene_ID(str, k):
    dictionary = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k == 1:
        return dictionary[str]
    q, r = str // 4, str % 4
    gene_number = dictionary[r]
    value = gene_ID(q, k - 1) + gene_number
    return value


def pattern_generator(lis):

    ret = ""

    dic = {0: "A", 1: "C", 2: "G", 3: "T"}

    for i in lis:
        ret += dic[i]

    return ret


def calculate_kmer(DNA, k, profile):
    dictionary = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    maximum_probability = 0
    kmer = DNA[0:k]
    size = len(DNA) - k + 1
    for i in range(0, size):
        probability = 1
        motif = DNA[i:i + k]
        for j in range(k):
            pattern = dictionary[motif[j]]
            probability *= profile[pattern][j]
        if probability > maximum_probability:
            maximum_probability = probability
            kmer = motif
    return kmer


def ham_dis(str1, str2):
    n = len(str1)
    ham = 0

    for i in range(n):
        if str1[i] == str2[i]:
            continue
        ham += 1

    return ham


def create_profile(array):
    dictionary = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    size = len(array[0])
    profile = [[1 for i in range(size)] for j in range(4)]
    for str in array:
        for i in range(len(str)):
            j = dictionary[str[i]]
            profile[j][i] += 1
    for str in profile:
        for string in str:
            string /= len(array)
    return profile


def find_motif_distances(motif, DNA):
    k = len(motif)
    distance = 0
    for str in DNA:
        hamming = k + 1
        distance = len(str) - k
        for i in range(distance+1):
            hamming_dist = ham_dis(motif, str[i:i + k])
            if hamming > hamming_dist:
                hamming = hamming_dist
        distance += hamming
    return distance


def calculate_score(array):
    dictionary = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    new_string = ''
    profile = create_profile(array)
    size = len(profile[0])
    for i in range(size):
        maximum = 0
        index = 0
        for j in range(len(dictionary)):
            if profile[j][i] > maximum:
                index = j
                maximum = profile[j][i]
        new_string += dictionary[index]
    calculate_score = 0
    for str in array:
        for i in range(len(str)):
            if new_string[i] != str[i]:
                calculate_score += 1
    return calculate_score


def greedy_search(DNA, k, t):
    matches = []
    for str in DNA:
        matches.append(str[0:k])
    size=len(DNA[0]) - k
    for i in range(size+ 1):
        array = []
        array.append(DNA[0][i:i + k])
        for j in range(1, t):
            profile = create_profile(array)
            array.append(calculate_kmer(DNA[j], k, profile))
        if calculate_score(array) < calculate_score(matches):
            matches = array
    return matches


inp = open("input.txt", 'r')
lines = inp.read().splitlines()

DNA = []
k, t = map(int, lines[0].split())

for i in range(1, len(lines)):
    DNA.append(lines[i])


motifs = greedy_search(DNA, k, t)

output = open("output.txt", 'w')

for i in motifs:
    output.write(i)
    output.write('\n')
