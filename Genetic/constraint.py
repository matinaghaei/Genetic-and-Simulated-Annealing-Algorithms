class Constraint:

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def check(self):
        return self.node1.color != self.node2.color
