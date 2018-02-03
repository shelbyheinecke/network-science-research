import networkx as nx
import itertools as it
import random

'''This module contains tools to autogenerate graphs that can be used
in simulations.'''

def all_nodes(num_nodes):
    '''Generate list of num nodes.'''
    return [node for node in range(1,num_nodes+1)]

def all_edges(num_nodes):
    '''Return list of all possible edges.'''
    return [(x,y) for x in range(1,num_nodes+1) for y in range(x+1,num_nodes+1)]

def create_graph(node_list, edges_list):
    '''Create a graph object.'''
    new_graph = nx.Graph()
    new_graph.add_nodes_from(node_list)
    new_graph.add_edges_from(edges_list)
    return new_graph

def all_graphs(num_nodes, num_edges):
    '''Generate list of all possible graphs on n nodes and m edges.'''
    nodes = all_nodes(num_nodes)
    all_possible_edges = all_edges(num_nodes)
    edge_sets = list(it.combinations(all_possible_edges, num_edges))
    graphs = []
    for edges in edge_sets:
        graphs.append(create_graph(nodes, edges))
    return graphs

def generate_random_graphs(num_nodes, num_edges, num_graphs):
    '''Generate list of random graphs.'''
    graph_set = []

    nodes = all_nodes(num_nodes)
    all_possible_edges = all_edges(num_nodes)

    for i in range(num_graphs):
        new_edge_list = pick_random_edges(all_possible_edges, num_edges)
        graph_set.append(create_graph(nodes, new_edge_list))

    return graph_set

def pick_rand_edges(edges, num_rand_edges):
    '''Pick edges uniformly at random.'''
    new_edge_set = []
    for i in range(num_rand_edges):
        new_edge = random.choice(edges)
        while new_edge in new_edge_set:
            new_edge = random.choice(edges)
        new_edge_set.append(new_edge)
    return new_edge_set
