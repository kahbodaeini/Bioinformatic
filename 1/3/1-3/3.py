find_mid = [0, -1, 1, 2, 3, 4, 5, 6, 7, -1, 8, 9, 10, 11, -1, 12, 13, 14, 15, 16, -1, 17, 18, -1, 19, -1]

BLOSUM62 = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
                [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
                [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
                [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
                [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
                [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
                [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
                [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
                [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
                [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
                [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
                [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
                [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
                [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
                [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
                [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
                [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
                [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
                [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
                [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]


def output(score, a1, a2):
    output_file = open("output1.txt", 'w')
    output_file.write(str(score))
    output_file.write('\n')
    output_file.write(a1)
    output_file.write('\n')
    output_file.write(a2)


def input_Rosalind():
    seq1 = ''
    seq2 = ''
    counter = 0
    input_file = open('rosalind_laff.txt', 'r')
    lines = input_file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if counter == 0 or counter == 1:
                counter += 1
        else:
            if counter == 1:
                seq1 += line
            else:
                seq2 += line
    return seq1, seq2


def local_alignment(seq1, seq2):
    n = len(seq1)
    m = len(seq2)

    up = [[0 for x in range(m + 1)] for y in range(n + 1)]
    mid = [[0 for x in range(m + 1)] for y in range(n + 1)]
    low = [[0 for x in range(m + 1)] for y in range(n + 1)]

    maximum = -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            x = up[i - 1][j] - 1
            y = mid[i - 1][j] - 11
            up[i][j] = max(x, y)

            x = low[i][j - 1] - 1
            y = mid[i][j - 1] - 11
            low[i][j] = max(x, y)

            a = ord(seq1[i - 1]) - ord('A')
            b = ord(seq2[j - 1]) - ord('A')
            z = mid[i - 1][j - 1] + BLOSUM62[find_mid[a]][find_mid[b]]
            mid[i][j] = max(low[i][j], up[i][j], z, 0)

            if mid[i][j] > maximum:
                maximum = mid[i][j]
                first_index = i
                second_index = j

    i = first_index
    j = second_index
    align1 = ''
    align2 = ''

    while (i > 0) and (j > 0):
        a = ord(seq1[i - 1]) - ord('A')
        b = ord(seq2[j - 1]) - ord('A')
        if mid[i][j] == mid[i - 1][j - 1] + BLOSUM62[find_mid[a]][find_mid[b]]:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif mid[i][j] == up[i][j]:
            align1 = seq1[i - 1] + align1
            i -= 1
        elif mid[i][j] == low[i][j]:
            align2 = seq2[j - 1] + align2
            j -= 1
        else:
            break

    return maximum, align1, align2


s, t = input_Rosalind()
maximum, align1, align2 = local_alignment(s, t)
print(maximum)
print(align1)
print(align2)
output(maximum, align1, align2)
