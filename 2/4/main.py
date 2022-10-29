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


def calculate_hamming_distance(DNA_1, DNA_2):
    hamming_distance = 0
    for x, y in zip(DNA_1, DNA_2):
        if x != y:
            hamming_distance += 1
    return hamming_distance


def get_result(corrections_arr, mistakes):
    corrections = []
    for mistake in mistakes:
        for DNA_str in corrections_arr:
            distance1 = calculate_hamming_distance(mistake, DNA_str)
            distance2 = calculate_hamming_distance(mistake, calculate_complement(DNA_str))
            str = ''
            if distance1 == 1:
                str = mistake + '->' + DNA_str
                corrections.append(str)
            elif distance2 == 1:
                completment = calculate_complement(DNA_str)
                str = mistake + '->' + completment
                corrections.append(str)
            corrections.append(str)
    return corrections

strings = {}

input = open("input.txt", 'r')
count = -1

for line in input:
    line = line.strip()
    if line.startswith('>'):
        count += 1
        strings[count] = []
        continue
    DNA = line
    strings[count].append(DNA)

DNA_sequences = []
corrections_arr = []
mistakes = []

DNA = ''
for key in strings:
    value = strings[key]
    for num in value:
        DNA += num
        strings[key] = DNA
    DNA = ''

keys = strings

for key in keys:
    DNA_sequences.append(keys[key])
for DNA in DNA_sequences:
    number_of_complements = DNA_sequences.count(calculate_complement(DNA))
    count = DNA_sequences.count(DNA) + number_of_complements
    if DNA == calculate_complement(DNA):
        count -= 1
    if count > 1 and DNA not in corrections_arr:
        if calculate_complement(DNA) not in corrections_arr:
            corrections_arr.append(DNA)
    else:
        mistakes.append(DNA)
corrections = get_result(corrections_arr, mistakes)

output = open("output.txt", 'w')
for i in range(len(list(set(corrections)))):
    if i > 0:
        output.write(list(set(corrections))[i] + '\n')