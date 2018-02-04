import multiprocessing
import IndependentCascadeTools as i
import SimulationTools as s

'''Tools for splitting computation across many cores (single node).'''

def partition(mu, p, graphs, num_cores, core):
    '''Generate partition functions for multiprocessing.'''
    graphs_per_core = graphs//num_cores
    graph_partition = graphs[graphs_per_core*core:graphs_per_core*(core+1)]
    s.quick_test(mu, p, graph_partition)


if __name__ == '__main__':
    '''Start processes.'''
    mu, p, graphs, num_cores = sys.argv[1:4]
    for i in range(num_cores):
        p = multiprocessing.Process(target=partition,
        args = (mu, p, graphs, num_cores, i))
        p.start()
