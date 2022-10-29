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
find_middle = [0, -1, 1, 2, 3, 4, 5, 6, 7, -1, 8, 9, 10, 11, -1, 12, 13, 14, 15, 16, -1, 17, 18, -1, 19, -1]

string1 = ""
string2 = ""

input_file = open('input.txt', 'r')
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

n1 = len(string1)
n2 = len(string2)

up = [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]
mid = [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]
low = [[0 for x in range(n2 + 1)] for y in range(n1 + 1)]

maximum = -1
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):

        x = up[i - 1][j] - 1
        y = mid[i - 1][j] - 11
        up[i][j] = max(x, y)

        x = low[i][j - 1] - 1
        y = mid[i][j - 1] - 11
        low[i][j] = max(x, y)

        a = ord(string1[i - 1]) - ord('A')
        b = ord(string2[j - 1]) - ord('A')
        z = mid[i - 1][j - 1] + BLOSUM62[find_middle[a]][find_middle[b]]
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
    a = ord(string1[i - 1]) - ord('A')
    b = ord(string2[j - 1]) - ord('A')
    if mid[i][j] == mid[i - 1][j - 1] + BLOSUM62[find_middle[a]][find_middle[b]]:
        align1 = string1[i - 1] + align1
        align2 = string2[j - 1] + align2
        i -= 1
        j -= 1
    elif mid[i][j] == up[i][j]:
        align1 = string1[i - 1] + align1
        i -= 1
    elif mid[i][j] == low[i][j]:
        align2 = string2[j - 1] + align2
        j -= 1
    else:
        break

output_file = open("output.txt", 'w')
output_file.write(str(maximum))
output_file.write('\n')
output_file.write(align1)
output_file.write('\n')
output_file.write(align2)

print(maximum)
print(align1)
print(align2)
