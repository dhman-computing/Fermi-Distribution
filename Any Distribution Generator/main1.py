from support1 import n_dimensional_monte_carlo_integration as ndmci
from support1 import xy as f

xlimit = [[0, 1], [0, 1]]
N = 10**9

print(ndmci(f, xlimit, N))
