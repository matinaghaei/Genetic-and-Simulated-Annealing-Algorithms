from chromosome import Chromosome
import random
import matplotlib.pyplot as plt


class Population:

    @staticmethod
    def find_best(chromosomes):
        best = None
        best_fitness = None
        for c in chromosomes:
            fitness = c.get_fitness()
            if best is None or fitness > best_fitness:
                best = c
                best_fitness = fitness
        return best, best_fitness

    @staticmethod
    def find_worst(chromosomes):
        worst = None
        worst_fitness = None
        for c in chromosomes:
            fitness = c.get_fitness()
            if worst is None or fitness < worst_fitness:
                worst = c
                worst_fitness = fitness
        return worst, worst_fitness

    @staticmethod
    def find_average(chromosomes):
        sum_fitness = 0
        for c in chromosomes:
            sum_fitness += c.get_fitness()
        return sum_fitness / len(chromosomes)

    def __init__(self, population_size, tournament_size, mutation_rate):
        self.generation = 0
        self.best_fitnesses = []
        self.worst_fitnesses = []
        self.average_fitnesses = []
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.mutation_rate = mutation_rate
        self.chromosomes = []
        for i in range(population_size):
            chromosome = Chromosome()
            chromosome.initialize_nodes()
            chromosome.initialize_constraints()
            self.chromosomes.append(chromosome)
        self.update_statistics()

    def generate(self, number_of_generations):
        for i in range(number_of_generations):
            self.select_chromosomes()
            self.crossover_chromosomes()
            self.mutate_chromosomes()
            self.generation += 1
            self.update_statistics()
            if self.goal_test():
                break

    def select_chromosomes(self):
        random.shuffle(self.chromosomes)
        selected = []
        while len(self.chromosomes) > 0:
            tournament = []
            while len(self.chromosomes) > 0 and len(tournament) < self.tournament_size:
                tournament.append(self.chromosomes.pop())
            selected.append(self.find_best(tournament)[0])
        self.chromosomes = selected

    def crossover_chromosomes(self):
        children = []
        while len(children) < self.population_size:
            parents = random.sample(self.chromosomes, 2)
            children.append(Chromosome.crossover(parents[0], parents[1]))
        self.chromosomes = children

    def mutate_chromosomes(self):
        total_mutations = int(self.mutation_rate * self.population_size)
        number_of_mutations = [0] * self.population_size
        for i in range(total_mutations):
            number_of_mutations[random.randrange(0, self.population_size)] += 1
        for i in range(self.population_size):
            self.chromosomes[i].mutate_nodes(number_of_mutations[i])

    def goal_test(self):
        return self.find_best(self.chromosomes)[1] == 1

    def update_statistics(self):
        print("generation #{}".format(self.generation))
        best_fitness = self.find_best(self.chromosomes)[1]
        self.best_fitnesses.append(best_fitness)
        print("best fitness: {}".format(best_fitness))
        worst_fitness = self.find_worst(self.chromosomes)[1]
        self.worst_fitnesses.append(worst_fitness)
        print("worst fitness: {}".format(worst_fitness))
        average_fitness = self.find_average(self.chromosomes)
        self.average_fitnesses.append(average_fitness)
        print("average fitness: {}\n".format(average_fitness))

    def print_answer(self):
        print("answer:")
        self.find_best(self.chromosomes)[0].print()
        print()

    def show_statistics(self):
        plt.plot(range(self.generation + 1), self.best_fitnesses, label="Best")
        plt.plot(range(self.generation + 1), self.worst_fitnesses, label="Worst")
        plt.plot(range(self.generation + 1), self.average_fitnesses, label="Average")
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.legend()
        plt.show()
