from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("Hello from process",rank)

if rank == 0:
   a = comm.recv(source = 1)
   print("This is the message I got:", a)   
if rank == 1:
    comm.send("Guten Abend", dest = 0)
if rank == 4:
    data = comm.recv(source=0)
    print("Data received:", data)
if rank == 8:
    data1 = comm.recv(source=1)
    print("Data received:", data1)
