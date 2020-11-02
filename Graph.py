# -*- coding: utf-8 -*-
# !/usr/bin/env pypy

from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, source, dest, weight):
        self.edges[source].append(dest)
        self.weights[(source, dest)] = weight

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def print_graph(self):
        # Function just to see if the algorithm is creating the right graph
        for i in range(1, len(self.vertices)):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            for vertex in self.edges[i]:
                print(" -> {}".format(vertex), end="")
            print(" \n")


def cities(vertices, G):
    # abs(int(uniform(0, 100)) + 1)
    cities_matrix = [[-1 for _ in range(vertices + 1)] for _ in range(vertices + 1)]
    for k, v in G.edges.items():
        for w in v:
            cities_matrix[k][w] = G.weights[(k, w)]
    return cities_matrix
