import numpy as np


def limb(matrix, t):
    index = n - t - 2
    summations = sum(matrix)
    arr = np.zeros(shape=matrix.shape)
    distance_matrix = np.zeros(shape=matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            a = summations[i]
            b = summations[j]
            if i != j:
                arr[i][j] = index * matrix[i][j]
                arr[i][j] -= (a + b)
            if j > i:
                distance_matrix[i][j] = (a - b) / index
                distance_matrix[j][i] = distance_matrix[i][j]
    min_candidates = np.argwhere(arr == np.min(arr))
    min_arr = min_candidates[0]
    x01 = distance_matrix[min_arr[0]][min_arr[1]]
    x10 = distance_matrix[min_arr[1]][min_arr[0]]
    y01 = matrix[min_arr[0]][min_arr[1]]
    y10 = matrix[min_arr[1]][min_arr[0]]
    w1 = (x01 + y01) / 2
    w2 = (y10 - x10) / 2
    a1 = matrix[min_arr[0]][min_arr[1]]
    new_matrix = [(matrix[k2][min_arr[0]] + matrix[k2][min_arr[1]] - a1) * (0.5) for k2 in range(index + 2)]
    new_matrix = np.delete(new_matrix, min_arr)
    matrix = np.delete(np.delete(matrix, min_arr, 0), min_arr, 1)
    matrix = np.vstack([matrix, new_matrix])
    new_matrix = np.append(new_matrix, [0]).reshape(index + 1, 1)
    pair= [matrix, new_matrix]
    matrix = np.hstack(pair)
    return w2, w1, min_arr, matrix


def nj(matrix, n, nodes_array):
    distance_matrix = {}
    for i in range(n):
        w2, w1, min_arr, matrix = limb(matrix, i)
        nodes_array.append(nodes_array[-1] + 1)
        fir_cons = nodes_array[min_arr[0]]
        sec_cons = nodes_array[min_arr[1]]
        if fir_cons not in distance_matrix:
            distance_matrix[nodes_array[min_arr[0]]] = []
        distance_matrix[nodes_array[min_arr[0]]].append([nodes_array[-1], round(w1, 3)])
        if sec_cons not in distance_matrix:
            distance_matrix[nodes_array[min_arr[1]]] = []
        pair = [nodes_array[-1], round(w2, 3)]
        distance_matrix[nodes_array[min_arr[1]]].append(pair)
        distance_matrix[nodes_array[-1]] = []
        pair = [nodes_array[min_arr[0]], round(w1, 3)]
        distance_matrix[nodes_array[-1]].append(pair)
        pair = [nodes_array[min_arr[1]], round(w2, 3)]
        distance_matrix[nodes_array[-1]].append(pair)
        nodes_array = np.array(nodes_array)
        nodes_array = np.delete(nodes_array, min_arr).tolist()
        if i == (n - 3):
            min1 = nodes_array[0]
            min2 = nodes_array[1]
            if min1 not in distance_matrix:
                distance_matrix[nodes_array[0]] = []
            if min2 not in distance_matrix:
                distance_matrix[nodes_array[1]] = []
            max_num = np.amax(matrix)
            pair = [nodes_array[1], round(max_num, 3)]
            distance_matrix[nodes_array[0]].append(pair)
            pair = [nodes_array[0], round(max_num, 3)]
            distance_matrix[nodes_array[1]].append(pair)
            return distance_matrix


input_file = open('input.txt', 'r')
lines = input_file.readlines()

n = int(lines[0])

dis_matrix = np.zeros(shape=(n, n))
nodes_array = [i for i in range(n)]

for i in range(n):
    lis = list(map(int, lines[1 + i].split()))
    # dis_matrix.append(list(lis))
    for j in range(n):
        dis_matrix[i][j] = int(lis[j])

res_dic = nj(dis_matrix, n, nodes_array)


final_dic = {}

i = 0

while True:

    if i in res_dic.keys():
        final_dic[i] = res_dic[i]
        i += 1
    else:
        break

output_file = open("output.txt", 'w')

for i in final_dic.keys():
    for j in final_dic[i]:
        output_file.write(str(i) + "->" + str(j[0]) + ":" + str(int(j[1])))
        output_file.write('\n')