import numpy as np
from math import inf


class FloydWarshall():
    def __init__(self, graph):
        self.graph = graph

    def print(self):
        return np.matrix(self.graph)

    def algorithm(self):
        rows = len(self.graph)

        for k in range(0, rows):
            for i in range(0, rows):
                for j in range(0, rows):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

    def print_shortest_path(self, i, j):
        if i >= len(self.graph) or j >= len(self.graph[0]):
            print("Index out of range")
            return
        if i == j:
            print(self.graph[i][j])
            return
        elif self.graph[i][j] == inf:
            print(f"No path from {i} to {j}")
            return
        else:
            self.print_shortest_path(i, self.graph[i][j])
            print(f"{j}->")

    def __str__(self):
        return str(np.matrix(self.graph))

