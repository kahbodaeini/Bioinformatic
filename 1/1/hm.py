class Node :
    value = 0
    parent = None

strings = input().split(">")
strings.pop(0)
arrays = [''.join(x.split()[1:]) for x in strings]
s = arrays[0]
t = arrays[1]

matrix = []
for i in range (0 , len(s)+1):
    matrix.append([])
    for j in range (0 , len(t)+1):
        matrix[i].append(Node())

for i in range (1 , len(s)+1):
    matrix[i][0].value = i
    matrix[i][0].parent = "up"    
for i in range (1 , len(t)+1):
    matrix[0][i].value = i
    matrix[0][i].parent = "left"

for i in range (1 , len(s)+1):
    for j in range (1 , len(t)+1):
        delta = 0 if s[i-1]==t[j-1] else 1
        if matrix[i-1][j-1].value+delta <= matrix[i][j-1].value+1 and matrix[i-1][j-1].value+delta <= matrix[i-1][j].value+1 :
            matrix[i][j].value = matrix[i-1][j-1].value+delta
            matrix[i][j].parent = "upper left"
        elif matrix[i][j-1].value+1 <= matrix[i-1][j-1].value+delta and matrix[i][j-1].value+1 <= matrix[i-1][j].value+1 :
            matrix[i][j].value = matrix[i][j-1].value+1
            matrix[i][j].parent = "left"
        elif matrix[i-1][j].value+1 <= matrix[i-1][j-1].value+delta and matrix[i-1][j].value+1 <= matrix[i][j-1].value+1 :
            matrix[i][j].value = matrix[i-1][j].value+1
            matrix[i][j].parent = "up"

sprime = []
tprime = []


i = len(s)
j = len(t)
node = matrix[i][j]

while(node.parent != None):
    if node.parent == "upper left":
        i-=1
        j-=1
        sprime.append(s[i])
        tprime.append(t[j])
    elif node.parent == "up":
        i-=1
        sprime.append(s[i])
        tprime.append("-")
    elif node.parent == "left":
        j-=1
        sprime.append("-")
        tprime.append(t[j])
    node = matrix[i][j]

sprime.reverse()
tprime.reverse()

print(matrix[len(s)][len(t)].value)
print(''.join(sprime))
print(''.join(tprime))
