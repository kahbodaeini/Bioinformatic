from collections import defaultdict as dict


def find_node_neighbors(dictionary, parent_node, current_node):
    difference = parent_node.length - current_node.length
    parent_node_pair = (parent_node.number, difference)
    current_node_pair = (current_node.number, difference)
    dictionary[parent_node.number].append(current_node_pair)
    dictionary[current_node.number].append(parent_node_pair)


class Cluster:
    def __init__(self, number, length, nodes):
        self.number = number
        self.length = length
        self.nodes = nodes

    def compute_distance_with_other_clusters(self, cluster, adj):
        sum_of_distances = sum(int(adj[i][j]) for i in self.nodes for j in cluster.nodes)
        sum_of_distances /= float(len(self.nodes))
        sum_of_distances /= len(cluster.nodes)
        return sum_of_distances


def merge_clusters(first_cluster, second_cluster, number, length):
    number_of_points1 = first_cluster.nodes
    number_of_points2 = second_cluster.nodes
    new_number_of_nodes = number_of_points1 + number_of_points2
    new_cluster = Cluster(number, length, new_number_of_nodes)
    return new_cluster


def find_neighbor_cluster(all_clusters, clusters, adj):
    new_clusters = []
    for first_cluster in clusters:
        for second_cluster in clusters:
            if first_cluster != second_cluster:
                pair = (first_cluster, second_cluster)
                new_clusters.append(pair)
    first_cluster, second_cluster = min(new_clusters, key=lambda node: all_clusters[node[0]].
                                        compute_distance_with_other_clusters(all_clusters[node[1]], adj))
    first_cluster = all_clusters[first_cluster]
    second_cluster = all_clusters[second_cluster]
    return first_cluster, second_cluster


def fill_adjacency_matrix(new_cluster, all_clusters, adj):
    distances = []
    size = len(adj)
    for cluster in all_clusters:
        new_c = new_cluster.compute_distance_with_other_clusters(cluster, adj)
        distances.append(new_c)
    for i in range(size):
        adj[i].append(distances[i])
    new_element = distances + [0]
    adj.append(new_element)


def implement_upgma(adj, n):
    all_clusters = []
    arr = []
    for number in range(n):
        c = Cluster(number, length=0, nodes=[number])
        all_clusters.append(c)
    for number in range(n):
        arr.append(number)
    clusters = set(arr)
    dictionary = dict(list)
    current_number = n
    while len(clusters) >= 2:
        first_cluster, second_cluster = find_neighbor_cluster(all_clusters, clusters, adj)
        length = first_cluster.compute_distance_with_other_clusters(second_cluster, adj) / 2
        new_cluster = merge_clusters(first_cluster, second_cluster, current_number, length)
        find_node_neighbors(dictionary, new_cluster, first_cluster)
        find_node_neighbors(dictionary, new_cluster, second_cluster)
        clusters.remove(first_cluster.number)
        clusters.remove(second_cluster.number)
        clusters.add(new_cluster.number)
        all_clusters.append(new_cluster)
        fill_adjacency_matrix(new_cluster, all_clusters, adj)
        current_number += 1
    return dictionary


input_file = open('input.txt', 'r')
lines = input_file.readlines()

n = int(lines[0])
adj_matrix = []

for i in range(n):
    lis = lines[1 + i].split()
    adj_matrix.append(lis)


upgma = implement_upgma(adj_matrix, n)

final_dic = {}

i = 0

while True:

    if i in upgma.keys():
        final_dic[i] = upgma[i]
        i += 1
    else:
        break


output_file = open("output.txt", 'w')
for i in final_dic.keys():
    for j in final_dic[i]:
        output_file.write(str(i) + "->" + str(j[0]) + ":" + str(int(j[1])))
        output_file.write('\n')
