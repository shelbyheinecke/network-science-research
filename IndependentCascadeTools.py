import networkx as nx
import itertools as it
import time
import random
import doctest

'''This module provides tools for computing the expected number of infected
nodes in the independent cascade model of infection.'''

#CREDIT: Stackoverflow, contributed by user hughdbrown.
def powerset(s):
    '''Return the set of all subsets of set s.'''
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

def compute_infected_nodes(mu, p, graph):
    '''Compute the expected number of infected nodes under the
    independent cascade model of infection spread.

    >>> test_nodes = [1,2,3,4]
    >>> test_edges = [(1,2),(2,3),(3,4)]
    >>> graph = nx.Graph()
    >>> graph.add_nodes_from(test_nodes)
    >>> graph.add_edges_from(test_edges)
    >>> compute_infected_nodes(.2,.5,graph)
    0.3527999999999999
    '''
    #generate the edges of all subgraphs possible
    subgraphs_powerset = list(powerset(graph.edges()))
    original_num_edges = len(graph.edges())
    nodes = graph.nodes()

    nodes_and_connected_components = prob_connected_comp_size(subgraphs_powerset,
    nodes, original_num_edges, p)

    #compute the sum of the expected value over all nodes
    exp_val = 0
    for node in nodes:
        sum_over_components = 0
        for component_size in range(len(nodes_and_connected_components[node])):
            sum_over_components += (((1 - mu)**(component_size+1))*
            nodes_and_connected_components[node][component_size])
        exp_val += sum_over_components

    #compute the objective function = expected fraction of infected nodes
    obj = 1 - ((exp_val)/(len(nodes)))

    return obj

def prob_connected_comp_size(subgraphs_powerset, nodes, original_num_edges, p):
    '''Return dictionary with KEY each node and VALUE a list indicating
    the probability that the node is contained in a component size of
    1 to len(nodes).
    '''
    nodes_and_connected_components = {}
    for node in nodes:
        nodes_and_connected_components[node] = [0]*(len(nodes))

    #for each edgeset, generate a graph, compute the probability of obtaining
    #that graph, and compute the size of the connected components for each
    #vertex of the graph and add the graph probability to the appropriate count.
    new_graph = nx.Graph()
    new_graph.add_nodes_from(nodes)
    conn_comp = nx.node_connected_component
    for i in range(len(subgraphs_powerset)):
        new_edges = subgraphs_powerset[i]
        num_edges = len(new_edges)
        new_graph.add_edges_from(new_edges)
        subgraph_prob = p**(num_edges)*(1-p)**(original_num_edges - num_edges)
        for node in nodes:
            size = len(conn_comp(new_graph, node))
            nodes_and_connected_components[node][size-1] += subgraph_prob
        new_graph.remove_edges_from(new_edges)

    return nodes_and_connected_components


if __name__ == "__main__":
    doctest.testmod()
