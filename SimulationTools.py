import IndependentCascadeTools as i
import GenerateGraphs as g
import pandas as pd
import itertools as it
import doctest

'''This module contains tools to run simulations.'''

def quick_test(mu, p, graphs):
    '''Return graphs that minimize expected number of infected nodes for
    given mu and p.'''
    lowest = 1
    for graph in graphs:
        exp_val = i.compute_infected_nodes(mu, p, graph)
        if exp_val < lowest:
            lowest = exp_val
            lowest_edges = graph.edges()
    result = (lowest_edges, lowest)
    print(result)

def simulation(graphs, granularity = 'low'):
    '''Return graphs that minimize the expected number of infected nodes
    in the independent cascade model under parameters mu = p = .1, .5, .9
    if granularity == low, parameters mu = p = .1, .3, .5, .7, .9
    if granularity == med, parameters mu = p = .1 - .9 if granularity == high.

    >>> graphs = g.all_graphs(4,3)
    >>> results = simulation(graphs)
    Winner for 0.1, 0.1 with probability 0.11429739999999988:  [(1, 2), (1, 3), (2, 4)]
    Winner for 0.1, 0.5 with probability 0.18099999999999994:  [(1, 2), (1, 3), (2, 3)]
    Winner for 0.1, 0.9 with probability 0.2258739999999999:  [(1, 2), (1, 3), (2, 3)]
    Winner for 0.5, 0.1 with probability 0.538125:  [(1, 2), (1, 3), (2, 4)]
    Winner for 0.5, 0.5 with probability 0.6875:  [(1, 2), (1, 3), (2, 3)]
    Winner for 0.5, 0.9 with probability 0.77675:  [(1, 2), (1, 3), (2, 3)]
    Winner for 0.9, 0.1 with probability 0.913014:  [(1, 2), (1, 3), (2, 3)]
    Winner for 0.9, 0.5 with probability 0.954:  [(1, 2), (1, 3), (2, 3)]
    Winner for 0.9, 0.9 with probability 0.973386:  [(1, 2), (1, 3), (2, 3)]
    '''
    results = []
    if granularity == 'low':
        p_vals = mu_vals = [.1,.5,.9]
    if granularity == 'med':
        p_vals = mu_vals = [.1,.3,.5,.7,.9]
    if granularity == 'high':
        p_vals = mu_vals = [.1, .2, .3, .4, .5, .6, .7, .8, .9]

    for mu, p in list(it.product(p_vals, mu_vals)):
        lowest = 1
        edges = []
        for graph in graphs:
            exp_val = i.compute_infected_nodes(mu, p, graph)
            if exp_val < lowest:
                lowest = exp_val
                lowest_edges = graph.edges()
        results.append((mu, p, lowest_edges, lowest))

    print_results(results)

    return results

def print_results(results):
    '''Print results.'''
    for result in results:
        print('Winner for {}, {} with probability {}: '.format(result[0],
        result[1], result[3]), result[2])




if __name__ == "__main__":
    doctest.testmod()
