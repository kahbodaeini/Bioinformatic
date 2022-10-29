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

matrix = []

align1, align2 = "", ""

arr = [[[0, ''] for j in range(len(string2) + 1)] for i in range(len(string1) + 1)]

for i in range(1, len(string1) + 1):
    arr[i][0] = [i, ""]

for j in range(1, len(string2) + 1):
    arr[0][j] = [j, ""]

for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        temp = 0
        if string1[i - 1] == string2[j - 1]:
            temp = arr[i - 1][j - 1][0]
        else:
            temp = arr[i - 1][j - 1][0] + 1
        arr[i][j] = min([arr[i - 1][j][0] + 1, arr[i - 1][j][1] + '0'], [arr[i][j - 1][0] + 1, arr[i][j - 1][1] + '1'], [temp, arr[i - 1][j - 1][1] + '2'])

i, j = 0, 0
for num in arr[-1][-1][1]:
    if num == '0':
        align1 += string1[j]
        align2 += '-'
        j += 1
    elif num == '1':
        align1 += '-'
        align2 += string2[i]
        i += 1
    else:
        align1 += string1[j]
        align2 += string2[i]
        j += 1
        i += 1

print(arr[-1][-1][0])
print(align1)
print(align2)

output_file = open("output.txt", 'w')
output_file.write(str(arr[-1][-1][0]))
output_file.write('\n')
output_file.write(align1)
output_file.write('\n')
output_file.write(align2)
