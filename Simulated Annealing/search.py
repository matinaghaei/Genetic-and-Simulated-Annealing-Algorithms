import math
import random

from state import State


class Search:

    def __init__(self, scheduling_method, alpha, initial_time):
        self.initial_time = self.time = initial_time
        self.step = 0
        self.scheduling_method = scheduling_method
        self.alpha = alpha
        self.state = State()
        self.fitness = self.state.get_fitness()

    def next(self):
        while True:
            next_state = self.state.get_neighbour()
            delta_e = next_state.get_fitness() - self.fitness
            if delta_e > 0 or random.random() < math.exp(delta_e / self.time):
                return next_state

    def search(self):
        while self.state.get_fitness() != 1 and self.time != 0:
            self.state = self.next()
            self.fitness = self.state.get_fitness()
            self.schedule()
        self.state.print()
        print("fitness: {}".format(self.fitness))

    def schedule(self):
        self.step += 1
        if self.scheduling_method == 0:
            self.time = self.time * self.alpha
        elif self.scheduling_method == 1:
            self.time = self.initial_time / (1 + self.alpha * math.log2(1 + self.step))
        elif self.scheduling_method == 2:
            self.time = self.initial_time / (1 + self.alpha * self.step)
        elif self.scheduling_method == 3:
            self.time = self.initial_time / (1 + self.alpha * self.step * self.step)
