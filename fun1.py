from mpi4py import MPI  
# Message passing interface
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()
print(f"Hello from process {rank} out of {size} processes")
print(f"Running on {name}")
if rank == 0:
    print("This is the master process.")
if rank == size - 1:
    print("This is the last process.")