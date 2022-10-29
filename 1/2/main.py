import math

dic = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9, 'M': 10,
              'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}

blosum62 = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
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

string1, string2 = "", ""

input_file = open('rosalind_gaff.txt', 'r')
Lines = input_file.readlines()

count = 0
for line in Lines:
    l = line.strip()
    if l.startswith(">") and count == 0:
        count += 1
        continue
    elif not l.startswith(">") and count == 1:
        string1 += l
        continue
    elif l.startswith(">") and count == 1:
        count += 1
        continue
    elif not l.startswith(">") and count == 2:
        string2 += l
        continue

input_file.close()

align1, align2 = "", ""

low = [[0 for j in range(len(string2) + 1)] for i in range(len(string1) + 1)]
mid = [[0 for j in range(len(string2) + 1)] for i in range(len(string1) + 1)]
up = [[0 for j in range(len(string2) + 1)] for i in range(len(string1) + 1)]

for i in range(1, len(string1) + 1):
    low[i][0] = -11 - (i - 1) * 1
    mid[i][0] = -11 - (i - 1) * 1
    up[i][0] = -math.inf

for j in range(1, len(string2) + 1):
    low[0][j] = -math.inf
    mid[0][j] = -11 - (j - 1) * 1
    up[0][j] = -11 - (j - 1) * 1

for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        low[i][j] = max(low[i - 1][j] - 1, mid[i - 1][j] - 11)
        up[i][j] = max(up[i][j - 1] - 1, mid[i][j - 1] - 11)
        score = blosum62[dic[string1[i - 1]]][dic[string2[j - 1]]]
        mid[i][j] = max(low[i][j], mid[i - 1][j - 1] + score, up[i][j])

i, j = len(string1), len(string2)
while i > 0 and j > 0:
    if mid[i][j] == mid[i - 1][j - 1] + blosum62[dic[string1[i - 1]]][dic[string2[j - 1]]]:
        i -= 1
        j -= 1
        align1 = string1[i] + align1
        align2 = string2[j] + align2
    elif mid[i][j] == low[i][j]:
        i -= 1
        align1 = string1[i] + align1
        align2 = '-' + align2
    else:
        j -= 1
        align1 = '-' + align1
        align2 = string2[j] + align2

print(mid[-1][-1])
print(align1)
print(align2)

output_file = open("output.txt", 'w')
output_file.write(str(mid[-1][-1]))
output_file.write('\n')
output_file.write(align1)
output_file.write('\n')
output_file.write(align2)
