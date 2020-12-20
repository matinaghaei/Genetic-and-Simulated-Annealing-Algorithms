import copy
import random

from constraint import Constraint
from node import Node


class State:
    number_of_nodes = 0
    neighbours = []

    @classmethod
    def set_number_of_nodes(cls, number_of_nodes):
        cls.number_of_nodes = number_of_nodes

    @classmethod
    def set_neighbours(cls, neighbours):
        cls.neighbours = neighbours

    def __init__(self):
        self.nodes = []
        self.initialize_nodes()
        self.constraints = []
        self.initialize_constraints()

    def add_node(self, node):
        self.nodes.append(node)

    def initialize_nodes(self):
        for i in range(self.number_of_nodes):
            self.add_node(Node())

    def initialize_constraints(self):
        for pair in self.neighbours:
            self.add_constraint(Constraint(self.nodes[pair[0]], self.nodes[pair[1]]))

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def get_fitness(self):
        fitness = 0
        for c in self.constraints:
            if c.check():
                fitness += 1
        return fitness / len(self.constraints)

    def get_neighbour(self):
        new_state = copy.deepcopy(self)
        new_state.nodes[random.randrange(0, self.number_of_nodes)].mutate()
        return new_state

    def print(self):
        for i in range(self.number_of_nodes):
            print("node #{} color: {}".format(i, self.nodes[i].color))
