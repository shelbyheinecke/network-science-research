from mpi4py import MPI
import GenerateGraphs as g
import SimulationTools as s

'''MPI script to distribute computations over many cores (multiple nodes).'''

comm = MPI.COMM_WORLD
cores = comm.Get_size()
rank = comm.Get_rank()

graphs = g.all_graphs(8,7)
num_graphs = len(graphs)
graphs_per_core = num_graphs//cores
graphs_this_core = graphs[graphs_per_core*rank:graphs_per_core*(rank+1)]

s.simulation(graphs_this_core)
