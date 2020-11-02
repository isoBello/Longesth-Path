# -*- coding: utf-8 -*-
# !/usr/bin/env pypy

import sys
import Graph
import PSO

from Graph import cities

G = Graph.Graph()


def input():  # Read file to construct the Graph
    global G

    with open(sys.argv[1], "r") as archive:
        lines = archive.readlines()
        for line in lines:
            edges = line.split()
            try:
                G.add_vertex(int(edges[0]))
                G.add_vertex(int(edges[1]))

                G.add_edge(int(edges[0]), int(edges[1]), int(edges[2]))
            except IndexError:
                break
    archive.close()


def main():
    global G

    input()
    matrix = cities(len(G.vertices) + 1, G)
    PSO.inicialize(G, matrix)


# Parameters to experimental analysis
def ants():
    return sys.argv[2]


def iterations():
    return sys.argv[3]


def evaporation():
    return sys.argv[4]


def Q():
    return sys.argv[5]


def alpha():
    return sys.argv[6]


def beta():
    return sys.argv[7]


def parameters():
    return int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), \
            float(sys.argv[7])


if __name__ == "__main__":
    # Read file, create graph, call PSO
    main()
