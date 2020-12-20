import random


class Node:
    colors = []

    @classmethod
    def set_number_of_colors(cls, number_of_colors):
        cls.colors = range(number_of_colors)

    def __init__(self):
        self.color = random.choice(self.colors)

    def mutate(self):
        self.color = random.choice(self.colors)
