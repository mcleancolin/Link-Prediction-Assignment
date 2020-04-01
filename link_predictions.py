import pandas as pd
import numpy as np
import networkx as nx
import csv, random

# Loading in the file into a dictionary with the json library
def open_file():

    with open('train.txt', 'r') as f:
        lines = f.readlines()

    lines = [line.replace(' ', '\t') for line in lines]

    with open('train.txt', 'w') as f:
        f.writelines(lines)

    with open('train.txt') as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)

    data = []
    for row in d:
        data.append([ int(x) for x in row ])
    return data

def open_test_file():
    input = pd.read_csv('test-public.csv')
    return input

def genereate_test_edge_list(data):
    node_list_1 = []
    node_list_2 = []
    for i,j in data.iterrows():
        node_list_1.append(j[1])
        node_list_2.append(j[2])

    test_edge_list = pd.DataFrame({'node_1': node_list_1, 'node_2': node_list_2})
    print(test_edge_list.head())

    edge_tuples = []
    for index, row in test_edge_list.iterrows():
        edge_tuples.append((row['node_1'],row['node_2']))

    return edge_tuples

def generate_training_edge_list(content):
    node_list_1 = []
    node_list_2 = []
    for row in content:
        for connection in range(0,len(row)):
            if connection == 0:
                continue
            else:
                node_list_1.append(row[0])
                node_list_2.append(row[connection])

    training_edge_list = pd.DataFrame({'node_1': node_list_1, 'node_2': node_list_2})

    return training_edge_list

def create_graph(edge_list):
    graph = nx.from_pandas_edgelist(edge_list, "node_1", "node_2", create_using=nx.Graph())
    n = graph.number_of_nodes()
    m = graph.number_of_edges()
    print("Number of nodes :", str(n))
    print("Number of edges :", str(m))
    print("Number of connected components :" + str(nx.number_connected_components(graph)))
    return graph

def trim_graph(graph):
    edge_subset = random.sample(graph.edges(), int(0.10 * graph.number_of_edges()))
    graph_train = graph.copy()
    graph_train.remove_edges_from(edge_subset)
    return edge_subset, graph_train

def jaccard_coefficient(graph, test_edge_list):
    predictions_preferential = nx.jaccard_coefficient(graph, test_edge_list)

    scores = {}
    count = 0

    for u in predictions_preferential:


        #print(u)
        count += 1

        #scores[(u,v)] = p
    print(count)

    print("scores/labels calculated")
    return scores


if __name__ == "__main__":
    test_data = open_test_file()
    test_edge_list = genereate_test_edge_list(test_data)

    training_data = open_file()
    training_edge_list = generate_training_edge_list(training_data)
    graph = create_graph(training_edge_list)

    scores = jaccard_coefficient(graph, test_edge_list)
