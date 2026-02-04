from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
# Synchronize before timing
comm.Barrier()
start_time = MPI.Wtime()

# --------- Communication ----------
if rank == 0:
    data_dict = {'Jan': 1, 'Feb': 2}
    comm.send("Hi", dest=1, tag=1)
    comm.send(data_dict, dest=2, tag=2)

elif rank == 1:
    data = comm.recv(source=0, tag=1)
    print("Rank 1 received:", data)

elif rank == 2:
    data = comm.recv(source=0, tag=2)
    print("Rank 2 received:", data)

# Synchronize after work
comm.Barrier()
end_time = MPI.Wtime()

# --------- Timing & Performance ----------
parallel_time = end_time - start_time

# Assume serial time = time taken by rank 0 alone
serial_time = comm.bcast(parallel_time if rank == 0 else None, root=0)

speedup = serial_time / parallel_time
efficiency = (speedup / size) * 100

if rank == 0:
    print("\nParallel Time:", parallel_time)
    print("Speedup:", speedup)
    print("Efficiency:", efficiency, "%")
