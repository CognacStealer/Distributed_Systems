from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 3:
    if rank == 0:
        print("Run with at least 3 processes")
    MPI.Finalize()
    exit()

if rank == 0:
    comm.send("Hi", dest=1)
    comm.send({'Jan': 1, 'Feb': 2}, dest=2)

elif rank == 1:
    data = comm.recv(source=0)
    print("Rank 1 received:", data)

elif rank == 2:
    data = comm.recv(source=0)
    print("Rank 2 received:", data)
