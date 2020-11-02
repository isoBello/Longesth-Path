# -*- coding: utf-8 -*-
# !/usr/bin/env pypy

from collections import OrderedDict

# Class that represent the ants in the Ant Colony Algorithm.
# In this class, we can control the trail from each ant, besides the "miles" each ant walked.
# We can control the vertices she visited eather.


class Ant:
    def __init__(self, tour_size):
        self.trail_size = tour_size
        self.trail = []
        self.visited = [False] * tour_size

    def visit(self, city):
        try:
            self.trail.append(city)
            self.visited[city] = True
        except (IndexError, TypeError) as e:
            return False

    def isvisited(self, city):
        return self.visited[city]

    def mileswalked(self, graph):
        length = 0.0
        i = 0

        # self.trail = list(OrderedDict.fromkeys(self.trail))

        while True:
            try:
                length += graph[self.trail[i]][self.trail[i + 1]]
                i += 1
            except IndexError:
                break

        return length

    def clearvisits(self):
        self.trail = []
        self.visited = [False] * self.trail_size
