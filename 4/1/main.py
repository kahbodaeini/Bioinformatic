import math


def ham_dis(str1, str2):
    n = len(str1)
    ham = 0

    for i in range(n):
        if str1[i] == str2[i]:
            continue
        ham += 1

    return ham


def min_ham_dis(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    min_ham = n1

    for i in range(n2 - n1):
        temp = ham_dis(str1, str2[i: i + n1])
        if temp < min_ham:
            min_ham = temp

    return min_ham


def number_to_4_based(n, l):
    if n == 0:
        return [0] * l
    digits = [0] * l
    i = 0
    while n:
        digits[i] = int(n % 4)
        n //= 4
        i += 1
    return digits[::-1]


def pattern_generator(lis):

    ret = ""

    dic = {0: "A", 1: "C", 2: "G", 3: "T"}

    for i in lis:
        ret += dic[i]

    return ret


def generate_all_patterns(n):

    lis = []
    for i in range(4 ** n):
        lis.append(pattern_generator(number_to_4_based(i, n)))

    return lis


inp = open("input.txt", 'r')
lines = inp.read().splitlines()

DNA = []
n = int(lines[0])

for i in range(1, len(lines)):
    DNA.append(lines[i])

all_patterns = generate_all_patterns(n)

best_score = math.inf
best_median = all_patterns[0]

for i in range(4 ** n):

    median = all_patterns[i]
    median_score = 0

    for j in DNA:
        median_score += min_ham_dis(median, j)

    if median_score < best_score:
        best_score = median_score
        best_median = median

output = open("output.txt", 'w')
output.write(best_median)