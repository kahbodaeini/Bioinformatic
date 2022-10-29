class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


input_file = open('input.txt', 'r')
lines = input_file.readlines()

n = int(lines[0])

adj_dic = {}


def bfs(s):
    dist = dict()
    q = Queue()
    dist[s] = 0
    q.enqueue(s)
    while not q.isEmpty():
        currNode = q.dequeue()
        for node, weight in adj_dic[currNode]:
            if not node in dist:
                dist[node] = dist[currNode] + weight
                if node < n:
                    distMatrix[s][node] = dist[node]
                q.enqueue(node)


for i in range(1, len(lines)):
    lis = lines[i].split('->')
    l = lis[1].split(':')
    if not int(lis[0]) in adj_dic:
        adj_dic[int(lis[0])] = []
    adj_dic[int(lis[0])].append((int(l[0]), int(l[1])))

distMatrix = [[0] * n for _ in range(n)]

for i in range(n):
    bfs(i)

output_file = open('output.txt', 'w')

for d in distMatrix:
    output_file.write(' '.join([str(i) for i in d]))
    output_file.write('\n')

