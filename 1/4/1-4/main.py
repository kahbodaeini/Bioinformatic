import math

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

matrix = [[[0, ''] for j in range(n2 + 1)] for i in range(n1 + 1)]

for i in range(1, n1 + 1):
    matrix[i][0] = [0, 'zero']
for i in range(1, n2 + 1):
    matrix[0][i] = [-math.inf, '']

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        s1 = matrix[i - 1][j - 1][0] + int(string1[i - 1] == string2[j - 1]) * 2 - 1
        s2 = matrix[i][j - 1][0] - 1
        s3 = matrix[i - 1][j][0] - 1
        max_s = max(s1, s2, s3)
        if max_s == s1:
            matrix[i][j] = [s1, 'diagonal']
        elif max_s == s2:
            matrix[i][j] = [s2, 'up']
        else:
            matrix[i][j] = [s3, 'left']

maximum_node = matrix[0][n2]
max_i = 0
for i in range(n1 + 1):
    if matrix[i][n2][0] > maximum_node[0]:
        maximum_node = matrix[i][n2]
        max_i = i

maximum = maximum_node[0]

align1, align2 = '', ''
i = max_i
j = n2
while i != 0 and j != 0:
    if matrix[i][j][1] == 'zero' or matrix[i][j][1] == '':
        break
    if matrix[i][j][1] == 'up':
        align1 = '-' + align1
        align2 = string2[j - 1] + align2
        j -= 1
    elif matrix[i][j][1] == 'left':
        align1 = string1[i - 1] + align1
        align2 = '-' + align2
        i -= 1
    elif matrix[i][j][1] == 'diagonal':
        align1 = string1[i - 1] + align1
        align2 = string2[j - 1] + align2
        i -= 1
        j -= 1
    else:
        pass

output_file = open("output.txt", 'w')
output_file.write(str(maximum))
output_file.write('\n')
output_file.write(align1)
output_file.write('\n')
output_file.write(align2)
    
print(maximum)
print(align1[::-1])
print(align2[::-1])
