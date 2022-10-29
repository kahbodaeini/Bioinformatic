def read_file():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        dis_matrix = []
        for line in lines[1:]:
            split_line = list(map(int, line.strip().split()))
            dis_matrix.append(list(split_line))

    return dis_matrix, n


def limb_length(n, j, d):

    i = (j + 1) % n
    k = (j + 2) % n
    min_len = (int(d[i][j]) + int(d[j][k]) - int(d[i][k])) / 2

    for i in range(n):
        for k in range(i + 1, n):
            if i == j or k == j:
                continue
            curr_len = (int(d[i][j]) + int(d[j][k]) - int(d[i][k])) / 2
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
                pathـlen = path[-1][1] + w
                n_path = path[:]
                n_path.append((v, pathـlen))
                if v == j:
                    return n_path
                result = dfs(n_path)
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
        for i in range(l):
            for k in range(i + 1, l):
                if d[i][k] == d[i][l] + d[l][k]:
                    return i, k

    def recursive(nn):
        if nn == 2:
            return
        limb = limb_length(nn, nn - 1, d[:nn][:nn])
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


def tree_tostring(T):
    s = ''
    for u in sorted(T):
        vw = T[u]
        for (v, w) in vw:
            s += str(u) + '->' + str(v) + ':' + str(int(w)) + '\n'
    return s


if __name__ == "__main__":
    additive_matrix, n = read_file()
    # d = np.array([[0, 13, 21, 22], [13, 0, 12, 13], [21, 12, 0, 13], [22, 13, 13, 0]])
    # adjacency = additive_phylogeny(4, d)
    dic = additive_phylogeny(n, additive_matrix)

    output = {}

    i = 0

    while True:
        if i in dic.keys():
            output[i] = dic[i]
            i += 1
        else:
            break
    print(tree_tostring(output))


