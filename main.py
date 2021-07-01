from floyd_warshall import *
from fw_test import *
from floyd_warshall_nested import *
from math import inf


graph = [
    [0, 1, inf, inf, inf, inf],
    [inf, 0, 3, inf, 2, inf],
    [inf, 5, 0, 2, inf, inf],
    [inf, inf, inf, 0, 1, 7],
    [inf, inf, 4, inf, 0, inf],
    [inf, inf, inf, 3, inf, 0]
]

graph2 = [
    [0, 1, inf, inf],
    [inf, 0, 2, inf],
    [inf, 3, 0, 1],
    [inf, 4, inf, 0]
]

# ----------------nested-----------
# alg = FloydWarshallNested(graph2)
#
# print(alg.matrix[0][0].pred)
#
# print(f"Graph matrix:\n{alg}\n")
# # alg.algorithm()
# print(f"Shortest path matrix:\n{alg}\n")



# alg.print_shortest_path(1, 3)

#--------------------normal--------------
# alg = FloydWarshall(graph)
#
# print(f"Graph matrix:\n{alg}\n")
# alg.algorithm()
# print(f"Shortest path matrix:\n{alg}\n")
#
# alg.print_shortest_path(0, 1)


# -----------test-----------------
alg = FloydWarshallTest(graph)
print(f"Graph matrix:\n{alg}\n")
alg.algorithm()
print(f"Shortest paths matrix:\n{alg}\n")

print(alg.print_shortest_path(4, 1))
