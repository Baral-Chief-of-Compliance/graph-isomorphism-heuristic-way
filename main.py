import sys
from evr_algorithm import algorithm
import networkx as nx
import matplotlib.pyplot as plt


graph_1 = {}
list_of_nodes_1 = []
graph_nx_1 = nx.Graph()

graph_2 = {}
list_of_nodes_2 = []
graph_nx_2 = nx.Graph()

counter = 0


def enter_matrix(n,graph,graph_nx,list_of_nodes,number_graph):
    for i in range(n):
        key = input(f"Название {i + 1}-ой вершины в {number_graph}-ом графе: ")
        list_of_nodes.append(key)
        graph_nx.add_node(key)
        graph[key] = set()

    for key in graph:
        value = input(f"\n\nВведите вершины, которые связаны с вершиной {key}:")
        for v in value:
            graph_nx.add_edge(key, v)
        graph[key] = set(value)
        if len(graph[key]) >= n:
            print("Количество соединенных вершин не может быть равно или больше количеству вершин в графе")
            sys.exit()


def create_adj_matrix(n, graph, list_of_nodes, adj_m):
    for i in range(n):
        nodes = graph[list_of_nodes[i]]
        for j in range(n):
            if list_of_nodes[j] in nodes:
                adj_m[i][j] = 1
            else:
                adj_m[i][j] = 0

    return adj_m


n_1 = int(input("Введите число вершин в 1-ом графе: "))
adj_m_1 = [[0]*n_1 for i in range(n_1)]

enter_matrix(n_1, graph_1, graph_nx_1, list_of_nodes_1, 1)

print('\n\nПолучившейся 1-ый граф:')
print(graph_1)

adj_m_1 = create_adj_matrix(n_1, graph_1, list_of_nodes_1, adj_m_1)
print(adj_m_1)

plt.figure("1-ый Граф")
nx.draw_circular(graph_nx_1, node_color='red', node_size=1000, with_labels = True)


'''
Для второго графа
'''


n_2 = int(input("\n\nВведите число вершин во 2-ом графе: "))
adj_m_2 = [[0]*n_2 for i in range(n_2)]

enter_matrix(n_2, graph_2, graph_nx_2, list_of_nodes_2, 2)

print('\n\nПолучившейся 2-ый граф:')
print(graph_2)

adj_m_2 = create_adj_matrix(n_2, graph_2, list_of_nodes_2, adj_m_2 )
print(adj_m_2)

algorithm(adj_m_1,adj_m_2, counter)

plt.figure('2-ой Граф')
nx.draw_circular(graph_nx_2, node_color='red', node_size=1000, with_labels = True)

plt.show()