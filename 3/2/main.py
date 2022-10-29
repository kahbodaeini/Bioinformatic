input_file = open('input.txt', 'r')
lines = input_file.readlines()

n = int(lines[0])
j = int(lines[1])
adj_matrix = []

for i in range(n):
    lis = lines[2+i].split()
    adj_matrix.append(lis)
    
i = (j+1) % n
k = (j+2) % n
min_len = (int(adj_matrix[i][j]) + int(adj_matrix[j][k]) - int(adj_matrix[i][k])) / 2

for i in range(n):
    for k in range(i+1, n):
        if i == j or k == j:
            continue
        curr_len = (int(adj_matrix[i][j]) + int(adj_matrix[j][k]) - int(adj_matrix[i][k])) / 2
        min_len = min(min_len, curr_len)

output_file = open('output.txt', 'w')
output_file.write(str(int(min_len)))
