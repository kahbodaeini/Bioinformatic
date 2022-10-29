def limb_length_linear(n, j, d):

    i = (j + 1) % n
    k = (j + 2) % n
    min_len = (d[i][j] + d[j][k] - d[i][k]) / 2
    for k in range(n):
        if i == j or k == j:
            continue
        curr_len = (d[i][j] + d[j][k] - d[i][k]) / 2
        min_len = min(min_len, curr_len)
    return min_len


def additive_phylogeny(n, d):

    def find_path(i, j):
        visited = [None] * (max(adj.keys()) + 1)

        def dfs(path):
            for (v, w) in adj[path[-1][0]]:
                if visited[v]:
                    continue
                visited[v] = True
                pathlen = path[-1][1] + w
                npath = path[:]
                npath.append((v, pathlen))
                if v == j:
                    return npath
                result = dfs(npath)
                if result is not None:
                    return result
            return

        return dfs([(i, 0)])

    def add_leaf(leaf, i, j, x, w):
        path = find_path(i, j)
        parent = None
        for k in range(len(path) - 1):
            if path[k][1] == x:
                parent = path[k][0]
                break
            if path[k][1] < x < path[k + 1][1]:
                u = path[k][0]
                v = path[k + 1][0]
                w0 = path[k + 1][1] - path[k][1]
                w1 = x - path[k][1]
                w2 = w0 - w1

                parent = max(list(adj.keys()) + [n - 1]) + 1

                adj[u].remove((v, w0))
                adj[v].remove((u, w0))
                adj[parent] = []

                adj[u].append((parent, w1))
                adj[parent].append((u, w1))

                adj[v].append((parent, w2))
                adj[parent].append((v, w2))

                break
        assert parent is not None

        adj.setdefault(leaf, []).append((parent, w))
        adj[parent].append((leaf, w))
        return

    def find_condition(d, l):
        # (i,l,k) ← three leaves such that
        # Di,k = Di,l + Dl,k
        # i < k < l
        for i in range(l):
            for k in range(i + 1, l):
                if d[i][k] == d[i][l] + d[l][k]:
                    return i, k
        assert 0
        return

    def recursive(nn):
        if nn == 2:
            return
        limb = limb_length_linear(nn, nn - 1, d[:nn][:nn])
        for j in range(nn - 1):
            d[nn - 1][j] -= limb
            d[j][nn - 1] -= limb
        (i, k) = find_condition(d, nn - 1)
        x = d[i][nn - 1]
        recursive(nn - 1)
        add_leaf(nn - 1, i, k, x, limb)
        return

    adj = {0: [(1, d[0][1]), ], 1: [(0, d[1][0]), ]}
    recursive(n)
    return adj


input_file = open('input.txt', 'r')
lines = input_file.readlines()

n = int(lines[0])

adj_matrix = []

for i in range(n):
    lis = map(int, lines[1 + i].split())
    adj_matrix.append(list(lis))

res_dic = additive_phylogeny(n, adj_matrix)

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


