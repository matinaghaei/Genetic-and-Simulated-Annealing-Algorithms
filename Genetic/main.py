from population import Population
from chromosome import Chromosome
from node import Node

if __name__ == '__main__':
    number_of_nodes = int(input("number of nodes: "))
    number_of_neighbours = int(input("number of neighbours: "))
    print("enter neighbours:")
    neighbours = []
    for i in range(number_of_neighbours):
        arr = input()
        neighbours.append(list(map(int, arr.split())))
    number_of_generations = int(input("number of generations: "))
    population_size = int(input("population size: "))
    tournament_size = int(input("tournament size: "))
    mutation_rate = float(input("mutation rate: "))

    Chromosome.set_number_of_nodes(number_of_nodes)
    Chromosome.set_neighbours(neighbours)
    Node.set_number_of_colors(3)
    population = Population(population_size, tournament_size, mutation_rate)
    population.generate(number_of_generations)
    population.print_answer()
    population.show_statistics()
