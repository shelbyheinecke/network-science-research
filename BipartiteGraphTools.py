import IndependentCascadeTools as i

LEFT = ['a','b','c','d','e','f','g','h','i','j']
RIGHT = [1,2,3,4,5,6,7,8,10]

def random_bipartite_graph(nodes_per_side):
    '''Generate balanced bipartite graph uniformly at random. Supports graphs
    with at most 10 nodes per side.
    '''
    random_graph = nx.Graph()
    edgeset = []
    right_nodes = RIGHT[:nodes_per_side]
    left_nodes = LEFT[:nodes_per_side]
    edges = [(a,b) for a in right_nodes for b in left_nodes]

    for edge in edges:
            random_value = random.randint(0,1)
            if random_value == 0:
                edgeset.append(edge)

    random_graph.add_nodes_from(right_nodes, bipartite = 0)
    random_graph.add_nodes_from(left_nodes, bipartite = 1)
    random_graph.add_edges_from(edgeset)

    return random_graph

def random_half_reg_bipartite(nodes_per_side, d):
    '''Generate balanced d-half regular bipartite graph uniformly at random.
    Supports graphs with at most 10 nodes per side.
    '''
    random_graph = nx.Graph()
    edges = []
    right_nodes = RIGHT[:nodes_per_side]
    left_nodes = LEFT[:nodes_per_side]
    edges_per_node = [[(a,b) for a = right_nodes[i] for b in left_nodes] for
    i in range(1, nodes_per_side + 1)]

    for edge_set in edges_per_nodes:
        rand = range(1, nodes_per_side + 1)
        for i in range(d):
            random_value = random.choice(rand)
            edges.append(edge_set[random_value])
            rand.remove(random_value)

    random_graph.add_nodes_from(right_nodes, bipartite = 0)
    random_graph.add_nodes_from(left_nodes, bipartite = 1)
    random_graph.add_edges_from(edges)

    return random_graph
