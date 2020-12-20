from node import Node
from constraint import Constraint
import random
import copy


class Chromosome:
    number_of_nodes = 0
    neighbours = []

    @classmethod
    def set_number_of_nodes(cls, number_of_nodes):
        cls.number_of_nodes = number_of_nodes

    @classmethod
    def set_neighbours(cls, neighbours):
        cls.neighbours = neighbours

    @classmethod
    def crossover(cls, chr1, chr2):
        cut = random.randrange(0, cls.number_of_nodes)
        new_nodes = chr1.nodes[0:cut]
        new_nodes.extend(chr2.nodes[cut:cls.number_of_nodes])
        chromosome = cls(copy.deepcopy(new_nodes))
        chromosome.initialize_constraints()
        return chromosome

    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
        self.constraints = []

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

    def mutate_nodes(self, number_of_mutations):
        for node in random.sample(self.nodes, number_of_mutations):
            node.mutate()

    def print(self):
        for i in range(self.number_of_nodes):
            print("node #{} color: {}".format(i, self.nodes[i].color))
