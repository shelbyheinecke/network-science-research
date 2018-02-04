import IndependentCascadeTools as i
import networkx as nx

'''Tools for computing the expected fraction of infected nodes using
approximations (sampling).'''


def compute_infected_nodes_approx(mu, p, graph, percent_of_subsets):
    '''Compute num of infected nodes by sampling the powerset of the target graph.'''
    subgraphs_with_probs = randomly_sample_subgraphs(p, graph, percent_of_subsets)

    #for each node create a list that sums the probabilities of subgraphs that yield connected components equal to
    #the index minus 1 of the list
    nodes = graph.nodes()
    nodes_and_connected_components = {}
    for node in nodes:
        nodes_and_connected_components[node] = [0]*(len(nodes))

    normalizing_factor = sum(subgraphs_with_probs.values())

    subgraph = nx.Graph()
    subgraph.add_nodes_from(nodes)
    for edgeset in subgraphs_with_probs:
        subgraph.add_edges_from(edgeset)
        for node in nodes:
            size = len(nx.node_connected_component(subgraph, node))
            nodes_and_connected_components[node][size-1] += (subgraphs_with_probs[subgraph]/normalizing_factor)
        subgraph.remove_edges_from(edgeset)

    #compute the sum of the expected value over all nodes
    approx_exp_val = 0
    for node in nodes:
        sum_over_components = 0
        for component_size in range(len(nodes_and_connected_components[node])):
            sum_over_components += (((1 - mu)**(component_size+1))*
            nodes_and_connected_components[node][component_size])
        approx_exp_val += sum_over_components

    approx_obj = 1 - ((approx_exp_val)/(len(nodes)))

    return approx_obj


def randomly_sample_subgraphs(p, graph, percent_of_subsets):
    '''Randomly sample subgraphs. Return edge sets and probabilities.'''
    nodes = graph.nodes()
    edges = graph.edges()
    subgraphs_with_probs = {}
    iterations = int(percent_of_subsets * 2**(len(edges)))
    for i in range(iterations):
        edgeset = []
        probability_of_occurence = 1
        for edge in edges:
            random_value = random.randint(0,1)
            if random_value == 0:
                edgeset.append(edge)
                probability_of_occurence *= p
            else:
                probability_of_occurence *= (1-p)
        subgraphs_with_probs[edgeset] = probability_of_occurence
    return subgraphs_with_probs

def find_counterexamples(mu, p, percent_of_subsets, reference_graph, graphs):
    '''Find graphs whose number of expected infected nodes is smaller
    than that of a reference graph. Uses approximation to find candidates
    and computes exact expected value on candidates.
    '''
    reference_val = i.compute_infected_nodes(mu, p, reference_graph)
    counterexamples = []

    for graph in graphs:
        if (compute_infected_nodes_approx(mu, p, graph, percent_of_subsets)
        <= reference_val):
            if i.compute_infected_nodes(mu, p, graph) <= reference_val:
                counterexamples.append(graph)
    return counterexamples
