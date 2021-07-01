import numpy as np
from math import inf


class Data:
    def __init__(self):
        self.distance = inf
        self.pred = '-'


class FloydWarshallNested:
    def __init__(self, graph):
        self.graph = graph

        rows = len(graph)
        element = Data()
        self.matrix = [[element]*rows]*rows

        for row in range(0, rows):
            for col in range(0, rows):
                if row != col and self.graph[row][col] != inf:
                    print(f"row: {row}")
                    print(f"col: {col}")
                    self.matrix[row][col].pred = row
                elif row == col:
                    self.matrix[row][col].distance = 0

    def print(self):
        return np.matrix(self.graph)

    def algorithm(self):
        rows = len(self.graph)

        for k in range(0, rows):
            for i in range(0, rows):
                for j in range(0, rows):
                    current_cost = self.graph[i][j]
                    new_cost = self.graph[i][k] + self.graph[k][j]
                    self.graph[i][j] = min(current_cost, new_cost)
                    self.matrix[i][j].distance = min(current_cost, new_cost)

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
            print(f"{self.matrix[i][j].pred}->")
            self.print_shortest_path(i, self.matrix[i][j].pred)


    def __str__(self):
        return str(np.matrix(self.graph))

