import math

Blosum = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
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

nums_dic = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9, 'M': 10,
              'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}


def input_Rosalind():
    seq1 = ''
    seq2 = ''
    counter = 0
    input_file = open('input.txt', 'r')
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


def global_alignment(seq1, seq2):
    
    glob_align1, glob_align2 = "", ""
    n, m = len(seq1), len(seq2)

    low = [[0 for j in range(m + 1)] for i in range(n + 1)]
    mid = [[0 for j in range(m + 1)] for i in range(n + 1)]
    up = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        low[i][0] = -11 - (i - 1) * 1
        mid[i][0] = -11 - (i - 1) * 1
        up[i][0] = -math.inf

    for j in range(1, m + 1):
        low[0][j] = -math.inf
        mid[0][j] = -11 - (j - 1) * 1
        up[0][j] = -11 - (j - 1) * 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            low[i][j] = max(low[i - 1][j] - 1, mid[i - 1][j] - 11)
            up[i][j] = max(up[i][j - 1] - 1, mid[i][j - 1] - 11)
            score = Blosum[nums_dic[seq1[i - 1]]][nums_dic[seq2[j - 1]]]
            mid[i][j] = max(low[i][j], mid[i - 1][j - 1] + score, up[i][j])

    i, j = n, m

    while i > 0 and j > 0:
        if mid[i][j] == mid[i - 1][j - 1] + Blosum[nums_dic[seq1[i - 1]]][nums_dic[seq2[j - 1]]]:
            i -= 1
            j -= 1
            glob_align1 = seq1[i] + glob_align1
            glob_align2 = seq2[j] + glob_align2
        elif mid[i][j] == low[i][j]:
            i -= 1
            glob_align1 = seq1[i] + glob_align1
            glob_align2 = '-' + glob_align2
        else:
            j -= 1
            glob_align1 = '-' + glob_align1
            glob_align2 = seq2[j] + glob_align2

    return mid[-1][-1], glob_align1, glob_align2


s, t = input_Rosalind()
score, align1, align2 = global_alignment(s, t)
print(score)
print(align1)
print(align2)
